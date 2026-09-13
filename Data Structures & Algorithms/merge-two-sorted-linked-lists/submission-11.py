# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #So I am given two lists
        #[1,2,4] and [1,3,5]
        #I know that I have to iterate through both of the list.
        #I know that I have to check the values in order to see which is lowests.
        #I know that I have to create a dummy node and update it.
        #I know that i have to update the dummy node on every iteration.

        dummy = ListNode()
        node = dummy
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next