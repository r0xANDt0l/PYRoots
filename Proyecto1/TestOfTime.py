import time
secs = 0
mins = 0
hours = 0
days = 0
years = 0

while True:
    secs += 1
    # if secs == 60:
    #     secs = 0
    #     mins += 1
        # if mins == 60:
        #     mins = 0
        #     hours += 1
            # if hours == 24:
            #     hours = 0
            #     days += 1
                # if days == 365:
                #     days = 0
                #     years += 1
    mins = int(secs % 60)
    hours = int(secs / 60) % 60
    days = int(secs / 3600)
    years = int(days % 365)

    print(years, " : ", days, " : ", hours, " : ", mins, " : ", secs, end="\r")
    time.sleep(1)
