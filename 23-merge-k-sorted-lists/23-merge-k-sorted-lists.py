from heapq import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #put the head of each sorted array to minHeap, then pop out to put into the merged sorted list
        #Complexity: O(n*logk) time, O(n) space where n is length of lists, k is length of heap
        
        minHeap = []
        for root in lists:
            if root is not None:
                heapq.heappush(minHeap, (root.val, root)) #add the top node of linkedlists to the heap
        resultHead = None
        resultTail = None
        while minHeap:
            node = heapq.heappop(minHeap)[1]
            if resultHead is None:
                resultHead = node # take the smallest(top) element form the min-heap and add it to the result
                resultTail = node
            else:
                resultTail.next = node
                resultTail = resultTail.next
            if node.next is not None:
                heapq.heappush(minHeap, (node.next.val, node.next)) # if the top element has a next element add it to the heap
        return resultHead
                