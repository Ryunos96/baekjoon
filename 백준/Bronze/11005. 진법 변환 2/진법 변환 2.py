N, B = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while True:
    if N == 0:
        break
    result += digits[N % B]
    N = N // B

print(result[::-1])