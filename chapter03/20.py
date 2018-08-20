#!/usr/bin/env python3
import re
import sys

pattern = re.compile(u'.*イギリス.*', re.DOTALL)
for line in sys.stdin:
    if pattern.match(line):
        sys.stdout.write(line)
