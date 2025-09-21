arr = []
for idx in range(9):
    a = int(input())
    arr.append((idx+1, a))

max_num = max(arr, key=lambda x: x[1])

print(max_num[1])
print(max_num[0])