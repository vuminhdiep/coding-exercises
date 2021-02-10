from collections import deque

tc = 1

while True:
    P, C = map(int, input().split())
    if P == 0 and C == 0:
        break

    q = deque()
    for i in range(1, min(P, C) + 1):
        q.append(i)

    print('Case {}:'.format(tc))
    tc += 1

    for _ in range(C):
        line = input().split()
        cmd = line[0]

        if cmd == 'N':
            print(q[0])
            q.append(q.popleft())
        else:
            x = int(line[1])
            n = len(q)
            q.append(x)
            for i in range(n):
                temp = q.popleft()
                if temp != x:
                    q.append(temp)
                    