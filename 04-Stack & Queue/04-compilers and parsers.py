# Với mỗi biểu thức, ta bắt đầu duyệt lần lượt từng kí tự trong chuỗi: Gặp kí tự ‘<<’ ta bỏ vào stack, ngược lại:

# Xét xem stack có rỗng không: nếu rỗng nghĩa là có dấu ‘>>’ nhưng không có dấu ‘<<’ nào trước nó nên ta ngưng duyệt chuỗi.
# Ngược lại, ta lấy phần đầu của stack ra và một lần nữa kiểm tra xem stack có rỗng không, nếu có ta cập nhật kết quả là i+1.
# Độ phức tạp: O(T∗N) với T là số lượng test case và N là số lượng biểu thức.

t = int(input())
for j in range(t):
    expression = input()
    res = 0
    stack = []

    for i in range(len(expression)):
        if expression[i] == '<':
            stack.append(expression[i])
        elif len(stack) == 0:
            break

        else:
            stack.pop()
            if len(stack) == 0:
                res = i + 1
            # res = i + 1 if len(stack) == 0 else res

    print(res)





















# T = int(input())
#
# for _ in range(T):
#     s = input()
#     expr = []
#     ans = 0
#
#     for i in range(len(s)):
#         if s[i] == '<':
#             expr.append(s[i])
#         elif len(expr) == 0:
#             break
#         else:
#             expr.pop()
#             ans = i + 1 if len(expr) == 0 else ans
#
#     print(ans)