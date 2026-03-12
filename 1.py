# 将一颗色子掷 6000 次，统计每种点数出现的次数
import random

list = [0] * 6

for i in range(6000):
    list[random.randint(0, 5)] += 1

for i in list:
    # print(round(i/6000, 3), end='\t')
    print(i, end='\t')