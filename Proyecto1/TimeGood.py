import time
secs = 0
mins = 0
hours = 0
days = 0
years = 0

t = time.time()

while True:
    print(int(years), "y ", int(days), "d ", int(hours), "h ", int(mins), "m ", int(secs), "s") # Imprimir los numeros

    secs = t%60 # Obtener resto de t / 60
    mins = (t//60)%60 # Dividir t / 60 y asegurarse de que solo sea entero
    hours = (t//3600)%24 # obtener horas dividiendo t entre 3600 (60 mins)
    days = (t//86400) %365
    years = t//31536000
    time.sleep(1) #
    t +=1
