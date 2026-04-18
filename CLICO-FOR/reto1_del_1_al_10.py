 Retos Autónomos
¡Ahora tú solo! Escribe el código en PythonTutor y reclama tus puntos.

Reto 1: Del 1 al 10
Escribe un ciclo FOR que imprima los números del 1 al 10, uno por línea.
# Tu código aquí:
for i in range(0, 11):
    print(i)

Reto 2: Números Pares
Escribe un ciclo FOR que imprima solo los números pares del 0 al 20.
Resultado esperado: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
  # Pista: usa range(inicio, fin, paso)
for i in range(0, 22, 2):
    print(i)

Pide al usuario un número con input() y muestra su tabla de multiplicar del 1 al 10.
Si el usuario escribe 7, imprime: 7x1=7, 7x2=14... hasta 7x10=70
num = int(input("Ingresa un número: "))
for i in range(1, 11):
    print(num, "x", i, "=", i * 7)
