class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

    #Dung stack de luu cac parentheses. Neu o trong stack chua co gi thi push vao {, [, (. Neu gap }, ], ) ma match voi phan tu dang truoc cua stack thi pop ra
    #So sanh cac phan tu pop cua stack voi cac values cua dict parentheses, neu k match thi return False, else True
    # Avoid pop from empty stack thi can initialize stack co 1 empty string

        parentheses = {")":"(", "}":"{","]":"["}
        stack = [""]
        for char in s:
            if char in parentheses.keys():
                if stack.pop() != parentheses[char]:
                    return False
            
            else:
                stack.append(char)

        return len(stack) == 1 #avoid pop from empty stack
                
if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{()}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid(""))
    


        