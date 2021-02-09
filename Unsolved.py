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

need_tree = array = automaton = False
def getChar(s):
    return chr(s + ord('a'))

s = input()
t = input()

for i in range(26):
    count_t = t.count(getChar(t))
    count_s = s.count(getChar(s))
if count_t > count_s:
    need_tree = True
elif count_t < count_s:
    automaton = True

index = 0
match = -1

for i in range(t):
    index = s.find(t[i],match+1)
    if index > match:
        match = index
    else:
        array = True
        break


if need_tree:
    print("Need tree")
elif automaton:
    print("Automaton")
elif array:
    print("Array")
else:
    print("both")