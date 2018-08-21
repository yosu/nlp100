#!/usr/bin/env python3
#
# 25. テンプレートの抽出
#
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
import sys
import re
from pprint import pprint

info = {}

for line in sys.stdin:
    if re.match(u'^{{基礎情報', line):
        break;

# 複数行にまたがることがあるのでキーを保持しておく
key = ''

for line in sys.stdin:
    if re.match(u'^}}$', line):
        break

    m = re.match(u'\|(?P<key>.*?)\s*=\s*(?P<value>.*)$', line)
    if m:
        key = m.group('key')
        info[key] = m.group('value')
    elif key:
        info[key] += line

pprint(info)
