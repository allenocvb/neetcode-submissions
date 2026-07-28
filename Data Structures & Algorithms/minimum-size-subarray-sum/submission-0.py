class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = float("inf")
        l = 0
        curr_size = 0

        for r in range(len(nums)):

            curr_size += nums[r]

            while curr_size >= target:
                min_length = min(min_length, r-l+1)
                curr_size -= nums[l]
                l += 1
        
        return min_length if min_length < float("inf") else 0
        