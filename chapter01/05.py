#!/usr/bin/env python3
# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

from collections import defaultdict

def ngram(n, seq):
    list = []

    for i in range(len(seq) - (n-1)):
        list.append(seq[i:i+n])

    return list

text = "I am an NLPer"
words = text.split()

# 単語bi-gram
print(ngram(2, words))

# 文字bi-gram
print(ngram(2, text))

