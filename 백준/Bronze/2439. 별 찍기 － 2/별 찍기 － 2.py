num = int(input())

for i in range(1, num+1):
    st = ""
    for j in range(1, num-i+1):
        st += " "
    for k in range(num-i, num):
        st += "*"
    print(st)