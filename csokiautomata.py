from random import randint


def csoki():
    print("I/A, B:")
    csokiKod = input("\tCsoki kódja: ")
    db = int(input("\tDarabszáma: "))
    fajta = ""
    hely = False
    for index in range(1, 11, 1):
        if csokiKod == "A"+str(index):
            hely = True
            fajta = "Kitkatt"
        elif csokiKod == "B"+str(index):
            hely = True
            fajta = "Kinder"
        elif csokiKod == "C"+str(index):
            hely = True
            fajta = "Milka"
        elif csokiKod == "D"+str(index):
            hely = True
            fajta = "Snickers"
        elif csokiKod == "H"+str(index):
            hely = True
            fajta = "Tibi"
    print("I/C:")
    if hely:
        print(f"\tKiadott csoki: {fajta}")
        szam = randint(10, 20)
        if szam == 20:
            print(f"\tNyerőszám: {str(szam)} -> Ön nyert: Vendégünk a csokira!")
        else:
            print(f"\tNyerőszám: {str(szam)} -> Ma sajnos nem nyert ingyen csokit!")
    else:
        print(f"\tNincs ilyen sor.")
