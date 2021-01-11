# Hướng giải bài này là dựng cây Trie.
# Để đảm bảo điều kiện không có chuỗi nào là tiền tố của chuỗi khác thì trên đường đi từ gốc của cây Trie đến chuỗi bất kì không được đi qua nút có đánh dấu là tận cùng của chuỗi khác.
# Ví dụ tạo cây có 2 chuỗi độ dài là 2, 32,3. Nếu chuỗi có độ dài 2 đã có đường đi là Root \to 0 \to 0Root→0→0 thì nút 00 sau cùng được đánh dấu là kết thúc chuỗi thì chuỗi có độ dài 3 không được phép lưu dạng Root \to 0 \to 0 \to 0Root→0→0→0 hay Root \to 0 \to 0 \to 1Root→0→0→1.
#
# Nếu có hai chuỗi mà chuỗi này là tiền tố của chuỗi còn lại ta gọi đó là vi phạm.
# Có hai ưu tiên trong bài này:
# Do lưu từ gốc đến cuối chuỗi nên ưu tiên tạo chuỗi theo độ dài từ nhỏ đến lớn, để có thể xử lý tránh bị vi phạm.
# Để có thể tạo được nhiều chuỗi hợp lý nhất ta ưu tiên tạo theo thứ tự từ điển nhỏ nhất.
# Ví dụ tạo cây có độ dài chuỗi là 22 và 33. Nếu chuỗi có độ dài 22 lưu là Root \to 0 \to 0Root→0→0 thì chuỗi có độ dài 33 ta ưu tiên lưu là Root \to 0 \to 1 \to 0Root→0→1→0 (mặc dù Root \to 0 \to 1 \to 1Root→0→1→1 và Root \to 1 \to 0 \to 0Root→1→0→0 là 2 cách vẫn đúng nhưng về thứ tự từ điển hai cách này đều lớn hơn cách đã chọn).
# Tiến hành dựng cây:
# Khái niệm nút chặn là nút khi đi qua chắc chắn bị vi phạm.
# Ví dụ: Ở ví dụ trên khi tạo chuỗi có độ dài 22 lưu là Root \to 0 \to 0Root→0→0 thì nút 00 sau cùng được coi là nút chặn vì khi tạo chuỗi độ dài 33 đi qua nút đó có thể được các chuỗi lưu là Root \to 0 \to 0 \to 0Root→0→0→0 và Root \to 0 \to 0 \to 1Root→0→0→1 và chúng đều vi phạm.
#
# Nếu một nút đi tới 2 nút chặn thì nó cũng là nút chặn. Ví dụ tạo 3 chuỗi độ dài lần lượt là 2, 2, 32,2,3. Sau khi tạo 2 chuỗi độ dài 22 lưu là Root \to 0 \to 0Root→0→0 và Root \to 0 \to 1Root→0→1 thì nút 00 đầu tiên trở thành nút chặn bởi đi qua nút 00 đó chắn chắn sẽ tiếp tực đi qua nút chặn khác và sẽ bị vi phạm.
# Phải sắp xếp lại các độ dài tăng dần để tiến hành tạo chuỗi.
# Tiến hành tạo chuỗi:
# Lần lượt đi qua các nút, ưu tiên đi qua nút 00 trước nếu có thể, để có thứ tự từ điển nhỏ nhất.
# Không đi qua các nút chặn.
# Sau khi tạo chuỗi phải kiểm tra cập nhật lại các nút chặn mới trên đường đi từ gốc tới nút tận cùng lưu chuỗi đó.
# Ví dụ tạo 3 chuỗi độ dài lần lượt là 2, 2, 32,2,3. Sau khi tạo 2 chuỗi độ dài 22 lưu là Root \to 0 \to 0Root→0→0 và Root \to 0 \to 1Root→0→1 thì nút 0 đầu tiên được cập nhập trở thành nút chặn. (Lưu ý nút chặn mới được hình thành chỉ trên đường đi từ gốc tới nút tận cùng lưu chuỗi mới tạo)
#
# Độ phức tạp: O(N \cdot L)O(N⋅L), với NN là số lượng từ trong ngôn ngữ Old Berland, LL là độ dài tối đa của mỗi từ.
#


import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, val):
        self.child = dict()
        self.is_blocked = False
        self.val = val


class Trie:
    def __init__(self):
        self.root = Node('')

    def add(self, length, id, res):
        st = [self.root]
        while length and len(st):
            u = st[-1]
            length -= 1
            if 0 not in u.child:
                u.child[0] = Node('0')
            if not u.child[0].is_blocked:
                st.append(u.child[0])
            else:
                if 1 not in u.child:
                    u.child[1] = Node('1')
                if not u.child[1].is_blocked:
                    st.append(u.child[1])
                else:
                    u.is_blocked = True
                    length += 2
                    st.pop()
        if length == 0:
            st[-1].is_blocked = True
            res[id] = ''.join(node.val for node in st)
            return True
        return False


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted([(a[i], i) for i in range(n)])

    trie = Trie()
    res = [None] * n
    for length, i in a:
        if not trie.add(length, i, res):
            print('NO')
            exit()

    print('YES')
    for length in res:
        print(length)


