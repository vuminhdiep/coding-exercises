#Find the longest substring with same letter begin and end

s = "performance"
if not s:
    print(s)
longest_substring = ""
for i in range(len(s)):
    index = s.rfind(s[i]) #Find the index of the last occurrence of a specific value. If not found return -1
    if len(s[i:index+1]) > len(longest_substring):
        longest_substring = s[i:index+1]
print(longest_substring)
