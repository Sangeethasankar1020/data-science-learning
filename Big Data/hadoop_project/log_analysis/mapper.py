#!/usr/bin/env python3
import sys

# Read each line from log file
for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) > 8:
        ip = parts[0]  # Extract IP address
        status_code = parts[-2]  # Extract HTTP status code
        print(f"{status_code}\t1")  # Emit (status_code, 1)
