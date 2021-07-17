# Codegoda City is preparing to welcome back international tourists. The city is full of attractions, many of which can be reached through several bi-directional connections. However, some attractions are connected through only one pathway. These one-path connections are called Goji Connections, and the local mayor is concerned that once tourism is open, these connections may produce large crowds that inhibit social distancing.
#
# The mayor wants to expand these one-path connections to create more connections and safer tourism. However, Codegoda City has never mapped all the Goji Connections. Please help the local mayor to find all the Goji Connections so international travel to Codegoda City can start again!
#
# Input Format:
#
# First line: N represents the number of attractions.
#
# Next N lines: attraction number, colon, then attraction numbers separated by commas.
#
# Ex. 2:3, 4 means that Attraction 2 is connected to Attraction 3 and Attraction 4.
#
# Output Format:
#
# First line: C - number of Goji Connections
#
# Next lines: list of Goji connections in ascending order by number of the first attraction. The connection starts from the attractions with lower number.
#
# For example, this is a valid output:
#
# 2
# 1-4
# 3-5
# and these are not valid:
#
# 2
# 3-5
# 1-4
# 2
# 4-1
# 3-5
# Sample Input:
#
# 4
# 1: 2
# 2: 1, 3, 4
# 3: 2, 4
# 4: 2, 3
#
# Sample Output:
# 1
# 1-2


import queue

MAX = 1000 + 5
visited = [False] * MAX
dist = [0] * MAX
graph = [[] for i in range(MAX)]

def BFS(s):
    q = queue.Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.put(v)
def main():
    Q = int(input())

    for _ in range(Q):
        V, E = map(int, input().split())

        for i in range(MAX):        #reset graph
            graph[i].clear()
            visited[i] = False
            dist[i] = 0

        for i in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        s = int(input())
        BFS(s)

        for i in range(1, V + 1):
            if i == s:
                continue

            print(dist[i] * 6 if visited[i] else -1, end=' ')

        print()

if __name__ == '__main__':
    main()