def ist_primzahl(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
                                return False
    return True

while True:
    zahl = input("Geben Sie eine Zahl ein (oder 'q' zum Beenden): ")
    if zahl.lower() == 'q':
        break
    else:
        zahl = int(zahl)
        if ist_primzahl(zahl):
            print(str(zahl) + " ist eine Primzahl.")
        else:
            print(str(zahl) + " ist keine Primzahl.")