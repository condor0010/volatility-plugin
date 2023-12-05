import os
import re
import socket

from expressions import *

checks = {"ip4": ip4,
          "ip6": ip6,
          "MAC": MAC,
          "B64": B64,
          "Hashes": dollarSigns
          }


def validateIP6(addr):
    """
    Checks if IPv6 addresses have the correct format using socket
    :param addr: An IPv6-similar address
    :return: True if addr is in a valid IPv6 format
    """
    try:
        socket.inet_pton(socket.AF_INET6, addr)
        return True
    except:
        return False


def appendMe(statusDict, s):
    """
    Appends the string s to the results. Only used to clean up any code that appends to statusDict
    :param statusDict: Contains the statuses of the current file
    :param s: The string to append
    :return: Nothing
    """
    statusDict["returnResults"].append(s)


def printUniqueMatches(statusDict):
    """
    Formats unique matches in preparation for printing to file
    :param statusDict: Contains the statuses of the current file
    :return: Nothing
    """
    if statusDict["printedFileName"]:
        appendMe(statusDict, "\nEvery Unique Match:\n")
        for match in statusDict["matchSet"]:
            appendMe(statusDict, '    ' + match + '\n')


def printShortLines(statusDict, line, maxLen):
    """
    If line is shorter than maxLen, adds a header and the line to results
    :param statusDict: Contains the statuses of the current file
    :param line: A line containing a match
    :param maxLen: Maximum length of the line we want to add to the results
    :return: Nothing
    """
    if len(line) < maxLen and statusDict["shortLineCount"] < statusDict["shortLineLimit"]:
        if not statusDict["printedShortLine"]:
            appendMe(statusDict, "\nShort Lines Containing A Match:\n")
            statusDict["printedShortLine"] = True
        appendMe(statusDict, '    ' + line.strip() + '\n')
        statusDict["shortLineCount"] += 1


def printFileName(statusDict):
    """
    Prints file name containing a match
    :param statusDict: Contains the statuses of the current file
    :return: Nothing
    """
    appendMe(statusDict, '-' * 100 + '\n')
    appendMe(statusDict, os.path.join(statusDict["root"], statusDict["file"]) + '\n')
    statusDict["shortLineCount"] = 0
    statusDict["printedFileName"] = True


def addMatchesToSet(matchIter, matchedSet, minLen=0, IP6=False):
    """
    Adds all matches in matchIter to matchedSet
    :param matchIter: An iterable object containing matches
    :param matchedSet: The set of unique matches
    :param minLen: The minimum length a match must be before it is added to the results
    :param IP6: Checking IPv6 addresses for validity or not
    :return: Nothing
    """
    for match in matchIter:
        if not IP6 or validateIP6(match):
            if len(match) > minLen:
                matchedSet.add(match)


def matchHandler(statusDict, line, matchIter, maxLen=100):
    """
    Takes valid matches and handles the calls needed to generate the correct output
    :param statusDict: Contains the statuses of the current file
    :param line: The line containing a match
    :param matchIter: An iterable containing all matches found in line
    :param maxLen: How long a line can be before it isn't included in the printed results
    :return: Nothing
    """
    if not statusDict["printedFileName"]:
        printFileName(statusDict)
    printShortLines(statusDict, line, maxLen)
    addMatchesToSet(matchIter, statusDict["matchSet"])


def checkRegEx(line, check):
    """
    Checks if check matches anything in line, ignoring the case of the string
    :param line: The line to search
    :param check: The check to use to search line
    :return: Matches if any are found
    """
    matches = []
    for i in re.finditer(check, line, re.IGNORECASE):
        matches.append(i.group().strip())
    if len(matches) > 0:
        return matches


def decodeLine(line):
    """
    Attempts to decode a given string and returns that string decoded
    :param line: The line we are trying to decode and verify it's a valid string
    :return: Returns the decoded line if it doesn't throw any errors
    """
    try:
        return line.decode()
    except:
        pass


def checkIP6(status, lines):
    """
    Method to handle checking for IP6 addresses
    :param status: Contains the statuses of the current file
    :param lines: The contents of a file
    :return: Nothing
    """
    for line in lines:
        if line := decodeLine(line):
            matchedIP6Set = set()
            if lineMatches := checkRegEx(line, ip6):
                addMatchesToSet(lineMatches, matchedIP6Set, 5, True)
                if matchedIP6Set:
                    matchHandler(status, line, matchedIP6Set)


def checkFile(lines, check, file, root, checkName):
    """
    Checks a file to see if anything inside matches the RegEx check
    :param lines: The contents of a file
    :param check: A RegEx pattern
    :param file: File's name
    :param root: Path of file
    :param checkName: The name of the RegEx check
    :return: A string to write to a file
    """
    status = {
        "printedFileName": False,
        "printedShortLine": False,
        "matchSet": set(),
        "returnResults": [],
        "shortLineLimit": 10,
        "shortLineCount": 0,
        "root": root,
        "file": file
    }

    if checkName == 'ip6':
        checkIP6(status, lines)
    else:
        for line in lines:
            if line := decodeLine(line):
                if lineMatches := checkRegEx(line, check):
                    matchHandler(status, line, lineMatches)
    printUniqueMatches(status)
    return ''.join(status["returnResults"])


def findInFiles(target, results):
    """
    The findInFiles method that handles reading and writing to each file
    :param target: The directory containing files you wish to search through
    :param results: The directory you wish the results to be written to
    :return:
    """

    buffer = dict()
    for check in checks.keys():
        buffer[check] = dict()
        buffer[check]["checkName"] = check
        buffer[check]["fileName"] = results + '/results_' + check + '.txt'
        buffer[check]["buffer"] = []

    for root, dirs, files in os.walk(target):
        for file in files:
            try:
                with open(os.path.join(root, file), "rb") as inputFile:
                    fileData = inputFile.readlines()
            except PermissionError:
                break
            except FileNotFoundError:
                break
            for check in checks:
                buffer[check]["buffer"].append(checkFile(fileData, checks[check], file, root, buffer[check]["checkName"]))

    for check in checks:
        with open(buffer[check]["fileName"], "w+") as outputFile:
            outputFile.write(''.join(buffer[check]["buffer"]))

