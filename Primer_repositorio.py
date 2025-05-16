import tkinter as tk
from tkinter import ttk, messagebox

def convertir_longitud(valor, tipo):
    try:
        valor = float(valor)
        if tipo == "Metros a Kilómetros":
            return valor / 1000
        elif tipo == "Kilómetros a Metros":
            return valor * 1000
        elif tipo == "Pulgadas a Metros":
            return valor * 0.0254
        elif tipo == "Metros a Pulgadas":
            return valor / 0.0254
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return None

def convertir_masa(valor, tipo):
    try:
        valor = float(valor)
        if tipo == "Kilogramos a Gramos":
            return valor * 1000
        elif tipo == "Gramos a Kilogramos":
            return valor / 1000
        elif tipo == "Libras a Kilogramos":
            return valor * 0.453592
        elif tipo == "Kilogramos a Libras":
            return valor / 0.453592
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return None

def convertir_tiempo(valor, tipo):
    try:
        valor = float(valor)
        if tipo == "Segundos a Minutos":
            return valor / 60
        elif tipo == "Minutos a Segundos":
            return valor * 60
        elif tipo == "Horas a Días":
            return valor / 24
        elif tipo == "Días a Horas":
            return valor * 24
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return None

def ventana_conversion(tipo_conversion):
    ventana = tk.Toplevel()
    ventana.title(f"Conversión de {tipo_conversion}")
    ventana.configure(bg="#e0f0ff")

    tk.Label(ventana, text="Valor a convertir:", bg="#e0f0ff", fg="#003366", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=10)
    entrada_valor = tk.Entry(ventana, bg="#ffffff", fg="#003366", font=("Arial", 11))
    entrada_valor.grid(row=0, column=1, padx=10, pady=10)

    opciones = {
        "Longitud": [
            "Metros a Kilómetros", "Kilómetros a Metros",
            "Pulgadas a Metros", "Metros a Pulgadas"
        ],
        "Masa": [
            "Kilogramos a Gramos", "Gramos a Kilogramos",
            "Libras a Kilogramos", "Kilogramos a Libras"
        ],
        "Tiempo": [
            "Segundos a Minutos", "Minutos a Segundos",
            "Horas a Días", "Días a Horas"
        ]
    }

    tk.Label(ventana, text="Selecciona el tipo de conversión:", bg="#e0f0ff", fg="#003366", font=("Arial", 11, "bold")).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    resultado_label = tk.Label(ventana, text="Resultado: ", bg="#e0f0ff", fg="#003366", font=("Arial", 11, "bold"))
    resultado_label.grid(row=3+len(opciones[tipo_conversion]), column=0, columnspan=2, padx=10, pady=10)

    def realizar_conversion(tipo):
        valor = entrada_valor.get()
        if not valor:
            messagebox.showerror("Error", "Por favor, ingresa un valor.")
            return
        if tipo_conversion == "Longitud":
            resultado = convertir_longitud(valor, tipo)
        elif tipo_conversion == "Masa":
            resultado = convertir_masa(valor, tipo)
        elif tipo_conversion == "Tiempo":
            resultado = convertir_tiempo(valor, tipo)
        if resultado is not None:
            resultado_label.config(text=f"Resultado: {resultado}")

    for idx, tipo in enumerate(opciones[tipo_conversion]):
        tk.Button(
            ventana,
            text=tipo,
            width=25,
            bg="#3399ff",
            fg="#ffffff",
            activebackground="#005580",
            activeforeground="#ffffff",
            font=("Arial", 10, "bold"),
            command=lambda t=tipo: realizar_conversion(t)
        ).grid(row=2+idx, column=0, columnspan=2, padx=10, pady=2)

def main():
    root = tk.Tk()
    root.title("Conversor de Unidades")
    root.configure(bg="#e0f0ff")

    menu = tk.Menu(root)
    root.config(menu=menu)

    menu_conversion = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Conversión", menu=menu_conversion)
    menu_conversion.add_command(label="Conversión de Longitud", command=lambda: ventana_conversion("Longitud"))
    menu_conversion.add_command(label="Conversión de Masa", command=lambda: ventana_conversion("Masa"))
    menu_conversion.add_command(label="Conversión de Tiempo", command=lambda: ventana_conversion("Tiempo"))

    tk.Label(root, text="Selecciona una opción para comenzar.", font=("Arial", 14, "bold"), bg="#e0f0ff", fg="#003366").pack(pady=20)

    tk.Button(root, text="Conversión de Longitud", width=25, bg="#3399ff", fg="#ffffff", activebackground="#005580", activeforeground="#ffffff", font=("Arial", 11, "bold"), command=lambda: ventana_conversion("Longitud")).pack(pady=5)
    tk.Button(root, text="Conversión de Masa", width=25, bg="#3399ff", fg="#ffffff", activebackground="#005580", activeforeground="#ffffff", font=("Arial", 11, "bold"), command=lambda: ventana_conversion("Masa")).pack(pady=5)
    tk.Button(root, text="Conversión de Tiempo", width=25, bg="#3399ff", fg="#ffffff", activebackground="#005580", activeforeground="#ffffff", font=("Arial", 11, "bold"), command=lambda: ventana_conversion("Tiempo")).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()