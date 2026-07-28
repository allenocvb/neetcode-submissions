class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Remove duplicates and sort
        nums = sorted(set(nums))
        
        longest = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:  # Consecutive elements
                current_length += 1
            else:
                longest = max(longest, current_length)
                current_length = 1
        
        # Check one more time after the loop ends
        return max(longest, current_length)
        