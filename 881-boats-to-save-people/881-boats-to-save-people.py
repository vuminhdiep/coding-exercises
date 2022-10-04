class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        #Sort the people
        #Iteratively Pair lightest to heaviest
        #if heaviest > limit, move to the second heaviest
        #stop iteration when pass pointer
        #Complexity: O(nlogn) time, O(logn) space
        
        
        n = len(people)   
        people.sort()     
        count_boats = 0
        i = 0
        j = n - 1
      
        while i <= j:
            count_boats += 1
            if people[i] + people[j] <= limit: 
                i += 1 
            j -= 1
            
        return count_boats 
        
        