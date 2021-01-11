# Bạn sẽ thêm từng chuỗi trong danh sách vào cây trie. Mỗi nút của cây trie sẽ chứa liên kết đến 26 nút con và một biến xác định nút này có phải nút lá hay không. Sẽ có hai trường hợp cần chú ý khi thêm một chuỗi vào cây trie: • Trong cây trie hiện tại tồn tại một chuỗi trùng với phần đầu của chuỗi đang thêm: khi đó chỉ cần kiểm tra nút mình đang xét có phải là nút lá hay không. • Chuỗi đang thêm vào trùng với phần đầu của một chuỗi nào đó đã được thêm vào trie trước đó: lúc này cần kiểm tra xem đường đi từ gốc đến nút lá của chuỗi này có tạo thêm nút mới hay không. Độ phức tạp: O(string\_length * N)O(string_length∗N) với NN là số lượng mật khẩu và string\_lengthstring_length là độ dài tối đa mật khẩu.


class Node:
    def __init__(self):
        self.child = dict()
        self.isLeaf = False

def addWord(root, s):
    flag = False
    temp = root
    for ch in list(s):
        if ch not in temp.child:
            flag = True
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.isLeaf:
            return False
    temp.isLeaf = True
    return flag

n = int(input())
root = Node()
nonVulnerable = True
for i in range(n):
    s = input()
    nonVulnerable &= addWord(root, s)
print(("non " if nonVulnerable else "") + "vulnerable")