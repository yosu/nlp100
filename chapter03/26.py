#!/usr/bin/env python3
# 26. 強調マークアップの除去
#
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
import sys
import re
from pprint import pprint


def read_basic_info():
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
    return info

def extract(text):
    p = re.compile(u"(?P<content>.*?)(?P<quote>'{2,4})(?P<highlighted_content>.*?)(?P=quote)(?P<remaining_content>.*)")
    m = p.match(text)
    if m:
        content = m.group('content')
        highlighted_content = m.group('highlighted_content')
        remaining_content = m.group('remaining_content')
        return content + highlighted_content + extract(remaining_content)

    return text

result = {}
for key, value in read_basic_info().items():
    result[key] = extract(value)

pprint(result)
