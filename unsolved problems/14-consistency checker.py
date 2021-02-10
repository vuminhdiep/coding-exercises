# Bạn sẽ thêm từng từ trong danh sách các từ, hàm thêm từ bạn cần phải chỉnh sửa lại một chút. Trong lúc thêm từng ký tự vào bạn xét nếu như trước đó đã có ký tự đó rồi thì lúc này bạn sẽ “break” và thoát khỏi hàm ngay lập tức. Ngược lại thì bạn vẫn thêm vào bình thường như thêm một từ mới.


class Node:
    def __init__(self):
        self.end_word = False
        self.child = dict()


def addWord(root, s):
    temp = root
    s_prefix_other = False
    other_prefix_s = True

    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
            other_prefix_s = False

        temp = temp.child[ch]
        if temp.end_word:
            s_prefix_other = True

    temp.end_word = True
    return s_prefix_other or other_prefix_s


t = int(input())
for tc in range(t):
    n = int(input())
    root = Node()
    is_inconsistent = False

    for _ in range(n):
        if not is_inconsistent:
            is_inconsistent = addWord(root, input())
        else:
            input()

    print('Case {}: {}'.format(tc + 1, 'NO' if is_inconsistent else 'YES'))