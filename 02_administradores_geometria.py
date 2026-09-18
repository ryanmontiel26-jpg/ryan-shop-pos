"""
02_administradores_geometria.py
Tema: Diseño de Vitrinas y Estanterías de Perfumería
Demostración visual de los 3 administradores de geometría de Tkinter:
1. pack()  — Mostrador lineal: frascos organizados por lados (TOP, BOTTOM, LEFT, RIGHT).
2. grid()  — Estantería de fragancias: matriz organizada por nichos y diseñadores.
3. place() — Vitrina VIP: colocación de frascos en coordenadas exactas del escaparate.
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("02 - Vitrinas de Perfumes | Administradores de Geometría")
root.geometry("680x540")
root.config(bg="#121212")

# Header
tk.Label(
    root, 
    text="🧴 DISEÑO DE VITRINAS DE PERFUMERÍA", 
    font=("Helvetica", 14, "bold"), 
    bg="#121212", 
    fg="#d4af37"
).pack(pady=(12, 4))

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=12, pady=10)

# ==========================================
# PESTAÑA 1: PACK (Vitrina Lineal)
# ==========================================
tab_pack = tk.Frame(notebook, bg="#1a1a1a")
notebook.add(tab_pack, text=" 1. Vitrina Lineal (pack) ")

tk.Label(
    tab_pack, 
    text="pack(): Distribuye los perfumes en repisas superiores, inferiores y laterales.",
    bg="#1a1a1a", fg="#aaaaaa", font=("Helvetica", 9, "italic")
).pack(pady=8)

# Repisa Superior (Lanzamiento Estrella)
tk.Label(
    tab_pack, 
    text="👑 LANZAMIENTO ESTRELLA: Baccarat Rouge 540 (Extrait) — pack(side='top')", 
    bg="#800020", 
    fg="#ffd700", 
    font=("Helvetica", 9, "bold"), 
    pady=6
).pack(side="top", fill="x", padx=15, pady=4)

# Repisa Inferior (Decants Económicos)
tk.Label(
    tab_pack, 
    text="🧪 SECCIÓN DECANTS 10ML: Afnan 9pm & Lattafa Asad — pack(side='bottom')", 
    bg="#1f3a24", 
    fg="#80e892", 
    font=("Helvetica", 9, "bold"), 
    pady=6
).pack(side="bottom", fill="x", padx=15, pady=4)

# Vitrinas Laterales Centrales
frame_centro_pack = tk.Frame(tab_pack, bg="#1a1a1a")
frame_centro_pack.pack(fill="both", expand=True, padx=15, pady=5)

tk.Label(
    frame_centro_pack, 
    text="🏛️ COLECCIÓN NICHO\n\n• Xerjoff Erba Pura\n• Creed Aventus\n• Nishane Hacivat\n\npack(side='left', expand=True)", 
    bg="#23201d", 
    fg="#d4af37", 
    font=("Helvetica", 9), 
    relief="solid", 
    bd=1
).pack(side="left", fill="both", expand=True, padx=4)

tk.Label(
    frame_centro_pack, 
    text="💎 COLECCIÓN DISEÑADOR\n\n• Dior Sauvage Elixir\n• Tom Ford Black Orchid\n• JPG Le Male Elixir\n\npack(side='right', expand=True)", 
    bg="#1b222c", 
    fg="#70b5ff", 
    font=("Helvetica", 9), 
    relief="solid", 
    bd=1
).pack(side="right", fill="both", expand=True, padx=4)

# ==========================================
# PESTAÑA 2: GRID (Estantería Matricial)
# ==========================================
tab_grid = tk.Frame(notebook, bg="#1a1a1a")
notebook.add(tab_grid, text=" 2. Estantería Modular (grid) ")

tk.Label(
    tab_grid, 
    text="grid(): Cuadrícula de frascos organizados por Filas (Categoría) y Columnas (Gama).",
    bg="#1a1a1a", fg="#aaaaaa", font=("Helvetica", 9, "italic")
).grid(row=0, column=0, columnspan=3, pady=10, padx=10)

catalogo_grid = [
    ("Nicho Ultra", "Xerjoff Naxos\n$220.00", "#3d3014", "#ffd700"),
    ("Nicho Alta", "Erba Pura\n$185.00", "#3d3014", "#ffd700"),
    ("Nicho Excl.", "Roja Elysium\n$295.00", "#3d3014", "#ffd700"),
    ("Diseño VIP", "Sauvage Elixir\n$125.50", "#142634", "#70b5ff"),
    ("Diseño Top", "TF Ombré Leather\n$140.00", "#142634", "#70b5ff"),
    ("Diseño Pop", "JPG Le Male\n$95.00", "#142634", "#70b5ff"),
]

for idx, (categoria, perfume, bg_col, fg_col) in enumerate(catalogo_grid):
    fila = 1 + (idx // 3)
    col = idx % 3
    lbl_frasco = tk.Label(
        tab_grid, 
        text=f"[{categoria}]\n{perfume}", 
        bg=bg_col, 
        fg=fg_col, 
        font=("Helvetica", 8, "bold"), 
        padx=12, 
        pady=10, 
        relief="groove", 
        bd=1
    )
    lbl_frasco.grid(row=fila, column=col, padx=8, pady=8, sticky="nsew")

# Banner con columnspan=3
lbl_promo = tk.Label(
    tab_grid, 
    text="✨ OFERTA EXCLUSIVA DEL MES: 15% OFF EN DECANTES — grid(columnspan=3) ✨", 
    bg="#d4af37", 
    fg="#121212", 
    font=("Helvetica", 9, "bold"), 
    pady=8
)
lbl_promo.grid(row=3, column=0, columnspan=3, sticky="ew", padx=8, pady=12)

for c in range(3):
    tab_grid.columnconfigure(c, weight=1)

# ==========================================
# PESTAÑA 3: PLACE (Escaparate VIP)
# ==========================================
tab_place = tk.Frame(notebook, bg="#1a1a1a")
notebook.add(tab_place, text=" 3. Escaparate VIP (place) ")

tk.Label(
    tab_place, 
    text="place(): Ubicación milimétrica de frascos en el escaparate VIP con coordenadas (x, y, relx, rely).",
    bg="#1a1a1a", fg="#aaaaaa", font=("Helvetica", 9, "italic")
).pack(pady=8)

area_escaparate = tk.Frame(tab_place, bg="#0d0d0d", bd=1, relief="solid")
area_escaparate.pack(fill="both", expand=True, padx=15, pady=(5, 15))

# Esquina Superior Izquierda (x=20, y=20)
tk.Label(
    area_escaparate, 
    text="🧴 Tester Entrada\n(x=20, y=20)", 
    bg="#242424", 
    fg="#ffffff", 
    font=("Consolas", 8), 
    padx=8, 
    pady=6
).place(x=20, y=20)

# Esquina Superior Derecha (x=480, y=20)
tk.Label(
    area_escaparate, 
    text="🎁 Muestrario Decants\n(relx=0.72, y=20)", 
    bg="#242424", 
    fg="#ffffff", 
    font=("Consolas", 8), 
    padx=8, 
    pady=6
).place(relx=0.70, y=20)

# Centro del Escaparate (relx=0.5, rely=0.5)
tk.Label(
    area_escaparate, 
    text="👑 PIEZA CENTRAL DEL ESCAPARATE\nClive Christian No. 1 (Pure Parfum)\n$850.00 USD\n\n(relx=0.5, rely=0.48, anchor='center')", 
    bg="#d4af37", 
    fg="#121212", 
    font=("Helvetica", 10, "bold"), 
    padx=20, 
    pady=16, 
    relief="raised", 
    bd=2
).place(relx=0.5, rely=0.48, anchor="center")

# Barra dorada inferior (relx=0.05, rely=0.84, relwidth=0.9)
tk.Label(
    area_escaparate, 
    text="✨ Ryan.ShopMx | Vitrina de Fragancias de Colección Exclusiva ✨", 
    bg="#1b1b1b", 
    fg="#d4af37", 
    font=("Helvetica", 9, "bold"), 
    pady=4
).place(relx=0.05, rely=0.84, relwidth=0.90)

if __name__ == "__main__":
    root.mainloop()
