import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

def validar_numeros(char):
    """Permite solo números y el punto decimal."""
    if char.isdigit() or char == "." or char == "-":
        return True
    return False

def validar_enteros(char):
    """Permite solo números enteros."""
    return char.isdigit()
    
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

    tk.Label(ventana, text="Cantidad de rectángulos:", bg="#0c1433", fg="white").pack(pady=10)

    entry_n = tk.Entry(ventana, width=10, validate="key")
    entry_n['validatecommand'] = (ventana.register(validar_enteros), '%S')  
    entry_n.pack(pady=5)

    resultado_var = tk.StringVar()
    tk.Label(ventana, textvariable=resultado_var, bg="#0c1433", fg="white").pack(pady=10)

    def calcular_y_graficar():
        resultado = calcular_area_rectangulos(entry_a, entry_b, entry_c, entry_x1, entry_x2, entry_n)
        resultado_var.set(resultado)
        a, b, c = obtener_coeficientes(entry_a, entry_b, entry_c)
        if a is not None:
            try:
                x1 = float(entry_x1.get())
                x2 = float(entry_x2.get())
                n = int(entry_n.get())
                if n > 0 and x1 < x2:
                    graficar_funcion(a, b, c, x1, x2, n)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Coeficientes inválidos.")

    tk.Button(ventana, text="Calcular y Graficar", command=calcular_y_graficar, bg="yellow", fg="black", width=35, height=4).pack(pady=20)

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

    def resolver_ecuaciones():
        A = np.array([[float(matriz_entries[i][j].get()) for j in range(3)] for i in range(3)])
        b = np.array([float(matriz_entries[i][-1].get()) for i in range(3)])

        try:
            solucion = np.linalg.solve(A, b)
            resultado_var.set(f"Solución: {solucion}")
        except np.linalg.LinAlgError:
            resultado_var.set("El sistema no tiene solución única.")

    tk.Button(ventana, text="Resolver", command=resolver_ecuaciones, bg="yellow", fg="black", width=35, height=4).pack(pady=20)

# Ventana principal
root = tk.Tk()
root.title("Calculadora de Matemáticas")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#0c1433")

# Botones
tk.Button(root, text="Resolver Sistema de Ecuaciones", command=abrir_sistema_ecuaciones, bg="yellow", fg="black", width=35, height=4).pack(pady=20)
tk.Button(root, text="Gráfica y Área Bajo la Curva", command=abrir_grafica_y_area, bg="yellow", fg="black", width=35, height=4).pack(pady=20)
tk.Button(root, text="Salir", command=root.quit, bg="red", fg="white", width=35, height=4).pack(pady=20)

root.mainloop()
