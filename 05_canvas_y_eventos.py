"""
05_canvas_y_eventos.py
Tema: Taller de Grabado y Personalización de Frascos de Perfume
Demostración de gráficos interactivos y eventos en Tkinter:
- Canvas (renderizado vectorial de un frasco de perfume de alta gama)
- Manejo de Eventos del Ratón (<Button-1>, <B1-Motion>, <Motion>)
- Grabado a mano alzada de iniciales/firmas en la placa dorada del frasco
- Cambio de color del líquido de la fragancia (Erba Pura, Baccarat, Sauvage, Oud)
"""

import tkinter as tk

class GrabadoFrascoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("05 - Grabado de Frascos | Canvas y Eventos")
        self.root.geometry("700x620")
        self.root.config(bg="#121212")

        self.color_grabado = "#121212"
        self.color_liquido = "#d4af37"
        self.ultimo_x = None
        self.ultimo_y = None

        self.crear_interfaz()
        self.dibujar_frasco()

    def crear_interfaz(self):
        # Header
        tk.Label(
            self.root, 
            text="✨ TALLER DE GRABADO Y PERSONALIZACIÓN DE FRASCOS ✨", 
            font=("Helvetica", 12, "bold"), 
            bg="#121212", 
            fg="#d4af37"
        ).pack(pady=(12, 6))

        # Barra de herramientas
        frame_tools = tk.Frame(self.root, bg="#1b1b1b", padx=12, pady=6)
        frame_tools.pack(fill="x", padx=15)

        tk.Label(frame_tools, text="Líquido:", bg="#1b1b1b", fg="#e0e0e0", font=("Helvetica", 9, "bold")).pack(side="left", padx=(0, 4))

        fragancias_demo = [
            ("Dorado (Erba Pura)", "#d4af37"),
            ("Azul Noche (Sauvage)", "#1a3b5c"),
            ("Rubí (Baccarat 540)", "#800020"),
            ("Ámbar (Oud Wood)", "#8a4f1d")
        ]

        for nombre, col in fragancias_demo:
            btn = tk.Button(
                frame_tools, 
                text=nombre.split()[0], 
                bg=col, 
                fg="white" if col != "#d4af37" else "#121212",
                font=("Helvetica", 8, "bold"), 
                relief="flat", 
                cursor="hand2", 
                padx=6,
                command=lambda c=col: self.cambiar_liquido(c)
            )
            btn.pack(side="left", padx=3)

        tk.Label(frame_tools, text="Trazo:", bg="#1b1b1b", fg="#e0e0e0", font=("Helvetica", 9, "bold")).pack(side="left", padx=(15, 4))
        self.scale_grosor = tk.Scale(
            frame_tools, 
            from_=1, 
            to=8, 
            orient="horizontal", 
            bg="#1b1b1b", 
            fg="#d4af37", 
            troughcolor="#2a2a2a", 
            highlightthickness=0, 
            length=70
        )
        self.scale_grosor.set(2)
        self.scale_grosor.pack(side="left")

        btn_limpiar = tk.Button(
            frame_tools, 
            text="🔄 Restaurar Frasco", 
            command=self.dibujar_frasco, 
            bg="#3a1c1c", 
            fg="#ff7575", 
            font=("Helvetica", 8, "bold"), 
            relief="flat", 
            cursor="hand2", 
            padx=8
        )
        btn_limpiar.pack(side="right")

        # Canvas
        self.canvas = tk.Canvas(self.root, bg="#0d0d0d", cursor="crosshair", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=15, pady=10)

        # Enlace de eventos del ratón para grabado sobre la placa
        self.canvas.bind("<Button-1>", self.iniciar_grabado)
        self.canvas.bind("<B1-Motion>", self.grabar_trazo)
        self.canvas.bind("<ButtonRelease-1>", self.terminar_grabado)
        self.canvas.bind("<Motion>", self.mostrar_coordenadas)

        # Barra de estado
        self.lbl_estado = tk.Label(
            self.root, 
            text="Haz clic y arrastra sobre la placa dorada del frasco para grabar tus iniciales o diseño personalizado.", 
            bg="#1a1a1a", 
            fg="#888888", 
            font=("Consolas", 8), 
            anchor="w", 
            padx=12, 
            pady=4
        )
        self.lbl_estado.pack(fill="x", side="bottom")

    def cambiar_liquido(self, color):
        self.color_liquido = color
        self.dibujar_frasco()

    def dibujar_frasco(self):
        self.canvas.delete("all")
        cx = 350  # Centro horizontal aproximado

        # Fondo sutil de luz
        self.canvas.create_oval(cx - 160, 100, cx + 160, 480, fill="#141414", outline="")

        # 1. Tapón dorado de lujo
        self.canvas.create_rectangle(cx - 35, 70, cx + 35, 120, fill="#d4af37", outline="#ffd700", width=2)
        self.canvas.create_line(cx - 30, 85, cx + 30, 85, fill="#8a7322", width=2)
        self.canvas.create_line(cx - 30, 105, cx + 30, 105, fill="#8a7322", width=2)

        # 2. Cuello y Atomizador
        self.canvas.create_rectangle(cx - 15, 120, cx + 15, 150, fill="#c0c0c0", outline="#999999", width=1)

        # 3. Cuerpo del Frasco (Cristal Grueso)
        self.canvas.create_rectangle(cx - 110, 150, cx + 110, 430, fill="#1e1e1e", outline="#ffffff", width=2)

        # 4. Líquido de la Fragancia
        self.canvas.create_rectangle(cx - 100, 190, cx + 100, 420, fill=self.color_liquido, outline="")

        # 5. Brillo del cristal
        self.canvas.create_line(cx - 95, 160, cx - 95, 420, fill="#ffffff", width=3)

        # 6. Placa Dorada para Grabado de Personalización
        self.canvas.create_rectangle(cx - 80, 240, cx + 80, 360, fill="#ecd68a", outline="#d4af37", width=3)
        self.canvas.create_text(cx, 260, text="HAUTE PARFUMERIE", fill="#3d3014", font=("Helvetica", 7, "bold"))
        self.canvas.create_text(cx, 275, text="— RYAN.SHOPMX —", fill="#5a471e", font=("Helvetica", 6))
        self.canvas.create_text(cx, 345, text="• 100ml / 3.4 FL. OZ. •", fill="#5a471e", font=("Helvetica", 6))

        # Texto indicativo para el usuario
        self.canvas.create_text(cx, 455, text="Frasco de Vidrio Francés — Edición Limitada", fill="#777777", font=("Helvetica", 9, "italic"))

    def iniciar_grabado(self, event):
        self.ultimo_x = event.x
        self.ultimo_y = event.y

    def grabar_trazo(self, event):
        if self.ultimo_x and self.ultimo_y:
            grosor = self.scale_grosor.get()
            self.canvas.create_line(
                self.ultimo_x, self.ultimo_y, event.x, event.y,
                width=grosor, fill=self.color_grabado, capstyle="round", smooth=True
            )
            self.ultimo_x = event.x
            self.ultimo_y = event.y

    def terminar_grabado(self, event):
        self.ultimo_x = None
        self.ultimo_y = None

    def mostrar_coordenadas(self, event):
        self.lbl_estado.config(text=f"Puntero láser de grabado en: X={event.x}, Y={event.y} | Dibujando sobre la placa")

if __name__ == "__main__":
    root = tk.Tk()
    app = GrabadoFrascoApp(root)
    root.mainloop()
