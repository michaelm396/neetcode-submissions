# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # loop through linked list and swap nodes
        """
        count = k
        cur = head
        while count != 1:
            cur = head.next
            count -= 1
        
        """
        cur = head
        for i in range(k-1):
            cur = cur.next
        
        swapl = cur
        swapr = head
        
        while cur.next:
            cur = cur.next
            swapr = swapr.next
        swapl.val, swapr.val = swapr.val, swapl.val
        return head



        

        