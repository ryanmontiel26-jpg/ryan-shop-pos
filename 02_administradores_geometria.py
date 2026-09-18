"""
02_administradores_geometria.py
Demostración visual de los 3 administradores de geometría de Tkinter:
1. pack()  — Empaquetado por lados (top, bottom, left, right), fill y expand.
2. grid()  — Distribución en cuadrícula matricial (filas, columnas, sticky, spans).
3. place() — Posicionamiento absoluto y relativo (x, y, relx, rely).
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("02 - Administradores de Geometría (pack, grid, place)")
root.geometry("640x520")
root.config(bg="#2b2d42")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# ==========================================
# PESTAÑA 1: PACK
# ==========================================
tab_pack = tk.Frame(notebook, bg="#1a1a24")
notebook.add(tab_pack, text=" 1. pack() ")

lbl_info_pack = tk.Label(
    tab_pack, 
    text="pack() organiza elementos apilándolos por lados (TOP, BOTTOM, LEFT, RIGHT).",
    bg="#1a1a24", fg="#8d99ae", font=("Helvetica", 9, "italic")
)
lbl_info_pack.pack(pady=8)

tk.Label(tab_pack, text="pack(side='top', fill='x')", bg="#ef233c", fg="white", font=("Helvetica", 10, "bold"), pady=6).pack(side="top", fill="x", padx=20, pady=4)
tk.Label(tab_pack, text="pack(side='bottom', fill='x')", bg="#2b2d42", fg="white", font=("Helvetica", 10, "bold"), pady=6).pack(side="bottom", fill="x", padx=20, pady=4)

frame_pack_medio = tk.Frame(tab_pack, bg="#1a1a24")
frame_pack_medio.pack(fill="both", expand=True, padx=20, pady=4)

tk.Label(frame_pack_medio, text="pack(side='left', expand=True)", bg="#3a86ff", fg="white", font=("Helvetica", 9, "bold")).pack(side="left", fill="both", expand=True, padx=4)
tk.Label(frame_pack_medio, text="pack(side='right', expand=True)", bg="#8338ec", fg="white", font=("Helvetica", 9, "bold")).pack(side="right", fill="both", expand=True, padx=4)

# ==========================================
# PESTAÑA 2: GRID
# ==========================================
tab_grid = tk.Frame(notebook, bg="#1a1a24")
notebook.add(tab_grid, text=" 2. grid() ")

lbl_info_grid = tk.Label(
    tab_grid, 
    text="grid() organiza elementos en una matriz de filas (row) y columnas (column).",
    bg="#1a1a24", fg="#8d99ae", font=("Helvetica", 9, "italic")
)
lbl_info_grid.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

# Formulario típico usando grid
colores = ["#06d6a0", "#118ab2", "#ffd166", "#f78c6b", "#e76f51"]

for fila in range(1, 4):
    for col in range(3):
        color = colores[(fila * 3 + col) % len(colores)]
        lbl = tk.Label(
            tab_grid, 
            text=f"Fila {fila}, Col {col}", 
            bg=color, 
            fg="#121212", 
            font=("Helvetica", 9, "bold"), 
            padx=15, 
            pady=12
        )
        lbl.grid(row=fila, column=col, padx=8, pady=8, sticky="nsew")

# Elemento con columnspan
lbl_span = tk.Label(
    tab_grid, 
    text="Elemento con columnspan=3 (Ocupa 3 columnas)", 
    bg="#8338ec", 
    fg="white", 
    font=("Helvetica", 10, "bold"), 
    pady=10
)
lbl_span.grid(row=4, column=0, columnspan=3, sticky="ew", padx=8, pady=12)

# Configurar expansión de columnas
for c in range(3):
    tab_grid.columnconfigure(c, weight=1)

# ==========================================
# PESTAÑA 3: PLACE
# ==========================================
tab_place = tk.Frame(notebook, bg="#1a1a24")
notebook.add(tab_place, text=" 3. place() ")

lbl_info_place = tk.Label(
    tab_place, 
    text="place() ubica elementos por coordenadas fijas (x, y) o proporcionales (relx, rely).",
    bg="#1a1a24", fg="#8d99ae", font=("Helvetica", 9, "italic")
)
lbl_info_place.pack(pady=8)

canvas_area = tk.Frame(tab_place, bg="#0f0f17", bd=1, relief="solid")
canvas_area.pack(fill="both", expand=True, padx=20, pady=(5, 20))

tk.Label(canvas_area, text="Coordenada fija:\nx=20, y=30", bg="#06d6a0", fg="#121212", font=("Consolas", 8, "bold"), padx=6, pady=4).place(x=20, y=30)
tk.Label(canvas_area, text="Coordenada fija:\nx=180, y=90", bg="#ffd166", fg="#121212", font=("Consolas", 8, "bold"), padx=6, pady=4).place(x=180, y=90)

# Centro relativo
tk.Label(
    canvas_area, 
    text="Centro exacto:\nrelx=0.5, rely=0.5\nanchor='center'", 
    bg="#ef233c", 
    fg="white", 
    font=("Consolas", 9, "bold"), 
    padx=12, 
    pady=8
).place(relx=0.5, rely=0.5, anchor="center")

# Barra inferior relativa
tk.Label(
    canvas_area, 
    text="relx=0.05, rely=0.85, relwidth=0.90", 
    bg="#3a86ff", 
    fg="white", 
    font=("Consolas", 8, "bold"), 
    pady=4
).place(relx=0.05, rely=0.85, relwidth=0.90)

if __name__ == "__main__":
    root.mainloop()
