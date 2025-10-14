x, y, w, h = map(int, input().split())

arr = []

arr.append(int(w - x))
arr.append(int(h - y))
arr.append(int(x))
arr.append(int(y))

print(min(arr))