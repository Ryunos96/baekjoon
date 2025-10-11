N, K = map(int, input().split())

arr = []
a = int(N/2)
for i in range(1, a+1):
    if N % i == 0:
        arr.append(i)
arr.append(N)
if K > len(arr):
    print("0")
else:
    print(arr[K-1])