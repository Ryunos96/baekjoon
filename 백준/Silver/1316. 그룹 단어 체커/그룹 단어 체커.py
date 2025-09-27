N = int(input())
cnt = 0

for s in range(N):
    str_s = input()
    seen = set()
    prev = ''
    truth = True
    for i in str_s:
        if i != prev:
            if i in seen:
                truth = False
                break
            seen.add(i)
        prev = i
    if truth:
        cnt += 1
print(cnt)