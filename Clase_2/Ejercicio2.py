

metros = input('Ingrese una medida en metros ')

def is_float(valor):
    try:
        float(valor)
        return True
    except Exception as ex:
        return False

if is_float:
    
    metros = float(metros)
    centimetros = metros * 100
    milimetros = metros * 1000
    
    print(f"Conversion de {metros} metros a centimetros es {centimetros}")
    print(f"Conversion de {metros} metros a milimetros es {milimetros}")
    





