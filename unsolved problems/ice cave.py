# Bạn bắt đầu đi từ ô bị nứt (X) sau đó bạn phải đi được tới đích bằng những đường đấu “.” (ô nguyên)

# Nếu ô đích của bạn là ô X (ô nứt) thì bạn chỉ cần 1 đường đi tới đó. Vì nhiệm vụ của bạn là thoát khỏi Level này nên cần gặp ô nứt để qua Level khác.
# Nếu ô đích của bạn là “.” thì phải đi đến được đó và xung quanh của ô đó phải có ít nhất 1 ô “.” Để sau khi bạn nhảy xong 1 lần nó trở thành ô nứt rồi bạn nhảy qua ô khác rồi nhảy lại để qua được Level đó.

from queue import Queue

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

MAX = 500 + 1
level = [None] * MAX

def BFS(sr, sc, fr, fc):
    q = Queue()
    q.put((sr, sc))
    level[sr][sc] = 'X'

    while q.qsize() > 0:
        ur, uc = q.get()

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r == fr and c == fc and level[r][c] == 'X':
                return True

            if r in range(n) and c in range(m) and level[r][c] == '.':
                level[r][c] = 'X'
                q.put((r, c))

    return False

n, m = map(int, input().split())

for i in range(n):
    level[i] = list(input())

sr, sc = map(int, input().split())
fr, fc = map(int, input().split())

print("YES" if BFS(sr - 1, sc - 1, fr - 1, fc - 1) else "NO")