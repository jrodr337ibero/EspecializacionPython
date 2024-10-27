
numero_1 = input("Ingrese el primer número ")
numero_2 = input("Ingrese el segundo número ")


def validar_valor(numero_1, numero_2):
    try:
        float(numero_1,numero_2)
        return True
    except Exception as ex:
        return False

if validar_valor(numero_1,numero_2):
    if(numero_1 > numero_2):
        print("El primer número es mayor al segundo número")
    if(numero_1 < numero_2):
        print("El primer número es menor al segundo número")
    if(numero_1 == numero_2):
        print("El primer número es igual al segundo número")
else:
    print("Debe ingresar un numero valido")