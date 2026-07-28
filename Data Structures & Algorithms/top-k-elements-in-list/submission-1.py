class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq_count = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, freq in count.items():
            freq_count[freq].append(num)
        
        result = []
        for lst in range(len(freq_count) - 1, 0, -1):
            for num in freq_count[lst]:
                result.append(num)
                if len(result) == k:
                    return result
        