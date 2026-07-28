class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # 1️⃣ skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            l, r = i + 1, n - 1
            
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    # 2️⃣ record a valid triplet
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # 3️⃣ advance both pointers
                    l += 1
                    r -= 1
                    
                    # 4️⃣ skip duplicates on the left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    #    and on the right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
                elif s < target:
                    l += 1
                else:
                    r -= 1
        
        return res