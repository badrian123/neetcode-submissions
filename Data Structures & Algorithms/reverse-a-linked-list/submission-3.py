# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        #Going to iterate through the list of nodes
        while curr:
            #Need to get the next node and store it temporarily.
            temp = curr.next
            #Now that it is saved, need to update curr.next to prev
            curr.next = prev
            #Need to store this node so that the next iteration can about it.
            prev = curr
            #Need to move on to the next iteration.
            curr = temp
        
        return prev #I wonder why we return prev but i guess it is due to reversing the node.