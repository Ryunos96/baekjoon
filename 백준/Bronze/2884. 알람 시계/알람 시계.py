hour_, minute_ = map(int, input().split())
result_hour = hour_
result_minute = minute_ - 45
if result_minute < 0 :
    result_minute = 60 + result_minute
    result_hour = result_hour - 1
    if result_hour < 0 :
        result_hour = 23

print(result_hour, result_minute)