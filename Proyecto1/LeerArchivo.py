file = open("Proyecto1/datos.txt")

lines = file.readlines()

print(lines)

firstLine = lines[0].split(" ")

print(firstLine)