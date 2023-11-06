date = input()
if "-" not in date:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
else:
    lst_date = date.split("-")
    day = lst_date[2]
    month = lst_date[1]
    year = lst_date[0]
    day = int(day)
    month = int(month)
    year = int(year)
    if month <= 12 and day <= 31:
        if month in (1, 3, 5, 7, 8, 10, 12):
            days = 31
        elif month == 2:
            days = 28
        else:
            days = 30
        if day < days:
            day += 1
            print("Next date: %04d-%02d-%02d" % (year, month, day))
        elif day == days:
            day = 1
            month += 1
            if month == 13:
                month = 1
                year += 1
                print("Next date: %04d-%02d-%02d" % (year, month, day))
            else:
                print("Next date: %04d-%02d-%02d" % (year, month, day))
    else:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")