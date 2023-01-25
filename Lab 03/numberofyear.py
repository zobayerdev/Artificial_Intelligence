def numberOfDays(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 366
    else:
        return 365


total_days = 0
for year in range(2010, 2021):
    print(f"{year} has {numberOfDays(year)} days.")
    total_days += numberOfDays(year)

print(f"Total days from 2010 to 2020: {total_days}")
