N = int(input())
answer = 0

for i in range(1, N):
    if N == sum(map(int, str(i))) + i:
        answer = i
        break
print(answer)