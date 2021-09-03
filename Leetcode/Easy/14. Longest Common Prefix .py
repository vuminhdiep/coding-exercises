class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #Vertical scanning
        #Compare character by character of two words in strs, if the characters are different at index i, return the substring starting from index 0 up to index i

        if not strs:
            return ""

        shortest = min(strs, key=len)  # Find the word with the shortest length in strs

        for i, char in enumerate(shortest):

            for words in strs:
                if words[i] != char:
                    return shortest[:i]  # Going up but not including the last i characters
        return shortest


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
