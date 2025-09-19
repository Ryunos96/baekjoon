a = int(input())
b = int(input())
original = b
while(b != 0):
    tmp = b % 10
    print(a * tmp)
    b = b // 10
print(a * original)