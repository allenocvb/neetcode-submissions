class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for i in range(len(nums)):
            if nums[i] in check:
                return True
            else:
                check.add(nums[i])

        return False
         