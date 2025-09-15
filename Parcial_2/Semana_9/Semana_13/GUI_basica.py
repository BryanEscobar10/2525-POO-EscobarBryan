import tkinter as tk
from tkinter import ttk

def agregar_dato():
    # Obtiene el texto de la entrada
    texto = entrada_texto.get()
    if texto:  # Valida que no esté vacío
        # Inserta el valor en la tabla
        tabla.insert("", "end", values=(texto,))
        # Limpia la caja de texto después de agregar
        entrada_texto.delete(0, tk.END)

def limpiar_datos():
    # Obtiene los elementos seleccionados en la tabla
    seleccionado = tabla.selection()
    if seleccionado:
        # Si hay selección, elimina solo esos elementos
        for item in seleccionado:
            tabla.delete(item)
    else:
        # Si no hay selección, elimina todas las filas de la tabla
        for fila in tabla.get_children():
            tabla.delete(fila)

# Ventana principal
ventana = tk.Tk()
ventana.title("Aplicacion con GUI")   # Título de la ventana
ventana.geometry("600x500")           # Dimensiones iniciales

# Etiqueta
label = tk.Label(ventana, text="Ingrese datos")
label.pack(pady=5)

# Entrada de texto
entrada_texto = tk.Entry(ventana)
entrada_texto.pack(pady=5)

# Botón para agregar datos
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Botón para eliminar
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
btn_limpiar.pack(pady=5)

# Tabla con una columna
tabla = ttk.Treeview(ventana, columns=("Datos",), show="headings")
tabla.heading("Datos", text="Dato ingresado")
tabla.pack(pady=10, fill=tk.BOTH, expand=True)

# Bucle principal de la aplicación
ventana.mainloop()
