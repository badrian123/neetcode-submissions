class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None


        # =========================================
        # STAGE 1: CREATE THE COPIES
        # =========================================

        l1 = head

        while l1:

            # Create the copy
            l2 = Node(l1.val)

            # Temporarily store the original random target
            # inside the copy's .next
            l2.next = l1.random

            # Temporarily store the copy
            # inside the original node's .random
            l1.random = l2

            # Move through the original list
            l1 = l1.next


        # Save the head of the copied list
        newHead = head.random



        # =========================================
        # STAGE 2: SET THE COPIES' RANDOM POINTERS
        # =========================================

        l1 = head

        while l1:

            # Retrieve the copy
            l2 = l1.random

            # Give the copy its correct random pointer
            l2.random = l2.next.random if l2.next else None

            # Move through the original list
            l1 = l1.next



        # =========================================
        # STAGE 3: RESTORE + SEPARATE THE TWO LISTS
        # =========================================

        l1 = head

        while l1 is not None:

            # Retrieve the copy
            l2 = l1.random

            # Restore the original node's random pointer
            l1.random = l2.next

            # Connect this copy to the next copy
            l2.next = l1.next.random if l1.next else None

            # Move through the original list
            l1 = l1.next



        # =========================================
        # FINAL: RETURN THE COPIED LIST
        # =========================================

        return newHead