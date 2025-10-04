X = int(input())

num = 1

while X > (num * (num + 1) // 2):    
    num += 1

if num % 2 == 0:
    numup = X - ((num - 1) * num // 2)
    numdown = num - (X - (num - 1) * num // 2) + 1
else:
    numup = num - (X - (num - 1) * num // 2) + 1
    numdown = X - ((num - 1) * num // 2)

print(f"{numup}/{numdown}")