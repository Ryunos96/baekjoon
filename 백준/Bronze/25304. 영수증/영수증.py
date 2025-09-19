sum = int(input())
cnt = int(input())
exp = 0

while (cnt):
    cost, num = map(int, input().split())
    exp += cost * num
    cnt -= 1

if sum == exp:
    print("Yes")
else:
    print("No")