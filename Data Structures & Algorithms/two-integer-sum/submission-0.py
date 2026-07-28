class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # (target-num) : index
        # for each number, check dict
        # if target - number in dict return value(index) and 
        # current index
        store = {}
        for i in range(len(nums)):
            if (nums[i]) in store:
                return [store[nums[i]], i]
            store[target - nums[i]] = i
        return []
            