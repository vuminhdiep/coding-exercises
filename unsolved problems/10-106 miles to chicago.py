# Để giải quyết bài này, trước hết ta cần nhớ lại kiến thức về xác suất, cụ thể là quy tắc nhân được phát biểu như sau: “Nếu một công việc nào đó phải hoàn thành qua nn giai đoạn liên tiếp, trong đó:
#
# Phương án thứ 1 có m_1 cách thực hiện.
# Phương án thứ 2 có m_2 cách thực hiện.
# ...
# Phương án thứ n có m_n cách thực hiện.
# Khi đó sẽ có m_1 * m_2 * ... * m_n cách để hoàn thành công việc được cho.
#
# Từ đó ta quy ra công thức tính xác suất đi từ uu đến vv qua nn tuyến đường chính bằng tích của nn tuyến đường đó với nhau, với trọng số của mỗi tuyến đường được quy về xác suất thay vì phần trăm như đề cho.
#
# Sau đó sử dụng thuật toán Bellman-Ford để tìm tuyến đường có tích lớn nhất xuất phát từ đỉnh 1 và không cần thiết kiểm tra chu trình âm vì chắc chắn tích xác suất luôn lớn hơn hoặc bằng 00:
#
# Gán xác suất để đi từ đỉnh 1 đến các đỉnh còn lại là -1.0 (nghĩa là ta chưa tìm được đường đi tới các đỉnh này).
# Xác suất để đi từ đỉnh 1 đến chính nó bằng 1.0
# Với mỗi cạnh (u, v)(u,v):
# Nếu tích xác suất của con đường mới từ 1 đến uu thông qua vv lớn hơn xác suất hiện tại đi từ 1 đến uu thì ta cập nhật lại.
# Tương tự, nếu tích xác suất của con đường mới từ 1 đến vv thông qua uu lớn hơn xác suất hiện tại đi từ 1 đến vv thì cập nhật lại.
# Cuối cùng in ra kết quả chính xác đến 6 chữ số thập phân.
#
# Lưu ý: Thuật toán Bellman-Ford chỉ có thể áp dụng trên đồ thị vô hướng có trọng số dương vì một cạnh có trọng số âm trong đồ thị vô hướng tạo nên một chu trình âm.

def BellmanFord():
    prob[1] = 1.0

    for i in range(n - 1):
        for edge in graph:
            u, v, w = edge
            prob[u] = max(prob[u], prob[v] * w)
            prob[v] = max(prob[v], prob[u] * w)


while True:
    line = list(map(int, input().split()))
    if len(line) == 1:
        break

    graph = []
    n, m = line[0], line[1]

    for _ in range(m):
        u, v, c = map(int, input().split())
        graph.append((u, v, c / 100))

    prob = [-1.0] * (n + 1)
    BellmanFord()

    print("{:.6f} percent".format(prob[n] * 100))