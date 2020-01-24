items = [100, 200, 600, 400, 1200, 1400, 1500]

item_len = len(items)

print(item_len)

for i in items:
    print(i)

for i in range(0, 3, 2):
    print(items[i])


items = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

for i in range(1, len(items) - 1, 2):
    print(items[i])