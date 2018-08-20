#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 18. 各行を3コラム目の数値の降順にソート
#
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
#
# sort -k 3 hightemp.txt
import sys

def temperature(record):
    pref, city, temp, date = record.split()
    return float(temp)


lines = [line for line in sys.stdin]
lines.sort(key=temperature)

sys.stdout.writelines(lines)