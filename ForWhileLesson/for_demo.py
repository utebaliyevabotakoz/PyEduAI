total_weeks = 0
total_days = 365
step = 7

for day in range(99, total_days, step):
    print(day)
    total_weeks = total_weeks + 1
    print(total_weeks)

print(total_weeks)


while (total_days >= total_weeks * 7):
    total_weeks = total_weeks + 1


print(total_weeks)