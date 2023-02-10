#1. Sumar una cantidad N números MAYORES a 0 utilizando MIENTRAS.
'''bandera = True
num, total = 0, 0

while bandera == True:
    num = float(input("Digita un numero superior a 0: "))  
    total += num
    if num <0:
        total-=num
        print("Error: El numero ingresado no es superior a 0")
    elif num == 0:
        print(f'La suma total de todos los numeros digitados es: {total}')
        bandera = False'''
           

#2. Imprimir números aleatorios en el rango de 0 a 10 mientras el número no sea igual a cero.
'''import random
bandera = True

while bandera == True:
    num = random.randint(0,10)
    if num != 0:
        print(num, end= ", ")
    elif num == 0:
        print(num)
        bandera = False'''

#3. Imprimir 20 números aleatorios en el rango de 1 a 1000.
'''import random

for i in range(1,21):
    print(random.randint(1,1000), end=", ")'''

#4. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
#todos los números impares desde 1 hasta ese número.

'''num = int(input("Digita un numero entero positivo: "))

if num > 0:
    for i in range(1,num+1):
        if i%2 == 1:
            print(i, end = ", ")
    if num%2 == 0:
        print(num)
elif num < 0:
    print("Error: El numero ingresado no es un numero entero positivo")'''

# 5. Una persona debe realizar un muestreo con 20 personas para determinar el promedio de peso
#de los niños, jóvenes, adultos y viejos que existen en su zona habitacional. Se determinan las
#categorías con base en la sig., tabla:
#CATEGORIA     EDAD
#Niños        0 - 12
#Jóvenes     13 - 29
#Adultos     30 - 59
#Viejos      60 en adelante

contNiñ, contJov, contAdul, contViej = 0, 0, 0, 0
totalPesoNiñ, totalPesoJov, totalPesoAdul, totalPesoViej, total = 0, 0, 0, 0, 0
promNiñ, promJov, promAdul, promViej = 0, 0, 0, 0
bandera = 1

'''for i in range(1,21):
    while bandera > 0:
        edad = int(input(f'Digita la edad de la persona {i}: '))  
        if edad <= 0:
            print("Error: La edad no es valida")
            continue          
        elif edad > 0 and edad <= 12:
            while bandera>0:
                pesoNiñ = float(input(f'Digita el peso de la persona {i}: '))
                if pesoNiñ > 0:
                    contNiñ +=1
                    totalPesoNiñ += pesoNiñ
                    total +=1
                    promNiñ = totalPesoNiñ/contNiñ
                    break
                elif pesoNiñ <=0:
                    print("Error: El peso no es valido")
                    continue
            break
        elif edad >= 13 and edad <= 29:
            while bandera >0:
                pesoJov = float(input(f'Digita el peso de la persona {i}: '))
                if pesoJov > 0:
                    contJov +=1
                    totalPesoJov += pesoJov
                    total += 1
                    promJov = totalPesoJov/contJov
                    break
                elif pesoJov <= 0:
                    print("Error: El peso no es valido")
                    continue
            break
        elif edad >= 30 and edad <= 59:
            while bandera > 0:
                pesoAdul = float(input(f'Digita el peso de la persona {i}: '))
                if pesoAdul > 0:
                    contAdul +=1
                    totalPesoAdul += pesoAdul
                    total +=1
                    promAdul = totalPesoAdul/contAdul
                    break
                elif pesoAdul <= 0:
                    print("Error: El peso no es valido")
                    continue
            break
        elif edad >= 60:
            while bandera > 0:
                pesoViej = float(input(f'Digita el peso de la persona {i}: '))
                if pesoViej > 0:
                    contViej +=1
                    totalPesoViej  += pesoViej
                    total +=1
                    promViej = totalPesoViej/contViej
                    break
                elif pesoViej <= 0:
                    print("Error: El peso no es valido")
                    continue
            break    
if i == 20:
    print(f'Categoria\tEdad\tNumero de personas\tPeso promedio\nNiños    \t0-12    \t{contNiñ}        \t{promNiñ}Kg \nJovenes    \t13-29    \t{contJov}        \t{promJov}Kg \nAdultos    \t30-59    \t{contAdul}        \t{promAdul}Kg \nViejos\t\t60 o más    \t{contViej}        \t{promViej}Kg ')'''

# 6. Diseñen un algoritmo que imprima la siguiente secuencia:
#1.1.1 - 1.1.2 - 1.1.3 - 1.1.4
#1.2.1 - 1.2.2 - 1.2.3 - 1.2.4
#1.3.1 - 1.3.2 - 1.3.3 - 1.3.4
#1.4.1 - 1.4.2 - 1.4.3 - 1.4.4
#1.5.1 - 1.5.2 - 1.5.3 - 1.5.4

'''for i in range(1, 2):
    for j in range(1,6):
        print(" ")
        for k in range(1,5):
            if k < 4:
                print(f'{i}.{j}.{k}', end = " - ")
            if k == 4:
                print(f'{i}.{j}.{k}')'''


# 7. Un Zoólogo pretende determinar el porcentaje de animales que hay en las siguientes tres
#categorías de edades: de 0 a 1 año, de más de 1 año y menos de 3 y de 3 o más años. El
#zoológico todavía no está seguro del animal que va a estudiar. Si se decide por elefantes solo
#tomara una muestra de 20 de ellos; si se decide por las jirafas, tomara 15 muestras, y si son
#chimpancés tomara 40.

'''opcion = int(input('' 
1. Elefantes
2. Girafas
3. Chimpancés
Escoge una opcion: '')) #Colocar las comillas faltantes para que den un total de 3
bandera = 1
contBebeElef, contJovElef, contAdulElef = 0, 0, 0
contBebeJiraf, contJovJiraf, contAdulJiraf = 0, 0, 0
contBebeChimp, contJovChimp, contAdulChimp = 0, 0, 0

match opcion:
    case 1:
        for i in range(1,21):
            while bandera == 1:
                edadElef = int(input(f'Digita la edad del elefante #{i}: '))
                if edadElef <=0 or edadElef > 70:
                    print("Error: La edad no es valida")
                    continue
                elif edadElef > 0 and edadElef <= 1:
                    contBebeElef +=1
                    break
                elif edadElef > 1 and edadElef < 3:
                    contJovElef +=1
                    break
                elif edadElef >= 3 and edadElef <= 70:
                    contAdulElef +=1
                    break
        if i == 20:
            print(f'Categoria\t Edad\t        Numero de Elefantes\t Promedio\nElefante bebe\t 0-menor1 \t        {contBebeElef}\t           {(contBebeElef*100)/20}%\nElefante joven\t menor1-mayor3\t        {contJovElef}\t           {(contJovElef*100)/20}%\nElefante adulto\t mayor 3 \t        {contAdulElef}\t           {(contAdulElef*100)/20}%')
    case 2: 
        for i in range(1,16):
            while bandera == 1:
                edadJiraf = int(input(f'Digita la edad de la Jirafa #{i}: '))
                if edadJiraf <=0 or edadJiraf > 25:
                    print("Error: La edad no es valida")
                    continue
                elif edadJiraf > 0 and edadJiraf <= 1:
                    contBebeJiraf +=1
                    break
                elif edadJiraf > 1 and edadJiraf < 3:
                    contJovJiraf +=1
                    break
                elif edadJiraf >= 3 and edadJiraf <= 25:
                    contAdulJiraf +=1
                    break
        if i == 15:
            print(f'Categoria\t Edad\t        Numero de Jirafas\t Promedio\nJirafa bebe\t 0-menor1 \t        {contBebeJiraf}\t           {(contBebeJiraf*100)/15}%\nJirafa joven\t menor1-mayor3\t        {contJovJiraf}\t           {(contJovJiraf*100)/15}%\nJirafa adulto\t mayor 3 \t        {contAdulJiraf}\t           {(contAdulJiraf*100)/15}%')
    case 3:
        for i in range(1,41):
            while bandera == 1:
                edadChimp = int(input(f'Digita la edad del chimpance #{i}: '))
                if edadChimp <=0 or edadChimp > 40:
                    print("Error: La edad no es valida")
                    continue
                elif edadChimp > 0 and edadChimp <= 1:
                    contBebeChimp +=1
                    break
                elif edadChimp > 1 and edadChimp < 3:
                    contJovChimp +=1
                    break
                elif edadChimp >= 3 and edadChimp <= 40:
                    contAdulChimp +=1
                    break
        if i == 40:
            print(f'Categoria\t     Edad\t        Numero de Chimpancés\t Promedio\nChimpancé bebe\t     0-menor1 \t                {contBebeChimp}\t           {(contBebeChimp*100)/40}%\nChimpancé joven\t     menor1-mayor3\t        {contJovChimp}\t           {(contJovChimp*100)/40}%\nChimpancé adulto\tmayor3 \t                {contAdulChimp}\t           {(contAdulChimp*100)/40}%')
    case _:
        print("Error: opcion no valida")'''
    
# 8. Una compañía de seguros tiene contratados a una cantidad N vendedores. Cada vendedor
#hace tres ventas a la semana. Su política de pagos es que un vendedor recibe un sueldo base, y
#además un 10% extra por comisiones del total de sus ventas. El gerente de la compañía desea
#saber cuánto dinero recibirá cada vendedor en una semana por concepto de comisiones por
#las ventas, y cuanto será el total tomando en cuenta su sueldo base y sus comisiones.

'''bandera = True
sumaVentas = 0
sueldoBase = 1150000

while bandera == True:
    nombre = input("Digita el nombre del empleado: ")
    for i in range(1,4):
        ventas = int(input(f'Digita el valor de la venta semanal #{i}: '))
        sumaVentas += ventas
    if i == 3:
        comision = sumaVentas*0.10
        print(f'El empleado {nombre} recibira un valor total de {comision} por comision de las tres ventas semanales, y el valor total del sueldo semanal es de {(sueldoBase/4)+comision}')
        bandera == False
        print(" ")
    print("Deseas seguir calculando el sueldo de otro empleado?")
    seguir = int(input("1.Si ó 2.No: "))
    if seguir != 1:
        break
    elif seguir == 1:
        sumaVentas = 0
        comision = 0
        bandera == True'''

# 9. Una agencia de venta de autos paga a su personal de ventas un salario de $950.000, más una
#comisión de $170.000 por cada auto vendido, y también un 5% extra del valor total de las
#ventas. Diseñar un algoritmo para calcular el salario de un vendedor en un determinado mes,
#realizando la lectura por pantalla del nº de automóviles vendidos y el valor de cada auto para
#hallar el monto total de ventas.

'''sueldoBase = 950000
sumaValorAutos, comision = 0, 0
bandera = 1

nVentas = int(input("Digita el numero de ventas realizadas en el mes: "))
if nVentas >= 1:
    for i in range(1,nVentas+1):
        while bandera == 1:
            valorAuto = int(input(f'Digita el valor total del auto vendido #{i}: '))
            if valorAuto <= 0:
                print("Error: El valor ingresado no es valido")
                continue
            elif valorAuto > 0:
                sumaValorAutos += valorAuto
                break
    comision = (170000*nVentas)+(sumaValorAutos*0.05)
    print(f'Para un total de {nVentas} autos vendidos, por un valor total vendido de {sumaValorAutos}, la comision es de {comision}. El sueldo total del vendedor es de {sueldoBase+comision}')
elif nVentas < 0:
    print("Error: el numero ingresado no es valido")
elif nVentas == 0:
    print(f'El sueldo total del vendedor es de {sueldoBase}')'''
        
# 10. Hallar el promedio de calificaciones de un estudiante, teniendo en cuenta el nombre estudiante
#y 5 notas; calculando la nota final de acuerdo a los siguientes porcentajes: Dos (2) notas valen
#el 40% y las otras tres (3) valen el 60%. 

'''nombre = input("Digita el nombre del estudiante: ")
sumaNotas40, sumaNotas60 = 0, 0
porcentaje1, porcentaje2 = 0, 0
bandera = 1

for i in range (1,6):
    if i <= 2:
        while bandera == 1:
            notas = float(input(f'Digita la nota de la calificacion #{i}: '))
            if notas < 0 or notas > 5:
                print("Error: la calificacion de la nota no esta en el rango de 0 a 5")
            elif notas > 0 and notas <= 5:
                sumaNotas40 += notas
                break   
    elif i > 2:
        while bandera == 1:
            notas = float(input(f'Digita la nota de la calificacion #{i}: '))
            if notas < 0 or notas > 5:
                print("Error: la calificacion de la nota no esta en el rango de 0 a 5")
            elif notas > 0 and notas <= 5:
                sumaNotas60 += notas
                break  
porcentaje1 = round(((sumaNotas40*0.40)/2),2)
porcentaje2 = round(((sumaNotas60*0.60)/3),2) 
print(f'El promedio del estudiante {nombre} es de {porcentaje1+porcentaje2}')'''

