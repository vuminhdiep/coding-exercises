# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        prev = None

        while temp is not None and temp.val == val:
            head = temp.next
            temp = head
        while temp is not None:
            while temp is not None and temp.val != val:
                prev = temp
                temp = temp.next

            if temp is None:
                return head

            prev.next = temp.next
            temp = prev.next
        return head
