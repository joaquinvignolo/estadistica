import math
from tabulate import tabulate

# Funciones para medidas de posición
def MEDIA(lista):
    return sum(lista) / len(lista)

def CALCULAR_MODA(lista):
    Max_Contador = 0
    Modas = []
    for Numero in lista:
        Cont = 0
        for Elem in lista:
            if Elem == Numero:
                Cont += 1
        if Cont > Max_Contador:
            Max_Contador = Cont
            Modas = [Numero]
        elif Cont == Max_Contador and Numero not in Modas:
            Modas.append(Numero)
    if len(Modas) == len(set(lista)):  # set elimina elementos duplicados
        return "No hay moda"
    else:
        return Modas

def CALCULAR_MEDIANA(lista):
    listaOrdenada = sorted(lista)
    longitudLista = len(listaOrdenada)
    if longitudLista % 2 == 0:
        medioIzq = listaOrdenada[longitudLista // 2 - 1]
        medioDer = listaOrdenada[longitudLista // 2]
        return (medioIzq + medioDer) / 2
    else:
        return listaOrdenada[longitudLista // 2]

def CALCULAR_PROMEDIO(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def CALCULAR_CUARTILES(lista):
    Longitud_Lista = len(lista)
    mediana = CALCULAR_MEDIANA(lista)
    if Longitud_Lista % 2 == 0:
        mitad_inferior = lista[:Longitud_Lista // 2]
        mitad_superior = lista[Longitud_Lista // 2:]
    else:
        mitad_inferior = lista[:Longitud_Lista // 2]
        mitad_superior = lista[Longitud_Lista // 2 + 1:]
    q1 = CALCULAR_MEDIANA(mitad_inferior)
    q2 = mediana
    q3 = CALCULAR_MEDIANA(mitad_superior)
    return q1, q2, q3

def DESVIACION_ESTANDAR(lista):
    n = len(lista)
    if n <= 1:
        return 0
    promedio = MEDIA(lista)
    suma_resta_cuadrado = sum((x - promedio) ** 2 for x in lista)
    desviacion = (suma_resta_cuadrado / (n - 1)) ** 0.5
    return round(desviacion, 4)

def RANGO(lista):
    return lista[-1] - lista[0]

# Funciones para frecuencias
def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias

def CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista):
    Frecuencias_Absolutas = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    Frecuencia_Absoluta_Acumulada = {}
    Acumulador = 0
    for elemento, frecuencia in Frecuencias_Absolutas.items():
        Acumulador += frecuencia
        Frecuencia_Absoluta_Acumulada[elemento] = Acumulador
    return Frecuencia_Absoluta_Acumulada

def SOLO_UN_ELEMENTO(lista):
    return list(set(lista))

def CALCULAR_FRECUENCIA_RELATIVA(lista):
    frecuencia_relativa = []
    frecuencia_absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    lista_simple = SOLO_UN_ELEMENTO(lista)
    for elemento in lista_simple:
        absoluta = frecuencia_absoluta[elemento]
        frecuencia = absoluta / len(lista)
        frecuencia_relativa.append(round(frecuencia, 4))
    return frecuencia_relativa

def CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista):
    frecuencia_relativa_acumulada = []
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    total = 0
    for frecuencia in frecuencia_relativa:
        total += frecuencia
        frecuencia_relativa_acumulada.append(round(total, 2))
    return frecuencia_relativa_acumulada

def CALCULAR_FRECUENCIA_PORCENTUAL(lista):
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    return [elemento * 100 for elemento in frecuencia_relativa]

def CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista):
    frecuencia_porcentual = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
    frecuencia_porcentual_acumulada = []
    acumulada = 0
    for elemento in frecuencia_porcentual:
        acumulada += elemento
        frecuencia_porcentual_acumulada.append(acumulada)
    return frecuencia_porcentual_acumulada

# Funciones para intervalos
def CALCULAR_AMPLITUD_INTERVALOS(datos):
    Minimo = min(datos)
    Maximo = max(datos)
    numero_intervalos = math.sqrt(len(datos))
    Amplitud = (Maximo - Minimo) / numero_intervalos
    return Amplitud

def CALCULAR_INTERVALOS_CLASE(datos):
    Cantidad_Datos = len(datos)
    Numero_Intervalos = math.sqrt(Cantidad_Datos)
    Amplitud = CALCULAR_AMPLITUD_INTERVALOS(datos)
    Amplitud = round(Amplitud, 4)
    Limite_Inferior = min(datos)
    Limite_Superior = Limite_Inferior + Amplitud
    Intervalos = []
    while Limite_Superior <= max(datos):
        Limite_Inferior = round(Limite_Inferior, 4)
        Limite_Superior = round(Limite_Superior, 4)
        Intervalos.append((Limite_Inferior, Limite_Superior))
        Limite_Inferior = Limite_Superior
        Limite_Superior += Amplitud
    return Intervalos

# Función para agregar elementos
def AGREGAR_ELEMENTOS_INPUT(lista):
    numero_muestra = 0
    print("Ingrese los datos uno por uno, y apriete enter para confirmar y continuar agregando más datos. Cuando ya no desee agregar más, coloque la palabra FIN")
    while True:
        valor = input(f"Ingrese dato número {numero_muestra + 1}: ")
        if valor.isdigit():
            lista.append(float(valor))
            numero_muestra += 1
        elif valor.isalpha():
            if valor.upper() == "FIN":
                print("Fin de la muestra")
                break
            else:
                print("Comando no válido, intente de nuevo.")
        else:
            try:
                valor = float(valor)
                lista.append(valor)
                numero_muestra += 1
            except:
                print("Comando no válido, intente de nuevo.")
    lista = sorted(lista)
    return lista

# Funciones para distribuciones
def distribucion_binomial(n, p, k):
    from math import comb
    return comb(n, k) * (p * k) * ((1 - p) * (n - k))

def distribucion_poisson(lambd, k):
    from math import exp, factorial
    return (exp(-lambd) * (lambd ** k)) / factorial(k)

def distribucion_hipergeometrica(n, M, N, k):
    from math import comb
    return (comb(M, k) * comb(N - M, n - k)) / comb(N, n)

def distribucion_normal(x, mu, sigma):
    from math import exp, sqrt, pi
    return (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sigma) ** 2)

# Funciones para el menú de distribución
def MEDIDAS_POSICION(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = MEDIA ARITMÉTICA.\n 2 = MODA.\n 3 = MEDIANA.\n 4 = MÁXIMO.\n 5 = MÍNIMO.\n 6 = CUARTILES.\n ==> "))
        if comando == 1:
            valor = "La > Media Aritmética < de la lista es "
            resultado = MEDIA(lista)
            break
        elif comando == 2:
            valor = "La > Moda < de la lista es "
            resultado = CALCULAR_MODA(lista)
            break
        elif comando == 3:
            valor = "La > Mediana < de la lista es "
            resultado = CALCULAR_MEDIANA(lista)
            break
        elif comando == 4:
            valor = "El > Máximo < de la lista es "
            resultado = lista[-1]
            break
        elif comando == 5:
            valor = "El > Mínimo < de la lista es "
            resultado = lista[0]
            break
        elif comando == 6:
            valor = "Los > Cuartiles < de la lista son "
            resultado = CALCULAR_CUARTILES(lista)
            break
        else:
            print("Comando no válido, intente de nuevo.")
    print(valor, resultado)

def FUNCIONES_ESTADISTICAS(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = MEDIA ARITMÉTICA.\n 2 = DESVIACIÓN ESTÁNDAR.\n 3 = VARIANZA.\n 4 = RANGO.\n ==> "))
        if comando == 1:
            valor = "La > Media Aritmética < de la lista es "
            resultado = CALCULAR_PROMEDIO(lista)
            break
        elif comando == 2:
            valor = "La > Desviación Estándar < de la lista es "
            resultado = DESVIACION_ESTANDAR(lista)
            break
        elif comando == 3:
            valor = "La > Varianza < de la lista es "
            resultado = DESVIACION_ESTANDAR(lista) ** 2
            break
        elif comando == 4:
            valor = "El > Rango < de la lista es "
            resultado = RANGO(lista)
            break
        else:
            print("Comando no válido, intente de nuevo.")
    print(valor, resultado)

def FRECUENCIAS(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = FRECUENCIA ABSOLUTA.\n 2 = FRECUENCIA ABSOLUTA ACUMULADA.\n 3 = FRECUENCIA RELATIVA.\n 4 = FRECUENCIA RELATIVA ACUMULADA.\n 5 = FRECUENCIA PORCENTUAL.\n 6 = FRECUENCIA PORCENTUAL ACUMULADA.\n ==> "))
        if comando == 1:
            valor = "La > Frecuencia Absoluta < de la lista es"
            resultado = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
            break
        elif comando == 2:
            valor = "La > Frecuencia Absoluta Acumulada < de la lista es"
            resultado = CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista)
            break
        elif comando == 3:
            valor = "La > Frecuencia Relativa < de la lista es"
            resultado = CALCULAR_FRECUENCIA_RELATIVA(lista)
            break
        elif comando == 4:
            valor = "La > Frecuencia Relativa Acumulada < de la lista es"
            resultado = CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista)
            break
        elif comando == 5:
            valor = "La > Frecuencia Porcentual < de la lista es"
            resultado = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
            break
        elif comando == 6:
            valor = "La > Frecuencia Porcentual Acumulada < de la lista es"
            resultado = CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista)
            break
        else:
            print("Comando no válido, intente de nuevo.")
    print(valor)
    print(tabulate(resultado.items(), headers=["Elemento", "Frecuencia"], tablefmt="fancy_grid"))

def FUNCIONES_INTERVALOS(lista):
    while True:
        comando = int(input("¿Qué desea conocer sobre la lista?\n 1 = AMPLITUD DE INTERVALOS.\n 2 = INTERVALOS CLASE.\n ==> "))
        if comando == 1:
            valor = "La > Amplitud de Intervalos < de la lista es "
            resultado = CALCULAR_AMPLITUD_INTERVALOS(lista)
            break
        elif comando == 2:
            valor = "Los > Intervalos de Clase < de la lista son "
            resultado = CALCULAR_INTERVALOS_CLASE(lista)
            break
        else:
            print("Comando no válido, intente de nuevo.")
    print(valor, resultado)

def DISTRIBUCIONES():
    while True:
        comando = int(input("¿Qué distribución desea calcular?\n 1 = BINOMIAL.\n 2 = POISSON.\n 3 = HIPERGEOMÉTRICA.\n 4 = NORMAL.\n ==> "))
        if comando == 1:
            n = int(input("Ingrese el número de ensayos (n): "))
            p = float(input("Ingrese la probabilidad de éxito (p): "))
            k = int(input("Ingrese el número de éxitos (k): "))
            resultado = distribucion_binomial(n, p, k)
            valor = "La probabilidad para la distribución binomial es "
            break
        elif comando == 2:
            lambd = float(input("Ingrese el valor de lambda (λ): "))
            k = int(input("Ingrese el número de éxitos (k): "))
            resultado = distribucion_poisson(lambd, k)
            valor = "La probabilidad para la distribución Poisson es "
            break
        elif comando == 3:
            n = int(input("Ingrese el tamaño de la muestra (n): "))
            M = int(input("Ingrese el número de éxitos en la población (M): "))
            N = int(input("Ingrese el tamaño de la población (N): "))
            k = int(input("Ingrese el número de éxitos en la muestra (k): "))
            resultado = distribucion_hipergeometrica(n, M, N, k)
            valor = "La probabilidad para la distribución hipergeométrica es "
            break
        elif comando == 4:
            x = float(input("Ingrese el valor de x: "))
            mu = float(input("Ingrese la media (μ): "))
            sigma = float(input("Ingrese la desviación estándar (σ): "))
            resultado = distribucion_normal(x, mu, sigma)
            valor = "La probabilidad para la distribución normal es "
            break
        else:
            print("Comando no válido, intente de nuevo.")
    print(valor, resultado)

def menu_principal():
    while True:
        print("**************")
        print("**     SOFTWARE DE ESTADISTICA    **")
        print("**         VERSIÓN INICIAL        **")
        print("**************")
        print("1. Trabajar con la lista de datos")
        print("2. Distribuciones")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista = []
            while True:
                print("\nMenu de Datos")
                print("1. Agregar Elementos")
                print("2. Medidas de Posición")
                print("3. Funciones Estadísticas")
                print("4. Frecuencias")
                print("5. Funciones de Intervalos")
                print("6. Volver al menú principal")
                submenu_opcion = input("Seleccione una opción: ")

                if submenu_opcion == "1":
                    lista = AGREGAR_ELEMENTOS_INPUT(lista)
                elif submenu_opcion == "2":
                    MEDIDAS_POSICION(lista)
                elif submenu_opcion == "3":
                    FUNCIONES_ESTADISTICAS(lista)
                elif submenu_opcion == "4":
                    FRECUENCIAS(lista)
                elif submenu_opcion == "5":
                    FUNCIONES_INTERVALOS(lista)
                elif submenu_opcion == "6":
                    break
                else:
                    print("Opción no válida. Inténtelo de nuevo.")

        elif opcion == "2":
            DISTRIBUCIONES()

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Ejecución del menú principal
if __name__ == "__main__":
    menu_principal()