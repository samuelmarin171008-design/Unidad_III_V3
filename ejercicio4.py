contrasena = input("ingrese una contraseña: ")

tiene_mayuscula = False
tiene_minuscula = False
tiene_digito = False
tiene_espacio = False

for caracter in contrasena:
    if caracter.isupper():
        tiene_mayuscula = True
    elif caracter.islower():
        tiene_minuscula = True
    elif caracter.isdigit():
        tiene_digito = True
    elif caracter.isspace():
        tiene_espacio = True

longitud = len(contrasena)

criterios_cumplidos = 0

if longitud >= 8:
    criterios_cumplidos = criterios_cumplidos + 1

if tiene_mayuscula:
    criterios_cumplidos = criterios_cumplidos + 1

if tiene_minuscula:
    criterios_cumplidos = criterios_cumplidos + 1

if tiene_digito:
    criterios_cumplidos = criterios_cumplidos + 1

if tiene_espacio:
    clasificacion = "débil"
else:
    if criterios_cumplidos == 4:
        clasificacion = "fuerte"
    elif criterios_cumplidos == 3:
        clasificacion = "aceptable"
    else:
        clasificacion = "débil"

if tiene_mayuscula:
    texto_mayus = "sí"
else:
    texto_mayus = "no"

if tiene_minuscula:
    texto_minus = "sí"
else:
    texto_minus = "no"

if tiene_digito:
    texto_digito = "sí"
else:
    texto_digito = "no"

if tiene_espacio:
    texto_espacio = "sí"
else:
    texto_espacio = "no"

print("longitud:", longitud)
print("contiene mayúscula:", texto_mayus)
print("contiene minúscula:", texto_minus)
print("contiene número:", texto_digito)
print("contiene espacios:", texto_espacio)
print("criterios cumplidos:", criterios_cumplidos, "de 4")
print("clasificación:", clasificacion)
