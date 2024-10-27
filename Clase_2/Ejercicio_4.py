

edad = input("Ingresa tu edad ")

def is_value_edad(edad):
    try:
        int(edad)
        return True
    except Exception as ex:
        return False
    
if is_value_edad(edad):
    edad = int(edad)
    if edad >= 18 and edad < 112:
        print("Es mayor de edad")
    elif edad < 18:
        print("Es menor de edad")
    elif edad >= 112:
        print("Edad no validad")
else:
    print("Ingrese una edad valida")
        
    