n = int(input("Введите целое число больше 1: "))
simple = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        simple = False
        break
print(f"Число {n} простое" if simple else f"Число {n} составное")
