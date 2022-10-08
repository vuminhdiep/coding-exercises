class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        #Constraints: O(1) space
        #Frequency > 10 -> split to characters
        #counter to store freq of characters
        #use two pointers to loop through array
        
        #Complexity: O(n) time, O(1) space
        if len(chars) < 2: #if only 1 character -> no need to compress
            return len(chars)
        index = 0 #the index to the new compress character in the array
        i = 0 #slow pointer to the first index
        while i < len(chars):
            j = i #fast pointer to loop through the array
            while j < len(chars) and chars[j] == chars[i]: #check if see the same character, increment j
                j += 1
            count_freq = j - i #the frequency of chars[i]
            chars[index] = chars[i] #set the chars[index] to represent chars[i] 
            index += 1
            
            if count_freq > 1: #only consider 2 more characters
                for digit in str(count_freq): #append the frequency of chars[i]
                    chars[index] = digit
                    index += 1
            i = j #set pointer i = j when chars[i] != chars[j] to iterate next
        chars = chars[:index] #modify the array to have the new length up to index with the string compressed
        return index #the current index is also the new length of the array