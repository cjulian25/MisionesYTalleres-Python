CantFamiliares = 0 
Edad = 0
Peso = 0
Altura = 0
Imc = 0
step1,step2 = False,False
Menu = 0
resultado = ""
TipoImc = ""
bandera = True


while Menu !=5 : 

    Menu = int(input('''
    1) Ingresar La Cantidad De Familiares
    2) Ingresar Datos de Edad, Peso y Altura
    3) Mostrar Resultados 
    4) Acerca de 
    5) Salir
    Selecciona una opcion : '''))
    print("")

    match Menu : 

        case 1 : 
            while bandera == True : 
                CantFamiliares = int(input("\t Ingrese La Cantidad De Familiares : " ))
                if CantFamiliares > 0:
                    break
                else : 
                    print(" \t Por favor ingrese un valor superior o igual 1 \n \t\t ")

            step1 = True

        case 2 :
            if step1 == True : 
                for i in range (1,CantFamiliares+1) : 
                    while bandera == True:
                        Edad = int(input(f" \t Ingrese la edad del familiar #{i}: \n \t\t"))
                        if Edad <= 0:
                            print("\n Error: la edad debe ser mayor a 1 \n")
                        elif Edad > 0:
                            break
                    while bandera == True:
                        Peso = float(input(f" \t Ingrese el peso del familiar #{i} : \n \t\t "))
                        if Peso <= 0:
                            print("\n Error: El peso debe ser mayor a 0 \n")
                        elif Peso > 0:
                            break
                    while bandera == True:
                        Altura = float(input(f" \t Ingrese la altura en Metros del familiar #{i}: \n \t\t "))
                        if Altura <= 0:
                            print(" \n Error: La altura debe ser mayor a 0 \n")
                        elif Altura > 3:
                            print("\n Ingrese un valor valido entre 0.1 y 3.0 \n")
                            continue
                        elif Altura <= 3 : 
                            break                   
                    Imc = round((Peso/Altura**2),1)

                    if Imc <18.5 and Imc > 0 :
                        TipoImc = "Bajo Peso"
                    elif Imc >= 18.5 and Imc < 25 :
                        TipoImc = "Normal"
                    elif Imc >= 25 and Imc < 29 : 
                        TipoImc = "Sobrepeso"
                    elif Imc >= 29 and Imc < 35 : 
                        TipoImc = "Obeso 1"
                    elif Imc >=  35 : 
                        TipoImc = "Obeso 2"                    

                    resultado += f"\t\t El encuestado #{i} tiene una edad de {Edad}, con un peso de {Peso}, Una altura de {Altura} Metros para un IMC de {Imc} y su nivel de peso es {TipoImc} \n"

                step2 = True
            elif step1 == False :
                print(" \t\t Por favor realice el paso #1 primero")

            
        
        case 3 : 
            if step1 == True and step2 == True : 
                print(resultado)

            elif step1 == False and step2 ==False :
                print("\t\t Por favor realice el paso #1 y el #2 primero")


        case 4 : 
            print(f"\t\t Creditos \n \t\t 1)Julian Carrillo \n \t\t 2)Ramon Marquez ")
        
        case 5 : 
            print("\t \t Menu Finalizado")
            break

        case _ :
            print("\t \t Ingrese una opcion valida")

