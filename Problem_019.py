# Counting Sundays

#1 Jan 1900 was a monday
#Therefor, 1 Jan 1901 is Tuesday
#Mon%7=0, Tue%7=1, Wed%7=2, Thu%7=3, Fri%7=4, Sat%7=5
#Sun%7=6

date = [1, 1, 1901] #Day month year
days = 1
count = 0
while date != [31, 12, 2000]:
    #print(days)
    #print(date)
    if days % 7 == 6 and date[0] == 1:
        count = count + 1
    if date[0] == 31 and date[1] == 12:
        date[2] = date[2] + 1
        date[1] = 1
        date[0] = 1
    else:    
        #Apr, Jun, Sep, Nov: 30 days
        if date[1] == 4 or date[1] == 6 or date[1] == 9 or date[1] == 11:
            if date[0] == 30:
                date[1] = date[1] + 1
                date[0] = 0
        if date[1] == 2: #Leap year
            if (date[2] % 4 == 0 and date[2] % 100 != 0) or date[2] % 400 == 0:
                if date[0] == 29:
                    date[1] = date[1] + 1
                    date[0] = 0
            else: #not Leap year
                if date[0] == 28:
                    date[1] = date[1] + 1
                    date[0] = 0
        #Jan, Mar, May, Jul, Aug, Oct, Dec
        if date[1] == 1 or date[1] == 3 or date[1] == 5 or date[1] == 7 or date[1] == 8 or date[1] == 10 or date[1] == 12:
            if date[0] == 31:
                date[1] = date[1] + 1
                date[0] = 0
        date[0] = date[0] + 1
    days = days + 1
print(count, days, date)