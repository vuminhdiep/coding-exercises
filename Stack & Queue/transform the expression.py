#Source code transform the expression: https://www.spoj.com/problems/ONP/
def transform(expression):
    s = []
    for symbol in expression:
        if symbol.isalpha():
            print(symbol, end=' ')
        elif symbol == ')':
            print(s.pop(), end=' ')
        elif symbol != '(':
            s.append(symbol)

    print()

t= int(input())
for i in range(t):
    expression = input()
    transform(expression)