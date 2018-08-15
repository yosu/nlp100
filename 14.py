#!/usr/bin/env python3
#
# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
from sys import argv, stdin, stdout

n = int(argv[1])

for i in range(0, n):
    line = stdin.readline()
    stdout.write(line)
