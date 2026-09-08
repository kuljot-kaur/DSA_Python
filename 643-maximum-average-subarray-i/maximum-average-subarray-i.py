class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win = sum(nums[:k])
        maxarr = win
        for i in range(k, len(nums)):
            win += nums[i] - nums[i-k]
            maxarr = max(win, maxarr)
        return maxarr/k