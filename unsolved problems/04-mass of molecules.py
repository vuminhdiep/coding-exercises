# Duyệt từng ký tự trong chuỗi hóa chất:

# Nếu ký tự đó là chữ ‘C’, ‘H’, hoặc ‘O’ thì bỏ lần lượt số 1212, 11, 1616 vào stack.

# Nếu ký tự là số thì lấy phần tử đầu stack ra và nhân với số này, rồi bỏ lại vào trong stack.

# Nếu ký tự đó là mở ngoặc ‘((‘ thì bỏ vào -1−1 stack giống ‘C’, ‘H’, ‘O’.

# Nếu ký tự đó là đóng ngoặc ‘))’ thì lấy các số trong stack ra và cộng lại với nhau cho đến khi nào gặp -1−1 (nghĩa là dấu mở ngoặc) thì ngưng.

# Khi duyệt xong toàn bộ chuỗi hóa chất thì lấy toàn bộ số trong stack ra cộng lại và đó là kết quả của bài toán cần tìm.

atom = []
mass = lambda c : 1 if c == 'H' else 12 if c == 'C' else 16
 
for c in input().strip():
    if c.isalpha():
        atom.append(mass(c))
    elif c.isnumeric():
        mol = atom[-1] * int(c)
        atom.pop()
        atom.append(mol)
    elif c == '(':
        atom.append(-1)
    elif c == ')':
        w = 0
        while atom[-1] != -1:
            w += atom[-1]
            atom.pop()
        atom.pop()
        atom.append(w)
 
print(sum(atom))