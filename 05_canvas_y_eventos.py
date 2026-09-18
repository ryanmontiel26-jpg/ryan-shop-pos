"""
05_canvas_y_eventos.py
Demostración de gráficos y eventos interactivos en Tkinter:
- Canvas (lienzo de dibujo bidimensional)
- Manejo de Eventos del Ratón (<Button-1>, <B1-Motion>, <Motion>)
- Creación de formas (create_line, create_oval, create_rectangle, create_text)
- Miniproyecto: Pizarra interactiva de dibujo (Mini Paint)
"""

import tkinter as tk

class PizarraCanvas:
    def __init__(self, root):
        self.root = root
        self.root.title("05 - Canvas y Manejo de Eventos del Ratón")
        self.root.geometry("680x580")
        self.root.config(bg="#1a1a1a")

        self.color_actual = "#00ffcc"
        self.grosor = 3
        self.ultimo_x = None
        self.ultimo_y = None

        self.crear_interfaz()

    def crear_interfaz(self):
        # Barra superior de herramientas
        frame_herramientas = tk.Frame(self.root, bg="#2a2a2a", pady=8, padx=10)
        frame_herramientas.pack(fill="x")

        tk.Label(frame_herramientas, text="Color:", bg="#2a2a2a", fg="white", font=("Helvetica", 9, "bold")).pack(side="left", padx=(0, 6))

        # Botones de paleta de colores
        colores = ["#00ffcc", "#ff007f", "#ffea00", "#00e676", "#ffffff"]
        for c in colores:
            btn_col = tk.Button(
                frame_herramientas, 
                bg=c, 
                width=2, 
                height=1, 
                relief="flat", 
                cursor="hand2",
                command=lambda col=c: self.cambiar_color(col)
            )
            btn_col.pack(side="left", padx=3)

        tk.Label(frame_herramientas, text="Grosor:", bg="#2a2a2a", fg="white", font=("Helvetica", 9, "bold")).pack(side="left", padx=(15, 6))
        
        self.scale_grosor = tk.Scale(
            frame_herramientas, 
            from_=1, 
            to=15, 
            orient="horizontal", 
            bg="#2a2a2a", 
            fg="white", 
            troughcolor="#444444", 
            highlightthickness=0, 
            length=100
        )
        self.scale_grosor.set(3)
        self.scale_grosor.pack(side="left")

        btn_figuras = tk.Button(
            frame_herramientas, 
            text="Dibujar Figuras Demo", 
            command=self.dibujar_figuras_demo, 
            bg="#3a86ff", 
            fg="white", 
            font=("Helvetica", 9, "bold"), 
            relief="flat", 
            cursor="hand2", 
            padx=8
        )
        btn_figuras.pack(side="left", padx=15)

        btn_limpiar = tk.Button(
            frame_herramientas, 
            text="🗑️ Limpiar", 
            command=self.limpiar_canvas, 
            bg="#e63946", 
            fg="white", 
            font=("Helvetica", 9, "bold"), 
            relief="flat", 
            cursor="hand2", 
            padx=8
        )
        btn_limpiar.pack(side="right")

        # Lienzo (Canvas)
        self.canvas = tk.Canvas(self.root, bg="#0d0d0d", cursor="crosshair", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=15, pady=10)

        # Barra de estado con coordenadas del mouse
        self.lbl_coords = tk.Label(
            self.root, 
            text="Posición del mouse: X=0, Y=0 | Haz clic y arrastra para dibujar libremente.", 
            bg="#2a2a2a", 
            fg="#aaaaaa", 
            font=("Consolas", 9), 
            anchor="w", 
            padx=12, 
            pady=4
        )
        self.lbl_coords.pack(fill="x", side="bottom")

        # Enlace de eventos del ratón (Event Bindings)
        self.canvas.bind("<Button-1>", self.iniciar_trazo)
        self.canvas.bind("<B1-Motion>", self.dibujar_trazo)
        self.canvas.bind("<ButtonRelease-1>", self.terminar_trazo)
        self.canvas.bind("<Motion>", self.actualizar_coordenadas)

        self.dibujar_figuras_demo()

    def cambiar_color(self, nuevo_color):
        self.color_actual = nuevo_color

    def iniciar_trazo(self, event):
        self.ultimo_x = event.x
        self.ultimo_y = event.y

    def dibujar_trazo(self, event):
        if self.ultimo_x and self.ultimo_y:
            ancho = self.scale_grosor.get()
            self.canvas.create_line(
                self.ultimo_x, self.ultimo_y, event.x, event.y,
                width=ancho, fill=self.color_actual, capstyle="round", smooth=True
            )
            self.ultimo_x = event.x
            self.ultimo_y = event.y

    def terminar_trazo(self, event):
        self.ultimo_x = None
        self.ultimo_y = None

    def actualizar_coordenadas(self, event):
        self.lbl_coords.config(text=f"Posición del mouse: X={event.x}, Y={event.y} | Dibujando en color {self.color_actual}")

    def dibujar_figuras_demo(self):
        # Figuras geométricas de muestra
        self.canvas.create_rectangle(40, 30, 200, 110, outline="#3a86ff", width=2, fill="#1c2d4a")
        self.canvas.create_text(120, 70, text="Rectángulo Demo", fill="white", font=("Helvetica", 10, "bold"))

        self.canvas.create_oval(240, 30, 360, 110, outline="#ff007f", width=2, fill="#3d152a")
        self.canvas.create_text(300, 70, text="Óvalo Demo", fill="white", font=("Helvetica", 10, "bold"))

        self.canvas.create_line(400, 110, 600, 30, fill="#ffea00", width=3, dash=(4, 2))
        self.canvas.create_text(500, 85, text="Línea con Trazo (Dash)", fill="#ffea00", font=("Helvetica", 9))

    def limpiar_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PizarraCanvas(root)
    root.mainloop()
