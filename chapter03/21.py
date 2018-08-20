#!/usr/bin/env python3
import sys

for line in sys.stdin:
    if "Category" in line:
        sys.stdout.write(line)
