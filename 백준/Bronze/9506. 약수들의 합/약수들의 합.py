while True:
    N = int(input())
    if N == -1:
        break

    arr =[]
    sum = 0
    cnt = 0
    str = ""
    a = int(N/2)
    for i in range(1, a+1):
        if N % i == 0:
            sum += i
            cnt += 1
            arr.append(i)

    if sum == N:
        str += f"{N} = "
        for j in range(cnt):
            if j == cnt - 1:
                str += f"{arr[j]}"
            else:
                str += f"{arr[j]} + "
        print(str)
    else:
        print(f"{N} is NOT perfect.")