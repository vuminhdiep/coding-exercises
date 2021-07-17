# Agoji Print
#  Flag Question
# Agoda has its own line of emojis called Agojis, and because every Agodan loves Agojis, now everyone wants Agoji stickers! To fulfill this request, the People Team director wants to print $N$ Agojis.
#
# Agojis come in $M$ unique styles, and for each style, there is a minimum $A$ requirement and a maximum $B$ requirement ($A\gt 0$, $B\ge A$) for printing.
#
# In order to print the Agojis, you must calculate the number of distinct ways that $N$ Agojis can be printed, while satisfying the minimum and maximum requirement for each unique style of Agoji. Since the answer could be a very large number, please calculate your answer using mod $1e9+7$.
#
# Input Format
# The first line contains two integers, $N$ and $M$ (total Agojis and types of Agojis).
#
# The second line ($M$) contains two integers, $A$ and $B$ (minimum and maximum requirements of $0 \lt A \le B \le N$ for Agojis of $i^{th}$ type in $i^{th}$ line).
#
# Constraints:
# $1\le N \le 1e6$
#
# $1\le M\le 16$
#
# $0\lt A \le B \le N$
#
# Output Format
# A single integer (using mod $1e9+7$) that represents the number of distinct ways the Agojis can be printed.

from itertools import permutations

def main():
    N, M = map(int, input().split())
    for k in range(M):
        A, B = map(int,input().split())

        x = [numbers for numbers in range(A,B+1)]
    # Get all permutations of [1, 2, 3]
        perm = permutations(x)
        res = []
        for j in range(1,len(x)-1):
            res.append((x[j],x[j],x[j]))
        # Print the obtained permutations
        for i in list(perm):
            res.append(i)
    print(res)
if __name__ == '__main__':
    main()
