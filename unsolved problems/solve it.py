# Bài này có 2 cách giải:
#
# Cách 1: Ta sẽ dùng phương pháp tìm nghiệm của Newton. Cụ thể, ta sẽ đặt một nghiệm x_0x
#  cho trước, tất nhiên x_0phải nằm trong tập xác định ban đầu của đề bài. Sau đó, ta duyệt một vòng lặp từ 11 đến một hằng số nào đó, ở đây ta sẽ chọn số lần lặp là một số nn nào đó, với công thức như sau: x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}x'
#                                                                                                                                                                                                                                            f'n+1
# =x
# n
#  −
# f
# ′
# (x
# n
# )
# f(x
# n
# )
# , trong đó, f'(x)f
# ​′
# ​​ (x) là đạo hàm bậc một của hàm số f(x)f(x) trên một tập xác định cho trước. Kết quả là x_nx
# ​n
# ​​ . Số nn ở đây ta sẽ chọn đủ lớn để f(x_n)f(x
# ​n
# ​​ ) chênh lệch so với giá trị 00 một giá trị eps nào đó mà bạn cảm thấy ổn.
#
# Cách 2: Nếu ta để ý với dữ kiện của đề bài, cộng với một số tính chất đặc biệt của hàm số. Ta quan tâm đến các điều kiện 0 \leq p,r \leq 200≤p,r≤20 và {-20} \leq q,s,t \leq 0−20≤q,s,t≤0, đồng thời ta thấy nghiệm xx lại là một số không âm. Điều này đặt ra cho ta một câu hỏi, liệu hàm số f(x)f(x) của ta có một tính chất đặc biệt nào đó?
#
# Thật vậy, trước hết ta có nhận xét: f(x)f(x) là một hàm số liên tục trên tập xác định D=[0,1]D=[0,1]. Do có tính chất liên tục như thế, ta hoàn toàn có thể lấy đạo hàm bậc một của f(x)f(x) với mọi nghiệm x trong tập xác định cho trước. Hàm số sau khi ta lấy đạo hàm bậc 11 như sau: f'(x) = {-p} \cdot e^{-x} + q \cdot \cos(x) - r \cdot \sin(x) + \frac{s}{\cos(x)^2} + 2 \cdot x \cdot t\ \forall x \in Df
# ​′
# ​​ (x)=−p⋅e
# ​−x
# ​​ +q⋅cos(x)−r⋅sin(x)+
# ​cos(x)
# ​2
# ​​
# ​
# ​s
# ​​ +2⋅x⋅t ∀x∈D Như vậy, ta có thể phát hiện ra các tính chất sau:
#
# p \geq 0,\ e^{-x} > 0\ \forall x \in [0,1] \Rightarrow -p \cdot e^{-x} \leq 0p≥0, e
# ​−x
# ​​ >0 ∀x∈[0,1]⇒−p⋅e
# ​−x
# ​​ ≤0
# q \leq 0,\ \cos(x) > 0\ \forall x \in [0,1] \Rightarrow q \cdot \cos(x) \leq 0q≤0, cos(x)>0 ∀x∈[0,1]⇒q⋅cos(x)≤0
# r \geq 0,\ \sin(x) > 0\ \forall x \in [0,1] \Rightarrow {-r} \cdot \sin(x) \leq 0r≥0, sin(x)>0 ∀x∈[0,1]⇒−r⋅sin(x)≤0
# s \leq 0,\ \frac{1}{\cos(x)^2} \geq 0\ \forall x \in [0,1] \Rightarrow \frac{s}{\cos(x)^2} \leq 0s≤0,
# ​cos(x)
# ​2
# ​​
# ​
# ​1
# ​​ ≥0 ∀x∈[0,1]⇒
# ​cos(x)
# ​2
# ​​
# ​
# ​s
# ​​ ≤0
# t \leq 0 \Rightarrow 2 \cdot x \cdot t \leq 0\ \forall x \in [0,1]t≤0⇒2⋅x⋅t≤0 ∀x∈[0,1]
# Do đó: f'(x) \leq 0\ \forall x \in [0,1]f
# ​′
# ​​ (x)≤0 ∀x∈[0,1]. Tuy nhiên, trường hợp f'(x) = 0f
# ​′
# ​​ (x)=0 khi và chỉ khi các hệ số p,q,r,s,tp,q,r,s,t đều bằng 00. Khi đó, phương trình sẽ vô nghiệm do lúc đó ta chỉ còn lại phương trình u = 0u=0. Nên đây là trường hợp không thể xảy ra.
#
# Từ đó, ta hoàn toàn có thể dễ dàng đánh giá được f'(x) < 0f
# ​′
# ​​ (x)<0 ∀x ∈ [0,1] . Khi đạo hàm bậc một của một hàm số có giá trị âm, ta có thể đưa ra kết luận f(x)f(x) là một hàm số nghịch biến trên tập xác định D = [0,1]D=[0,1]. Như vậy, với x_0 > x_1x
# ​0
# ​​ >x
# ​1
# ​​  thì f( x_0 ) \leq f( x_1 )f(x
# ​0
# ​​ )≤f(x
# ​1
# ​​ ). Như vậy, dựa vào tính chất hàm số nghịch biến này, ta hoàn toàn có thể sử dụng kỹ thuật chặt nhị phân như sau:
#
# Ta sẽ kiểm tra xem phương trình của ta có vô nghiệm hay không. Đồng nghĩa với việc ta kiểm tra f(1) > 0f(1)>0 hay f(0) < 0f(0)<0 hay không ? Nếu có thì ta kết luận phương trình này vô nghiệm, ta in ra No solution.
# Ta đặt l = 0, r = 1l=0,r=1, cứ mỗi lần l \leq rl≤r, ta đặt x = \frac{l+r}{2}x=
# ​2
# ​
# ​l+r
# ​​ , nếu f(x) > 0f(x)>0, ta kết luận rằng nghiệm của phương trình phải nằm trong đoạn [x ... r][x...r], do đó, ta di chuyển l = xl=x, ngược lại, ta kết luận nghiệm phương trình nằm trong đoạn [l ... x][l...x], nên ta di chuyển r = xr=x. Tuy nhiên, thực tế việc chặt nhị phân trên một đoạn số thực cho đến khi l > rl>r là điều không thể. Do đó, ta sẽ cố định số lần lặp là một hằng số, để từ đó kết quả của ta chính là x sau khi lặp đúng số lần như thế. Ta sẽ chọn số lần lặp là một số TT nào đó sao cho bạn đọc thấy ổn là được.
# Cách để ta tìm số TT như sau: Ta thấy rằng mỗi lần ta chọn giá trị ở giữa, thì khoảng cách giữa l,rl,r lại giảm đi \frac{1}{2}
# ​2
# ​
# ​1
# ​​ . Đề yêu cầu ta phải tìm ra kết quả phải chính xác tới 4 chữ số thập phân, điều này có nghĩa là giá trị ta tìm ra chênh lệch so với giá trị đáp án thực tế tối đa là 10^{-6}10
# ​−6
# ​​ .
#
# Như vậy, nếu như ta lặp lại TT lần, thì khoảng cách r - l = \frac{1}{2}^Tr−l=
# ​2
# ​
# ​1
# ​​
# ​T
# ​​  , đồng thời chắc chắn đáp án thực tế phải là một số KK nào đó mà l \leq K \leq rl≤K≤r.
#
# Ta có: K - l \leq r - l = \frac{1}{2}^TK−l≤r−l=
# ​2
# ​
# ​1
# ​​
# ​T
# ​​ ; nên ta chỉ cần chọn TT sao cho \frac{1}{2}^T \leq 10^{-6} \Leftrightarrow 2^{-T} \leq 10^{-6} \Leftrightarrow T \geq 20
# ​2
# ​
# ​1
# ​​
# ​T
# ​​ ≤10
# ​−6
# ​​ ⇔2
# ​−T
# ​​ ≤10
# ​−6
# ​​ ⇔T≥20.
#
# Tức là ta phải cho số lần lặp tối thiểu 2020 lần. Bạn có thể cho số lần lặp nhiều hơn để có thể ra kết quả ổn định hơn.
#
# Độ phức tạp: O(T.N)O(T.N) với TT là số bộ test và NN là số vòng lặp (NN tối thiểu là 20).

import math

def inp():
    return map(int, input().split(' '))

def f(p , q , r , s , t , u , x):
    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u

def solve():
    while True:
        try:
            p, q, r, s, t, u = map(float, input().split(' '))

            if f(p, q, r, s, t, u, 1.0) > 1e-9 or p + r + u < 0:
                print("No solution")
                continue

            res = -1
            lo = 0.000
            hi = 1.000
            for i in range(100):
                mid = (lo + hi) / 2.0
                F = f(p, q, r, s, t, u, mid)
                if F > 0:
                    lo = mid
                else:
                    hi = mid
            print('{:0.4f}'.format(lo))
        except EOFError:
            break

solve()