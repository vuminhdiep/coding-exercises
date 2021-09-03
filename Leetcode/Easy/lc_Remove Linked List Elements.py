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

        while (temp != None and temp.val == val):
            head = temp.next
            temp = head
        while (temp != None):
            while (temp != None and temp.val != val):
                prev = temp
                temp = temp.next

            if (temp == None):
                return head

            prev.next = temp.next
            temp = prev.next
        return head