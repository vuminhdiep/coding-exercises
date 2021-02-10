# Nhận xét: Nếu làm theo thứ tự bình thường như mô tả của đề thì việc khi xóa đi một đỉnh sẽ làm mất rất nhiều cạnh, gây ảnh hưởng lớn đến đồ thị và khiến việc tính lại đường đi ngắn nhất giữa mọi cặp đỉnh là rất khó khăn.
#
# Duyệt ngược thứ tự các đỉnh và giả sử như ta đang thêm dần các đỉnh vào đồ thị để xử lý dễ dàng hơn.
# Ứng dụng Floyd Warshall vào bài này, ta nhận xét rằng bản chất của việc xóa các đỉnh (thêm các đỉnh nếu xét theo chiều người lại) chính là đang chọn đỉnh đó làm một đỉnh trung gian mới. Từ đó ta chạy thuật toán với đỉnh trung gian được chọn và tính tổng khoảng cách ngắn nhất lúc bấy giờ, lưu vào mảng kết quả.


n = int(input())
dist = [[0] * (n + 1)]

for i in range(1, n + 1):
    dist.append([0] + list(map(int, input().split())))

middleV = list(map(int, input().split()))
res = [0] * n

for index in range(n - 1, -1, -1):
    k = middleV[index]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for u in middleV[index:]:
        for v in middleV[index:]:
            res[index] += dist[u][v]

print(*res)