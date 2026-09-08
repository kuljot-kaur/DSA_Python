class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        csum = 0
        count = 0
        for num in nums:
            csum += num
            rem = csum % k
            if rem in seen:
                count += seen[rem]      
            seen[rem] = seen.get(rem, 0)+1
        return count