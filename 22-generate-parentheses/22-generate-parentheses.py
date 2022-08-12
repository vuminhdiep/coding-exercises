from collections import deque

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #Take all combinations previously and add ( or )
        #Can't have more than N ( 
        #Keep count of ( and )
        #Use BFS
        #Complexity: O(n * 2^N) time and space
        
        result = []
        queue = deque()
        openCount = 0
        closeCount = 0
        queue.append(("", openCount, closeCount))
        while queue:
            paren = queue.popleft()
           
            
            if paren[1] == n and paren[2] == n: #if reach maximum ( and ), add to result
                result.append(paren[0])
            else:
                if paren[1] < n: #if we can add more open paren
                    queue.append((paren[0] + "(", paren[1] + 1, paren[2]))
                
                if paren[1] > paren[2]: #if we can add more close paren
                    queue.append((paren[0] + ")", paren[1], paren[2] + 1))
        
        return result