class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}

        for i in range(len(nums)):
            goal = target - nums[i]
            if goal not in store:
                store[nums[i]] = i
            else:
                return [store[goal], i]
        
        return []