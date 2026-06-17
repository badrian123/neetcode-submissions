# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, head

        while curr:
            tmp = curr.next #Node 2
            curr.next = pre #None
            pre = curr #Node 1
            curr = tmp #Node 2
        return pre