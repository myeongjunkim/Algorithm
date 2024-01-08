### 1번째 2차 개선 정답( 이진탐색을 통해 N^2 를 N*logN 으로  )

from itertools import combinations
import bisect

class Solution:

    def minimumDifference(self, nums: list[int]) -> int:

        def get_part_sums(nums, i):
            if i == 0:
                return [0]
            sums = []
            for case in combinations(nums, i):
                sums.append(sum(case))
            return sums

        N = len(nums) // 2
        total_sum = sum(nums)
        half_sum = total_sum // 2
        left, right = nums[:N], nums[N:]
        ans = abs( sum(left) - sum(right) )

        for i in range(0,N+1):
            left_part_sums, right_part_sums = get_part_sums(left, i), get_part_sums(right, N-i)
            right_part_sums.sort()
            for left_part_sum in left_part_sums:
                # right_part_sums 중 하나와 left_part_sum 합
                # 1. 완전탐색 -> n^2
                # 2. 이진탐색 -> n * log n
                goal_of_right_part_sum = half_sum - left_part_sum
                index = bisect.bisect_left(right_part_sums, goal_of_right_part_sum)
                for index_case in [index, index-1]:
                    if 0<=index < len(right_part_sums):
                        diff = abs(total_sum - 2*(right_part_sums[index_case] + left_part_sum))
                        ans = min(ans, diff)
        
        return ans