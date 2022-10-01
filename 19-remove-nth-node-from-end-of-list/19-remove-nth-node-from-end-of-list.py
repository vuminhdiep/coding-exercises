# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #Complexity: O(L) time, L is length of linkedlist, O(1) space
        #i = jump to length(head) - n 
        #j = 0
        #remove length - n + 1 element from the list
        #find list length
        #set a pointer to dummy node and move till L - n node and connect with L - n + 2 node
        dummy = ListNode(0)
        dummy.next = head
        temp = head
        length = 0
        while temp is not None: #find the length of linkedlist
            length += 1
            temp = temp.next
        length = length - n #get to L - n node
        temp = dummy
        while length > 0:
            length -= 1
            temp = temp.next
        temp.next = temp.next.next #connect length - n node to length - n + 2 node
        return dummy.next