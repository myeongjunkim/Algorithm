"""
구현 럭키 스트레이트 321p 
123402 -> L
7755 -> R

"""

import sys
input = sys.stdin.readline

nums = list(map(int, input()[:-1]))

left_n = []
right_n= []
for i in range(len(nums)):
    if i < len(nums)//2:
        left_n.append(nums[i])
    else:
        right_n.append(nums[i])

if sum(left_n) == sum(right_n):
    print("LUCKY")
else:
    print("READY")
