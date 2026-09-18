"""
04_ttk_avanzado.py
Tema: Inventario de Alta Perfumería y Laboratorio de Maceración
Demostración de widgets modernos de ttk (Themed Tk):
- Treeview (inventario de perfumes con columnas, formateo de moneda y scrollbar)
- Combobox (filtrado interactivo por Casa de Perfumes: Nicho, Diseñador, Árabes)
- Progressbar (simulación del proceso de maceración y reposo de aceites esenciales)
"""

import tkinter as tk
from tkinter import ttk, messagebox

def filtrar_inventario():
    filtro = combo_casa.get()
    for item in tree.get_children():
        tree.delete(item)

    for row in inventario_fragancias:
        # row: (ID, Perfume, Casa, Familia, Concentracion, Precio, Stock)
        if filtro == "Todas las Casas" or row[2] == filtro:
            tree.insert("", "end", values=row)

def iniciar_maceracion():
    valor = barra_maceracion["value"]
    if valor < 100:
        barra_maceracion["value"] += 20
        dias = int((barra_maceracion["value"] / 100) * 45)
        lbl_estado_lab.config(
            text=f"Macerando aceites esenciales... Día {dias}/45 de reposo ({int(barra_maceracion['value'])}%)",
            fg="#ffd700"
        )
        root.after(140, iniciar_maceracion)
    else:
        lbl_estado_lab.config(text="✨ ¡Lote de fragancias perfectamente macerado y listo para embotellar! ✨", fg="#80e892")
        messagebox.showinfo("Laboratorio Ryan.ShopMx", "¡Maceración finalizada con éxito!\nLa fragancia alcanzó su fijación óptima.")

def reiniciar_laboratorio():
    barra_maceracion["value"] = 0
    lbl_estado_lab.config(text="Laboratorio en espera. Presione 'Comenzar Maceración'.", fg="#888888")

root = tk.Tk()
root.title("04 - Inventario y Maceración | TTK Avanzado")
root.geometry("740x600")
root.config(bg="#121212")

# Estilo TTK adaptado a perfumería
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Treeview", 
    background="#1a1a1a", 
    foreground="#ffffff", 
    fieldbackground="#1a1a1a", 
    rowheight=26, 
    font=("Helvetica", 9)
)
style.configure(
    "Treeview.Heading", 
    background="#2a2415", 
    foreground="#d4af37", 
    font=("Helvetica", 9, "bold")
)
style.map("Treeview", background=[("selected", "#d4af37")], foreground=[("selected", "#121212")])

tk.Label(
    root, 
    text="💎 INVENTARIO Y MACERACIÓN DE ALTA PERFUMERÍA 💎", 
    font=("Helvetica", 13, "bold"), 
    bg="#121212", 
    fg="#d4af37"
).pack(pady=(15, 6))

# 1. Filtro con Combobox
frame_filtro = tk.Frame(root, bg="#121212")
frame_filtro.pack(fill="x", padx=20, pady=6)

tk.Label(frame_filtro, text="Filtrar por Casa / Marca:", bg="#121212", fg="#e0e0e0", font=("Helvetica", 9, "bold")).pack(side="left", padx=(0, 8))

casas = ["Todas las Casas", "Xerjoff", "Tom Ford", "Dior", "Jean Paul Gaultier", "Perfumería Árabe / Decants"]
combo_casa = ttk.Combobox(frame_filtro, values=casas, state="readonly", width=26)
combo_casa.set("Todas las Casas")
combo_casa.pack(side="left")
combo_casa.bind("<<ComboboxSelected>>", lambda e: filtrar_inventario())

# 2. Treeview con Scrollbar
frame_tabla = tk.Frame(root, bg="#121212")
frame_tabla.pack(fill="both", expand=True, padx=20, pady=8)

columnas = ("ID", "Perfume", "Casa", "Familia", "Concentración", "Precio", "Stock")
tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)

tree.heading("ID", text="ID")
tree.heading("Perfume", text="Fragancia")
tree.heading("Casa", text="Casa")
tree.heading("Familia", text="Familia")
tree.heading("Concentración", text="Concentración")
tree.heading("Precio", text="Precio (USD)")
tree.heading("Stock", text="Stock")

tree.column("ID", width=40, anchor="center")
tree.column("Perfume", width=180, anchor="w")
tree.column("Casa", width=120, anchor="w")
tree.column("Familia", width=110, anchor="center")
tree.column("Concentración", width=95, anchor="center")
tree.column("Precio", width=85, anchor="e")
tree.column("Stock", width=55, anchor="center")

scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Catálogo completo
inventario_fragancias = [
    ("P01", "Erba Pura", "Xerjoff", "Frutal Oriental", "EdP (100ml)", "$185.00", "12"),
    ("P02", "Naxos 1861", "Xerjoff", "Tabaco / Miel", "EdP (100ml)", "$220.00", "7"),
    ("P03", "Black Orchid", "Tom Ford", "Floral Oscuro", "EdP (100ml)", "$145.00", "9"),
    ("P04", "Oud Wood", "Tom Ford", "Amaderada Lujo", "EdP (50ml)", "$165.00", "5"),
    ("P05", "Sauvage Elixir", "Dior", "Especiada Cálida", "Parfum (60ml)", "$125.50", "22"),
    ("P06", "Le Male Elixir", "Jean Paul Gaultier", "Vainilla / Miel", "Parfum (125ml)", "$95.00", "18"),
    ("P07", "Afnan 9pm", "Perfumería Árabe / Decants", "Ambarina Dulce", "Decant 10ml", "$18.00", "45"),
    ("P08", "Lattafa Asad", "Perfumería Árabe / Decants", "Pimienta / Clavo", "Decant 10ml", "$16.00", "38"),
]
filtrar_inventario()

# 3. Laboratorio de Maceración con Progressbar
frame_lab = tk.LabelFrame(
    root, 
    text=" 🧪 Laboratorio Olfativo: Control de Maceración (ttk.Progressbar) ", 
    bg="#1a1a1a", 
    fg="#d4af37", 
    padx=15, 
    pady=10
)
frame_lab.pack(fill="x", padx=20, pady=(5, 15))

barra_maceracion = ttk.Progressbar(frame_lab, orient="horizontal", length=360, mode="determinate")
barra_maceracion.pack(side="left", fill="x", expand=True, padx=(0, 10))

btn_macerar = tk.Button(
    frame_lab, 
    text="⚗️ Iniciar Maceración", 
    command=iniciar_maceracion, 
    bg="#d4af37", 
    fg="#121212", 
    font=("Helvetica", 8, "bold"), 
    relief="flat", 
    cursor="hand2"
)
btn_macerar.pack(side="left", padx=4)

btn_reset_lab = tk.Button(
    frame_lab, 
    text="Reiniciar", 
    command=reiniciar_laboratorio, 
    bg="#333333", 
    fg="white", 
    font=("Helvetica", 8), 
    relief="flat", 
    cursor="hand2"
)
btn_reset_lab.pack(side="left", padx=4)

lbl_estado_lab = tk.Label(
    root, 
    text="Laboratorio en espera. Presione 'Iniciar Maceración'.", 
    bg="#121212", 
    fg="#888888", 
    font=("Helvetica", 8, "italic")
)
lbl_estado_lab.pack(pady=(0, 10))

if __name__ == "__main__":
    root.mainloop()
