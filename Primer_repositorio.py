import tkinter as tk
from tkinter import ttk, messagebox

# Funciones de conversión
def convertir_longitud(valor, tipo):
    try:
        valor = float(valor)
        if tipo == "Metros a Kilómetros":
            return valor / 1000
        elif tipo == "Pulgadas a Metros":
            return valor * 0.0254
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return None

def convertir_masa(valor, tipo):
    try:
        valor = float(valor)
        if tipo == "Kilogramos a Gramos":
            return valor * 1000
        elif tipo == "Libras a Kilogramos":
            return valor * 0.453592
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return None

def convertir_tiempo(valor, tipo):
    try:
        valor = float(valor)
        if tipo == "Segundos a Minutos":
            return valor / 60
        elif tipo == "Horas a Días":
            return valor / 24
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return None

# Ventana de conversión
def ventana_conversion(tipo_conversion):
    ventana = tk.Toplevel()
    ventana.title(f"Conversión de {tipo_conversion}")

    tk.Label(ventana, text="Valor a convertir:").grid(row=0, column=0, padx=10, pady=10)
    entrada_valor = tk.Entry(ventana)
    entrada_valor.grid(row=0, column=1, padx=10, pady=10)

    opciones = {
        "Longitud": ["Metros a Kilómetros", "Pulgadas a Metros"],
        "Masa": ["Kilogramos a Gramos", "Libras a Kilogramos"],
        "Tiempo": ["Segundos a Minutos", "Horas a Días"]
    }

    tk.Label(ventana, text="Tipo de conversión:").grid(row=1, column=0, padx=10, pady=10)
    combo_tipo = ttk.Combobox(ventana, values=opciones[tipo_conversion])
    combo_tipo.grid(row=1, column=1, padx=10, pady=10)

    resultado_label = tk.Label(ventana, text="Resultado: ")
    resultado_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def realizar_conversion():
        valor = entrada_valor.get()
        tipo = combo_tipo.get()
        if tipo_conversion == "Longitud":
            resultado = convertir_longitud(valor, tipo)
        elif tipo_conversion == "Masa":
            resultado = convertir_masa(valor, tipo)
        elif tipo_conversion == "Tiempo":
            resultado = convertir_tiempo(valor, tipo)
        if resultado is not None:
            resultado_label.config(text=f"Resultado: {resultado}")

    tk.Button(ventana, text="Convertir", command=realizar_conversion).grid(row=2, column=0, columnspan=2, pady=10)

# Ventana principal
def main():
    root = tk.Tk()
    root.title("Conversor de Unidades")

    menu = tk.Menu(root)
    root.config(menu=menu)

    menu_conversion = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Conversión", menu=menu_conversion)
    menu_conversion.add_command(label="Conversión de Longitud", command=lambda: ventana_conversion("Longitud"))
    menu_conversion.add_command(label="Conversión de Masa", command=lambda: ventana_conversion("Masa"))
    menu_conversion.add_command(label="Conversión de Tiempo", command=lambda: ventana_conversion("Tiempo"))

    tk.Label(root, text="Selecciona una opción del menú para comenzar.", font=("Arial", 14)).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()