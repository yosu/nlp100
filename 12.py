#!/usr/bin/env python3
# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．
#
# col1.txt: cut -f 1 < hightemp.txt
# col2.txt: cut -f 2 < hightemp.txt
#
from sys import stdin


def write_lines(path, lines):
    with open(path, 'w') as f:
        for line in lines:
            f.write(line + "\n")


def main():
    col1 = []
    col2 = []

    for line in stdin:
        words = line.split()

        col1.append(words[0])
        col2.append(words[1])

    write_lines('col1.txt', col1)
    write_lines('col2.txt', col2)


main()
