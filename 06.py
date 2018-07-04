#!/usr/bin/env python3
#
# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
#
def ngram(n, seq):
    list = []

    for i in range(len(seq) - (n-1)):
        list.append(seq[i:i+n])

    return list

x = "paraparaparadise"
y = "paragraph"

bi_x = set(ngram(2, x))
bi_y = set(ngram(2, y))

print("union: %r" % (bi_x | bi_y))
print("intersection: %r" % (bi_x & bi_y))
print("difference: %r" % (bi_x - bi_y))

print('"se" in x: %r' % ("se" in x))
print('"se" in y: %r' % ("se" in y))
