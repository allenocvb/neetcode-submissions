class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        cleanedNums = set(nums)
        longest = 0

        for num in cleanedNums:
            if (num - 1) not in cleanedNums:
                current_length = 1
                while (num + current_length) in cleanedNums:
                    current_length += 1
                
                longest = max(longest, current_length)
        
        return longest
        