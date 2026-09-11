# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            #Need to store temporarily the next node
            #Then need to adjust the current node's next pointer
            #Then need to store this node so that next iteration node knows about this node.
            #Need to update the iteration to the next iteration.
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev #Because if done correctlt, prev should be the head of the list