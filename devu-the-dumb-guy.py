# https://codeforces.com/problemset/problem/439/B

n, x = map(int, input().split())
subjects = list(map(int, input().split()))


def selfLearning(subjects, x):
    subjects.sort()
    min_time = 0
    for subject in subjects:
        min_time += subject * x
        if x > 1:
            x -= 1
    return min_time


res = selfLearning(subjects, x)
print(res)