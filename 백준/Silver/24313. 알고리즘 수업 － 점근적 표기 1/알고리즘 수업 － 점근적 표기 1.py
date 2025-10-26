a, b = map(int, input().split())
c = int(input())
num = int(input())


if a <= c and a * num + b <= c * num:
    print(1)
else:
    print(0)