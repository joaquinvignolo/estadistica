import math
import statistics
from tabulate import tabulate
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Funciones para la gráfica y área bajo la curva
def graficar_funcion(a, b, c, x1, x2):
    """Genera y muestra la gráfica de una función cuadrática."""
    x = np.linspace(x1, x2, 400)
    y = a * x**2 + b * x + c
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.title('Gráfica de la función cuadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()

def obtener_coeficientes():
    """Solicita y devuelve los coeficientes de la función cuadrática."""
    while True:
        try:
            a, b, c = map(float, input("Ingrese los coeficientes (a, b, c) separados por espacios: ").split())
            return a, b, c
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def calcular_area_rectangulos():
    """Calcula el área bajo la curva usando el método de rectángulos."""
    a, b, c = obtener_coeficientes()
    
    while True:
        try:
            x1, x2 = map(float, input("Ingrese el rango de visualización para x (x1, x2): ").split())
            intervalo = input("Ingrese el intervalo (a, b) (con coma): ").split(',')
            a_intervalo, b_intervalo = float(intervalo[0]), float(intervalo[1])
            n = int(input("Ingrese la cantidad de rectángulos: "))
            break
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
    
    def f(x):
        return a * x**2 + b * x + c

    dx = (b_intervalo - a_intervalo) / n
    suma_inferior = sum(f(a_intervalo + i * dx) * dx for i in range(n))
    suma_superior = sum(f(a_intervalo + (i + 1) * dx) * dx for i in range(n))

    x_values = np.linspace(a_intervalo, b_intervalo, 1000)
    y_values = f(x_values)
    area_real = np.trapz(y_values, x_values)

    error_inferior = abs(area_real - suma_inferior)
    error_superior = abs(area_real - suma_superior)

    print(f"\nResultados con {n} rectángulos:")
    print(f"Suma inferior: {suma_inferior}")
    print(f"Suma superior: {suma_superior}")
    print(f"Área real: {area_real}")
    print(f"Error suma inferior: {error_inferior}")
    print(f"Error suma superior: {error_superior}")

# Funciones para medidas de posición
def MEDIA(lista):
    return sum(lista) / len(lista)

def CALCULAR_MODA(lista):
    Max_Contador = 0
    Modas = []
    for Numero in lista:
        Cont = lista.count(Numero)
        if Cont > Max_Contador:
            Max_Contador = Cont
            Modas = [Numero]
        elif Cont == Max_Contador and Numero not in Modas:
            Modas.append(Numero)
    return Modas if len(Modas) < len(set(lista)) else "No hay moda"

def CALCULAR_MEDIANA(lista):
    listaOrdenada = sorted(lista)
    longitudLista = len(listaOrdenada)
    return (listaOrdenada[(longitudLista - 1) // 2] + listaOrdenada[longitudLista // 2]) / 2

def CALCULAR_PROMEDIO(lista):
    return sum(lista) / len(lista) if lista else 0

def CALCULAR_CUARTILES(lista):
    listaOrdenada = sorted(lista)
    longitudLista = len(listaOrdenada)
    mediana = CALCULAR_MEDIANA(listaOrdenada)
    mitad_inferior = listaOrdenada[:longitudLista // 2]
    mitad_superior = listaOrdenada[(longitudLista + 1) // 2:]
    q1 = CALCULAR_MEDIANA(mitad_inferior)
    q3 = CALCULAR_MEDIANA(mitad_superior)
    return q1, mediana, q3

def DESVIACION_ESTANDAR(lista):
    n = len(lista)
    if n <= 1:
        return 0
    promedio = MEDIA(lista)
    return round((sum((x - promedio) ** 2 for x in lista) / (n - 1)) ** 0.5, 4)

def RANGO(lista):
    return lista[-1] - lista[0]

# Funciones para frecuencias
def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    return {elem: lista.count(elem) for elem in set(lista)}

def CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista):
    frecuencias = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    acumulada = {}
    total = 0
    for elem, freq in frecuencias.items():
        total += freq
        acumulada[elem] = total
    return acumulada

def SOLO_UN_ELEMENTO(lista):
    return list(set(lista))

def CALCULAR_FRECUENCIA_RELATIVA(lista):
    frecuencias_absolutas = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    total = len(lista)
    return {elem: round(freq / total, 4) for elem, freq in frecuencias_absolutas.items()}

def CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista):
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    acumulada = {}
    total = 0
    for elem, freq in frecuencia_relativa.items():
        total += freq
        acumulada[elem] = round(total, 2)
    return acumulada

def CALCULAR_FRECUENCIA_PORCENTUAL(lista):
    return {elem: freq * 100 for elem, freq in CALCULAR_FRECUENCIA_RELATIVA(lista).items()}

def CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista):
    frecuencia_porcentual = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
    acumulada = {}
    total = 0
    for elem, freq in frecuencia_porcentual.items():
        total += freq
        acumulada[elem] = total
    return acumulada

# Funciones para intervalos
def CALCULAR_AMPLITUD_INTERVALOS(datos):
    Minimo = min(datos)
    Maximo = max(datos)
    numero_intervalos = math.sqrt(len(datos))
    return (Maximo - Minimo) / numero_intervalos

def CALCULAR_INTERVALOS_CLASE(datos):
    Amplitud = CALCULAR_AMPLITUD_INTERVALOS(datos)
    Limite_Inferior = min(datos)
    Intervalos = []
    while Limite_Inferior < max(datos):
        Limite_Superior = Limite_Inferior + Amplitud
        Intervalos.append((round(Limite_Inferior, 4), round(Limite_Superior, 4)))
        Limite_Inferior = Limite_Superior
    return Intervalos

# Función para agregar elementos
def AGREGAR_ELEMENTOS_INPUT(lista):
    print("Ingrese los datos uno por uno, y apriete enter para confirmar. Para finalizar, escriba 'FIN'.")
    while True:
        valor = input(f"Ingrese dato: ")
        if valor.upper() == "FIN":
            break
        try:
            lista.append(float(valor))
        except ValueError:
            print("Entrada no válida.")
    return sorted(lista)

# Funciones para distribuciones
def distribucion_binomial(n, p, k):
    from math import comb
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def distribucion_poisson(lambd, k):
    from math import exp, factorial
    return (exp(-lambd) * (lambd ** k)) / factorial(k)

def distribucion_hipergeometrica(n, M, N, k):
    from math import comb
    return (comb(M, k) * comb(N - M, n - k)) / comb(N, n)

def distribucion_normal(x, mu, sigma):
    return norm.cdf(x, mu, sigma)

def distribucion_normal_intervalo(x1, x2, mu, sigma):
    return norm.cdf(x2, mu, sigma) - norm.cdf(x1, mu, sigma)

# Funciones del menú
def menu_datos():
    lista = []
    while True:
        print("\nMenu de Datos")
        print("1. Agregar Elementos")
        print("2. Medidas de Posición")
        print("3. Funciones Estadísticas")
        print("4. Funciones de Distribución")
        print("5. Gráfica de Función Cuadrática")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            lista = AGREGAR_ELEMENTOS_INPUT(lista)
        elif opcion == "2":
            print("\nMedidas de Posición")
            if not lista:
                print("La lista está vacía.")
                continue
            print(f"Media: {MEDIA(lista)}")
            print(f"Mediana: {CALCULAR_MEDIANA(lista)}")
            print(f"Moda: {CALCULAR_MODA(lista)}")
            q1, mediana, q3 = CALCULAR_CUARTILES(lista)
            print(f"Cuartiles: Q1={q1}, Mediana={mediana}, Q3={q3}")
            print(f"Desviación Estándar: {DESVIACION_ESTANDAR(lista)}")
            print(f"Rango: {RANGO(lista)}")
        elif opcion == "3":
            print("\nFunciones Estadísticas")
            if not lista:
                print("La lista está vacía.")
                continue
            frec_abs = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
            frec_rel = CALCULAR_FRECUENCIA_RELATIVA(lista)
            frec_abs_acum = CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista)
            frec_rel_acum = CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista)
            frec_porcentual = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
            frec_porcentual_acum = CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista)

            print("\nFrecuencia Absoluta:")
            print(tabulate(frec_abs.items(), headers=['Elemento', 'Frecuencia Absoluta']))
            print("\nFrecuencia Relativa:")
            print(tabulate(frec_rel.items(), headers=['Elemento', 'Frecuencia Relativa']))
            print("\nFrecuencia Absoluta Acumulada:")
            print(tabulate(frec_abs_acum.items(), headers=['Elemento', 'Frecuencia Absoluta Acumulada']))
            print("\nFrecuencia Relativa Acumulada:")
            print(tabulate(frec_rel_acum.items(), headers=['Elemento', 'Frecuencia Relativa Acumulada']))
            print("\nFrecuencia Porcentual:")
            print(tabulate(frec_porcentual.items(), headers=['Elemento', 'Frecuencia Porcentual']))
            print("\nFrecuencia Porcentual Acumulada:")
            print(tabulate(frec_porcentual_acum.items(), headers=['Elemento', 'Frecuencia Porcentual Acumulada']))
        elif opcion == "4":
            print("\nFunciones de Distribución")
            # Implementar aquí las opciones para distribuciones
            pass
        elif opcion == "5":
            calcular_area_rectangulos()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_datos()