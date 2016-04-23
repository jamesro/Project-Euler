"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

days = {
        0:"Sunday",
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
}

months = {
            1:6,    # 5 in leap
            2:2,    # 1 in leap    
            3:2,
            4:5,
            5:0,
            6:3,
            7:5,
            8:1,
            9:4,
            10:6,
            11:2,
            12:4
}

years = {   0:0,
            1:1,
            2:2,
            3:3,
            4:5,
            5:6,
            6:0,
            7:1,
            8:3,
            9:4,
            10:5,
            11:6,
            12:1,
            13:2,
            14:3,
            15:4,
            16:6,
            17:0,
            18:1,
            19:2,
            20:4,
            21:5,
            22:6,
            23:0,
            24:2,
            25:3,
            26:4,
            27:5
        }



def isLeap(year):
    return (year%4==0) # ignore the century stuff for now

def yearCode(year): #must be greater than 2000 
    if year >= 2084:
        year -= 2084
    elif (year >= 2056) and (year < 2084):
        year -= 2056
    elif (year >= 2028) and (year < 2056):
        year -= 2028
    else:
        year -= 2000
    return years[year]






def monthCode(month,year):
    if (isLeap(year)) and (month == 1 or month == 2):
        return months[month] - 1
    else:
        return months[month]


def getDay(day,month,year):
    total = 0
    if year < 2000: # for 1900s
        year += 100
        total += 1
    total += yearCode(year) + monthCode(month,year) + day
    return days[total%7]

if __name__ == "__main__":
    number = 0
    for yr in range(1901,2001): 
        for mo in range(1,13):
            if getDay(1,mo,yr) == "Sunday":
                print(mo,yr)
                number += 1
    print(number)
