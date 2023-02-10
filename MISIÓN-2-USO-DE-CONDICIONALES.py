#En la escuela Pequeños Brocolitos, se desea registrar y calcular la nota de cada estudiante. Para calcular la nota definitiva de un estudiante y
#saber si aprueba, se toma en cuenta las notas de la siguiente manera:
#• El promedio de las notas de 3 Exámenes que corresponde al 55%
#• El promedio de las notas de 2 Trabajos que corresponde al 15%
#• La nota del examen final que será el 20%
#• El promedio de la nota de autoevaluación y heteroevaluación realizada por el estudiante y el profesor respectivamente que será del 10%.
#Realice un programa que permita registrar las notas que deben estar en un rango de 0-5. En caso de que una de las notas, se encuentre por fuera 
#de este rango, se debe mostrar un mensaje que indique error. Luego, debe evaluar, según la nota definitiva obtenida por el estudiante, e informar 
#el nivel en el que se encuentra y si aprueba el curso. Para aprobar el curso la nota definitiva debe ser igual o superior a 3. Los niveles que 
#los estudiantes pueden alcanzar son los siguientes:
#Nivel      Rango
#Superior   4.7 a 5.0
#Alto       4.0 a 4.6
#Básico     3.0 a 3.9
#Bajo       2.0 a 2.9
#Muy bajo     0 a 1.9
#Evalúe los requerimientos de la situación planteada y determine las variables y operaciones y condicionales requeridas para dar solución al mismo y escriba él código. 

#Solucion1
nota1 = float(input("Digite la calificacion de la primer nota: "))
if nota1>0 and nota1<=5.0:
    nota2 = float(input("Digite la calificacion de la segunda nota: "))
    if nota2>0 and nota2<=5.0:
        nota3 = float(input("Digite la calificacion de la tercer nota: "))
        if nota3>0 and nota3<=5.0:
            trabajo1 = float(input("Digite la calificacion del primer trabajo: "))
            if trabajo1>0 and trabajo1<=5.0:
                trabajo2 = float(input("Digite la calificacion del segundo trabajo: "))
                if trabajo2>0 and trabajo2<=5.0:
                    examenFinal = float(input("Digite la calificacion del examen final: "))
                    if examenFinal>0 and examenFinal<=5.0:
                        autoevaluacion = float(input("Digite la calificacion con la que se autoevalua el estudiante: "))
                        if autoevaluacion>0 and autoevaluacion<=5.0:
                            heteroevaluacion = float(input("Digite la calificacion de heteroevalaucion: "))
                            if heteroevaluacion>0 and heteroevaluacion<=5.0:
                                promedioNotas = ((nota1+nota2+nota3)/3)*0.55
                                promedioTrabajos = ((trabajo1+trabajo2)/2)*0.15
                                promedioExamFinal = examenFinal*0.20
                                promedioAutoeval = autoevaluacion*0.05
                                promedioHeteroeval = heteroevaluacion*0.05
                                definitiva = round((promedioNotas+promedioTrabajos+promedioExamFinal+promedioAutoeval+promedioHeteroeval),2)
                                if definitiva >= 4.7 and definitiva <= 5.0:
                                    nivel = "Superior"
                                    info = "Aprueba"
                                elif definitiva >= 4.0 and definitiva < 4.7:
                                    nivel = "Alto"
                                    info = "Aprueba"
                                elif definitiva >= 3.0 and definitiva < 4:
                                    nivel = "Basico"
                                    info = "Aprueba"
                                elif definitiva >= 2.0 and definitiva < 3:
                                    nivel = "Bajo"
                                    info = "No aprueba"
                                elif definitiva > 0.0 and definitiva < 2:
                                    nivel = "Muy bajo"
                                    info = "No aprueba"
                                print(f'El estudiante obtuvo una nota definitiva de {definitiva}, {info} el curso con nivel {nivel}')
                            else:
                                print("Error")                                                                    
                        else:
                            print("Error")                     
                    else :
                        print("Error")
                else :
                    print("Error")
            else :
                print("Error")
        else :
            print("Error")
    else :
        print("Error")
else :
    print("Error")
