import math


forma = str(input("Qual é a forma?"))

if (forma == "sphere"):
    r = float(input("Qual é o raio?"))
    volume = 4 / 3 * math.pi * r * r * r
    print(round(volume,1))
if (forma == "cylinder"):
    r = float(input("Qual é o raio?"))
    h = float(input("Qual é a altura?"))
    volume = math.pi * r * r * h
    print(round(volume,1))
if (forma == "cone"):
    r = float(input("Qual é o raio?"))
    h = float(input("Qual é a altura?"))
    volume = 1 / 3 * math.pi * r * r * h
    print(round(volume,1))