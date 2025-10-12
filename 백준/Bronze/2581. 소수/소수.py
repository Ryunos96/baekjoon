M = int(input())

N = int(input())

arr = []
for i in range(M, N + 1):
    if i == 1:
        continue
    is_prime = True
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        arr.append(i)

if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)