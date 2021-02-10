n = int(input())
penguins = {
    "Emperor Penguin": 0,
    "Macaroni Penguin": 0,
    "Little Penguin": 0
}
for i in range(n):
    x = input()
    if x == "Emperor Penguin":
        penguins["Emperor Penguin"] += 1
    elif x == "Macaroni Penguin":
        penguins["Macaroni Penguin"] += 1
    elif x == "Little Penguin":
        penguins["Little Penguin"] += 1

max_penguin = max(penguins["Emperor Penguin"],penguins["Macaroni Penguin"],penguins["Little Penguin"])

key_list = list(penguins.keys())
val_list = list(penguins.values())

position = val_list.index(max_penguin)
print(key_list[position])