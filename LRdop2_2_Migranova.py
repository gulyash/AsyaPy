max_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def prev_date():
    global day
    global month
    if day == 1:
        if month == 1:
            month = 12
        else:
            month -= 1
        day = max_days[month-1]
    else:
        day -= 1
    return [day, month]


print('Input D: ',)
day = int(input())

print('Input M: ',)
month = int(input())

print('Previous date is: ' + str(prev_date()[0]) + '.' + str(prev_date()[1]))




