# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #Use fast and slow pointer
        #connect the first half of linkedlist to the reverse of the second half of linkedlist
        #O(n) time, O(1) space
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
    
        second_half = self.reverse(slow)
        first_half = head

        while first_half is not None and second_half is not None:
            temp = first_half.next #To connect node of first half to second: Connect 1-> 4
            first_half.next = second_half
            first_half = temp

            temp = second_half.next #To connect node of second half to first: Connect 2->3
            second_half.next = first_half
            second_half = temp

        if first_half is not None:
            first_half.next = None
        return head
      
    def reverse(self, head):
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        