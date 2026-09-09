class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        left = 0
        ml  = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.append(s[right])
            cw = right - left + 1
            ml = max(cw, ml)
        return ml
            
