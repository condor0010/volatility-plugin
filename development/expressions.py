ip4 = r'(\b(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])(?=\s*.$)'

# Doesn't explicitly match IPv4-mapped IPv6, IPv4-Embedded IPv6, or link-local IPv6 addresses.
ip6 = r"\b([a-f0-9:]{1,5}:){1,7}([a-f0-9:]{1,5})|([:]{2}\d+)"

password = r'\b(password)'

wifi = r'\b(b?(ssid)+\b)'

MAC = r'([0-9a-f]{2}[:-]){5}([0-9a-f]{2})'

B64 = r"^(?:[A-Za-z0-9+/]{4})+(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)+$"

dollarSigns = r"(\s?.?\$\w+\$[\w*\-/$=.]{10,})"
