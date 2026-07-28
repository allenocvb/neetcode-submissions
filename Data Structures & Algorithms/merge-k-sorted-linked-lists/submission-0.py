# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        nodes = []

        for ll in lists:
            curr = ll
            while curr:
                nodes.append(curr.val)
                curr = curr.next
                
        nodes.sort()
        dum = ListNode()
        curr = dum

        for node_val in nodes:
            node = ListNode(node_val)
            curr.next = node
            curr = curr.next
        
        return dum.next

