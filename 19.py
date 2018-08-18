#!/usr/bin/env python3
# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
#
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
import sys

hist = {}
lines = [x for x in sys.stdin]

def prefecture(line):
    return line.split()[0]

for line in lines:
    pref = prefecture(line)
    hist[pref] = hist.get(pref, 0) + 1

def key(line):
    return -hist[prefecture(line)]

lines.sort(key=key)

sys.stdout.writelines(lines)

