import time
secs = 0
mins = 0
hours = 0
days = 0
years = 0

while True:
    secs += 1
    if secs == 60:
        secs = 0
        mins += 1
        if mins == 60:
            mins = 0
            hours += 1
            if hours == 24:
                hours = 0
                days += 1
                if days == 365:
                    days = 0
                    years += 1

    print(years, " : ", days, " : ", hours, " : ", mins, " : ", secs, end="\r")
    time.sleep(1)
