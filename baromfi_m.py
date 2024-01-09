import baromfi_o
from math import ceil


def beolvas():
    lista = []
    fajlbol = open("fajlok/baromfiak.txt", "r", encoding="utf-8")
    fajlbol.readline()
    sorok = fajlbol.readlines()
    fajlbol.close()
    for index in range(0, len(sorok)):
        tisztitottSor = sorok[index].strip()
        daraboltSor = tisztitottSor.split("ß")
        baromfiak = baromfi_o.Baromfi(daraboltSor[0], daraboltSor[1], daraboltSor[2], daraboltSor[3], daraboltSor[4], daraboltSor[5])
        lista.append(baromfiak)
    return lista


def vizsgalt(lista: list):
    evek = 0
    for index in range(0, len(lista)):
        evek += 1
    print("III/A, B:")
    print(f"\tA vizsgált évek száma: {str(evek)} db")


def kerekites(lista: list):
    osszlud = 0
    oszto = 0
    for index in range(0, len(lista)):
        osszlud += lista[index].lud
        oszto += 1
    atlag = osszlud / oszto
    print("III/C:")
    print(f"\tÁtlagos lúdszám: {str(atlag)} -> {str(ceil(atlag))} db")


def nagyKacsa(lista: list):
    legnagyobb = lista[0].kacsa
    ev = lista[0].idopont
    for index in range(1, len(lista)):
        if lista[index].kacsa > legnagyobb:
            legnagyobb = lista[index].kacsa
            ev = lista[index].idopont
    print("III/D:")
    print(f"\tA legnagyobb kacsa létszám: {legnagyobb} db, év: {ev}")
