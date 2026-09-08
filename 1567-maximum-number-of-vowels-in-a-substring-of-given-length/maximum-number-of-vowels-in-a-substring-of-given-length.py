class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        c = 0
        for a in s[:k]:
            if a in vowels:
                c+=1
        maxv = c
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                c-=1
            if s[i] in vowels:
                c+=1
            maxv = max(maxv, c)
        return maxv