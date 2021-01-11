class Node:
   def __init__(self):
      self.n_common = 0
      self.child = dict()


def addWord(root, s):
   global res
   temp = root
   for i in range(len(s)):
      ch = s[i]
      level = i + 1
      if ch not in temp.child:
         temp.child[ch] = Node()
      temp = temp.child[ch]
      temp.n_common += 1
      res = max(res, temp.n_common * level)

t = int(input())
for tc in range(t):
   n = int(input())
   root = Node()
   res = 0
   for _ in range(n):
      addWord(root, input())
   print('Case {}: {}'.format(tc + 1, res))