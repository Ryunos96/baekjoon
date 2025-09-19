start_hour, start_minute = map(int, input().split())
cooking_time = int(input())

result_hour = start_hour
result_minute = start_minute + cooking_time
plus_hour = result_minute // 60

if result_minute >= 60 :
    result_hour = result_hour + plus_hour
    if result_hour > 23 :
        result_hour = result_hour - 24
    result_minute = result_minute - plus_hour * 60
print(result_hour, result_minute)