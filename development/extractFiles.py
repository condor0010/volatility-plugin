import os
import subprocess
import argparse
from findInFiles import findInFiles
from pathlib import Path


def run_volatility_command(command, memory_dump):
    try:
        result = subprocess.run(f'volatility -f {memory_dump} {command}', shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command {command}: {e}")
        return None


def extract_files(memory_dump, extraction_dir):
    command = f'-o {extraction_dir} windows.dumpfiles'
    run_volatility_command(command, memory_dump)


# Main function
def main():
    parser = argparse.ArgumentParser(description="Memory dump file extraction using Volatility.")
    parser.add_argument("memory_dump", help="Path to the memory dump file")
    args = parser.parse_args()

    memory_dump = Path(args.memory_dump).resolve()
    if not memory_dump.is_file():
        print(f"Error: Memory dump file '{memory_dump}' not found.")
        return

    extraction_dir = os.path.join(os.getcwd(), 'extracted_files')
    results_dir = os.path.join(os.getcwd(), 'results')
    os.makedirs(extraction_dir, exist_ok=True)

    extract_files(str(memory_dump), extraction_dir)

    findInFiles(extraction_dir, results_dir)


main()
