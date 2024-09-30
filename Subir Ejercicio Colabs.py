suma = 0
i = 0
print("Ingrese los numeros que desee promediar y sumar: 4")
while True:
  number : int = int(input(" "))

  suma: int = suma + number
  if number != 0:
    i = i + 1

  if number == 0:
    promedio = suma / i
    print(f"La suma de los numeros es {suma}")

    print(f"El promedio de los numeros es {promedio}")
    break