#https://codeforces.com/problemset/problem/448/B

# Trước tiên ta có nhận xét như sau:
#
# Nếu có một ký tự nào trong tt mà không có trong ss thì chắc chắn ta không thể biến đổi chuỗi ss thành chuỗi tt được -> “need tree”.
# Nếu có một ký tự nào trong ss mà không có ký tự trong tt thì ta phải bỏ đi ký tự đó -> “automaton”.
# Phép biến đổi “array” hoán đổi vị trí của hai ký tự chỉ cần thiết nếu thứ tự xuất hiện của các ký tự trong chuỗi tt không trùng khớp với thứ tự của các ký tự đó trong chuỗi ss.
# Để giải quyết trường hợp 1 và 2, ta sử dụng một mảng đếm tần suất xuất hiện của từng ký tự trong chuỗi ss và chuỗi tt. Sau đó duyệt từng ký tự trong bảng chữ cái gồm 26 chữ:
#
# Nếu tần suất xuất hiện của ký tự đó trong chuỗi tt lớn hơn chuỗi ss, nghĩa là chuỗi ss không đủ ký tự để ta biến đổi thành chuỗi tt -> “need tree”.
# Nếu tần suất xuất hiện của ký tự đó trong chuỗi tt nhỏ hơn chuỗi ss, nghĩa là sẽ có một số ký tự thừa -> “automaton”.
# Ta cần giải quyết trường hợp 3 để có thể đưa ra kết luận là “array” hay “both”.
#
# Bằng cách duyệt qua từng ký tự trong chuỗi tt, ta tìm vị trí của ký tự tương ứng trong chuỗi ss. Nếu các vị trí này tăng dần nghĩa là các ký tự này đã đúng vị trí, ta không cần đổi chỗ. Ngược lại ta kết luận “array”.
#
# Xem xét liệu “automaton” và “array” có cùng thỏa hay không để đưa ra kết luận là “both”.
#
# Độ phức tạp: O(max(length(s), length(t))O(max(length(s),length(t))

def getChar(x):
    return chr(x + ord('a'))

s = input()
t = input()

need_tree = array = automaton = False

for i in range(26):
    t_count = t.count(getChar(i))
    s_count = s.count(getChar(i))

    if t_count > s_count:
        need_tree = True
    elif t_count < s_count:
        automaton = True

index_found, match = 0, -1

for i in range(len(t)):
    index_found = s.find(t[i], match + 1)
    if index_found > match:
        match = index_found
    else:
        array = True
        break

if need_tree:
    print("need tree")
elif automaton and array:
    print("both")
elif automaton:
    print("automaton")
else:
    print("array")