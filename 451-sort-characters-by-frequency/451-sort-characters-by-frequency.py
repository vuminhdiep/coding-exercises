from heapq import *
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        #put character in hash map
        #place character, freq in maxHeap
        #pop the maxHeap and append to empty string to get new sorted string
        #Complexity: O(nlogn + n) time, space: O(n)
        freq = {}
        maxHeap = []
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        for char, char_freq in freq.items():
            heapq.heappush(maxHeap, (-char_freq, char)) #make freq negative so that put in first
        sorted_str = ""
        while maxHeap:
            freq, char = heappop(maxHeap)
            for i in range(-freq): #have to revert back to positive number
                sorted_str += char
        return sorted_str
  