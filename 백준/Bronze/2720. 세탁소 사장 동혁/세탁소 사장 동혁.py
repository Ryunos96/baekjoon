T = int(input())

coins = [25, 10, 5, 1]

for _ in range(T):
    result = []
    C = int(input())

    for i in coins:
        result.append(C // i)
        C %= i
    
    print(*result, end="\n")
