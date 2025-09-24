T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    result = ""
    for st in S:
        result += st * R
    print(result)