# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #I would have to iterate through the list no?
            #Well, I'd mainly would have to use the while loop in order to access the head / current node
            #The loop would need to update the curr so that it can continue to iterate through the linkedlist
            #But doing this for two nodes though? How would that work?
                #I'd probably would need to keep track of the locations that I am at before proceeding ahead
                #Like I'd need to check the values and based on whichever value is the biggest or equal,two scenarios, i'd mainly would
                    #have to store the node that i did not work on to the side.
                    #Store the node that I did work on in the newely being created noded
                    #And then repeat the process in checking the nodes so that I can make a sorted linkedlist.
        dummy = node = ListNode()
        
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