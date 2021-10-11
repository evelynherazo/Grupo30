numero = int(input("Ingresa un numero: "))
cont = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        cont += 1

if cont == 2:
    print("El numero: ",numero, " es primo.")
else:
    print("El numero: ",numero, " no es primo.")