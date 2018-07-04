#!/usr/bin/env python3
#
# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
#
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
#
from operator import add
from functools import reduce

patrol_car = "パトカー"
taxi = "タクシー"

pairs = [p + t for p, t in zip(patrol_car, taxi)]
ans = reduce(add, pairs)

print(ans)
