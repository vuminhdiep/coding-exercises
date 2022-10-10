class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #Sliding window
        #Constraints: just all consist of lowercase english
        #length of s and p >= 1
        #hashmap or set to keep track of string p in s
        #{a: 1, b: 1, c: 1}
        #s = "cbaebabacd", p = "abc"
        #.       i
        #.    j
        #i - j = len(p)
        #if s[j:i] in hashmap -> add j to output array
        #increment i, j
        
        #"abcab" {a: 1, b: 1}
        #      i
         #   j 
            #if i == len(s) - 1:
            #check s[i - len(p) : i] in hashmap
            #i out ouf bound -> i - j < p
        #Use sliding window, check if hashmap_s == hashmap_p
        #pop the first added element in hashmap_s and add another element in hashmap_s as loop through string s to make sure hashmap_s always has the same number of key:value pairs as hashmap_p
        if len(s) < len(p):
            return []
        result = []
        hashmap_p = {}
        hashmap_s = {}
        
        #loop through string p and add to hashmap, initialize two hashmaps
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
            result = [0]
        else:
            result = []
        left = 0
        for right in range(len(p), len(s)):
            if s[right] not in hashmap_s:
                hashmap_s[s[right]] = 1
            else:
                hashmap_s[s[right]] += 1
            hashmap_s[s[left]] -= 1
            
            if hashmap_s[s[left]] == 0:
                hashmap_s.pop(s[left])
            left += 1
            
            if hashmap_s == hashmap_p:
                result.append(left)
        return result
            