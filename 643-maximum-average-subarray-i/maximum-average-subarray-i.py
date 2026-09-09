class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        csum = sum(nums[:k])
        maxw = csum
        for i in range(k, len(nums)):
            csum += nums[i] - nums[i-k]
            maxw = max(csum, maxw)
        return maxw/k
