arr = [list(map(int, input().split())) for _ in range(9)]

max_val, row, col = max(
    (val, i, j)
    for i, row in enumerate(arr)
    for j, val in enumerate(row)
)

print(max_val)
print(row+1, col+1)