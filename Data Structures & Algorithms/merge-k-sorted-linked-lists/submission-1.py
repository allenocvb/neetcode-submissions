import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []

        for i, node_head in enumerate(lists):
            heapq.heappush(min_heap, (node_head.val, i, node_head))

        dum = ListNode()
        curr = dum

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        return dum.next


        