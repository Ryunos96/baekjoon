while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    maxline = max(x, y, z)
    if maxline >= x + y + z - maxline:
        print("Invalid")
    elif x == y == z:
        print("Equilateral")
    elif x == y or x == z or y == z:
        print("Isosceles")
    else:
        print("Scalene")