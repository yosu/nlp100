#!/usr/bin/env python3
# 27. 内部リンクの除去
#
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
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

def remove_highlight_markup(text):
    p = re.compile(u"(?P<content>.*?)(?P<quote>'{2,4})(?P<highlighted_content>.*?)(?P=quote)(?P<remaining_content>.*)")
    m = p.match(text)
    if m:
        content = m.group('content')
        highlighted_content = m.group('highlighted_content')
        remaining_content = m.group('remaining_content')
        return content + highlighted_content + remove_highlight_markup(remaining_content)

    return text

def remove_inner_link(text):
    m = re.match(u"(?P<pre_text>.*?)\[\[(?P<link_text>.*?)\]\](?P<remaining_text>.*)", text)
    if m:
        pre_text = m.group('pre_text')
        # 内部リンクのテキストで表示名指定がある場合（[[記事名|表示名]]）は表示名を優先する
        link_text = m.group('link_text').split('|')[-1]
        remaining_text = m.group('remaining_text')
        return pre_text + link_text + remove_inner_link(remaining_text)

    return text

result = {}
for key, value in read_basic_info().items():
    result[key] = remove_inner_link(remove_highlight_markup(value))

pprint(result)
