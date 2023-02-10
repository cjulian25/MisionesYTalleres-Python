#COEX es una entidad que tiene como misión capacitar jóvenes que desean
#adquirir conocimientos y habilidades en el área de programación. Al llegar a
#COEX, cada talento es registrado con un código y su nombre. Un grupo puede
#estar conformado una cantidad N de talentos. Durante el transcurso del
#módulo uno, se presentan y explican diferentes temáticas y cada talento
#realiza una misión, que es una prueba para medir como va su proceso. Cada
#misión, es puntuada con un valor entre 1 y 100. En total se realizan 3
#misiones. Al finalizar el módulo, se realizará una misión final, conocida como
#prueba de Nivel. Se les solicita a ustedes como talentos que han adquirido los
#conceptos y habilidades de programadores para que creen un programa que
#permita llevar a cabo los registros correspondientes al proceso. Se les solicita
#que el programa tenga un menú que:
#1. Solicite la cantidad N de talentos (solo se debe hacer una vez y no debe permitir hacer los otros hasta no haberla realizado)
#2. Registrar los datos de los talentos en una matriz 2xN (Código y Nombre)
#3. Registrar nota de Misión 1
#4. Registrar nota de Misión 2
#5. Registrar nota de Misión 3
#6. Registrar prueba de nivel final
#7. Mostrar nombre y nota del talento con la mejor nota en la Misión 1
#8. Mostrar nombre y nota del talento con la mejor nota en la Misión 2
#9. Mostrar nombre y nota del talento con la mejor nota en la Misión 3
#10.Mostrar el nombre y el promedio de cada talento (el promedio se obtiene de las 4 pruebas)
#11.Mostrar código, nombre, nota misión1, nota mision2 y nota misión 3, y prueba final
#12.Nombre de los talentos que desarrollaron el ejercicio
#13.Salir
#Se debe validar que la nota de cada talento esté entre 0 y 100, Se debe evitar
#que se repitan códigos al registrar estudiantes, Se debe validar que el nombre del talento no esté vacío

bandera = True
bandera1, bandera2, bandera3, bandera4, bandera5, bandera6, bandera10 = False, False, False, False, False, False, False
registroTalentos, registroCodigos = [], []

while bandera == True:

    opcion = int(input('''
1. Definir cantidad de talentos a registrar
2. Registrar datos de los talentos
3. Registrar nota de Misión 1
4. Registrar nota de Misión 2
5. Registrar nota de Misión 3
6. Registrar prueba de nivel final
7. Mostrar nombre y nota del talento con la mejor nota en la Misión 1
8. Mostrar nombre y nota del talento con la mejor nota en la Misión 2
9. Mostrar nombre y nota del talento con la mejor nota en la Misión 3
10. Mostrar promedio de cada talento
11. Mostrar listado de talentos
12. Acerca del Autor
13. Salir

Escoge una opcion: '''))
    
    match opcion:

        case 1:
            cantTalentos = int(input("\n\tDigita la cantidad de talentos a registrar: "))
            while cantTalentos <= 0:
                print("\t\tError: el numero ingresado debe ser superior a 0")
                cantTalentos = int(input("\tDigita la cantidad de talentos a registrar: "))
            bandera1 = True
        
        case 2:
            if bandera1 == True:
                for i in range(cantTalentos):
                    registroTalentos.append({})
                    print("")
                    while bandera == True:
                        codigo = input("\tDigite el CODIGO del talento: ")                        
                        if i == 0 and codigo != "":
                            registroTalentos[i]["codigo"] = codigo
                            registroCodigos.append(codigo)
                            break
                        if i > 0 and codigo != "":
                            if codigo in registroCodigos:
                                print("\t\tError: el codigo ingresa ya esta registrado en la base de datos")
                                continue
                            if codigo not in registroCodigos:
                                registroTalentos[i]["codigo"] = codigo
                                registroCodigos.append(codigo)
                                break                            
                    while bandera == True:
                        nombre = input("\tDigite el NOMBRE del talento: ")                        
                        if nombre != "":
                            registroTalentos[i]["nombre"] = nombre
                            break                    
                bandera2 = True
            elif bandera1 == False:
                print("\tPrimero debes realizar la opcion 1\n")

        case 3:
            if bandera1 == True and bandera2 == True:
                for i in registroTalentos:
                    while bandera == True:
                        notaMision1 = int(input(f'\tDigita la calificacion de la MISION 1 del talento {i["nombre"]}: '))
                        if notaMision1 < 0 or notaMision1 > 100:
                            print("\tLa calificacion digita no esta en el rango entre 0 a 100")
                        elif notaMision1 >= 0 or notaMision1 <= 100:
                            i["mision1"] = notaMision1
                            break
                bandera3 = True
            elif bandera1 == False or bandera2 == False:
                print("\tPrimero debes realizar la opcion 1 y la opcion 2\n")

        case 4:
            if bandera1 == True and bandera2 == True and bandera3 == True:
                for i in registroTalentos:
                    while bandera == True:
                        notaMision2 = int(input(f'\tDigita la calificacion de la MISION 2 del talento {i["nombre"]}: '))
                        if notaMision2 < 0 or notaMision2 > 100:
                            print("\tLa calificacion digita no esta en el rango entre 0 a 100")
                        elif notaMision2 >= 0 or notaMision2 <= 100:
                            i["mision2"] = notaMision2
                            break
                bandera4 = True
            elif bandera1 == False or bandera2 == False or bandera3 == False:
                print("\tPrimero debes realizar la opcion 1, la opcion 2 y la opcion 3\n")

        case 5:
            if bandera1 == True and bandera2 == True and bandera3 == True and bandera4 == True:
                for i in registroTalentos:
                    while bandera == True:
                        notaMision3 = int(input(f'\tDigita la calificacion de la MISION 3 del talento {i["nombre"]}: '))
                        if notaMision3 < 0 or notaMision3 > 100:
                            print("\tLa calificacion digita no esta en el rango entre 0 a 100")
                        elif notaMision3 >= 0 or notaMision3 <= 100:
                            i["mision3"] = notaMision3
                            break
                bandera5 = True
            elif bandera1 == False or bandera2 == False or bandera3 == False or bandera4 == False:
                print("\tPrimero debes realizar la opcion 1, la opcion 2, la opcion 3 y la opcion 4\n")
        
        case 6:
            if bandera1 == True and bandera2 == True and bandera3 == True and bandera4 == True and bandera5 == True:
                for i in registroTalentos:
                    while bandera == True:
                        notaFinal = int(input(f'\tDigita la calificacion de la PRUEBA FINAL del talento {i["nombre"]}: '))
                        if notaFinal < 0 or notaFinal > 100:
                            print("\tLa calificacion digita no esta en el rango entre 0 a 100")
                        elif notaFinal >= 0 or notaFinal <= 100:
                            i["notaFinal"] = notaFinal
                            break
                bandera6 = True
            elif bandera1 == False or bandera2 == False or bandera3 == False or bandera4 == False or bandera5 == False:
                print("\tPrimero debes realizar la opcion 1, la opcion 2, la opcion 3, la opcion 4 y la opcion 5\n")

        case 7:
            if bandera1 == True and bandera2 == True and bandera3 == True:
                mayorMision1 = []
                for i in registroTalentos:
                    mayorMision1.append(i["mision1"])
                max1 = max(mayorMision1)
                for j in registroTalentos:
                    if j["mision1"] == max1:
                        print(f'\tEl talento {j["nombre"]} obtuvo la mejor calificacion en la MISION 1 igual a {j["mision1"]}')
            elif bandera1 == False or bandera2 == False or bandera3 == False:
                print("\tPrimero debes realizar la opcion 1, la opcion 2 y la opcion 3")
        
        case 8: 
            if bandera1 == True and bandera2 == True and bandera4 == True:
                mayorMision2 = []
                for i in registroTalentos:
                    mayorMision2.append(i["mision2"])
                max2 = max(mayorMision2)
                for j in registroTalentos:
                    if j["mision2"] == max2:
                        print(f'\tEl talento {j["nombre"]} obtuvo la mejor calificacion en la MISION 2 igual a {j["mision2"]}')
            elif bandera1 == False or bandera2 == False or bandera4 == False:
                print("\tPrimero debes realizar la opcion 1, la opcion 2 y la opcion 4")

        case 9:
            if bandera1 == True and bandera2 == True and bandera5== True:
                mayorMision3 = []
                for i in registroTalentos:
                    mayorMision3.append(i["mision3"])
                max3 = max(mayorMision3)
                for j in registroTalentos:
                    if j["mision3"] == max3:
                        print(f'\tEl talento {j["nombre"]} obtuvo la mejor calificacion en la MISION 3 igual a {j["mision3"]}')
            elif bandera1 == False or bandera2 == False or bandera5 == False:
                print("\tPrimero debes realizar la opcion 1, la opcion 2 y la opcion 5")
            
        case 10:
            if bandera1 == True and bandera2 == True and bandera3 == True and bandera4 == True and bandera5 == True and bandera6 == True:
                for i in registroTalentos:
                    sumatoria = i["mision1"] + i["mision2"] + i["mision3"] + i["notaFinal"]
                    promedio = sumatoria/4
                    i["promedio"] = promedio
                    print(f'\tEl talento {i["nombre"]} optuvo un promedio de {i["promedio"]}')
                bandera10 = True
            elif bandera1 == False or bandera2 == False or bandera3 == False or bandera4 == False or bandera5 == False or bandera6 == False:
                print("\tPrimero debes realizar la opcion 1, la opcion 2, la opcion 3, la opcion 4 y la opcion 5\n")

        case 11:
            if bandera1 == True and bandera2 == True and bandera3 == True and bandera4 == True and bandera5 == True and bandera6 == True and bandera10 == True:
                print(f'\n\tCodigo \t\tNombre \t\tMision1 \tMision2 \tMision3 \tPruebaFinal \tPromedio')
                for i in registroTalentos:
                    print(f'\t{i["codigo"]} \t\t{i["nombre"]} \t\t{i["mision1"]} \t\t{i["mision2"]} \t\t{i["mision3"]} \t\t{i["notaFinal"]} \t\t{i["promedio"]}')
            elif bandera1 == False or bandera2 == False or bandera3 == False or bandera4 == False or bandera5 == False or bandera6 == False or bandera10 == False:
                print("\tPrimero debes realizar la opcion 1, la opcion 2, la opcion 3, la opcion 4, la opcion 5, la opcion 6 y la opcion 10\n")
        
        case 12:
            print("\n\tAutor:\n\t\t Julian Carrillo")
        
        case 13:
            print("\n\t Cerrando...\n")
            bandera = False
        
        case _:
            print("\n\tError: opcion no valida")