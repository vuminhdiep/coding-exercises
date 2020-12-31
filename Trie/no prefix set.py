
def add(root, s):
    temp = root
    length = len(s)
    for ch, char in enumerate(s):
        if char in temp:
            if temp[char]:
                if ch == length - 1:
                    return False
                else:
                    temp = temp[char]
            else:
                return False
        else:
            temp[char] = dict()
            temp = temp[char]

    return True


if __name__ == '__main__':
    n = int(input())
    trie = dict()

    bad = False
    for i in range(n):
        new = input()
        if not add(trie, new):
            bad = True
            break

    if bad:
        print("BAD SET")
        print(new)
    else:
        print("GOOD SET")

