# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        #It is all based on fast and there is a destination that fast can go to.
        while fast and fast.next:
            #Slow is moving at a normal rate
            slow = slow.next
            #Fast is moving twice as fast.
            fast = fast.next.next
            if slow == fast:
                return True
        return False