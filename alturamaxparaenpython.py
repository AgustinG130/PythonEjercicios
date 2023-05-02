n=int(input("Ingrese alturas a ingresar ")) #El for en este caso se usa en medir las veces que quiero ingresar alturas.
amax=0
for i in range(1,n+1): # no es necesario uasr 1, n+1 ya que se ejecutara igual que si pones n solo.
    altura = int(input("Ingrese una altura "))
    if altura > amax:
        amax = altura
print("La altura mas alta ingresada es:", amax)