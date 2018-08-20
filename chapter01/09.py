#!/usr/bin/env python3
#
# 09. Typoglycemia
#
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
#
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand
# what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
from random import sample, shuffle

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(text):
    if len(text) <= 4:
        return text

    head = text[0]
    mid = text[1:-1]
    last = text[-1]

    return head + _shuffle(mid) + last

def _shuffle(s):
    l = list(s)
    shuffle(l)
    return ''.join(l)

for t in map(typoglycemia, text.split(' ')):
    print(t)
