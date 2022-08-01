# -*- coding: utf-8 -*-
"""
FILE       : codeing_test
DATE       : 2022/8/1 上午9:16
Author     : sxf
Description: 
"""
from typing import List


#######################################################################


def Q1(arr: List[int]):
    arr.sort()
    arr_len = len(arr)
    divide_num = 1
    if arr_len >= 5:
        divide_num = (arr_len - 2) // 3 + 1
    answer = []
    append_count = 0
    divide_index = 0
    for item in arr[divide_num: -1]:
        if divide_index == divide_num:
            break
        append_count += 1
        answer.append(item)
        if append_count == 2:
            answer.append(arr[divide_index])
            divide_index += 1
            append_count = 0
    if divide_index < divide_num and arr_len > 1:
        if arr_len % 2 == 0:
            answer.extend([arr[divide_index], arr[-1]])
        if arr_len % 2 == 1:
            answer.extend([arr[-1], arr[divide_index]])
    else:
        answer.append(arr[-1])
    return answer

a = [132,43,57,69,79,8,8,9,122,156,111,112]
a1 = [11,22,33]
answerQ1 = Q1(a)
print("Q1:", answerQ1)  # [57, 69, 8, 79, 111, 8, 112, 122, 9, 132, 43, 156]


#######################################################################


def Q2(teamA: List[int], teamB: List[int]):
    teamB = [i + 0.5 for i in teamB]
    teamB_copy = list(set(teamB.copy()))
    teamB_copy.sort()
    teamAB = teamA + teamB_copy
    teamAB.sort()
    answer = [teamAB.index(i) - teamB_copy.index(i) for i in teamB]
    return answer


teamA = [1, 4, 4, 3, 2, 2, 5, 8, 7]
teamB = [4, 4, 8, 3, 1, 0, 9]
answerQ2 = Q2(teamA, teamB)
print("Q2:",answerQ2)  # [6, 6, 9, 4, 1, 0, 9]


#######################################################################


class Stack:
    def __init__(self):
        self.item = list()

    def push(self, v: int):
        self.item.append(v)
        return self._return

    def pop(self):
        self.item.pop()
        return self._return

    def inc(self, i, v):
        for index in range(self._size - 1):
            if self.item[index] == i:
                self.item[index] += v
        return self._return

    @property
    def _size(self):
        return len(self.item)

    @property
    def _return(self):
        if self.item:
            print(self.item[-1])
            return
        print("EMPTY")


s = Stack()
s.push(1)  # 1
s.push(2)  # 2
s.push(3)  # 3
s.push(1)  # 1
s.push(2)  # 2
s.push(3)  # 3
s.pop()    # 2
s.inc(2,2) # 2
print(s.item)  # [1, 4, 3, 1, 2]

