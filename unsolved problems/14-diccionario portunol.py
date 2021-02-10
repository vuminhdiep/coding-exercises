# Ý tưởng cơ bản để giải quyết bài toán: Lấy từng prefixprefix ghép với từng suffixsuffix và đếm số lượng từ được tạo thành. Tuy nhiên với cách làm này, ta sẽ có những từ bị đếm trùng. Ta nhận thấy rằng từ “abc…defXuvt…xyz” sẽ bị đếm trùng nếu như ta xem “abc…defX” + “uvt…xyz” và “abc…def” + “Xuvt…xyz” là hai từ khác nhau. Tổng quát lên khi ta có X là ký tự cuối trong prefixprefix và X cũng là ký tự đầu trong suffixsuffix thì sẽ xuất hiện hiện tượng đếm trùng. Như vậy ta cách tốt nhất để tránh hiện tượng trên là ta sẽ loại bỏ đi hết tất cả các từ có X là ký tự đầu trong suffixsuffix (hoặc tất cả các từ có X là ký tự cuối trong prefixprefix). Gọi p[X]p[X] là số lượng từ trong prefixprefix bắt đầu bằng ký tự ‘X’, s[X]s[X] là số lượng từ trong suffixsuffix bắt đầu bằng ký tự ‘X’. Ta có công thức chung để tính số lượng từ khác nhau được tạo thành:
#
# Số từ = (Tổng prefix) * (Tổng suffix) - (p[‘a’] * s[‘a’] + … + p[‘z’] * s[‘z’])
#
# Trong đó:
#
# Tổng prefixprefix được tính bằng cách duyệt cây Trie các từ tiếng Bồ Đào Nha.
# Tổng suffixsuffix được tính bằng cách duyệt cây Trie các từ tiếng Tây Ban Nha. Tuy nhiên đề bài lại có ràng buộc rằng cả suffixsuffix và prefixprefix đều không được rỗng, do đó khi tính s[X]s[X] ta không được đếm ký tự ở cuối cùng (hay ký tự đầu tiên của suffixsuffix khi đảo ngược).
# Độ phức tạp: Độ phức tạp của thuật toán bằng tổng kích thước của 2 cây Trie. Trong trường hợp xấu nhất, mỗi từ sẽ nằm ở 1 nhánh khác nhau và tổng độ phức tạp sẽ bằng kích thước input. Tuy nhiên input chỉ chứa tối đa 10^510
# ​5
# ​​  kí tự cho các từ Tây Ban Nha và 10^510
# ​5
# ​​  kí tự cho các từ Bồ Đào Nha, suy ra độ phức tạp là O(2 * 10^5)O(2∗10
# ​5
# ​​ ).


import string
import sys

sys.setrecursionlimit(10000000)


class TrieNode:
    def __init__(self):
        self.count_leaf = 0
        self.child = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.count_leaf += 1


def suffix_traversal(root, level, start_with):
    cnt = 1
    for c in root.child:
        if level > 0:
            start_with[c] += 1
        cnt += suffix_traversal(root.child[c], level + 1, start_with)

    return cnt


def prefix_traversal(root, level, suffix_state_count, start_with):
    res = 0
    if level > 0:
        res = suffix_state_count
    for c in root.child:
        if level > 0:
            res -= start_with[c]
        res += prefix_traversal(root.child[c], level + 1, suffix_state_count, start_with)

    return res


if __name__ == '__main__':
    while True:
        p, s = map(int, input().split())
        if p == s == 0:
            break

        suffix_trie = Trie()
        prefix_trie = Trie()

        for i in range(p):
            prefix_trie.add_word(input())

        for i in range(s):
            suffix_trie.add_word(input()[::-1])

        start_with = {c: 0 for c in string.ascii_lowercase}
        suffix_state_count = suffix_traversal(suffix_trie.root, 0, start_with) - 1
        print(prefix_traversal(prefix_trie.root, 0, suffix_state_count, start_with))

