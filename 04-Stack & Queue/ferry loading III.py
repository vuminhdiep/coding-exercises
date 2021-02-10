
import queue


class Car:
    def __init__(self, _id, _arriveTime):
        self.id = _id
        self.arriveTime = _arriveTime
    


Q = int(input())

for _ in range(Q):
    qSide = [[], []]
    qSide[0] = queue.Queue()
    qSide[1] = queue.Queue()
    res = [0] * 10005

    n, t, m = map(int, input().split())

    for i in range(m):
        arrived, atBank = input().split()

        if atBank == "left":
            qSide[0].put(Car(i, int(arrived)))
        else:
            qSide[1].put(Car(i, int(arrived)))

    curTime, curSide = 0, 0
    waiting = (not qSide[0].empty()) + (not qSide[1].empty())

    while waiting:
        if waiting == 1:
            nextTime = qSide[1].queue[0].arriveTime if qSide[0].empty() else qSide[0].queue[0].arriveTime
        else:
            nextTime = min(qSide[0].queue[0].arriveTime, qSide[1].queue[0].arriveTime)

        curTime = max(curTime, nextTime)
        carried = 0

        while not qSide[curSide].empty():
            car = qSide[curSide].queue[0]
            if car.arriveTime <= curTime and carried < n:
                res[car.id] = curTime + t
                carried += 1
                qSide[curSide].get()
            else:
                break

        curTime += t
        curSide = 1 - curSide
        waiting = (not qSide[0].empty()) + (not qSide[1].empty())

    for i in range(m):
        print(res[i])

    if _ < Q - 1:
        print()

