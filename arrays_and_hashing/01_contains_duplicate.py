from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

if __name__ == "__main__":
    sol = Solution()
    
    # Assert statements throw an AssertionError if the test fails
    assert sol.hasDuplicate([1, 2, 3, 1]) == True, "Failed on duplicate array"
    assert sol.hasDuplicate([1, 2, 3, 4]) == False, "Failed on distinct array"
    assert sol.hasDuplicate([]) == False, "Failed on empty array"
    assert sol.hasDuplicate([1]) == False, "Failed on single-element array"
    
    print("All test cases passed successfully!")