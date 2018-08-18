#!/usr/bin/env python
#
# 17. １列目の文字列の異なり
#
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
import sys

first_letters = set([line[0] for line in sys.stdin])
print("\n".join(sorted(list(first_letters))))
