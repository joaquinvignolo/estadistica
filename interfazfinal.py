import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

def validar_numeros(char):
    """Permite solo números y el punto decimal."""
    return char.isdigit() or char == "." or char == "-"

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
        y_rect = a * x_rect**2 + b * x_rect + c

        # Dibuja el rectángulo solo hasta el nivel de la función
        if y_rect >= 0:
            # Dibuja el rectángulo hacia arriba
            plt.bar(x_rect, height=y_rect, bottom=0, width=dx, align='edge', alpha=0.5, color='blue')
        else:
            # Dibuja el rectángulo hacia abajo
            plt.bar(x_rect, height=-y_rect, bottom=y_rect, width=dx, align='edge', alpha=0.5, color='red')

    plt.title('Gráfica de la función cuadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.ylim(bottom=min(y) - 1, top=max(y) + 1)  # Ajustar límites para visualizar mejor
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
    ventana.geometry("750x700")
    ventana.resizable(False, False)
    ventana.configure(bg="#0c1433")

    tk.Label(ventana, text="Ingresar los coeficientes para una función cuadrática.\n Ejemplo: f(x) = Ax2 + Bx + C", bg="#0c1433", fg="white", font=("Helvetica", 14)).pack(pady=10)

    frame_coeficientes = tk.Frame(ventana, bg="#0c1433")
    frame_coeficientes.pack(pady=5)

    tk.Label(frame_coeficientes, text="a:", bg="#0c1433", fg="white", font=("Helvetica", 14)).grid(row=0, column=0, padx=5)
    entry_a = tk.Entry(frame_coeficientes, width=15, validate="key", font=("Helvetica", 14))
    entry_a['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_a.grid(row=0, column=1, pady=5)

    tk.Label(frame_coeficientes, text="b:", bg="#0c1433", fg="white", font=("Helvetica", 14)).grid(row=1, column=0, padx=5)
    entry_b = tk.Entry(frame_coeficientes, width=15, validate="key", font=("Helvetica", 14))
    entry_b['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_b.grid(row=1, column=1, pady=5)

    tk.Label(frame_coeficientes, text="c:", bg="#0c1433", fg="white", font=("Helvetica", 14)).grid(row=2, column=0, padx=5)
    entry_c = tk.Entry(frame_coeficientes, width=15, validate="key", font=("Helvetica", 14))
    entry_c['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_c.grid(row=2, column=1, pady=5)
    tk.Label(ventana, text="Rango de visualización (x1, x2):", bg="#0c1433", fg="white", font=("Helvetica", 14)).pack(pady=10)

    entry_x1 = tk.Entry(ventana, width=15, validate="key", font=("Helvetica", 14))
    entry_x1['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_x1.pack(pady=5)

    entry_x2 = tk.Entry(ventana, width=15, validate="key", font=("Helvetica", 14))
    entry_x2['validatecommand'] = (ventana.register(validar_numeros), '%S')
    entry_x2.pack(pady=5)

    tk.Label(ventana, text="Cantidad de rectángulos:", bg="#0c1433", fg="white", font=("Helvetica", 14)).pack(pady=10)

    entry_n = tk.Entry(ventana, width=15, validate="key", font=("Helvetica", 14))
    entry_n['validatecommand'] = (ventana.register(validar_enteros), '%S')  
    entry_n.pack(pady=5)

    resultado_var = tk.StringVar()
    tk.Label(ventana, textvariable=resultado_var, bg="#0c1433", fg="white", font=("Helvetica", 14)).pack(pady=10)

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

    tk.Button(ventana, text="Calcular y Graficar", command=calcular_y_graficar, bg="yellow", fg="black", font=("Helvetica", 14), width=35, height=4).pack(pady=20)

def abrir_sistema_ecuaciones():
    ventana = tk.Toplevel(root)
    ventana.title("Resolver Sistema de Ecuaciones")
    ventana.geometry("700x500")  # Aumentar la geometría
    ventana.resizable(False, False)
    ventana.configure(bg="#0c1433")

    tk.Label(ventana, text="Sistema de Ecuaciones 3x3:", bg="#0c1433", fg="white", font=("Helvetica", 14)).pack(pady=10)

    matriz_entries = []
    resultado_entries = []  # Añadimos esta lista para los resultados independientes
    for i in range(3):
        fila_frame = tk.Frame(ventana, bg="#0c1433")
        fila_frame.pack(pady=5)
        fila_entries = []
        for j in range(3):  # 3 incógnitas
            entry = tk.Entry(fila_frame, width=5, validate="key", font=("Helvetica", 14))  # Aumentar tamaño
            entry['validatecommand'] = (ventana.register(validar_numeros), '%S')
            entry.pack(side=tk.LEFT, padx=2)
            fila_entries.append(entry)
        matriz_entries.append(fila_entries)

        tk.Label(fila_frame, text="=", bg="#0c1433", fg="white", font=("Helvetica", 14)).pack(side=tk.LEFT, padx=2)

        # Entrada para el vector de resultados
        resultado_entry = tk.Entry(fila_frame, width=5, validate="key", font=("Helvetica", 14))  # Aumentar tamaño
        resultado_entry['validatecommand'] = (ventana.register(validar_numeros), '%S')
        resultado_entry.pack(side=tk.LEFT, padx=2)

    tk.Label(ventana, text="Resultados:", bg="#0c1433", fg="white", font=("Helvetica", 14)).pack(pady=10)

        resultado_var = tk.StringVar()
    tk.Label(ventana, textvariable=resultado_var, bg="#0c1433", fg="white", font=("Helvetica", 14)).pack(pady=10)

    def resolver_ecuaciones():
        try:
            # Construir la matriz A de coeficientes (3x3)
            A = np.array([[float(matriz_entries[i][j].get()) for j in range(3)] for i in range(3)]).astype(float)
            # Construir el vector b de resultados (3x1)
            b = np.array([float(resultado_entries[i].get()) for i in range(3)]).astype(float)

            # Verificamos el determinante para ver si el sistema es compatible determinado
            det_A = np.linalg.det(A)
            
            if det_A != 0:
                # Sistema compatible determinado (una única solución)
                solucion = np.linalg.solve(A, b)
                resultado_var.set(f"Solución: {solucion}\nEl sistema es compatible determinado.")
            else:
                # Verificamos el rango de la matriz aumentada [A|b] y el rango de A
                rango_A = np.linalg.matrix_rank(A)
                matriz_aumentada = np.column_stack((A, b))
                rango_aumentada = np.linalg.matrix_rank(matriz_aumentada)

                if rango_A == rango_aumentada:
                    # Sistema compatible indeterminado
                    resultado_var.set("El sistema es compatible indeterminado (tiene infinitas soluciones).")
                else:
                    # Sistema incompatible
                    resultado_var.set("El sistema es incompatible (no tiene solución).")
                    
        except ValueError:
            # Si hay un error al convertir las entradas a float
            resultado_var.set("Error: Asegúrese de que todos los valores sean números.")
        except np.linalg.LinAlgError:
            resultado_var.set("Error al intentar resolver el sistema.")

    tk.Button(ventana, text="Resolver", command=resolver_ecuaciones, bg="yellow", fg="black", font=("Helvetica", 14), width=35, height=4).pack(pady=20)

# Ventana principal
root = tk.Tk()
root.title("Calculadora de Matemáticas")
root.geometry("700x500")
root.resizable(False, False)
root.configure(bg="#0c1433")

# Botones
tk.Button(root, text="Resolver Sistema de Ecuaciones", command=abrir_sistema_ecuaciones, bg="yellow", fg="black", font=("Helvetica", 14), width=35, height=4).pack(pady=20)
tk.Button(root, text="Gráfica y Área Bajo la Curva", command=abrir_grafica_y_area, bg="yellow", fg="black", font=("Helvetica", 14), width=35, height=4).pack(pady=20)
tk.Button(root, text="Salir", command=root.quit, bg="red", fg="white", font=("Helvetica", 14), width=35, height=4).pack(pady=20)

root.mainloop()