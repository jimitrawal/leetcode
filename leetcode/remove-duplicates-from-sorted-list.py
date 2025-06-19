# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        mt = ListNode(head.val)
        niu = mt
        while curr:
            nextN=curr.next
            if curr.next and curr.val == nextN.val:
                curr = curr.next
            else:
                niu.next = ListNode(curr.val)
                niu = niu.next
                curr = curr.next
        return mt.next