#!/usr/bin/env python3
#
# 15. 末尾のN行を出力
#
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
from sys import stdin, stdout, argv
from collections import deque

n = int(argv[1])

for line in deque(stdin, n):
    stdout.write(line)
