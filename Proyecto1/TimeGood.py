import time
months = [31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31 ]
i = 0
while True:
    t = time.time()
    
    yearsUnix = t//31536000
    yearsCE = yearsUnix+1970

    if yearsCE % 4 == 0 and (not yearsCE % 100 == 0 or yearsCE % 400 == 0):
        months[1] = 29
    
    days = ((t//86400) % 365) - (yearsUnix-2)//4
    i = 0
    while days > months[i]:
        days -= months[i]
        i+=1

    month = i + 1

    secs = t % 60 # Obtener resto de t / 60
    mins = (t // 60)%60 # Dividir t / 60 y asegurarse de que solo sea entero
    hours = (t // 3600)%24 # Obtener horas dividiendo t entre 3600 (60 mins)

    time.sleep(1) #

    print("Year" ,int(yearsCE), "/",month ,"month /", int(days), "days /", int(hours), "hours /", int(mins), "mins /", int(secs), "secs") # Imprimir los numeros

