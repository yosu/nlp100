#!/usr/bin/env python3
#
# 16. ファイルをN分割する
#
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
import string
from sys import stdin, argv
from itertools import islice, product


def name_generator():
    l = string.ascii_lowercase

    for tup in product(l, l, l):
        yield ''.join(tup)


def take(n, iterable):
    while True:
        l = list(islice(iterable, n))
        if l:
            yield l
            continue
        break


def main():
    n = int(argv[1])

    gen = name_generator()

    for lines in take(n, stdin):
        filename = next(gen)
        with open(filename, 'w') as fh:
            fh.writelines(lines)


main()
