# Operadores de asignación
a = 75
print(a)
a += 15
print(a)
a -= 25
print(a)
a *= 8
print(a)
a /= 15
print(a)
a **= 3
print(a)
print("-" * 100)
# Operadores de comparación
b = 125
# Mayor que
print(b > 120)
# Mayor o igual que
print(b >= 120)
# Menor que
print(b < 130)
# Menor o igual que
print(b <= 100)
# Igual
print(b == 125)
# Distinto
print(b != 125)
print("-" * 100)
# Condicionales
numero = int(input("Ingrese un número:"))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
    ingresos = int(input("Ingrese sus ingresos:"))
if ingresos < 30000:
    print(f"Tienes para una salida básica; una película y palomitas.")
elif ingresos < 50000:
    print(f"Tienes para una salida decente; una cena en un restaurante.")
else:
    print(f"Tienes para una gran noche; cena elegante y entretenimiento.")
    nombre_referencia = "El Pepe"
comprobante = input("Ingrese su nombre:")
if comprobante == nombre_referencia:
    print("Adelante, estimado")
else:
    print("¿Que mirá bobo? Andá pa'shá")
print("-" * 100)
# Operadores lógicos
valor1 = 20
valor2 = 200
if valor1 < 25 or valor2 > 150:
    print(f"Me sirven esas cantidades")
else:
    print(f"No me sirven esas cantidades")
titulo = input("Ingrese su título académico:")
habPrograma = input("Sabe programar: Si o No:")
if titulo.lower() == "ingeniero" and habPrograma.lower() == "si":
    print("¡Adelante! Estás contratado")
else:
    print("Nosotros te avisamos, ¿vale?")
titulos_permitidos = ["economista", "ingeniero", "científico de datos"]

titulo = input("Ingrese su título: ")
habPrograma = input("¿Tiene habilitación para programación? (si/no): ")

if titulo.lower() in titulos_permitidos and habPrograma.lower() == "si":
    print("¡Contratado! ¿Cuándo puedes empezar?")
else:
    print("Nosotros te llamamos, ¿vale? Espera sentado.")
comida_favorita = "Pizza"
comida = input("Ingrese su comida favorita:")
if comida.lower() != comida_favorita.lower():
    print(f"No es tu comida favorita")
else:
    print(f"Es tu comida favorita")
print("-" * 100)
# Operadores de pertenencia
lista_alumnos = []
for i in range(8):
    nombre = input("Ingrese el nombre del alumno:")
    lista_alumnos.append(nombre)
print("María" in lista_alumnos)
print("María" not in lista_alumnos)
print("-" * 100)
# Bucles 
i = 1
while i < 8:
    print(f"Esto es un bucle con while.")
    i += 1

for i in range(8):
    print(f"Esto es otro bucle, pero con for")
print("-" * 100)

# Funciones
def multiplicación(valor1, valor2):
    return valor1 * valor2
print(f"El resultado de la multiplicación es:", multiplicación(3, 7))