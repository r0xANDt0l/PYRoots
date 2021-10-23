import time
secs = 0
mins = 0
hours = 0
days = 0
years = 0

t = 3599

while True:
    print(years, " : ", days, " : ", hours, " : ", mins, " : ", secs) # Imprimir los numeros

    secs = int(t%60) # Obtener resto de t / 60
    mins = int((t//60)%60) # Dividir t / 60 y asegurarse de que solo sea entero
    hours = int(t//3600) # obtener horas dividiendo t entre 3600 (60 mins)
    time.sleep(1) #
    t +=1
