# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummylen = head
        curr = head
        dummynode = ListNode()
        dummynode.next = curr
        tot = 1

        while dummylen.next:
            tot+=1
            dummylen=dummylen.next 

        dest=tot-n
        if n==tot:
            return curr.next
        while curr.next:
            dest-=1
            if dest==0:
                rep = curr.next.next
                curr.next=None
                curr.next = rep
                break
            else:
                curr=curr.next 
        return dummynode.next