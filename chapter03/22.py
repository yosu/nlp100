#!/usr/bin/env python3
#
# 22. カテゴリ名の抽出
#
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
import sys
import re

pattern = re.compile(u'^\[\[Category:(?P<category>.*?)(\||\])')
for line in sys.stdin:
    m = pattern.match(line)
    if m:
        print(m.group('category'))
