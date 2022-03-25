#!
# -*- coding: utf-8 -*- 
 
from binarytree import build
from functools import reduce


class SumTree(object):
    """
    This SumTree code is modified version and the original code is from:
    """
    def __init__(self, maxlen:int) -> None:
        self.maxlen = maxlen
        self.level = len(bin(maxlen - 1)) - 1
        self.datas = [None,] * maxlen # 2 ** (self.level - 1)
        self.tree = []
        for n in range(self.level):
            self.tree.append([0,] * 2 ** n)
        self.cursor = 0

    def add(self, priority, data:any) -> None:
        idx = self.cursor
        self.datas[idx] = data
        
        sum = priority
        current_idx = idx
        for l in range(1, self.level)[::-1]:
            self.tree[l][current_idx] = sum
            next_idx = current_idx - 2 * (current_idx % 2) + 1
            sum = self.tree[l][current_idx] + self.tree[l][next_idx]
            current_idx = min(current_idx, next_idx) >> 1

        self.tree[0][current_idx] = sum
        self.cursor = (self.cursor + 1) % self.maxlen

    def find(self, percentage:float):
        n = self.tree[0][0] * percentage
        idx = 0
        for l in range(1, self.level):
            idx = idx << 1
            if n >= self.tree[l][idx]:
                idx += 1
                n -= self.tree[l][idx - 1]

        return self.datas[idx], self.tree[-1][idx], idx
        # data, priority, index

        
    def __str__(self) -> str:
        print(self.tree)
        return str(build(reduce(lambda x, y: x + y, self.tree))) + '\n' + str(self.datas)


if __name__ == '__main__':

    s = SumTree(maxlen=16)
    for i in range(1, 8+60):
        s.add(i, i+0.2)
    print(s)
    print(s.find(0.5))

