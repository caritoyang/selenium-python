# Con raise podemos disparar excepciones explícitamente

def funcion():
    raise IndexError

try:
    funcion()

except Exception as E:
    # raise TypeError
    print("Exception")

finally:
    print("Ejecutando Finally")



########## Assert es un raise con condición ##########
def validar_edad(edad):
    assert edad > 0, 'La edad debe ser mayor a 0'
    return edad

try:
    validar_edad(-4)

