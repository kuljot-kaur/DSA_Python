class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        csum = 0
        minl = len(nums) + 1
        for right in range(len(nums)):
            csum += nums[right]
            while csum >= target:
                minl = min(minl, right - left + 1)
                csum -= nums[left]
                left += 1
        return minl if minl <= len(nums) else 0