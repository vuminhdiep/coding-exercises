
# Night at the Museum https://codeforces.com/problemset/problem/731/A

def main():
    n = input()
    s = map(ord, n)

    res = 0
    curr = 0

    A = ord('a')
    Z = ord('z')

    for x in s:
        if A <= x <= Z:
            x -= A
            res += min(abs(x - curr), 26 - abs(x - curr))
            curr = x
        else:
            break

    print(res)


if __name__ == '__main__':
    main()
