N = int(input())

arr = list(map(int, input().split()))

max_score = max(arr)

arr = [x / max_score * 100 for x in arr]

print(sum(arr)/ N)