class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:-1}
        csum = 0
        for i, num in enumerate(nums):
            csum += num
            a = csum % k
            if a in seen:
                if i - seen[a] >= 2:
                    return True
            else:
                seen[a] = i
        return False                       
            