class qandmax(object):
    def __init__(self):
        self.__a = list()
        self.__size = 0

    def __len__(self):
        return self.__size

    def add(self, num):
        self.__a.append(num)
        self.__size += 1

    def mayor(self):
        self.__may = 0
        for i in range(self.__len__()):
            if self.__may < self.__a[i][0]:
                self.__may = self.__a[i][0]

    def consulm(self):
        return self.__may

    def queue(self):
        if self.__a[0][0] < self.__may:
            self.__a.append(self.__a[0]);
            del self.__a[0]
            self.queue()

    def remove_m(self):
        assert self.__size > 0
        del self.__a[0]
        self.__size -= 1

    def verificar(self):
        if self.__a[0][1] == True:
            return True
        else:
            return False

    def consul(self):
        return self.__a


from sys import stdin


def solve(n, pior, A):
    QM = qandmax()
    for i in range(len(A)):
        if i == pior:
            QM.add([A[i], True])
        else:
            QM.add([A[i], False])
    ver, cont = False, 0
    while ver == False:
        QM.mayor()
        QM.queue()
        ver = QM.verificar()
        if ver == True:
            break
        else:
            QM.remove_m()
        cont += 1
    return cont + 1


def main():
    inp = stdin
    case = int(inp.readline())
    while case != 0:
        pre = [int(x) for x in inp.readline().strip().split()]
        n, pior = pre[0], pre[1]
        lista = [int(y) for y in inp.readline().strip().split()]
        print(solve(n, pior, lista))
        case -= 1

main()