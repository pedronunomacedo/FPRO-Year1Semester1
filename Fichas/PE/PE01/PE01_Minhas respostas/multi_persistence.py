n = int(input("NÃºmero?"))

count = 0


mult = n

while (mult > 9):
    resto = mult % 10
    div_int = n // 10
    mult = resto * div_int
    count = count + 1

print(count)