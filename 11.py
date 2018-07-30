#!/usr/bin/env python3
#
# 11. タブをスペースに置換
#
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
#
# OS X: sed "s/	/ /g"
# others: expand -t 1

import sys

for line in sys.stdin:
    print(line.strip().replace("\t", ' '))

