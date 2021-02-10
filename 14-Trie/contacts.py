contacts_book = dict()


def add(word):
    temp = contacts_book
    for ch in word:
        if ch not in temp:
            temp[ch] = {}
            temp[ch]['count'] = 1
        else:
            temp[ch]['count'] += 1
        temp = temp[ch]
    temp[None] = None


def find(word):
    temp = contacts_book
    for ch in word:
        if ch not in temp:
            return 0
        temp = temp[ch]
    return temp['count']


n = int(input())
for i in range(n):
    q = input().strip().split(' ')
    operation = q[0]
    name = q[1]
    if operation == 'add':
        add(name)
    else:
        print(find(name))