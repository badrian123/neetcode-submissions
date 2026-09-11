# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode, currentNode = None, head
        
        while currentNode: #This is just the list of nodes.
            temp = currentNode.next #Need to save the next node location.
            currentNode.next = prevNode #Going to set p
            prevNode = currentNode
            currentNode = temp
        return prevNode #THis was the only thing that I didn't do.