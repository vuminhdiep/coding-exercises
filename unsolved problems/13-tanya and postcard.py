# Ta thấy rằng các kí tự chỉ là kí tự alphabet in hoa hoặc in thường, vậy thì ta có thể tạo 22 cấu trúc tìm kiếm (map với C++, TreeMap với java hoặc dict với Python) là aa và bb, với aa dùng để lưu các kí tự cần trong chuỗi ss và số lượng tương ứng của nó, bb dùng để lưu các kí tự có trong chuỗi tt cùng số lần xuất hiện tương ứng của chúng.
#
# Vì đề yêu cầu ưu tiên “YAY!” trước, nghĩa là đúng kí tự và đúng hoa thường. Vậy thì ta sẽ duyệt qua 5252 loại kí tự khác nhau, giả sử dụng số lần xuất hiện của kí tự chch trong chuỗi ss là a[ch]a[ch] và số lần xuất hiện trong chuỗi tt sẽ là b[ch]b[ch]. Như vậy, số lần mà Tanya có thể hô lên “YAY!” sẽ là min(a[ch], b[ch])min(a[ch],b[ch]). Ta cộng vào kết quả, đồng thời giảm cả a[ch]a[ch], b[ch]b[ch] xuống một lượng bằng giá trị minmin vừa có (tức đã dùng các kí tự đó để tạo lá thư).
#
# Tương tự, với “WHOOPS” thì với mỗi kí tự chch trong aa, ta sẽ tìm số lần xuất hiện của kí tự ngược trạng thái hoa thường với chch ở trong bb và tính số lần hô “WHOOPS” tương tự như cách tính với “YAY!”
#
# Độ phức tạp: Độ phức tạp của thao tác tìm kiếm trong map là O(logK)O(logK) với KK là số loại kí tự khác nhau. Do đó:
#
# Độ phức tạp thao tác tìm kiếm và cập nhật số lượng ký tự trong chuỗi s là O(|s|logK)O(∣s∣logK), và tương tự trong t là O(|t|logK)O(∣t∣logK).
# Duyệt lại trên toàn bộ kí tự và truy cập giá trị trong map nên có độ phức tạp là O(KlogK)O(KlogK).
# Hơn nữa, |s| < |t|∣s∣<∣t∣ nên độ phức tạp của bài toán là O((K + |t|)logK)O((K+∣t∣)logK) với K = 52K=52.

message = input()
newspaper = input()
a = dict([ (i, 0) for i in range(52) ])
b = dict([ (i, 0) for i in range(52) ])
for ch in message:
    id = ord(ch) - 65
    if (ch > 'Z'):
        id = ord(ch) - 97 + 26
    if not id in a:
        a[id] = 1
    else:
        a[id] += 1
for ch in newspaper:
    id = ord(ch) - 65
    if (ch > 'Z'):
        id = ord(ch) - 97 + 26
    if not id in b:
        b[id] = 1
    else:
        b[id] += 1
yay = 0
whoops = 0
for i in range(52):
    tmp = min(a[i], b[i])
    yay += tmp
    a[i] -= tmp
    b[i] -= tmp
for i in range(26):
    whoops += min(a[i], b[i+26]) + min(a[i+26], b[i])
print("%d %d" % (yay, whoops))
