# Bài toán này khi ta gộp 2 người uu và vv lại với nhau, đồng nghĩa với việc ta sẽ gộp cả nhóm lại. Như vậy cấu trúc dùng để gộp tập hợp hay phân biệt tập hợp mà ta có thể nghĩ đến đó là Disjoint set Union find.
#
# Ta sử dụng một mảng cnt[x]cnt[x] với ý nghĩa: Số lượng người trong nhóm mà nhận xx làm người đại diện tối cao.
#
# Khi ta ở truy vấn hiện tại, số lượng người trong nhóm đông nhất chắc chắn sẽ không nhỏ hơn số lượng người trong nhóm đông nhất ở truy vấn trước. Bởi vì khi ta gộp nhóm lại thì nhóm đông nhất chỉ có thể tăng lên chứ không hề có sự sụt giảm. Vì vậy, để tính toán số lượng người trong nhóm đông nhất, ta chỉ cần một biến maximaxi dùng để lưu lại. Khi ta dùng hàm unionSet(u, v)unionSet(u,v) nhằm gộp 2 nhóm có chứa người uu và vv lại thành một, ta chỉ việc cập nhật maxi = max(maxi, cnt[r])maxi=max(maxi,cnt[r]) (với rr là đỉnh đại diện của nhóm tổng quát của cả 2 nhóm có chứa uu và vv).
#
# Tuy nhiên, vấn đề ở đây ta mắc phải đó là số lượng người trong nhóm ít nhất. Số lượng người trong nhóm ít nhất lại bị thay đổi theo chiều hướng tăng lên sau mỗi truy vấn. Để có thể xử lý vấn đề này, ta cần sử dụng một Min Heap để làm điều này. Ta sẽ tổ chức Min Heap với các phần tử trong Min Heap là một kiểu dữ liệu ta tự định nghĩa ra. Kiểu dữ liệu tự định nghĩa này của ta chứa 2 thành phần, gồm uu và cntcnt, tương ứng là đỉnh đại diện của một nhóm và số lượng người của nhóm mà uu làm đại diện. Min Heap sẽ ưu tiên phần tử có cntcnt nhỏ hơn lên đầu.
#
# Đầu tiên, vì NN người ban đầu là NN nhóm hoàn toàn riêng biệt, tức mỗi nhóm chỉ gồm 1 người, do đó ta bỏ các cặp (1, i)(1,i) vào Min Heap.
#
# Với mỗi truy vấn u vuv, sau khi ta cập nhật maximaxi rồi, ta sẽ tìm nhóm có số lượng người ít nhất bằng cách như sau:
#
# Bỏ (cnt[r], r)(cnt[r],r) vào Min Heap, với rr và cnt[r]cnt[r] tương ứng là đỉnh đại diện mới cho tập có chứa uu và vv và số lượng người trong tập có rr làm đại diện.
#
# Lấy phần tử đầu tiên trong Min Heap, giả sử là phần tử (cnt, u)(cnt,u).
#
# Đặt root = findRoot(u)root=findRoot(u), tức ta đang truy vấn tới người đại diện cho nhóm có chứa uu, nếu như root != uroot!=u thì rõ ràng uu hiện tại không phải là 1 người đại diện cho một nhóm nào cả, ta loại phần tử (cnt, u)(cnt,u) ra khỏi Min Heap.
#
# Trong trường hợp root = uroot=u, ta cần kiểm tra tiếp liệu cnt = cnt[root]cnt=cnt[root] hay không. Nếu không phải có nghĩa đây là một phần tử cũ rồi, nhóm mà người rootroot hiện tại đại diện có số lượng lớn hơn, ta cũng ngay lập tức loại (cnt, u)(cnt,u) ra khỏi Min Heap.
#
# Ngược lại thì dừng quá trình lấy phần tử trong Min Heap ra.
#
# In kết quả là maxi – cnt ra output.
#
# Độ phức tạp: O(Q * log(N))O(Q∗log(N)) với QQ là số lượng truy vấn, NN là số lượng người còn sống sót.
#
# Lưu ý: Bài này nếu ai sử dụng Disjoint set union find một cách bình thường thì sẽ bị timelimit, để Accepted được bài này cần sử dụng thêm Path Compression hoặc Union By Rank hoặc cả 2.


from queue import PriorityQueue

MAX_N = 100005

root = [0] * MAX_N
cnt = [0] * MAX_N
maxi = 1
pq = PriorityQueue()

def findRoot(u):
    if u == root[u]:
        return u
    root[u] = findRoot(root[u])

    return root[u]

def unionSet(u, v):
    global maxi

    uu = findRoot(u)
    vv = findRoot(v)

    if uu != vv:
        cnt[uu] += cnt[vv]
        root[vv] = uu
        pq.put((cnt[uu], uu))
        maxi = max(maxi, cnt[uu])

def main():
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        cnt[i] = 1
        root[i] = i
        pq.put((1, i))

    for i in range(m):
        u, v = map(int, input().split())
        unionSet(u, v)
        while True:
            tmp = pq.queue[0]
            r = findRoot(tmp[1])
            if r != tmp[1]:
                pq.get()
                continue

            if cnt[r] != tmp[0]:
                pq.get()
                continue

            break

        print(maxi - pq.queue[0][0])

if __name__ == "__main__":
    main()