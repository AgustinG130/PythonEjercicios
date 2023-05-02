N = int(input("Ingrese un numero de 5 cifras")) #no funciona
A5 = N% 10000
N = N // 10000
A4=N%1000
N = N //1000
A3=N%100
N=N//100
A2=N%10
N=N//10
if N==A5 and A4 == A2:
    print("El numero es capicua")
else:
    print("No es capicua")