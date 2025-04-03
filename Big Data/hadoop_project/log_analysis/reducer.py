#!/usr/bin/env python3
import sys
from collections import defaultdict

status_counts = defaultdict(int)

# Read input from Mapper
for line in sys.stdin:
    status, count = line.strip().split("\t")
    status_counts[status] += int(count)

# Print output (HTTP Status Code, Count)
for status, count in status_counts.items():
    print(f"{status}\t{count}")
