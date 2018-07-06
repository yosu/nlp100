#!/usr/bin/env python3
#
# 08. 暗号文
#
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．
from functools import reduce
from operator import add

def cipher(str):
    return reduce(add, map(_cipher, str))

def _cipher(ch):
    if 'a' <= ch <= 'z':
        return chr(219 - ord(ch))

    return ch

print(cipher("Hello world!"))
print(cipher("abc xyz"))
