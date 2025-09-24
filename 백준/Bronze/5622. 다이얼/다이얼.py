S = input()

dict = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

time = 0

for i in S:
    for j in range(len(dict)):
        if i in dict[j]:
            time += j + 3

print(time)