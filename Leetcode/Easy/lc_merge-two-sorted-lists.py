# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(node=ListNode):
    while node is not None:
        print(str(node.val), end=" ")
        node = node.next
    print()


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #Time complexity: O (m+n) with m and n are the number of nodes in l1, l2
        # Space complexity: O(1)
        # Compare both the list at every instance. If one node is less than the other, we will increment the count of
        # that list and add it to the dummy node Pointer is the current pointer of a dummy node
        dummy = pointer = ListNode(0)
        while l1 and l2:  # While both l1 and l2 not None
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next

            else:
                pointer.next = l2
                l2 = l2.next

            pointer = pointer.next

        # now we will see if there are still some elements left then we will add them as well
        # Add all the nodes in l1, if remaining
        if l1:
            pointer.next = l1
        elif l2:
            pointer.next = l2
        # Add all the nodes in l2, if remaining
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    printList(s.mergeTwoLists(l1, l2))
