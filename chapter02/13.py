#!/usr/bin/env python3
#
# 13. col1.txtとcol2.txtをマージ
#
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

import sys

def read_line(handles):
    while True:
        lines = [h.readline() for h in handles]
        if not all(lines):
            return []

        yield [line.rstrip() for line in lines]

files = sys.argv[1:]

if len(files) == 0:
    exit(0)

handles = [open(file) for file in files]

for lines in read_line(handles):
    print("\t".join(lines))

for handle in handles:
    handle.close()
