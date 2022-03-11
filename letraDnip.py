def pedirDni():
    dni = ""
    while len(dni) != 8:
        dni = input("introduce tu dni: ")

    return int(dni)

def calcularLetra(dni):
    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N',
        'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    
    return letras[dni%23]

#Probador

dni = pedirDni()
print(f"NIF: {calcularLetra(dni)} {dni}")
