# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        niu = ListNode()
        carry = 0
        fin = niu
        while l1 or l2:
            if l1 and l2:
                tot = (l1.val+l2.val)+carry
                l1=l1.next
                l2=l2.next
            elif l1:
                tot = l1.val + carry
                l1 = l1.next
            elif l2:
                tot = l2.val + carry
                l2 = l2.next
            carry = tot//10
            niu.next = ListNode(tot%10)
            niu=niu.next
        if carry>0:
            niu.next = ListNode(carry)
        return fin.next