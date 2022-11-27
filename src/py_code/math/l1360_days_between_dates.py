def month_to_day(month, is_leap):
    month = (month + 12) % 12
    if month == 2 and is_leap:
        return 29
    elif month == 2:
        return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30

def is_leap_year(year):
    leap_year = False
    if year % 100 != 0 and year % 4 == 0:
        leap_year = True
    if year % 100 == 0 and year % 400 == 0:
        leap_year = True
    return leap_year

def count_days(y, m, d):
    """
    count days starting from 1900-1-1
    """
    days = 0
    years = y - 1900
    leap_years = (years - 1) // 4 if years >= 1 else 0
    days += 366 * leap_years + 365 * (years - leap_years)
    m0 = 1
    while m0 < m:
        days += month_to_day(y, m0)
        m0 += 1
    days += d - 1
    return days

def daysBetweenDates(date1: str, date2: str) -> int:
    date1 = list(map(int, date1.split("-")))
    date2 = list(map(int, date2.split("-")))
    return abs(count_days(date1[0], date1[1], date1[2]) - count_days(date2[0], date2[1], date2[2]))

import datetime
if __name__ == '__main__':
    print(datetime.date(2100, 9, 22) - datetime.date(1900, 1, 1), count_days(2100, 9, 22))
    # y = 1900
    # for i in range(10):
    #     # count_days(y+i, 1, 1)
    # #     print(i+y, is_leap_year(i+y))
    #     print(y+i, datetime.date(y+i, 1, 1) - datetime.date(1900, 1, 1), count_days(y+i, 1, 1))