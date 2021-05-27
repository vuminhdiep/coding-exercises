class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        roman_value = 0
        for i in range(0,len(s)-1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                roman_value -= roman_dict[s[i]]
            else:
                roman_value += roman_dict[s[i]]
        return roman_value+roman_dict[s[-1]] #Do this to avoid index out of range

        # s = s.replace("IV", "IIII").replace("IX", "VIIII")
        # s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        # for char in s:
        #     roman_value += roman_dict[char]
        # return roman_value


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
