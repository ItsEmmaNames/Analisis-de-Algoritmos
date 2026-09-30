import tkinter as tk
import matplotlib.pyplot as plt
import time
import random 

ventana = tk.Tk()
ventana.geometry("600x500")
ventana.title("Comparador de Fibonacci con Programacion Dinamica")

tk.Label(ventana, text="Fibonacci vs Fibonacci Dinamico", font=("Times new roman", 14, "bold")).pack(pady=5)


#FIBONACCI N=10 -> N=60
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci (n-1)+ fibonacci (n-2)




print("--------------------------------")

#con programacion dinamica n=10 -> 90
def fibonacci_dp(n):
    if n<=1:
        return n
    F= [0] * (n+1)
    F[0] = 0
    F[1] = 1

    for i in range (2,  n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]


def enviar():

    val_inicio = int(in_elementos.get())
    val_incremento = int(in_cremento.get())
    val_limite = int(in_limite.get())
        
    valores_n = range(
        val_inicio,
        val_limite + 1,
        val_incremento
    )
        
    eje_x_tamanos = []
    eje_y_selection = []
    eje_y_bubble = []

    for n in valores_n:
       
        eje_x_tamanos.append(n)

        
        #copia_selection = lista_original.copy()
        t_inicio = time.time()                   
        fibonacci(n)
        t_fin = time.time()                      
        eje_y_selection.append(t_fin - t_inicio)

            
        #copia_bubble = lista_original.copy()
        t_inicio = time.time()                   
        fibonacci_dp(n)
        t_fin = time.time()                      
        eje_y_bubble.append(t_fin - t_inicio)

       
    plt.figure(figsize=(8, 5))
    plt.plot(eje_x_tamanos, eje_y_selection, marker="o", color="blue", label="Fibonacci recursivo")
    plt.plot(eje_x_tamanos, eje_y_bubble, marker="s", color="red", label="Fibonacci Dinamico")
    plt.title("Comparación ")
    plt.xlabel("Tamaño de la lista (N)")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True)
    plt.legend()
    plt.show()



    
tk.Label(ventana, text="Ingrese la cantidad inicial de elementos: ").pack(pady=5)
in_elementos = tk.Entry(ventana)
in_elementos.pack(pady=5)

tk.Label(ventana, text="Ingrese el incremento: ").pack(pady=5)
in_cremento = tk.Entry(ventana)
in_cremento.pack(pady=5)

tk.Label(ventana, text="Ingrese el límite: ").pack(pady=5)
in_limite = tk.Entry(ventana)
in_limite.pack(pady=5)

tk.Button(ventana, text="Comparar", command=enviar, bg="light green").pack(pady=30)

ventana.mainloop()