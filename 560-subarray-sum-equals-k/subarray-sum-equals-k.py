class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        count = 0
        csum = 0
        for num in nums:
            csum += num
            diff = csum - k
            if diff in seen:
                count += seen[diff]
            seen[csum] = seen.get(csum, 0) + 1
        return count
            