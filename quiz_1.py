# Author: JD 10/19/2021

year = int(input("Enter the year of the date: "))

m = int(input("Enter the month of the date: "))
if m > 0 and m < 13:
    if m > 0 and m <= 2:
        year_print = year
        m_print = m
        m += 12
        year -= 1
    else:
        year_print = year
        m_print = m


    j = year // 100

    k = year % 100

    q = int(input("Enter the day of the date: "))

    h = (q + 26 * (m + 1) // 10 + k + k // 4 + j // 4 + 5 * j) % 7

    if h == 0:
        day = "Saturday"
    elif h == 1:
        day = "Sunday"
    elif h == 2:
        day = "Monday"
    elif h == 3:
        day = "Tuesday"
    elif h == 4:
        day = "Wednesday"
    elif h == 5:
        day = "Thursday"
    elif h == 6:
        day = "Friday"
    else:
        day = "not valid date"

    print(m_print,"/",q,"/",year_print,"was a",day+".")
else:
    print("Thise is not a valid date.")