found = list(map(int, input().split()))


default = [1, 1, 2, 2, 2, 8]

result = [d - f for d, f in zip(default, found)]

print(*result)