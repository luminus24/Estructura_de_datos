#1.- Crear un programa que al ingreso de su contraseña deba salir correcta o incorrecta según se
#ponga (contraseña = 123).

contraseña = int(input("Ingrese su contraseña: "))

if(contraseña == 123):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")