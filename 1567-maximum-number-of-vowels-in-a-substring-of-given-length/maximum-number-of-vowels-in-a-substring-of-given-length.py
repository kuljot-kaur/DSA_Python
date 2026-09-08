class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        c = 0
        win = s[:k]
        for i in win:
            if i in vowels:
                c += 1
        maxv = c
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                c -= 1
            if s[i] in vowels:
                c += 1
            maxv = max(maxv, c)
        return maxv
            