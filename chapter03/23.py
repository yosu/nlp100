#!/usr/bin/env python3
#
# 23. セクション構造
#
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
import sys
import re

pattern = re.compile(u'(?P<level>=+) ?(?P<section>.*?) ?(?P=level)')
for line in sys.stdin:
    m = pattern.match(line)
    if m:
        print(m.group('section'), len(m.group('level')) -1)
