class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_len = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            
            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)
            
        return max_len

if __name__ == "__main__":
    solution = Solution()

    s1 = "abcabcbb"
    print(f"Örnek 1 Sonucu: {solution.lengthOfLongestSubstring(s1)} | Beklenen: 3")

    s2 = "bbbbb"
    print(f"Örnek 2 Sonucu: {solution.lengthOfLongestSubstring(s2)} | Beklenen: 1")

    s3 = "pwwkew"
    print(f"Örnek 3 Sonucu: {solution.lengthOfLongestSubstring(s3)} | Beklenen: 3")
