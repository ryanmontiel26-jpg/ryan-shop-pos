"""
06_menus_y_atajos.py
Tema: Bitácora de Fórmulas y Reseñas de Perfumería (Perfumist Lab Notebook)
Demostración de menús, atajos de teclado y eventos avanzados:
- Menu (barra superior: Archivo, Fórmulas Olfativas, Edición, Ayuda)
- Menú contextual flotante con clic derecho (insertar notas aromáticas y portapapeles)
- Atajos de teclado vinculados con bind (Ctrl+N, Ctrl+S, Ctrl+Q)
- Widget Text enriquecido con scrollbar para redactar pirámides olfativas y fórmulas
"""

import tkinter as tk
from tkinter import messagebox, filedialog

class BitacoraPerfumistaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("06 - Bitácora de Fórmulas | Menús y Atajos")
        self.root.geometry("680x540")
        self.root.config(bg="#121212")

        self.crear_barra_menus()
        self.crear_editor_texto()
        self.crear_menu_contextual()
        self.vincular_atajos()

    def crear_barra_menus(self):
        barra = tk.Menu(self.root)

        # 1. Menú Archivo
        m_archivo = tk.Menu(barra, tearoff=0)
        m_archivo.add_command(label="Nueva Bitácora", accelerator="Ctrl+N", command=self.nueva_bitacora)
        m_archivo.add_command(label="Cargar Fórmula...", accelerator="Ctrl+O", command=self.abrir_formula)
        m_archivo.add_command(label="Guardar Fórmula...", accelerator="Ctrl+S", command=self.guardar_formula)
        m_archivo.add_separator()
        m_archivo.add_command(label="Salir", accelerator="Ctrl+Q", command=self.root.quit)
        barra.add_cascade(label="Archivo", menu=m_archivo)

        # 2. Menú Acordes y Notas Olfativas (Específico de Perfumería)
        m_acordes = tk.Menu(barra, tearoff=0)
        m_acordes.add_command(label="Insertar Plantilla Pirámide Olfativa", command=self.insertar_plantilla_piramide)
        m_acordes.add_separator()
        m_acordes.add_command(label="+ Acorde Cítrico (Bergamota / Limón)", command=lambda: self.insertar_texto("• Salida: Bergamota de Calabria, Mandarina italiana\n"))
        m_acordes.add_command(label="+ Acorde Oriental (Ámbar / Vainilla)", command=lambda: self.insertar_texto("• Fondo: Vainilla de Madagascar, Ámbar gris, Benjuí\n"))
        m_acordes.add_command(label="+ Acorde Amaderado (Oud / Sándalo)", command=lambda: self.insertar_texto("• Corazón: Madera de Oud de Camboya, Sándalo de Mysore\n"))
        barra.add_cascade(label="Acordes Olfativos", menu=m_acordes)

        # 3. Menú Edición
        m_edicion = tk.Menu(barra, tearoff=0)
        m_edicion.add_command(label="Cortar", command=lambda: self.txt_editor.event_generate("<<Cut>>"))
        m_edicion.add_command(label="Copiar", command=lambda: self.txt_editor.event_generate("<<Copy>>"))
        m_edicion.add_command(label="Pegar", command=lambda: self.txt_editor.event_generate("<<Paste>>"))
        m_edicion.add_separator()
        m_edicion.add_command(label="Seleccionar Todo", command=self.seleccionar_todo)
        barra.add_cascade(label="Edición", menu=m_edicion)

        # 4. Menú Ayuda
        m_ayuda = tk.Menu(barra, tearoff=0)
        m_ayuda.add_command(label="Glosario del Perfumista", command=self.mostrar_glosario)
        m_ayuda.add_command(label="Acerca de Ryan.ShopMx", command=self.mostrar_acerca_de)
        barra.add_cascade(label="Ayuda", menu=m_ayuda)

        self.root.config(menu=barra)

    def crear_editor_texto(self):
        # Header de la Bitácora
        tk.Label(
            self.root, 
            text="📓 BITÁCORA DEL PERFUMISTA — CREACIÓN DE FÓRMULAS", 
            font=("Helvetica", 11, "bold"), 
            bg="#121212", 
            fg="#d4af37"
        ).pack(pady=(10, 4))

        frame_editor = tk.Frame(self.root, bg="#121212")
        frame_editor.pack(fill="both", expand=True, padx=15, pady=6)

        scroll = tk.Scrollbar(frame_editor)
        scroll.pack(side="right", fill="y")

        self.txt_editor = tk.Text(
            frame_editor, 
            bg="#181818", 
            fg="#f0f0f0", 
            insertbackground="#d4af37",
            font=("Consolas", 10), 
            wrap="word", 
            yscrollcommand=scroll.set,
            padx=12, 
            pady=12, 
            relief="solid", 
            bd=1
        )
        self.txt_editor.pack(fill="both", expand=True)
        scroll.config(command=self.txt_editor.yview)

        # Texto inicial
        self.insertar_plantilla_piramide()

        # Barra de estado
        self.lbl_estado = tk.Label(
            self.root, 
            text="Bitácora lista | Atajos: Ctrl+N (Nuevo), Ctrl+S (Guardar), Clic Derecho (Acordes)", 
            bg="#1a1a1a", 
            fg="#888888", 
            font=("Consolas", 8), 
            anchor="w", 
            padx=12, 
            pady=4
        )
        self.lbl_estado.pack(fill="x", side="bottom")

    def crear_menu_contextual(self):
        self.menu_contextual = tk.Menu(self.root, tearoff=0)
        self.menu_contextual.add_command(label="Insertar Acorde Cítrico", command=lambda: self.insertar_texto("• Salida: Bergamota y Neroli\n"))
        self.menu_contextual.add_command(label="Insertar Acorde Amaderado", command=lambda: self.insertar_texto("• Fondo: Cedro de Virginia y Pachulí\n"))
        self.menu_contextual.add_separator()
        self.menu_contextual.add_command(label="Cortar", command=lambda: self.txt_editor.event_generate("<<Cut>>"))
        self.menu_contextual.add_command(label="Copiar", command=lambda: self.txt_editor.event_generate("<<Copy>>"))
        self.menu_contextual.add_command(label="Pegar", command=lambda: self.txt_editor.event_generate("<<Paste>>"))

        self.txt_editor.bind("<Button-3>", lambda e: self.menu_contextual.post(e.x_root, e.y_root))

    def vincular_atajos(self):
        self.root.bind("<Control-n>", lambda e: self.nueva_bitacora())
        self.root.bind("<Control-s>", lambda e: self.guardar_formula())
        self.root.bind("<Control-q>", lambda e: self.root.quit())

    def insertar_texto(self, texto):
        self.txt_editor.insert(tk.INSERT, texto)

    def insertar_plantilla_piramide(self):
        plantilla = (
            "═══════════════════════════════════════════════════════\n"
            "  FÓRMULA OLFATIVA MAESTRA — HAUTE PARFUMERIE LAB      \n"
            "═══════════════════════════════════════════════════════\n"
            "NOMBRE DEL PROTOTIPO : Golden Elixir No. 7\n"
            "PERFUMISTA CREADOR   : Ryan Montiel\n"
            "CONCENTRACIÓN FINAL  : Extrait de Parfum (28% Aceite)\n\n"
            "[1. NOTAS DE SALIDA - TOP NOTES] (Evaporación: 0 - 30 min)\n"
            "• Bergamota de Calabria: 15%\n"
            "• Manzana Verde Crujiente: 8%\n"
            "• Pimienta Rosa de Madagascar: 4%\n\n"
            "[2. NOTAS DE CORAZÓN - HEART NOTES] (Evaporación: 30 min - 4 hrs)\n"
            "• Jazmín Sambac: 12%\n"
            "• Rosa Damascena: 10%\n"
            "• Miel Dorada Silvestre: 6%\n\n"
            "[3. NOTAS DE FONDO - BASE NOTES] (Fijación: 8+ hrs)\n"
            "• Madera de Agar (Oud): 18%\n"
            "• Ámbar Gris Suave: 12%\n"
            "• Vainilla Bourbon: 15%\n\n"
            "OBSERVACIONES DE MACERACIÓN:\n"
            "Reposo requerido de 30 días a 18°C en oscuridad total.\n"
            "═══════════════════════════════════════════════════════\n"
        )
        self.txt_editor.delete("1.0", tk.END)
        self.txt_editor.insert("1.0", plantilla)

    def nueva_bitacora(self):
        self.txt_editor.delete("1.0", tk.END)
        self.lbl_estado.config(text="Nueva bitácora en blanco iniciada.")

    def abrir_formula(self):
        ruta = filedialog.askopenfilename(filetypes=[("Fórmulas de Perfume (*.txt)", "*.txt"), ("Todos", "*.*")])
        if ruta:
            with open(ruta, "r", encoding="utf-8") as f:
                self.txt_editor.delete("1.0", tk.END)
                self.txt_editor.insert("1.0", f.read())
            self.lbl_estado.config(text=f"Fórmula cargada desde: {ruta}")

    def guardar_formula(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="formula_perfume.txt",
            filetypes=[("Fórmulas de Perfume (*.txt)", "*.txt"), ("Todos", "*.*")]
        )
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(self.txt_editor.get("1.0", tk.END))
            self.lbl_estado.config(text=f"Fórmula guardada exitosamente en: {ruta}")

    def seleccionar_todo(self):
        self.txt_editor.tag_add("sel", "1.0", tk.END)

    def mostrar_glosario(self):
        msg = (
            "GLOSARIO DE PERFUMERÍA:\n\n"
            "• Sillage: La estela aromática que deja una persona al pasar.\n"
            "• Longevidad: Cuántas horas permanece la fragancia en piel.\n"
            "• Decant: Porción de 2ml a 10ml extraída del frasco original.\n"
            "• Maceración: Tiempo de reposo químico para amalgamar aceites."
        )
        messagebox.showinfo("Glosario Olfativo", msg)

    def mostrar_acerca_de(self):
        messagebox.showinfo("Acerca de", "Bitácora de Laboratorio Olfativo\nRyan.ShopMx — Sistema de Creación de Fragancias")

if __name__ == "__main__":
    root = tk.Tk()
    app = BitacoraPerfumistaApp(root)
    root.mainloop()
