#!/usr/bin/env python3
# 28. MediaWikiマークアップの除去
#
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
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

def remove_inner_link_markup(text):
    m = re.match(u"(?P<pre_text>.*?)\[\[(?P<link_text>.*?)\]\](?P<remaining_text>.*)", text)
    if m:
        pre_text = m.group('pre_text')
        # 内部リンクのテキストで表示名指定がある場合（[[記事名|表示名]]）は表示名を優先する
        link_text = m.group('link_text').split('|')[-1]
        remaining_text = m.group('remaining_text')
        return pre_text + link_text + remove_inner_link_markup(remaining_text)

    return text


# {{lang|fr|Dieu et mon droit}}
def remove_lang_markup(text):
    m = re.match(u"(?P<pre>.*?){{lang\|.*?\|(?P<text>.*?)}}(?P<post>.*)", text)
    if m:
        pre = m.group('pre')
        # 内部リンクのテキストで表示名指定がある場合（[[記事名|表示名]]）は表示名を優先する
        text = m.group('text')
        post = m.group('post')
        return pre + text + remove_lang_markup(post)

    return text


def remove_outer_link_markup(text):
    m = re.match(u"(?P<pre>.*?)\[(?P<url>.*?)( (?P<text>.*?))?\](?P<post>.*)", text)
    if m:
        pre = m.group('pre')
        # 内部リンクのテキストで表示名指定がある場合（[[記事名|表示名]]）は表示名を優先する
        text = m.group('text') or m.group('url')
        post = m.group('post')
        return pre + text + remove_outer_link_markup(post)

    return text
    pass


result = {}
for key, text in read_basic_info().items():
    text = remove_highlight_markup(text)
    text = remove_inner_link_markup(text)
    text = remove_lang_markup(text)
    text = remove_outer_link_markup(text)
    result[key] = text

pprint(result)
