# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #I need to work in reverse becase 1 ends up pointing at zero.
        #I need to assign a new direction in which the node is pointing at
        #I also need to erase the direction that the node is pointing at
        #I know that 0 is pointing to 1
        #I know that I need to remember the node that I am in 

        prev = None
        while head:
            #Store what is next
            temp = head.next
            #Need to 
            head.next = prev
            prev = head
            head = temp
        
        return prev