"""
03_dialogos_y_ventanas.py
Demostración de cuadros de diálogo y ventanas secundarias:
- messagebox (alertas de información, advertencia, error y confirmación)
- filedialog (abrir y guardar archivos, seleccionar carpetas)
- colorchooser (selector interactivo de colores RGB/HEX)
- Toplevel (ventanas secundarias modales y flotantes)
"""

import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser

def msg_info():
    messagebox.showinfo("Información", "Esta es una ventana de información estándar.")

def msg_warning():
    messagebox.showwarning("Advertencia", "¡Cuidado! Esta es una advertencia de prueba.")

def msg_error():
    messagebox.showerror("Error", "Se ha simulado un error crítico del sistema.")

def msg_pregunta():
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de continuar con la acción?")
    resultado = "El usuario eligió: SÍ" if respuesta else "El usuario eligió: NO"
    lbl_log.config(text=resultado, fg="#00ffcc")

def abrir_archivo():
    ruta = filedialog.askopenfilename(
        title="Seleccionar Archivo",
        filetypes=[("Archivos de Texto / Python", "*.txt *.py"), ("Todos los archivos", "*.*")]
    )
    if ruta:
        lbl_log.config(text=f"Archivo seleccionado:\n{ruta}", fg="#a6e3a1")

def guardar_archivo():
    ruta = filedialog.asksaveasfilename(
        title="Guardar Como",
        defaultextension=".txt",
        filetypes=[("Texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta:
        lbl_log.config(text=f"Ruta para guardar:\n{ruta}", fg="#f9e2af")

def seleccionar_color():
    color = colorchooser.askcolor(title="Selecciona un color para la ventana")
    if color[1]:  # color[1] contiene el código HEX (ej: '#ff00aa')
        root.config(bg=color[1])
        lbl_log.config(text=f"Color aplicado: {color[1]} (RGB: {color[0]})", fg="white")

def abrir_ventana_secundaria():
    # Ventana Toplevel
    ventana_hija = tk.Toplevel(root)
    ventana_hija.title("Ventana Secundaria (Toplevel)")
    ventana_hija.geometry("340x220")
    ventana_hija.config(bg="#1e1e2e")
    
    # Hacerla modal (bloquea la ventana principal hasta cerrarse)
    ventana_hija.grab_set()

    tk.Label(
        ventana_hija, 
        text="✨ Ventana Secundaria Modal ✨", 
        font=("Helvetica", 11, "bold"), 
        bg="#1e1e2e", 
        fg="#f5c2e7"
    ).pack(pady=15)

    tk.Label(
        ventana_hija, 
        text="Esta ventana fue creada con tk.Toplevel.\nBloquea la principal hasta que la cierres.", 
        bg="#1e1e2e", 
        fg="#cdd6f4", 
        justify="center"
    ).pack(pady=10)

    tk.Button(
        ventana_hija, 
        text="Cerrar Ventana", 
        command=ventana_hija.destroy, 
        bg="#f38ba8", 
        fg="#11111b", 
        font=("Helvetica", 9, "bold"), 
        relief="flat", 
        cursor="hand2"
    ).pack(pady=12)

# Ventana Principal
root = tk.Tk()
root.title("03 - Diálogos, Archivos y Ventanas Secundarias")
root.geometry("560x580")
root.config(bg="#181825")

tk.Label(
    root, 
    text="Diálogos del Sistema y Ventanas", 
    font=("Helvetica", 14, "bold"), 
    bg="#181825", 
    fg="#cdd6f4"
).pack(pady=(15, 10))

# 1. Alertas de messagebox
frame_msgs = tk.LabelFrame(root, text=" 1. Cuadros de Mensaje (messagebox) ", bg="#1e1e2e", fg="#cdd6f4", padx=10, pady=10)
frame_msgs.pack(fill="x", padx=20, pady=8)

tk.Button(frame_msgs, text="Info", command=msg_info, bg="#89b4fa", fg="#11111b", font=("Helvetica", 9, "bold"), padx=10).pack(side="left", padx=4)
tk.Button(frame_msgs, text="Advertencia", command=msg_warning, bg="#fab387", fg="#11111b", font=("Helvetica", 9, "bold"), padx=10).pack(side="left", padx=4)
tk.Button(frame_msgs, text="Error", command=msg_error, bg="#f38ba8", fg="#11111b", font=("Helvetica", 9, "bold"), padx=10).pack(side="left", padx=4)
tk.Button(frame_msgs, text="Pregunta Sí/No", command=msg_pregunta, bg="#a6e3a1", fg="#11111b", font=("Helvetica", 9, "bold"), padx=10).pack(side="left", padx=4)

# 2. Explorador de Archivos (filedialog)
frame_files = tk.LabelFrame(root, text=" 2. Selector de Archivos (filedialog) ", bg="#1e1e2e", fg="#cdd6f4", padx=10, pady=10)
frame_files.pack(fill="x", padx=20, pady=8)

tk.Button(frame_files, text="📂 Abrir Archivo...", command=abrir_archivo, bg="#b4befe", fg="#11111b", font=("Helvetica", 9, "bold")).pack(side="left", padx=6)
tk.Button(frame_files, text="💾 Guardar Como...", command=guardar_archivo, bg="#f9e2af", fg="#11111b", font=("Helvetica", 9, "bold")).pack(side="left", padx=6)

# 3. Selector de color y Toplevel
frame_avanzado = tk.LabelFrame(root, text=" 3. Selector de Color y Nueva Ventana ", bg="#1e1e2e", fg="#cdd6f4", padx=10, pady=10)
frame_avanzado.pack(fill="x", padx=20, pady=8)

tk.Button(frame_avanzado, text="🎨 Elegir Color de Fondo", command=seleccionar_color, bg="#cba6f7", fg="#11111b", font=("Helvetica", 9, "bold")).pack(side="left", padx=6)
tk.Button(frame_avanzado, text="🪟 Abrir Ventana Modal", command=abrir_ventana_secundaria, bg="#94e2d5", fg="#11111b", font=("Helvetica", 9, "bold")).pack(side="left", padx=6)

# Área de registro de eventos
lbl_log = tk.Label(
    root, 
    text="Interactúa con los botones para ver los resultados aquí.", 
    font=("Consolas", 9), 
    bg="#11111b", 
    fg="#a6adc8", 
    relief="sunken", 
    bd=1, 
    padx=10, 
    pady=15, 
    wraplength=480
)
lbl_log.pack(fill="both", expand=True, padx=20, pady=(10, 20))

if __name__ == "__main__":
    root.mainloop()
