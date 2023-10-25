import csv
import sys


def hallar_inicio(arr, fin, valor):
    total = 0
    i = fin
    while total != valor:
        total += arr[i]
        i -= 1
    return i + 1


def max_contiguos_circular(arr, n):
    max_orig = arr[0]
    max_local = arr[0]
    fin_orig = 0
    for i in range(1, n):
        max_local = arr[i] + max(max_local, 0)
        if max_local > max_orig:
            max_orig = max_local
            fin_orig = i

    total = 0
    for i in range(n):
        total += arr[i]

    max_inv = -arr[0]
    max_local = -arr[0]
    for i in range(1, n):
        max_local = -arr[i] + max(max_local, 0)
        if max_local > max_inv:
            max_inv = max_local
            fin_inv = i

    if max_orig >= total + max_inv:
        return hallar_inicio(arr, fin_orig, max_orig), fin_orig

    return fin_inv + 1, hallar_inicio(arr, fin_inv, -max_inv) - 1


def main():
    caballeros_csv = csv.reader(open(sys.argv[1]), delimiter=",")
    caballeros = [row for row in caballeros_csv]
    nombres = [row[0] for row in caballeros]
    popularidad = [int(row[1]) for row in caballeros]
    n = len(nombres)
    inicio, fin = max_contiguos_circular(popularidad, n)
    i = inicio
    solucion = []
    while i != fin + 1:
        if i == n:
            i = 0
        solucion += [nombres[i]]
        i += 1

    print((', ').join(solucion))


if __name__ == "__main__":
    main()

