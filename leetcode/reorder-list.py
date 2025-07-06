# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        copy = head
        copy2 = head
        stack=[]
        while copy:
            stack.append(copy.val)
            copy=copy.next
        c=0
        while copy2:
            if c%2==0:
                copy2.val = stack[0]
                stack = stack[1:]
            else:
                copy2.val = stack[-1]
                stack.pop()
            c+=1
            copy2 = copy2.next
        return head