class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Complexity: Time O(m*n)
        # if needle == "":
        #     return 0
        # elif needle in haystack:
        #     return haystack.find(needle)
        # return -1

        if not needle or haystack == needle:
            return 0

        length_needle = len(needle)
        length_haystack = len(haystack)

        if length_needle > length_haystack:
            return - 1

        for i in range(length_haystack):
            index = 0
            for j in range(i, i + length_needle):
                if j >= length_haystack:
                    return -1
                if haystack[j] == needle[index]:
                    index += 1
                    continue
                else:
                    break
            if index == length_needle:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("", ""))
