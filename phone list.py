class Node:
    def __init__(self):
        self.end_word = False
        self.child = dict()


def addWord(root, s):
    temp = root
    s_prefix_other = False
    other_prefix_s = True

    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
            other_prefix_s = False

        temp = temp.child[ch]
        if temp.end_word:
            s_prefix_other = True

    temp.end_word = True
    return s_prefix_other or other_prefix_s


t = int(input())
for tc in range(t):
    n = int(input())
    root = Node()
    is_inconsistent = False

    for _ in range(n):
        if not is_inconsistent:
            is_inconsistent = addWord(root, input())
        else:
            input()

    print('NO' if is_inconsistent else 'YES')