from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in num_index:
                return [num_index[diff], i]
            
            num_index[num] = i
        
        return None

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
print('https://leetcode.com/problems/two-sum/', 'hello world')