"""
03_dialogos_y_ventanas.py
Tema: Centro de Consultas y Fichas Técnicas de Perfumería
Demostración de cuadros de diálogo y ventanas secundarias:
- messagebox (alertas de stock, avisos de fragancias y confirmación de compra)
- filedialog (exportar ticket a archivo .txt o cargar catálogo)
- colorchooser (personalizar el tono del frasco o la caja de regalo)
- Toplevel (ventana modal con la Pirámide Olfativa detallada de un perfume)
"""

import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser

def msg_stock():
    messagebox.showinfo(
        "Stock Confirmado", 
        "✅ Fragancia disponible en bodega:\n\n• Xerjoff Erba Pura (100ml EDP)\n• Ubicación: Anaquel Nicho VIP A-3"
    )

def msg_alerta():
    messagebox.showwarning(
        "Inventario Crítico", 
        "⚠️ ¡Atención!\nSolo quedan 2 piezas de 'Dior Sauvage Elixir' en exhibición."
    )

def msg_error_pago():
    messagebox.showerror(
        "Terminal Rechazada", 
        "❌ Error al procesar la tarjeta para la orden de Tom Ford Black Orchid.\nIntente con otro método de pago."
    )

def msg_envolver_regalo():
    respuesta = messagebox.askyesno(
        "Servicio de Lujo", 
        "¿Desea envolver la fragancia en caja rígida negra con lazo de satín dorado?"
    )
    resultado = "El cliente SOLICITÓ envoltura de lujo para regalo ✨" if respuesta else "El cliente prefirió empaque estándar ecológico."
    lbl_log.config(text=resultado, fg="#d4af37")

def exportar_deseos():
    ruta = filedialog.asksaveasfilename(
        title="Guardar Lista de Fragancias Deseadas",
        defaultextension=".txt",
        initialfile="wishlist_perfumes.txt",
        filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("WISHLIST RYAN.SHOPMX\n1. Xerjoff Naxos\n2. Baccarat Rouge 540\n3. Afnan 9pm\n")
        lbl_log.config(text=f"Lista de deseos guardada exitosamente en:\n{ruta}", fg="#80e892")

def cargar_catalogo():
    ruta = filedialog.askopenfilename(
        title="Seleccionar Archivo de Fragancias",
        filetypes=[("Archivos de Texto", "*.txt *.csv"), ("Todos los archivos", "*.*")]
    )
    if ruta:
        lbl_log.config(text=f"Catálogo externo importado desde:\n{ruta}", fg="#70b5ff")

def cambiar_color_frasco():
    color = colorchooser.askcolor(title="Selecciona el color del frasco o caja")
    if color[1]:
        root.config(bg=color[1])
        lbl_log.config(text=f"Color de frasco personalizado aplicado: {color[1]} (RGB: {color[0]})", fg="white")

def abrir_piramide_olfativa():
    modal = tk.Toplevel(root)
    modal.title("Pirámide Olfativa — Xerjoff Erba Pura")
    modal.geometry("380x340")
    modal.config(bg="#1c1b1f")
    modal.grab_set()  # Modal: bloquea la ventana principal

    tk.Label(
        modal, 
        text="🏛️ FICHA TÉCNICA OLFATIVA", 
        font=("Helvetica", 12, "bold"), 
        bg="#1c1b1f", 
        fg="#d4af37"
    ).pack(pady=(15, 6))

    tk.Label(
        modal, 
        text="Xerjoff — Erba Pura (Eau de Parfum)", 
        font=("Helvetica", 9, "italic"), 
        bg="#1c1b1f", 
        fg="#e0e0e0"
    ).pack()

    piramide_frame = tk.Frame(modal, bg="#27252c", padx=15, pady=10, relief="groove", bd=1)
    piramide_frame.pack(fill="x", padx=20, pady=12)

    tk.Label(piramide_frame, text="🍋 NOTAS DE SALIDA (Primeros 15 min):", font=("Helvetica", 8, "bold"), bg="#27252c", fg="#ffd700").pack(anchor="w")
    tk.Label(piramide_frame, text="   Naranja de Sicilia, Bergamota de Calabria, Limón", font=("Helvetica", 8), bg="#27252c", fg="#cccccc").pack(anchor="w", pady=(0, 6))

    tk.Label(piramide_frame, text="🍇 NOTAS DE CORAZÓN (2 - 6 horas):", font=("Helvetica", 8, "bold"), bg="#27252c", fg="#ffd700").pack(anchor="w")
    tk.Label(piramide_frame, text="   Cesta de Frutas Mediterráneas dulces", font=("Helvetica", 8), bg="#27252c", fg="#cccccc").pack(anchor="w", pady=(0, 6))

    tk.Label(piramide_frame, text="🪵 NOTAS DE FONDO (Fijación 8+ horas):", font=("Helvetica", 8, "bold"), bg="#27252c", fg="#ffd700").pack(anchor="w")
    tk.Label(piramide_frame, text="   Almizcle Blanco, Ámbar cálido, Vainilla de Madagascar", font=("Helvetica", 8), bg="#27252c", fg="#cccccc").pack(anchor="w")

    tk.Button(
        modal, 
        text="Cerrar Ficha", 
        command=modal.destroy, 
        bg="#d4af37", 
        fg="#121212", 
        font=("Helvetica", 9, "bold"), 
        relief="flat", 
        cursor="hand2"
    ).pack(pady=8)

root = tk.Tk()
root.title("03 - Consultas de Fragancias | Diálogos y Modales")
root.geometry("580x620")
root.config(bg="#121212")

tk.Label(
    root, 
    text="✨ CENTRO DE CONSULTAS DE PERFUMERÍA ✨", 
    font=("Helvetica", 14, "bold"), 
    bg="#121212", 
    fg="#d4af37"
).pack(pady=(15, 8))

# 1. Alertas messagebox
f_msg = tk.LabelFrame(root, text=" 1. Alertas de Tienda (tkinter.messagebox) ", bg="#1a1a1a", fg="#e0e0e0", padx=10, pady=10)
f_msg.pack(fill="x", padx=20, pady=6)

tk.Button(f_msg, text="Consultar Stock", command=msg_stock, bg="#2e4d34", fg="#80e892", font=("Helvetica", 8, "bold"), padx=6).pack(side="left", padx=3)
tk.Button(f_msg, text="Aviso Escasez", command=msg_alerta, bg="#4d4420", fg="#ffea75", font=("Helvetica", 8, "bold"), padx=6).pack(side="left", padx=3)
tk.Button(f_msg, text="Fallo Terminal", command=msg_error_pago, bg="#4d2020", fg="#ff7575", font=("Helvetica", 8, "bold"), padx=6).pack(side="left", padx=3)
tk.Button(f_msg, text="¿Envolver Lujo?", command=msg_envolver_regalo, bg="#d4af37", fg="#121212", font=("Helvetica", 8, "bold"), padx=6).pack(side="left", padx=3)

# 2. Selector de Archivos filedialog
f_files = tk.LabelFrame(root, text=" 2. Gestión de Listas y Catálogos (tkinter.filedialog) ", bg="#1a1a1a", fg="#e0e0e0", padx=10, pady=10)
f_files.pack(fill="x", padx=20, pady=6)

tk.Button(f_files, text="💾 Exportar Wishlist (.txt)", command=exportar_deseos, bg="#223344", fg="#70b5ff", font=("Helvetica", 9, "bold")).pack(side="left", padx=6)
tk.Button(f_files, text="📂 Cargar Catálogo Externo", command=cargar_catalogo, bg="#2f2244", fg="#cba6f7", font=("Helvetica", 9, "bold")).pack(side="left", padx=6)

# 3. Personalización y Ventana Toplevel
f_modal = tk.LabelFrame(root, text=" 3. Personalización y Ficha Técnica (Toplevel / colorchooser) ", bg="#1a1a1a", fg="#e0e0e0", padx=10, pady=10)
f_modal.pack(fill="x", padx=20, pady=6)

tk.Button(f_modal, text="🎨 Personalizar Color de Frasco", command=cambiar_color_frasco, bg="#3d2a1b", fg="#f5b971", font=("Helvetica", 8, "bold")).pack(side="left", padx=4)
tk.Button(f_modal, text="📜 Ver Pirámide Olfativa (Modal)", command=abrir_piramide_olfativa, bg="#d4af37", fg="#121212", font=("Helvetica", 8, "bold")).pack(side="left", padx=4)

# Log inferior
lbl_log = tk.Label(
    root, 
    text="Presione cualquiera de los botones para ver las acciones del sistema de perfumería.", 
    font=("Consolas", 8), 
    bg="#0a0a0a", 
    fg="#888888", 
    relief="solid", 
    bd=1, 
    padx=10, 
    pady=15, 
    wraplength=500
)
lbl_log.pack(fill="both", expand=True, padx=20, pady=(10, 15))

if __name__ == "__main__":
    root.mainloop()
