"""
04_ttk_avanzado.py
Demostración de widgets modernos de ttk (Themed Tk):
- Treeview (tablas de datos con múltiples columnas y barras de desplazamiento)
- Progressbar (barras de progreso determinadas e indeterminadas)
- Combobox (listas desplegables con autocompletado y eventos)
- Notebook (organización por pestañas múltiples)
"""

import tkinter as tk
from tkinter import ttk, messagebox

def filtrar_tabla():
    cat = combo_categoria.get()
    # Limpiar tabla
    for item in tree.get_children():
        tree.delete(item)
    
    # Insertar datos filtrados
    for row in inventario_original:
        if cat == "Todas" or row[1] == cat:
            tree.insert("", "end", values=row)

def simular_progreso():
    valor = barra_progreso["value"]
    if valor < 100:
        barra_progreso["value"] += 15
        lbl_porcentaje.config(text=f"{int(barra_progreso['value'])}%")
        root.after(120, simular_progreso)
    else:
        messagebox.showinfo("Completado", "¡Proceso de sincronización completado al 100%!")

def reiniciar_progreso():
    barra_progreso["value"] = 0
    lbl_porcentaje.config(text="0%")

root = tk.Tk()
root.title("04 - Widgets Avanzados de TTK (Treeview, Progressbar, Combobox)")
root.geometry("680x560")
root.config(bg="#1f242d")

# Estilo TTK
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#2a2e39", foreground="#ffffff", fieldbackground="#2a2e39", rowheight=24)
style.configure("Treeview.Heading", background="#12161f", foreground="#00ffcc", font=("Helvetica", 9, "bold"))

tk.Label(
    root, 
    text="Tablas de Datos (Treeview) y Barra de Progreso (TTK)", 
    font=("Helvetica", 13, "bold"), 
    bg="#1f242d", 
    fg="#00ffcc"
).pack(pady=(12, 6))

# 1. Filtro superior con Combobox
frame_top = tk.Frame(root, bg="#1f242d")
frame_top.pack(fill="x", padx=20, pady=6)

tk.Label(frame_top, text="Filtrar por Categoría:", bg="#1f242d", fg="white", font=("Helvetica", 9)).pack(side="left", padx=(0, 8))

combo_categoria = ttk.Combobox(frame_top, values=["Todas", "Nicho", "Diseñador", "Decants"], state="readonly", width=16)
combo_categoria.set("Todas")
combo_categoria.pack(side="left")
combo_categoria.bind("<<ComboboxSelected>>", lambda e: filtrar_tabla())

# 2. Tabla Treeview con Scrollbar
frame_tabla = tk.Frame(root, bg="#1f242d")
frame_tabla.pack(fill="both", expand=True, padx=20, pady=8)

columnas = ("ID", "Categoría", "Nombre", "Precio", "Stock")
tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)

tree.heading("ID", text="ID")
tree.heading("Categoría", text="Categoría")
tree.heading("Nombre", text="Nombre de Fragancia")
tree.heading("Precio", text="Precio (USD)")
tree.heading("Stock", text="Stock")

tree.column("ID", width=45, anchor="center")
tree.column("Categoría", width=110, anchor="center")
tree.column("Nombre", width=220, anchor="w")
tree.column("Precio", width=90, anchor="e")
tree.column("Stock", width=60, anchor="center")

scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Datos base
inventario_original = [
    ("01", "Nicho", "Xerjoff Erba Pura", "$185.00", "12"),
    ("02", "Nicho", "Tom Ford Black Orchid", "$145.00", "8"),
    ("03", "Diseñador", "Dior Sauvage Elixir", "$125.50", "25"),
    ("04", "Diseñador", "JPG Le Male Elixir", "$95.00", "19"),
    ("05", "Decants", "Afnan 9pm (10ml)", "$18.00", "40"),
    ("06", "Decants", "Lattafa Asad (10ml)", "$16.00", "35"),
    ("07", "Nicho", "Creed Aventus", "$290.00", "5"),
    ("08", "Diseñador", "Bleu de Chanel Parfum", "$155.00", "14")
]
filtrar_tabla()

# 3. Sección de Progressbar
frame_progreso = tk.LabelFrame(root, text=" 2. Control de Proceso (ttk.Progressbar) ", bg="#2a2e39", fg="white", padx=15, pady=10)
frame_progreso.pack(fill="x", padx=20, pady=(5, 20))

barra_progreso = ttk.Progressbar(frame_progreso, orient="horizontal", length=400, mode="determinate")
barra_progreso.pack(side="left", fill="x", expand=True, padx=(0, 10))

lbl_porcentaje = tk.Label(frame_progreso, text="0%", bg="#2a2e39", fg="#00ffcc", font=("Consolas", 10, "bold"), width=5)
lbl_porcentaje.pack(side="left", padx=5)

btn_iniciar = tk.Button(frame_progreso, text="▶ Iniciar", command=simular_progreso, bg="#00ffcc", fg="#12161f", font=("Helvetica", 9, "bold"), relief="flat", cursor="hand2")
btn_iniciar.pack(side="left", padx=4)

btn_reset = tk.Button(frame_progreso, text="↺ Reiniciar", command=reiniciar_progreso, bg="#ff5555", fg="white", font=("Helvetica", 9, "bold"), relief="flat", cursor="hand2")
btn_reset.pack(side="left", padx=4)

if __name__ == "__main__":
    root.mainloop()
