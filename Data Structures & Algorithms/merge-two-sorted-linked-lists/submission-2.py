# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #This will create a fake node
        dummy = ListNode()
        #This will be used to create our node
        node = dummy
        
        #I like this because it will examine both nodes
        while list1 and list2:
            #How we are doing this is by the values.
            if list1.val < list2.val:
                #Going to have to store list1.val into node b/c that's what we are creating.
                node.next = list1
                #Here we need to get the next value in this list
                list1 = list1.next
            else:
                node.next = list2
                #Here we need to get the next value in this list
                list2 = list2.next
            #Need to prepare for environment so going to go to the next node for node
            node = node.next #I think so because this is setting current node to the next node.    
        
        #This is for any remaining pointers that are left. 
        node.next = list1 or list2
        
        return dummy.next  #this is the actual beginning of the list