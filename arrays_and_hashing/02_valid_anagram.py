class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_char_count = {}
        t_char_count = {}
        
        for char in s:
            s_char_count[char] = s_char_count.get(char, 0) + 1
        for char in t:
            t_char_count[char] = t_char_count.get(char, 0) + 1
            
        return s_char_count == t_char_count

    def isAnagramOptimized(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
            
        for count in counts:
            if count != 0:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("anagram", "nagaram", True),   # Happy Path
        ("rat", "car", False),          # Same length, different chars
        ("a", "ab", False),             # Different lengths
        ("", "", True)                  # Edge case: empty strings
    ]
    
    for s, t, expected in test_cases:
        assert sol.isAnagram(s, t) == expected, f"Hash Map failed on {s}, {t}"
        assert sol.isAnagramOptimized(s, t) == expected, f"Array failed on {s}, {t}"
        
    print("All test cases passed successfully for both solutions!")