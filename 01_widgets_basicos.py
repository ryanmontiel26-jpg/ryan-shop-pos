"""
01_widgets_basicos.py
Demostración de los widgets fundamentales de Tkinter:
- Label (etiquetas de texto y estilo)
- Entry (campos de entrada de texto y contraseñas)
- Button (botones interactivos con funciones asociadas)
- Checkbutton (casillas de selección booleana)
- Radiobutton (opciones de selección única)
- Scale (control deslizante numérico)
- Variables de control (StringVar, IntVar, BooleanVar)
"""

import tkinter as tk

def actualizar_resumen():
    nombre = var_nombre.get() if var_nombre.get().strip() else "(Sin nombre)"
    notif = "Sí" if var_notificaciones.get() else "No"
    nivel = var_nivel.get()
    vol = scale_volumen.get()
    
    texto = (
        f"--- Datos Ingresados ---\n"
        f"Nombre: {nombre}\n"
        f"Recibir notificaciones: {notif}\n"
        f"Nivel de experiencia: {nivel}\n"
        f"Volumen seleccionado: {vol}%"
    )
    lbl_resultado.config(text=texto, fg="#00ffcc")

def limpiar_campos():
    var_nombre.set("")
    var_notificaciones.set(False)
    var_nivel.set("Intermedio")
    scale_volumen.set(50)
    lbl_resultado.config(text="Formulario reiniciado.", fg="#888888")

# Ventana Principal
root = tk.Tk()
root.title("01 - Widgets Básicos de Tkinter")
root.geometry("520x620")
root.config(bg="#1e1e2e")

# Título principal
lbl_titulo = tk.Label(
    root, 
    text="Demostración de Widgets Básicos", 
    font=("Helvetica", 14, "bold"), 
    bg="#1e1e2e", 
    fg="#f5c2e7"
)
lbl_titulo.pack(pady=(15, 10))

# 1. Campo de texto (Entry)
frame_entry = tk.LabelFrame(root, text=" 1. Entry (Entrada de Texto) ", bg="#181825", fg="#cdd6f4", padx=10, pady=8)
frame_entry.pack(fill="x", padx=20, pady=6)

tk.Label(frame_entry, text="Escribe tu nombre:", bg="#181825", fg="#a6adc8").pack(anchor="w")
var_nombre = tk.StringVar()
entry_nombre = tk.Entry(frame_entry, textvariable=var_nombre, font=("Helvetica", 10), bg="#313244", fg="#ffffff", insertbackground="white")
entry_nombre.pack(fill="x", pady=4)

# 2. Casilla de verificación (Checkbutton)
frame_check = tk.LabelFrame(root, text=" 2. Checkbutton (Casilla de Selección) ", bg="#181825", fg="#cdd6f4", padx=10, pady=8)
frame_check.pack(fill="x", padx=20, pady=6)

var_notificaciones = tk.BooleanVar(value=True)
chk_notif = tk.Checkbutton(
    frame_check, 
    text="Deseo recibir notificaciones por correo", 
    variable=var_notificaciones,
    bg="#181825", 
    fg="#cdd6f4", 
    selectcolor="#313244",
    activebackground="#181825",
    activeforeground="#f5c2e7"
)
chk_notif.pack(anchor="w")

# 3. Botones de opción (Radiobutton)
frame_radio = tk.LabelFrame(root, text=" 3. Radiobutton (Selección Única) ", bg="#181825", fg="#cdd6f4", padx=10, pady=8)
frame_radio.pack(fill="x", padx=20, pady=6)

var_nivel = tk.StringVar(value="Intermedio")
niveles = ["Principiante", "Intermedio", "Avanzado"]
for n in niveles:
    rb = tk.Radiobutton(
        frame_radio, 
        text=n, 
        variable=var_nivel, 
        value=n, 
        bg="#181825", 
        fg="#cdd6f4", 
        selectcolor="#313244",
        activebackground="#181825",
        activeforeground="#f5c2e7"
    )
    rb.pack(anchor="w", pady=2)

# 4. Control deslizante (Scale)
frame_scale = tk.LabelFrame(root, text=" 4. Scale (Control Deslizante) ", bg="#181825", fg="#cdd6f4", padx=10, pady=8)
frame_scale.pack(fill="x", padx=20, pady=6)

scale_volumen = tk.Scale(
    frame_scale, 
    from_=0, 
    to=100, 
    orient="horizontal", 
    bg="#181825", 
    fg="#cdd6f4", 
    troughcolor="#313244", 
    highlightthickness=0
)
scale_volumen.set(65)
scale_volumen.pack(fill="x")

# 5. Botones de acción (Button)
frame_botones = tk.Frame(root, bg="#1e1e2e")
frame_botones.pack(pady=10)

btn_guardar = tk.Button(
    frame_botones, 
    text="Enviar / Actualizar", 
    command=actualizar_resumen, 
    bg="#a6e3a1", 
    fg="#11111b", 
    font=("Helvetica", 9, "bold"), 
    padx=10, 
    pady=4,
    relief="flat",
    cursor="hand2"
)
btn_guardar.pack(side="left", padx=5)

btn_limpiar = tk.Button(
    frame_botones, 
    text="Limpiar", 
    command=limpiar_campos, 
    bg="#f38ba8", 
    fg="#11111b", 
    font=("Helvetica", 9, "bold"), 
    padx=10, 
    pady=4,
    relief="flat",
    cursor="hand2"
)
btn_limpiar.pack(side="left", padx=5)

# 6. Etiqueta para mostrar resultados dinámicos
lbl_resultado = tk.Label(
    root, 
    text="Presiona 'Enviar / Actualizar' para ver los datos aquí.", 
    font=("Consolas", 9), 
    bg="#11111b", 
    fg="#a6adc8", 
    justify="left", 
    relief="sunken", 
    bd=1, 
    padx=10, 
    pady=8
)
lbl_resultado.pack(fill="x", padx=20, pady=(5, 15))

if __name__ == "__main__":
    root.mainloop()
