#!/usr/bin/env python3
#
# 24. ファイル参照の抽出
#
# 記事から参照されているメディアファイルをすべて抜き出せ．
import sys
import re

pattern = re.compile(u'^\[\[File:(?P<file>.*?)(\|(?P<thumb>thumb))?(\|(?P<align>left|right))?(\|(?P<size>\d+px))?(\|(?P<desc>.*))\]\]$')
for line in sys.stdin:
    m = pattern.match(line)
    if m:
        print(m.group('file', 'thumb', 'align', 'size', 'desc'))

