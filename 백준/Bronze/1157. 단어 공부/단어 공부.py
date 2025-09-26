word = input().strip().upper()

unique = set(word)

max_cnt = 0
result = '?'

for i in unique:
    cnt = word.count(i)
    if cnt > max_cnt:
        max_cnt = cnt
        result = i
    elif cnt == max_cnt:
        result = '?'
print(result)