class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = {}
        left = 0
        maxf = 0
        for right in range(len(fruits)):
            seen[fruits[right]] = seen.get(fruits[right], 0) + 1
            while len(seen) > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1
            cw = right - left + 1
            maxf = max(maxf, cw)
        return maxf