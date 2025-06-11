# Definition for singly-linked list.
# class ListNode:
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        node=ListNode()
        final=node
        copy=final
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val >= curr2.val:
                    final.next=curr2
                    curr2=curr2.next
                    final= final.next
                else:
                    final.next=curr1
                    curr1=curr1.next
                    final= final.next
            elif curr1:
                final.next=curr1
                curr1=curr1.next
                final= final.next
            elif curr2:
                final.next=curr2
                curr2=curr2.next
                final= final.next
        return copy.next