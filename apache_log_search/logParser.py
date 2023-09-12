#!/usr/bin/env python3

import sys
import re

def display_usage():
    print("Usage: {} <access_log_file> <pattern>".format(sys.argv[0]))

if len(sys.argv) != 3:
    display_usage()
    sys.exit(1)

access_log_file = sys.argv[1]
pattern = sys.argv[2]

try:
    with open(access_log_file, 'r') as log_file:
        for line in log_file:
            # Use a regular expression to find the client IP address in each line
            match = re.search(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
            if match:
                client_ip = match.group(1)
                print("as",client_ip)
                # Check if the line contains the specified pattern
                if pattern in line:
                    print(client_ip)
except FileNotFoundError:
    print("Error: The access log file '{}' does not exist.".format(access_log_file))
    sys.exit(1)
