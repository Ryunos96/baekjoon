N = int(input())

arr = list(map(int, input().split()))
cnt = 0

for num in arr:
    if num == 1:
        continue
    flag = 1
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            flag = 0
            break
    if flag == 1:
        cnt += 1

print(cnt)