#!/usr/bin/env python3
#
# 03. 円周率
#
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
#
from re import sub

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# カンマとピリオドを除く
trimmed_str = sub(r"[,.]", '', str)

ans = [len(s) for s in trimmed_str.split()]

print(ans)
