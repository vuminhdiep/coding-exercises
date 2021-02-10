class Node:
    def __init__(self, value):
        self.countWord = 0
        self.child = dict()
        self.weight = value


def addWord(root, s, val):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node(val)
        temp = temp.child[ch]
        if val > temp.weight:
            temp.weight = val
    temp.countWord += 1


def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return False
        temp = temp.child[ch]
    return temp.weight


n, q = list(map(int, input().split()))

root = Node(0)

for _ in range(n):
    word, weight = input().split()
    addWord(root, word, int(weight))

results = []
for _ in range(q):
    t = input()
    results.append(findWord(root, t))

for item in results:
    if not item:
        print(-1)
    else:
        print(item)