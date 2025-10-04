A, B, V = map(int, input().split())

num = ((V - A) // (A - B)) + 1

if (V - A) % (A - B) != 0:
    num += 1

print(num)