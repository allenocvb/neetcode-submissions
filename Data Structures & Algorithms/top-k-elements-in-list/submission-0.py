import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        frequency_count = dict()
        for num in nums:
            frequency_count[num] = 1 + frequency_count.get(num, 0)
        
        # Create a min-heap
        heap = []
        for num in frequency_count.keys():
            heapq.heappush(heap, (frequency_count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
