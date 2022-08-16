class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #find all indices of word1
        #find all indices of word2
        #get min distance = min(index word1 - index word2)
        minIndex1 = -1
        minIndex2 = -1
        distance = len(wordsDict) + 1
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                minIndex1 = i
            if wordsDict[i] == word2:
                minIndex2 = i
            if minIndex1 != -1 and minIndex2 != -1:
                distance = min(distance, abs(minIndex1 - minIndex2))
        return distance