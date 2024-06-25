import os, random
os.system("cls")

#Comprueba si un numero es entero, ademas puedes poner rangos para validar el menu u otros numeros, retorna el numero si es valido
def fVerificarInt(numero,desde,hasta):
    try:
        numero = int(numero)
    except:
        numero = -1
    if hasta!='no':
        if numero <= desde or numero>=hasta:
            numero = fVerificarInt(input("Numero invalido\nIngrese nuevamente\n> "),desde,hasta)
    else:
        if numero <= desde:
            numero = fVerificarInt(input("Numero invalido\nIngrese nuevamente\n> "),desde,hasta)
    return numero

#Verifica el tipo del vehiculo, retorna la opcion
def fTipoVehiculo(opcion):
    if opcion == 1:
        vTipoVehiculo = 'Automóvil'
    elif opcion == 2:
        vTipoVehiculo = 'Camión'
    elif opcion == 3:
        vTipoVehiculo = 'Camioneta'
    elif opcion == 4:
        vTipoVehiculo = 'Moto'
    return vTipoVehiculo

#Comprueba que la patente ingresada sea valida, retorna esta misma si es valida
def fPatente(patente):
    vNopatente = "aeioumnñ"
    vPatenteSN = 1
    while True:
        for letra in range(len(vNopatente)):
            if vNopatente[letra] in patente:
                vPatenteSN = 0
        if len(patente) != 6:
            vPatenteSN = 0
        try:
            a = int(patente[-1])
            b = int(patente[-2])
        except:
            vPatenteSN = 0
        if vPatenteSN == 0:
            vPatenteSN = 1
            patente = input("***Patente invalida***\nIngrese patente del vehiculo\n(4 letras y dos numeros)\n> ")
        else:
            return patente
#Funcion de registro del vehiculo al completo
def fRegistroVehiculo():
    #Tipo
    vOpcionSecun = fVerificarInt(input("Ingrese tipo del Automovil\n1. Automóvil\n2. Camión\n3. Camioneta\n4. Moto\n> "),0,5)
    vTipoVehiculo = fTipoVehiculo(vOpcionSecun)
    #Patente
    vPatente = fPatente(input("Ingrese patente del vehiculo\n(4 letras y dos numeros)\n> "))
    #Marca
    vMarca = input("Ingrese marca del vehiculo\n> ")
    while True:
        if len(vMarca)>=2 and len(vMarca)<=15:
            break
        else:
            vMarca = input("***Marca Invalida***\nIngrese marca del vehiculo\n> ")
    #Precio
    vPrecio = fVerificarInt(input("Ingrese Precio del vehiculo\n> "),5000000,'no')
    #Multas
    vCantidadMultas = fVerificarInt(input("Ingrese cantidad de multas\n> "),-1,'no')
    if vCantidadMultas>0:
        for i in range(vCantidadMultas):
            #si la cantidad de multas es mayor a 0, Por la cantidad de multas elegidas devuelve un diccionario con las multas y la fecha de estas
            vMontoMulta = fVerificarInt(input("Ingrese monto de la multa\n> "),0,'no')
            vDFechaMulta = fVerificarInt(input("Ingrese fecha de la multa\nDia\n> "),0,32)
            vMFechaMulta = fVerificarInt(input("Mes\n> "),0,13)
            vAFechamulta = fVerificarInt(input("Año\n> "),1900,2024)
            lMultas.append({"Monto":vMontoMulta,"Fecha":f"{vAFechamulta}-{vMFechaMulta}-{vDFechaMulta}"})
    #fecha 
    vDFechaRegistro = fVerificarInt(input("Ingrese fecha del registro\nDia\n> "),0,32)
    vMFechaRegistro = fVerificarInt(input("Mes\n> "),0,13)
    vAFechaRegistro = fVerificarInt(input("Año\n> "),1900,2024)
    vFechaRegistro  = f"{vAFechaRegistro}-{vMFechaRegistro}-{vDFechaRegistro}"
    #Rut solo comprueba si esta vacio (por tiempo)
    vRut = input("Ingrese Rut del Dueño\n> ")
    while True:
        com = vRut.replace(" ","")
        if len(com)>0:
            break
        else:
            vRut = input("***Rut Invalido***\nIngrese Rut del Dueño\n> ")
    #nombre Solo comprueba si esta vacio (por tiempo)
    vNombreDuenio = input("Ingrese Nombre del dueño\n> ")
    while True:
        com = vNombreDuenio.replace(" ","")
        if len(com)>0:
            break
        else:
            vNombreDuenio = input("***Nombre Invalido***\nIngrese Nombre del dueño\n> ")
    #Retorna un diccionario con los valores del vehiculo
    return {"Tipo":vTipoVehiculo,"Patente":vPatente,"Marca":vMarca,"Precio":vPrecio,"Multas":lMultas,"Fecha Registro":vFechaRegistro,"Rut":vRut,"Nombre":vNombreDuenio}
#busca la patente, si la lista esta vacia o no encuentra la pantente devuelve al menu
def fBuscarPantente1(lVehiculos):
    vBuscarPantete = input("Ingrese patente a buscar\n> ")
    encontrado = 0
    if len(lVehiculos)>0:
        for vehiculo in lVehiculos:
            if vehiculo["Patente"]==vBuscarPantete:
                encontrado = 1
                print("**************************")
                for campos in vehiculo:
                    print(f"{campos}: {vehiculo[campos]}")
                print("**************************")
        if encontrado == 0:
            print("***Vehiculo No encontrado***")
    else:
        print("***no hay registros***")
#Busca la patente y reporta los datos de esta en forma de diccionario
def fBuscarPantente2(lVehiculos):
    vBuscarPantete = input("Ingrese patente a buscar\n> ")
    for vehiculo in lVehiculos:
        if vehiculo["Patente"]==vBuscarPantete:
            return vehiculo
#imprime los certificados
def fImprimirCertidicado(lVehiculos):
    vRandom = random.randint(1500,3500)
    dvehiculo = fBuscarPantente2(lVehiculos)
    if dvehiculo != None:
        vOpcionSecun = fVerificarInt(input("Ingrese opcion del certificado a imprimir\n1. Emisión de contaminantes\n2. Anotaciones vigentes\n3. multas\n> "),0,4)
        while True:
            if vOpcionSecun == 1:
                print("**************************")
                print(f"Certificado de Emisión de contaminantes: ${vRandom}\nPatente: {dvehiculo["Patente"]}\nNombre del Dueño {dvehiculo["Nombre"]}\nRut del dueño: {dvehiculo["Rut"]}")
                print("**************************")
                break
            elif vOpcionSecun == 2:
                print("**************************")
                print(f"Certificado de Anotaciones vigentes: ${vRandom}\nPatente: {dvehiculo["Patente"]}\nNombre del Dueño {dvehiculo["Nombre"]}\nRut del dueño: {dvehiculo["Rut"]}")
                print("**************************")
                break
            elif vOpcionSecun == 3:
                print("**************************")
                print(f"Certificado de multas: ${vRandom}\nPatente: {dvehiculo["Patente"]}\nNombre del Dueño {dvehiculo["Nombre"]}\nRut del dueño: {dvehiculo["Rut"]}")
                print("**************************")
                break
    else:
        print("***Vehiculo No encontrado***")

#menu principal
vNego       = "Automotora"
vNombreNego = "Auto Seguro"
vOpcionMenu = -1
vOpcionSecun = -1
lVehiculos  = []
lMultas     = []
while True:
    print(f"Bienvenido a {vNego}: {vNombreNego}\n1. Grabar Vehiculo\n2. Buscar Vehiculo\n3. Imprimir certificado\n4. Salir")
    vOpcionMenu = fVerificarInt(input(f"Ingrese opcion\n> "),0,5)
    if vOpcionMenu == 1:
        lVehiculos.append(fRegistroVehiculo())
    elif vOpcionMenu == 2:
        fBuscarPantente1(lVehiculos)
    elif vOpcionMenu == 3:
        fImprimirCertidicado(lVehiculos)
    elif vOpcionMenu == 4:
        print("***Adios!***\nPatrico Aguilera\nFPY1101_014V_P3_Aguilera_Patricio v1.0")
        break