

 
edad = int(input(" Ingrese su edad "))
tiene_licencia = True

if edad >= 18:
    if tiene_licencia:
        print("Puede conducir.")
    else:
        print("No tiene licencia.")
else:
    print("Es menor de edad.")
