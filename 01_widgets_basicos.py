"""
01_widgets_basicos.py
Tema: Perfil Olfativo y Asesor de Fragancias (Haute Parfumerie)
Demostración de widgets básicos de Tkinter:
- Label (títulos y estilo elegante oscuro/dorado)
- Entry (nombre del cliente)
- Radiobutton (selección de familia olfativa)
- Checkbutton (opciones de presentación y obsequio)
- Scale (presupuesto / concentración en slider)
- Button (generar recomendación)
- Variables reactivas (StringVar, IntVar, BooleanVar)
"""

import tkinter as tk

def generar_recomendacion():
    cliente = var_cliente.get().strip() or "Cliente VIP"
    familia = var_familia.get()
    concentracion = scale_concentracion.get()
    muestra = "Sí (Muestra gratis incluida)" if var_muestra.get() else "No"
    empaque = "Empaque de Lujo (+ Cintas doradas)" if var_empaque.get() else "Estándar"

    # Lógica de recomendación de perfumes
    recomendaciones = {
        "Amaderada": ("Tom Ford Oud Wood", "$160.00"),
        "Oriental": ("Xerjoff Erba Pura", "$185.00"),
        "Cítrica / Fresca": ("Dior Sauvage Elixir", "$125.50"),
        "Gourmand / Dulce": ("Afnan 9pm", "$38.00")
    }

    perfume, precio = recomendaciones.get(familia, ("Tom Ford Black Orchid", "$145.00"))

    resumen = (
        f"═══════════════════════════════════════════\n"
        f"  PERFIL OLFATIVO — BOUTIQUE RYAN.SHOPMX   \n"
        f"═══════════════════════════════════════════\n"
        f"• Cliente: {cliente}\n"
        f"• Familia Favorita: {familia}\n"
        f"• Concentración Deseada: {concentracion}% de Esencia (Extrait)\n"
        f"• Muestra de Cortesía: {muestra}\n"
        f"• Presentación: {empaque}\n"
        f"-------------------------------------------\n"
        f"✨ FRAGANCIA RECOMENDADA: {perfume}\n"
        f"💵 PRECIO ESTIMADO: {precio}\n"
        f"═══════════════════════════════════════════"
    )
    lbl_resultado.config(text=resumen, fg="#d4af37")

def reiniciar_formulario():
    var_cliente.set("")
    var_familia.set("Amaderada")
    scale_concentracion.set(20)
    var_muestra.set(True)
    var_empaque.set(False)
    lbl_resultado.config(text="Complete el perfil y presione 'Descubrir Fragancia'.", fg="#888888")

root = tk.Tk()
root.title("01 - Perfil Olfativo | Widgets Básicos")
root.geometry("540x660")
root.config(bg="#121212")

# Título
tk.Label(
    root, 
    text="✨ ASESOR DE ALTA PERFUMERÍA ✨", 
    font=("Helvetica", 14, "bold"), 
    bg="#121212", 
    fg="#d4af37"
).pack(pady=(15, 6))

# 1. Entry: Nombre del Cliente
frame_cliente = tk.LabelFrame(root, text=" 1. Datos del Cliente (tk.Entry) ", bg="#1b1b1b", fg="#e0e0e0", padx=10, pady=6)
frame_cliente.pack(fill="x", padx=20, pady=5)

tk.Label(frame_cliente, text="Nombre del Cliente:", bg="#1b1b1b", fg="#aaaaaa").pack(anchor="w")
var_cliente = tk.StringVar()
entry_cliente = tk.Entry(frame_cliente, textvariable=var_cliente, font=("Helvetica", 10), bg="#2a2a2a", fg="#ffffff", insertbackground="#d4af37")
entry_cliente.pack(fill="x", pady=4)

# 2. Radiobutton: Familia Olfativa
frame_familia = tk.LabelFrame(root, text=" 2. Familia Olfativa Favorita (tk.Radiobutton) ", bg="#1b1b1b", fg="#e0e0e0", padx=10, pady=6)
frame_familia.pack(fill="x", padx=20, pady=5)

var_familia = tk.StringVar(value="Amaderada")
familias = ["Amaderada", "Oriental", "Cítrica / Fresca", "Gourmand / Dulce"]
for f in familias:
    tk.Radiobutton(
        frame_familia, 
        text=f, 
        variable=var_familia, 
        value=f, 
        bg="#1b1b1b", 
        fg="#ffffff", 
        selectcolor="#2a2a2a",
        activebackground="#1b1b1b",
        activeforeground="#d4af37"
    ).pack(anchor="w", pady=1)

# 3. Checkbutton: Opciones de Compra
frame_opciones = tk.LabelFrame(root, text=" 3. Preferencias de Obsequio (tk.Checkbutton) ", bg="#1b1b1b", fg="#e0e0e0", padx=10, pady=6)
frame_opciones.pack(fill="x", padx=20, pady=5)

var_muestra = tk.BooleanVar(value=True)
var_empaque = tk.BooleanVar(value=False)

tk.Checkbutton(
    frame_opciones, 
    text="Incluir muestra decant 2ml de cortesía", 
    variable=var_muestra, 
    bg="#1b1b1b", 
    fg="#ffffff", 
    selectcolor="#2a2a2a",
    activebackground="#1b1b1b",
    activeforeground="#d4af37"
).pack(anchor="w")

tk.Checkbutton(
    frame_opciones, 
    text="Caja de regalo de lujo con sello lacrado", 
    variable=var_empaque, 
    bg="#1b1b1b", 
    fg="#ffffff", 
    selectcolor="#2a2a2a",
    activebackground="#1b1b1b",
    activeforeground="#d4af37"
).pack(anchor="w")

# 4. Scale: Concentración de Esencia
frame_esencia = tk.LabelFrame(root, text=" 4. Concentración de Esencia % (tk.Scale) ", bg="#1b1b1b", fg="#e0e0e0", padx=10, pady=4)
frame_esencia.pack(fill="x", padx=20, pady=5)

scale_concentracion = tk.Scale(
    frame_esencia, 
    from_=10, 
    to=40, 
    orient="horizontal", 
    bg="#1b1b1b", 
    fg="#d4af37", 
    troughcolor="#2a2a2a", 
    highlightthickness=0
)
scale_concentracion.set(20)
scale_concentracion.pack(fill="x")

# Botones de Acción
frame_botones = tk.Frame(root, bg="#121212")
frame_botones.pack(pady=8)

btn_recomendar = tk.Button(
    frame_botones, 
    text="✨ Descubrir Fragancia", 
    command=generar_recomendacion, 
    bg="#d4af37", 
    fg="#121212", 
    font=("Helvetica", 9, "bold"), 
    relief="flat", 
    cursor="hand2", 
    padx=12, 
    pady=4
)
btn_recomendar.pack(side="left", padx=5)

btn_limpiar = tk.Button(
    frame_botones, 
    text="Reiniciar", 
    command=reiniciar_formulario, 
    bg="#333333", 
    fg="#ffffff", 
    font=("Helvetica", 9), 
    relief="flat", 
    cursor="hand2", 
    padx=10, 
    pady=4
)
btn_limpiar.pack(side="left", padx=5)

# Resultado
lbl_resultado = tk.Label(
    root, 
    text="Complete el perfil y presione 'Descubrir Fragancia'.", 
    font=("Consolas", 8), 
    bg="#0a0a0a", 
    fg="#aaaaaa", 
    justify="left", 
    relief="solid", 
    bd=1, 
    padx=10, 
    pady=8
)
lbl_resultado.pack(fill="x", padx=20, pady=(5, 15))

if __name__ == "__main__":
    root.mainloop()
