class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        #Constraints: just all consist of lowercase english
        #length of s and p >= 1
        #hashmap or set to keep track of string p in s 
        #Use sliding window, check if hashmap_s == hashmap_p
        #pop the first added element in hashmap_s and add another element in hashmap_s as loop through string s to make sure hashmap_s always has the same number of key:value pairs as hashmap_p
        if len(s) < len(p):
            return []
        result = []
        hashmap_p = {}
        hashmap_s = {}
        
        #loop through string p and add to hashmap, initialize two hashmaps with the substring length p
        for i in range(len(p)):
            if p[i] not in hashmap_p:
                hashmap_p[p[i]] = 1
            else:
                hashmap_p[p[i]] += 1
            
            if s[i] not in hashmap_s:
                hashmap_s[s[i]] = 1
            else:
                hashmap_s[s[i]] += 1
        if hashmap_s == hashmap_p:
            result = [0] #this means the first substring s is an anagram of string p so we add 0 index
        else:
            result = []
        left = 0
        for right in range(len(p), len(s)): #check from the second substring at index len(p) because the first substring already checked above
            if s[right] not in hashmap_s:
                hashmap_s[s[right]] = 1
            else:
                hashmap_s[s[right]] += 1
            hashmap_s[s[left]] -= 1 #decrement the left pointer as we add more character from right pointer to the hashmap, to keep the hashmap_s has same length as hashmap_p
            
            if hashmap_s[s[left]] == 0: 
                hashmap_s.pop(s[left]) #delete the first added element in hashmap_s to keep hashmap_s hash same length as hashmap_p -> to have space add s[right] to hashmap_s
            left += 1 #increment left pointer to keep window distance of right - left = len(p)
            
            if hashmap_s == hashmap_p:
                result.append(left) #if two hashmaps are equal which means substring s has anagram of p, add the index of left pointer to result array
        return result
            