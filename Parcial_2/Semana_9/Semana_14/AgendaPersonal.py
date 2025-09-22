import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Clase principal de la aplicación Agenda
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")   # Título de la ventana
        self.root.geometry("650x400")        # Tamaño inicial de la ventana

        # --- FRAMES (contenedores para organizar la interfaz) ---
        # Frame donde se mostrará la lista de eventos
        self.frame_eventos = ttk.Frame(root)
        self.frame_eventos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Frame donde estarán los campos de entrada (fecha, hora, descripción)
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(fill=tk.X, padx=10)

        # Frame para los botones de acciones (agregar, eliminar, salir)
        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(fill=tk.X, padx=10, pady=10)

        # --- TREEVIEW (tabla para mostrar los eventos) ---
        self.tree = ttk.Treeview(
            self.frame_eventos,
            columns=("Fecha", "Hora", "Descripción"),
            show="headings"   # Solo mostrar encabezados, no un árbol
        )
        self.tree.heading("Fecha", text="Fecha")           # Columna de fecha
        self.tree.heading("Hora", text="Hora")             # Columna de hora
        self.tree.heading("Descripción", text="Descripción") # Columna de descripción
        self.tree.pack(fill=tk.BOTH, expand=True)          # Se expande para ocupar el espacio

        # --- DATEPICKER (selector de fecha sencillo con OptionMenu) ---
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)

        # Variables asociadas a los menús desplegables
        self.day_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.year_var = tk.StringVar()

        # Listas de valores posibles para los OptionMenu
        days = [str(i) for i in range(1, 32)]  # Días del 1 al 31
        months = [str(i) for i in range(1, 13)] # Meses del 1 al 12
        years = [str(i) for i in range(datetime.now().year, datetime.now().year + 5)] # Años desde el actual +4

        # Menús desplegables (día, mes, año)
        ttk.OptionMenu(self.frame_entrada, self.day_var, days[0], *days).grid(row=0, column=1)
        ttk.OptionMenu(self.frame_entrada, self.month_var, months[0], *months).grid(row=0, column=2)
        ttk.OptionMenu(self.frame_entrada, self.year_var, years[0], *years).grid(row=0, column=3)

        # --- Entrada de HORA y DESCRIPCIÓN ---
        ttk.Label(self.frame_entrada, text="Hora:").grid(row=0, column=4, padx=5)
        self.hora_entry = ttk.Entry(self.frame_entrada, width=10)  # Caja de texto para la hora
        self.hora_entry.grid(row=0, column=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=0, column=6, padx=5)
        self.descripcion_entry = ttk.Entry(self.frame_entrada, width=25)  # Caja de texto para la descripción
        self.descripcion_entry.grid(row=0, column=7)

        # --- BOTONES ---
        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=5)

    # --- FUNCIÓN PARA AGREGAR EVENTO ---
    def agregar_evento(self):
        # Se obtienen los valores de las entradas
        dia = self.day_var.get()
        mes = self.month_var.get()
        año = self.year_var.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validación: todos los campos deben estar completos
        if not (dia and mes and año and hora and descripcion):
            messagebox.showwarning("Campos Vacíos", "Completa todos los campos.")
            return

        # Validación: la fecha debe ser real (ejemplo: no permitir 31/02/2025)
        try:
            fecha = f"{int(dia):02d}/{int(mes):02d}/{año}"
            datetime.strptime(fecha, "%d/%m/%Y")  # Comprueba formato y validez
        except ValueError:
            messagebox.showerror("Fecha Inválida", "La fecha seleccionada no es válida.")
            return

        # Insertar el evento en el TreeView
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos de hora y descripción después de agregar
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    # --- FUNCIÓN PARA ELIMINAR EVENTO ---
    def eliminar_evento(self):
        seleccionado = self.tree.selection()  # Obtiene el/los ítems seleccionados
        if not seleccionado:
            messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")
            return

        # Confirmar con el usuario antes de eliminar
        confirmacion = messagebox.askyesno("Confirmar Eliminación", "¿Eliminar el evento seleccionado?")
        if confirmacion:
            self.tree.delete(*seleccionado)  # Elimina el evento del TreeView

# --- EJECUCIÓN DEL PROGRAMA ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)  # Crear la aplicación
    root.mainloop()        # Iniciar el bucle principal de Tkinter
