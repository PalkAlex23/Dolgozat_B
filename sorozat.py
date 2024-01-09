from random import randint


def sorozat():
    lista = []
    print("II/A, B, C:")
    print("\t", end="")
    for index in range(1, 8, 1):
        szam = randint(-50, 800)
        lista.append(szam)
        print(szam, end="|")
    szam = randint(-50, 800)
    lista.append(szam)
    print(szam)
    return lista


def harommaloszthatoak_szama(lista: list):
    print("II/D, E:")
    haromoszt = 0
    for index in range(0, len(lista)):
        if lista[index] % 3 == 0:
            haromoszt += 1
    print(f"\tA 3-al oszhatóak száma: {haromoszt}")
    return haromoszt


def fajlba_kiir(haromoszt):
    kiFajl = open("fajlok/eredmeny.txt", "w", encoding="utf-8")
    print("II/F:", file=kiFajl)
    print(f"\tA 3-al oszhatóak száma: {haromoszt}", file=kiFajl)
