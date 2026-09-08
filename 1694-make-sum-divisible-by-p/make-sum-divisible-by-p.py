class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p

        if target == 0:
            return 0

        seen = {0: -1}
        prefix = 0
        answer = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            needed = (prefix - target + p) % p

            if needed in seen:
                answer = min(answer, i - seen[needed])

            seen[prefix] = i

        return answer if answer < len(nums) else -1