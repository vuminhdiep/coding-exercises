class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        start = 0
        end = n - 1
        if target >= letters[n - 1] or target < letters[0]:
            return letters[0]
        while start <= end:
            mid = start + (end - start) // 2
            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return letters[start] 