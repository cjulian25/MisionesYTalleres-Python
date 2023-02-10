# 1. Leer dos (2) números y los imprima en forma ascendente.

'''num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

if num1 > num2:
    print(num1,"\n",num2)
else:
    print(num2,"\n",num1)'''

# 2. (Sentencia match) Diseñar un algoritmo que lea por teclado un número
#comprendido entre 1 y 10. Se desea visualizarsi el número es par o impar. En primer lugar, se deberá
#detectar si el número está comprendido en el rango válido (1 a 10) y a continuación
#si el número es 1, 3, 5, 7, 9, escribir un mensaje de “impar”;si es 2, 4, 6, 8, 10, escribir un mensaje de “par”.

'''num = int(input(''  
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Escoge un numero:  '')) #Colocar la comilla faltante para que sean 3

if num > 0 and num <=10:
    match num:
        case 1 | 3 | 5 | 7 | 9:
            print("Impar")
        case 2 | 4 | 6 | 8 | 10:
            print("Par")
else: 
    print("Error: opcion no valida")'''

# 3.(Sentencia match) Diseñar un algoritmo que lea un número entero entre 1 y 10, y
#nos muestre por pantalla el número ingresado en letra (1 = uno). Si el número leído
#no está comprendido entre 1 y 10 mostrar un mensaje de error.

'''num = int(input(''  
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Escoge un numero:  '')) #Colocar la comilla faltante para que sean 3

if num > 0 and num <=10:
    match num:
        case 1:
            print("Uno")
        case 2:
            print("Dos")
        case 3:
            print("Tres")
        case 4:
            print("Cuatro")
        case 5:
            print("Cinco")
        case 6:
            print("Seis")
        case 7:
            print("Siete")
        case 8:
            print("Ocho")
        case 9:
            print("Nueve")
        case 10:
            print("Diez")
else: 
    print("Error: opcion no valida")'''

# 4. Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta lo siguiente:
#• toda llamada que dure tres minutos o menos tiene un coste de 200 pesos.
#• cada minuto adicional a partir de los tres primeros es un paso de contador y cuesta 100 pesos.

'''minutos = int(input("Digite el numero de minutos gastados en la llamada: "))

if minutos > 0 and minutos <= 3:
    print("El costo de la llamada es de 200 pesos")
elif minutos > 3:
    print(f'El costo total de la llamada es de {(minutos*100)-100}')'''

# 5. En una Granja existen N conejos, C1 blancos y C2 negros. Se venden X conejos negros y Y conejos blancos. Hacer un algoritmo que:
#• Imprima la cantidad de conejos vendida
#• Si P1 es el precio de venta de los conejos blancos y P2 es el precio de venta de los conejos negros, imprima el monto total de la venta.
#• Imprima el color de los conejos que se vendieron más.

'''totalC1 = int(input("Digite la cantidad de conejos blancos existentes: "))
c1 = int(input("Digite la cantidad de conejos blancos vendidos: "))
p1 = int(input("Digite el precio unitario de los conejos blancos: "))
totalC2 = int(input("Digite la cantidad de conejos negros existentes: "))
c2 = int(input("Digite la cantidad de conejos negros vendidos: "))
p2 = int(input("Digite el precio unitario de los conejos negros: "))

p1Total= c1 * p1
p2Total = c2 * p2

if c1 > c2:
    print(f'El precio total vendido de los conejos es {p1Total+p2Total}, total de conejos vendidos {c1+c2} y se vendieron mas conejos C1 blancos, quedan en existencia {totalC1-c1} conejos blancos')
elif c2 > c1: 
    print(f'El precio total vendido de los conejos es {p1Total+p2Total}, total de conejos vendidos {c1+c2} y se vendieron mas conejos C2 negros, quedan en existencia {totalC2-c2} conejos negros')
elif c1 == c2:
    print(f'El precio total vendido de los conejos es {p1Total+p2Total}, total de conejos vendidos {c1+c2} y se vendieron la misma cantidad de conejos C1 blancos y C2 negros, no queda ninguno en existencia')'''

# 6. Diseñe un algoritmo que permita calcular la nota definitiva para los estudiantes, determinadas sobre las siguientes condiciones:
#• NOTA PREVIOS será el promedio de los previos por el 60%. Cada estudiante tendrá 3 evaluaciones.
#• NOTA TRABAJOS será el promedio de los trabajos por el 40%. Cada estudiantepresentara 2 trabajos.
#• NOTA FINAL será la suma de la nota de los previos y nota de los trabajos.
#• Nota mínima 1,0 nota máxima: 5,0

'''nota1 = float(input("Digite la calificacion de la primera evaluacion: "))
nota2= float(input("Digite la calificaicon de la segunda evaliacion: "))
nota3 = float(input("Digite la calificacion de la tercera evaluacion: "))
trabajo1 = float(input("Digite la calificacion del primer trabajo presentado: "))
trabajo2 = float(input("Digite la calificacion del segundo trabajo presentado: "))

totalNotas = (nota1+nota2+nota3)/3
totalTrabajos = (trabajo1+trabajo2)/2

print(f'La nota definitiva del estudiante es {round(((totalNotas*0.6)+(totalTrabajos*0.4)),2)}')'''

# 7. Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original,cantidad y su precio con descuento. El descuento lo hace en base a la clave, si la
#clave es 1 el descuento es del 10% y si la clave es 2 el descuento es del 20% (solo existen dos claves).

'''nombreArticulo = input("Escriba el nombre del articulo: ")
cantidad = int(input("Digite la cantidad de copias vendidas: "))
precio = int(input("Digite el precio del articulo: "))
clave = int(input('' 
Clave 1
Clave 2
Escoge una opcion: '')) #Colocarle las comillas faltantes para que sean 3

precioTotal = precio * cantidad

if clave > 0 and clave <=2:
    match clave:
        case 1:
            print(f'Se vendieron una cantidad de {cantidad} del articulo "{nombreArticulo}" por un valor unitario de {precio} se le aplica un descuento del {precio*0.10}%, valor total a pagar {precioTotal-(precioTotal*0.10)}')
        case 2: 
            print(f'Se vendieron una cantidad de {cantidad} del articulo "{nombreArticulo}" por un valor unitario de {precio} se le aplica un descuento del {precio*0.20}%, valor total a pagar {precioTotal-(precioTotal*0.20)}')
else:
    print("Error: opcion no valida")'''

# 8. En un hospital existen tres áreas: Psiquiatría, Pediatría, Traumatología. El presupuesto anual del hospital se reparte a estas tres (3) áreas; usted debe realizar
#un algoritmo que permita ingresar el valor del presupuesto anual, ingresar el porcentaje correspondiente a cada área, realizar el cálculo del presupuesto que
#corresponde a cada área,si la suma de los porcentajes no corresponde al 100% debe mostrar un mensaje de error.
#Mostrar el porcentaje asignado a cada área y el presupuesto obtenido

'''presupuestoAnual = float(input("Digite el valor total del presupuesto anual: "))
psiquiatria = float(input("Digite el prorcentaje que se le dara al area de Psiquiatria: "))
pediatria = float(input("Digite el porcentaje que se le dara al area de Pediatria: "))
traumatologia = float(input("Digite el porcentaje que se le dara al area de Traumatologia: "))

sumatoria = psiquiatria+pediatria+traumatologia
presupuestoPsi = round((presupuestoAnual*(psiquiatria/100)),2)
presupuestoPedi = round((presupuestoAnual*(pediatria/100)),2)
presupuestoTrau = round((presupuestoAnual*(traumatologia/100)),2)

if sumatoria == 100:
    print(f'El porcentaje para el area de Psiquiatria es de {psiquiatria}% equivalente a un total de {presupuestoPsi}')
    print(f'El porcentaje para el area de Pediatria es de {pediatria}% equivalente a un total de {presupuestoPedi}')
    print(f'el porcentaje para el area de Traumatologia es de {traumatologia}% equivalente a un total de {presupuestoTrau}')
else:
    print("Error: la sumatoria de los presupuestos no corresponde al 100% ")'''

# 9. Diseñar un algoritmo para determinar el precio del tiquete de ida y vuelta en avión,conociendo la distancia a recorrer, sabiendo que si el número de días de estancia 
# es superior o igual a 7 y la distancia superior a 800 km el billete tiene una reducción del 30%. El precio por km es de $2,5 dólares.

'''distancia = int(input("Cuanto es la distancia a recorrer en Kms?: "))
dias = int(input("Cuantos días de estancia serán?: "))

precioDolar = 2.5
#precioPeso = 11725.12
if dias >= 7 and distancia > 800:
    descuento = (((precioDolar * distancia))*0.30)
    print(f'Tiene un descuento del 30%, el valor total del tiquete es de {round(((precioDolar*distancia)-descuento),2)}USD')
else:
    print(f'El valor total del tiquete es de {precioDolar*distancia}')'''
        

