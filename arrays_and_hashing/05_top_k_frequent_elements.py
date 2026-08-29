from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)
        top_k = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),      
        ([1], 1, [1]),                         
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2])
    ]
    
    for nums, k, expected in test_cases:
        result = sol.topKFrequent(nums, k)
        
        assert sorted(result) == sorted(expected), f"Failed on {nums} with k={k}. Got {result}"
        
    print("All test cases passed successfully!")