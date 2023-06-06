# Funcion para agregar el espaciado centrado
def espacio_get(no):
    s = ""
    for n in range(1,no):
        s = s+" "
    return s
#funcion para conocer la cantidad de espacio
def nEspacios(noC):
    noE2 = noE = 18-noC
    if noC%2 == 0:
       noE2 = noE = noE/2
    else :
        noE = (noE+1)/2
        noE2 = noE-1
    return [noE,noE2]

# ingreso de la variable
mensaje = input("Mensaje de entrada: ")
# cantidad de variable
noCaracteres = len(mensaje)
print(" __________________ ")

# el texto es menor a 16 caracteres
if noCaracteres < 16:
    noEspacio = nEspacios(noCaracteres)
    # Insertar el mensaje corto       
    espacio = espacio_get(int(noEspacio[0]))
    espacio2 = espacio_get(int(noEspacio[1]))
    print("╱"+espacio+"\""+mensaje+"\""+espacio2+"╲")
# el texto pasa el rango de 16 caracteres
else:
    # conocer cuantas filas o lineas hay agregado
    grupo = int(noCaracteres/16)+1
    for n in range(grupo):
        # Es la primera linea
        if n == 0:
            print("╱\""+mensaje[:16]+" ╲")
        # Es la ultima linea 
        elif n+1 == grupo: 
            print("▏ "+mensaje[(n*16):noCaracteres]+"\""+espacio_get(16-(noCaracteres-(n*16)))+" ▕")
        # Son las lineas intermedias
        else:
            print("▏ "+mensaje[(n*16):((n*16)+16)]+" ▕")
#parte final de la nube del mensaje
print("╲_____  ___________╱"+"\n      ╲╱")
# imagen ASCCI DE UN CERDO    
print ("▂╱▔▔╲╱▔▔▔▔╲╱▔▔╲▂")
print ("╲┈▔╲┊╭╮┈┈╭╮┊╱▔┈╱")
print ("┊▔╲╱▏┈╱▔▔╲┈▕╲╱▔┊")
print ("┊┊┊┃┈┈▏┃┃▕┈┈┃┊┊┊")
print ("┊┊┊▏╲┈╲▂▂╱┈╱▕┊┊┊")

