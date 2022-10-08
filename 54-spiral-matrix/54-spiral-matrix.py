class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #Complexity: O(m * n) time, O(1) space
        #Go boundary to boundary and move inwards. First row, last column, last row, first column, move inwards by 1 and repeat
        #Go top left, move right, down, left, up
        #start with (row, col)
        #move right: (row, col + 1)
        #move down: (row + 1, col)
        #move left: (row, col - 1)
        #move up: (row - 1, col)
        
        #have 4 pointers left, right, top, bottom, go right, down, left, up
        #when go right => increment top pointer
        #when go down => decrement right pointer
        #when go left => decrement bottom pointer
        #when go up => increment left pointer
        #break when left, right pointer overlap over top,bottom pointer overlap
        
        left = 0
        right = len(matrix[0]) #set right to be out of bound initially
        top = 0
        bottom = len(matrix) #set bottom to be out of bound initially
        
        result = []
        
        while left < right and top < bottom:
            #Move right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1 #increment the top pointer after done moving top edge
            
            #Move down
            for i in range(top, bottom):
                result.append(matrix[i][right - 1]) #right - 1 because right is out of bound initially
            right -= 1 #decrement right pointer after done moving right edge
            
            if not(left < right and top < bottom): #break when there's no rectangle to traverse
                break
            #Move left
            for i in range(right - 1, left - 1, -1): #go reverse to move left
                result.append(matrix[bottom - 1][i]) #bottom - 1 because bottom is out of bound initially
            bottom -= 1 #decrement bottom pointer after done moving bottom edge
            
            #Move up
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1 #increment left pointer after done moving left edge
        
        return result