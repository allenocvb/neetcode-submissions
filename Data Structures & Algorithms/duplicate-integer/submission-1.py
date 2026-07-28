class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for number in nums:
            if number in check:
                return True
            check.add(number)
        return False
         