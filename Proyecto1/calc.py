# nombre = "Nombre"

# premi = nombre[0:5]
# segu = nombre[5:]

# print(premi)
# print(segu)

ac = float(input("Introduzca un valor inicial: "))

while True:
    print(ac)
    x = input(ac)

    ope = x[0]

    if ope == 'cl':
        ac = 0
        continue
    elif ope == 'exit':
        break

    num = float(x[1:])

    if ope == '+':
        ac += num
    if ope == '-':
        ac -= num
    if ope == '*':
        ac *= num
    if ope == ':':
        ac /= num
    if ope == '^':
        ac **= num
    if ope == 'r':
        ac **= 1 / num
