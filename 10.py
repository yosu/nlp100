#!/usr/bin/env python3
#
# 10. 行数のカウント
#
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
#
# 確認:

#   wc -l
#
import sys

count = 0
for line in sys.stdin:
    count += 1

print(count)
