# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide(lists, 0, len(lists)-1)
    
    def divide(self, lists, l, r):

        if l > r:
            return None

        if l == r:
            return lists[l]
        
        mid = (l + r) // 2

        left = self.divide(lists, l, mid) # Merge left half
        right = self.divide(lists, mid+1, r) # Merge right half

        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dum = ListNode()
        curr = dum
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 if l1 else l2
        return dum.next
        