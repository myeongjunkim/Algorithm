import sys
input = sys.stdin.readline

def execute():
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    M = int(input())
    req = list(map(int, input().split()))
    for n in req:
        print(is_there(nums, n))
        

def is_there(nums,n):
    N = len(nums)
    
    start, end = 0, N-1
    while start <= end:
        mid = (start + end)//2
        if nums[mid] == n:
            return 1
        elif nums[mid] < n:
            start = mid+1
        else:
            end = mid-1

    return 0


execute()