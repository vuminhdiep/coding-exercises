# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        #Complexity: O(logn) time, O(1) space
        start = 0
        end = 1
        while reader.get(end) < target:
            start = end
            end = end * 2
        return self.binary_search(reader, target, start, end)
    
    def binary_search(self, reader, target, start, end):
        while start <= end:
            mid = (end + start) // 2
            if reader.get(mid) > target:
                end = mid - 1
            elif reader.get(mid) < target:
                start = mid + 1
            else:
                return mid
        return -1
        