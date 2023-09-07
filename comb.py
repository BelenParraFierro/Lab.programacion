# Belén Parra Fierro

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

# abrir y leer archivo de entrada.
def leer(archivo):
    ar = open(archivo)
    linea = ar.readline()
    return linea

# combinar datos.
def codificar(linea):
    N2 = ""
    for i in linea:
        if i == 'A':
            N2 += 'T'
        elif i == 'T':
            N2 += 'A'
        elif i == 'C':
            N2 += 'G'
        elif i == 'G':
            N2 += 'C'
    return N2

# generar archivo de salida.
def crear():
    N1 = linea
    N2 = linea2
    helice = open("hélice.dat", 'w', encoding = 'UTF-8')
    helice.write(f"""Bases Nitrogenadas
N1: {N1}
N2: {N2}
    """)
    return helice

if __name__ =="__main__":
    linea = leer('cadena.dat')
    linea2 = codificar(linea)
    crear()