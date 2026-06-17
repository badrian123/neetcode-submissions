# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1 #Get's stored
                list1 = list1.next #Moves list1 to next node
            else:
                node.next = list2 #Get's stored
                list2 = list2.next #Moves list2 to next node
            node = node.next #Moving the node to the next node.
        node.next = list1 or list2 #This is getting any remaining nodes.
        return dummy.next #Why? Is this because it is still in the begining of the linkedlist?
