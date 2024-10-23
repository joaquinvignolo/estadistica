import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

def validar_numeros(char):
    """Permite solo números y el punto decimal."""
    if char.isdigit() or char == "." or char == "-":
        return True
    return False

def graficar_funcion(a, b, c, x1, x2, n):
    """Genera y muestra la gráfica de una función cuadrática y el área bajo la curva usando rectángulos."""
    x = np.linspace(x1, x2, 400)
    y = a * x**2 + b * x + c

    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')

    dx = (x2 - x1) / n
    for i in range(n):
        x_rect = x1 + i * dx
        plt.bar(x_rect, a * x_rect**2 + b * x_rect + c, width=dx, align='edge', alpha=0.3, color='orange')

    plt.title('Gráfica de la función cuadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()

def obtener_coeficientes(entry_a, entry_b, entry_c):
    """Obtiene los coeficientes de la función cuadrática de las entradas."""
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        return a, b, c
    except ValueError:
        return None

def calcular_area_rectangulos(entry_a, entry_b, entry_c, entry_x1, entry_x2, entry_n):
    """Calcula el área bajo la curva usando el método de rectángulos."""
    a, b, c = obtener_coeficientes(entry_a, entry_b, entry_c)
    if a is None:
        messagebox.showerror("Error", "Coeficientes inválidos.")
        return "Coeficientes inválidos"

    try:
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError("El número de rectángulos debe ser positivo.")
        if x1 >= x2:
            raise ValueError("x1 debe ser menor que x2.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return "Entradas inválidas"

    def f(x):
        return a * x**2 + b * x + c

    dx = (x2 - x1) / n
    suma_inferior = sum(f(x1 + i * dx) * dx for i in range(n))
    suma_superior = sum(f(x1 + (i + 1) * dx) * dx for i in range(n))

    x_values = np.linspace(x1, x2, 1000)
    y_values = f(x_values)
    area_real = np.trapz(y_values, x_values)

    error_inferior = abs(area_real - suma_inferior)
    error_superior = abs(area_real - suma_superior)

    resultado = (f"Suma inferior: {suma_inferior:.4f}\n"
                 f"Suma superior: {suma_superior:.4f}\n"
                 f"Área real: {area_real:.4f}\n"
                 f"Error Suma Inferior: {error_inferior:.4f}\n"
                 f"Error Suma Superior: {error_superior:.4f}")

    return resultado

def resolver_sistema(matriz_entries, vector_entries, resultado_var):
    """Resuelve un sistema de ecuaciones lineales usando el método de Gauss-Jordan."""
    matriz = []
    for entries in matriz_entries:
        try:
            fila = [float(entry.get()) for entry in entries]
            matriz.append(fila)
        except ValueError:
            messagebox.showerror("Error", "Entradas inválidas en la matriz.")
            return False  # Indicar que hubo un error

    vector = []
    for entry in vector_entries:
        try:
            vector.append(float(entry.get()))
        except ValueError:
            messagebox.showerror("Error", "Entradas inválidas en el vector de resultados.")
            return False  # Indicar que hubo un error

    matriz_np = np.array(matriz)
    vector_np = np.array(vector)
    determinante = np.linalg.det(matriz_np)

    if determinante != 0:
        solucion = gauss_jordan(matriz, vector)
        resultado = "Solución:\n" + "\n".join([f"x{i+1} = {x:.2f}" for i, x in enumerate(solucion)])
        resultado_var.set(resultado)
        return True  # Indicar que el cálculo fue exitoso
    else:
        resultado_var.set("Sistema Incompatible o Indeterminado")
        return False  # Indicar que no se pudo resolver

def gauss_jordan(matriz, vector):
    """Aplica el método de Gauss-Jordan para resolver el sistema."""
    n = len(matriz)
    for i in range(n):
        max_fila = max(range(i, n), key=lambda r: abs(matriz[r][i]))
        matriz[i], matriz[max_fila] = matriz[max_fila], matriz[i]
        vector[i], vector[max_fila] = vector[max_fila], vector[i]

        pivote = matriz[i][i]
        if pivote == 0:
            raise ValueError("El sistema es incompatible o indeterminado.")

        for j in range(i, n):
            matriz[i][j] /= pivote
        vector[i] /= pivote

        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(i, n):
                    matriz[k][j] -= factor * matriz[i][j]
                vector[k] -= factor * vector[i]

    return vector

def abrir_grafica_y_area():
    ventana = tk.Toplevel(root)
    ventana.title("Gráfica y Área Bajo la Curva")
    ventana.geometry("500x500")
    ventana.resizable(False, False)
    ventana.configure(bg="#0c1433")

    tk.Label(ventana, text="Coeficientes a, b, c:", bg="#0c1433", fg="white").pack(pady=10)

    entry_a = tk.Entry(ventana, width=10, validate="key")
    entry_a['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_a.pack(pady=5)

    entry_b = tk.Entry(ventana, width=10, validate="key")
    entry_b['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_b.pack(pady=5)

    entry_c = tk.Entry(ventana, width=10, validate="key")
    entry_c['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_c.pack(pady=5)

    tk.Label(ventana, text="Rango de visualización (x1, x2):", bg="#0c1433", fg="white").pack(pady=10)

    entry_x1 = tk.Entry(ventana, width=10, validate="key")
    entry_x1['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_x1.pack(pady=5)

    entry_x2 = tk.Entry(ventana, width=10, validate="key")
    entry_x2['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_x2.pack(pady=5)

    tk.Label(ventana, text="Número de rectángulos:", bg="#0c1433", fg="white").pack(pady=10)

    entry_n = tk.Entry(ventana, width=10, validate="key")
    entry_n['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_n.pack(pady=5)

    resultado_var = tk.StringVar()
    tk.Label(ventana, textvariable=resultado_var, bg="#0c1433", fg="white").pack(pady=10)

    def graficar():
        a, b, c = obtener_coeficientes(entry_a, entry_b, entry_c)
        if a is not None:
            try:
                x1 = float(entry_x1.get())
                x2 = float(entry_x2.get())
                n = int(entry_n.get())
                if n <= 0:
                    raise ValueError("El número de rectángulos debe ser positivo.")
                if x1 >= x2:
                    raise ValueError("x1 debe ser menor que x2.")
                graficar_funcion(a, b, c, x1, x2, n)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Coeficientes inválidos.")

    tk.Button(ventana, text="Graficar", command=lambda: resultado_var.set(calcular_area_rectangulos(entry_a, entry_b, entry_c, entry_x1, entry_x2, entry_n)), bg="yellow", fg="black", width=35, height=4).pack(pady=20)
    tk.Button(ventana, text="Calcular Área", command=graficar, bg="yellow", fg="black", width=35, height=4).pack(pady=20)


def abrir_sistema_ecuaciones():
    ventana = tk.Toplevel(root)
    ventana.title("Resolver Sistema de Ecuaciones")
    ventana.geometry("600x400")
    ventana.resizable(False, False)
    ventana.configure(bg="#0c1433")

    tk.Label(ventana, text="Sistema de Ecuaciones (Ax = b):", bg="#0c1433", fg="white").pack(pady=10)

    # Entradas para la matriz de coeficientes
    matriz_entries = []
    for i in range(3):  # 3 ecuaciones
        fila_frame = tk.Frame(ventana, bg="#0c1433")
        fila_frame.pack(pady=5)
        fila_entries = []
        for j in range(3):  # 3 incógnitas
            entry = tk.Entry(fila_frame, width=5, validate="key")
            entry['validatecommand'] = (ventana.register(validar_numeros), '%S')
            entry.pack(side=tk.LEFT, padx=2)
            fila_entries.append(entry)
        matriz_entries.append(fila_entries)

        tk.Label(fila_frame, text="=", bg="#0c1433", fg="white").pack(side=tk.LEFT, padx=2)

        # Entrada para el vector de resultados
        resultado_entry = tk.Entry(fila_frame, width=5, validate="key")
        resultado_entry['validatecommand'] = (ventana.register(validar_numeros), '%S')
        resultado_entry.pack(side=tk.LEFT, padx=2)

    tk.Label(ventana, text="Resultados:", bg="#0c1433", fg="white").pack(pady=10)

    resultado_var = tk.StringVar()
    tk.Label(ventana, textvariable=resultado_var, bg="#0c1433", fg="white").pack(pady=10)

    def resolver():
        vector_entries = [resultado_entry for _ in range(3)]
        if resolver_sistema(matriz_entries, vector_entries, resultado_var):
            return
        resultado_var.set("Error al resolver el sistema.")

    tk.Button(ventana, text="Resolver", command=resolver, bg="yellow", fg="black", width=35, height=4).pack(pady=20)

def limpiar_entries(entries):
    """Limpia los campos de entrada."""
    for entry in entries:
        entry.delete(0, tk.END)

def salir():
    root.quit()

# Ventana principal
root = tk.Tk()
root.title("Calculadora de Matemáticas")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#0c1433")

# Botones
tk.Button(root, text="Resolver Sistema de Ecuaciones", command=abrir_sistema_ecuaciones, bg="yellow", fg="black", width=35, height=4).pack(pady=20)
tk.Button(root, text="Gráfica y Área Bajo la Curva", command=abrir_grafica_y_area, bg="yellow", fg="black", width=35, height=4).pack(pady=20)
tk.Button(root, text="Salir", command=salir, bg="red", fg="white", width=35, height=4).pack(pady=20)

root.mainloop()
