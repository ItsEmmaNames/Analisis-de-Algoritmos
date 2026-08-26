import tkinter as tk



ventana = tk.Tk()
ventana.title("Saludador de compas")
ventana.geometry("360x320")

etiqueta1 = tk.Label(ventana, text="Hola, escribe un nombre y presiona el botón")
etiqueta1.config(font=("Arial", 10, "bold"))
etiqueta1.pack(pady=20)

entrada = tk.Entry(ventana)
entrada.pack(pady=20)

entrada_1 = entrada.get()

def saludar():
    nombre_lbl = tk.Label(ventana, text="")
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "Emmanuel!"
    nombre_lbl.config(text=f"Hola {nombre} !")
    nombre_lbl.pack(pady=10)

btn = tk.Button(ventana, text="Saludar",command=saludar)
btn.pack(pady=10)



ventana.mainloop()