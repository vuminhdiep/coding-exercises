#Find the maximum number of pairs that have sum equal. The numbers appear only once in the pairs.

A = [1,9,9,8,100,2]
A = list(set(A))
chk = []
count = 1
for i in range(len(A)):
    for j in (A[i + 1:]):
        if (A[i] + j) in chk:
            count += 1
            chk.append(A[i] + j)
        else:
            chk.append(A[i] + j)

print(count)

