from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], i]
            seen[num] = i

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]), 
        ([3, 3], 6, [0, 1]),
    ]
    
    for nums, target, expected in test_cases:
        result = sol.twoSum(nums, target)
        assert result == expected, f"Failed on {nums} with target {target}. Got {result}"
        
    print("All test cases passed successfully!")