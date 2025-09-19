num = int(input())

for i in range(1, num+1):
    st = ""
    for j in range(1, i+1):
        st += "*"
    print(st)