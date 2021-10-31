import time
import pytz
from datetime import datetime

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 0

Tm = pytz.timezone(input("Introduzca su zona horaria, por ejemplo, Europe/Madrid: "))
while True:
    t = time.time() + 3600 * Tm  # Obtener hora Unix y convertirla a zona horaria
    yearsUnix = t // 31536000  # Convertir hora unix y pasarla a años
    yearsCE = yearsUnix + 1970  # convertir la hora unix (reloj desde 1970) a años actuales

    if yearsCE % 4 == 0 and (
            not yearsCE % 100 == 0 or yearsCE % 400 == 0):  # Si el año es bisiesto, hacer que febrero tenga 29 dias
        months[1] = 29

    days = ((t // 86400) % 365) - (
                yearsUnix - 2) // 4  # Obtener dia a partir de la hora unix, asegurarse de que no sea mayor que 365 dias, y hacer que no sea siempre cuatro
    i = 0
    while days > months[i]:  # Contar el mes actual
        days -= months[i]
        i += 1

    month = i + 1  # Decir el mes

    secs = t % 60  # Obtener resto de t / 60
    mins = (t // 60) % 60  # Dividir t / 60 y asegurarse de que solo sea entero
    hours = (t // 3600) % 24  # Obtener horas dividiendo t entre 3600 (60 mins)

    time.sleep(1)  # hacer que espere 1 segundo

    print("Year", int(yearsCE), "/", month, "month /", int(days), "days /", int(hours), "hours /", int(mins), "mins /",
          int(secs), "secs", end="\r")  # Imprimir los numeros

# I'm sure this code isn't the most efficient one, but i'm learning
