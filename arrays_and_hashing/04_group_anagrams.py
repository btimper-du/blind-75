from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1   
            key = tuple(freq)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        result = []
        for key in groups:
            result.append(groups[key])
        return result

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        ),
        (
            [""],
            [[""]]
        ),
        (
            ["a"],
            [["a"]]
        )
    ]
    
    for strs, expected in test_cases:
        result = sol.groupAnagrams(strs)
        
        sorted_result = sorted([sorted(group) for group in result])
        sorted_expected = sorted([sorted(group) for group in expected])
        
        assert sorted_result == sorted_expected, f"Failed on {strs}"
        
    print("All test cases passed successfully!")