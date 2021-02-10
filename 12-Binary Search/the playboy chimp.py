def binSearch(a, length, val):
    left, right = 0, length - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == val:
            return mid - 1, mid + 1
        if a[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return right, left


def main():

    n = int(input())
    height = list(map(int,input().split()))
    sorted(height)

    chimps = []
    last = -1

    for x in height:
        if x != last:
            chimps.append(x)  # Keeps only the unique elements.
            last = x
    q = int(input())
    queries = list(map(int,input().split()))
    sorted(queries)

    sz = len(chimps)


    for q in queries:
        a, b = binSearch(chimps, sz, q)
        tallest = str(chimps[a]) if a >= 0 else 'X'
        shortest = str(chimps[b]) if b < sz else 'X'
        print(tallest,shortest)


if __name__ == '__main__':
    main()