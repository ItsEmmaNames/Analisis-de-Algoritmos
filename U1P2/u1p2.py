import tkinter as tk
import matplotlib.pyplot as plt
import time
import random 

ventana = tk.Tk()
ventana.geometry("600x500")
ventana.title("Comparador de algoritmos")

tk.Label(ventana, text="Bubble vs Selection", font=("Times new roman", 14, "bold")).pack(pady=5)

def generar_listas(inicio, incremento, limite):
    return [[random.randint(1, 1000) for _ in range(n)] for n in range(inicio, limite + 1, incremento)]

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort_brute_force(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def enviar():

    val_inicio = int(in_elementos.get())
    val_incremento = int(in_cremento.get())
    val_limite = int(in_limite.get())
        
    listas = generar_listas(val_inicio, val_incremento, val_limite)
        
    eje_x_tamanos = []
    eje_y_selection = []
    eje_y_bubble = []

    for lista_original in listas:
        n = len(lista_original)
        eje_x_tamanos.append(n)

        
        copia_selection = lista_original.copy()
        t_inicio = time.time()                   
        selection_sort(copia_selection)
        t_fin = time.time()                      
        eje_y_selection.append(t_fin - t_inicio)

            
        copia_bubble = lista_original.copy()
        t_inicio = time.time()                   
        bubble_sort_brute_force(copia_bubble)
        t_fin = time.time()                      
        eje_y_bubble.append(t_fin - t_inicio)

       
    plt.figure(figsize=(8, 5))
    plt.plot(eje_x_tamanos, eje_y_selection, marker="o", color="blue", label="Selection Sort")
    plt.plot(eje_x_tamanos, eje_y_bubble, marker="s", color="red", label="Bubble Sort")
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

tk.Button(ventana, text="Generar listas y comparar", command=enviar, bg="light green").pack(pady=30)

ventana.mainloop()