f_dice, s_dice, t_dice = map(int, input().split())
result = 0
if f_dice == s_dice == t_dice :
    result = 10000 + f_dice * 1000
elif f_dice == s_dice :
    result = 1000 + f_dice * 100
elif s_dice == t_dice :
    result = 1000 + s_dice * 100
elif f_dice == t_dice :
    result = 1000 + f_dice * 100
elif f_dice != s_dice and s_dice != t_dice and f_dice != t_dice :
    if f_dice > s_dice and f_dice > t_dice :
        result = f_dice * 100
    elif s_dice > f_dice and s_dice > t_dice :
        result = s_dice * 100
    elif t_dice > f_dice and t_dice > s_dice :
        result = t_dice * 100

print(result)