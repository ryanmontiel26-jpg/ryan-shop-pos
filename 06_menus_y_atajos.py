"""
06_menus_y_atajos.py
Demostración de menús, atajos de teclado y eventos avanzados:
- Menu (barra de menús superior con submenús Archivo, Edición, Ayuda)
- Menú Contextual (menú flotante que aparece con clic derecho)
- Atajos de teclado (Keyboard Accelerators con bind: Ctrl+N, Ctrl+S, Ctrl+Q)
- Widget Text interactivo (editor básico de notas)
"""

import tkinter as tk
from tkinter import messagebox, filedialog

class EditorConMenus:
    def __init__(self, root):
        self.root = root
        self.root.title("06 - Barra de Menús, Menú Contextual y Atajos")
        self.root.geometry("650x500")
        self.root.config(bg="#1e1e2e")

        self.crear_barra_menus()
        self.crear_area_texto()
        self.crear_menu_contextual()
        self.vincular_atajos()

    def crear_barra_menus(self):
        # Barra principal de menús
        barra_menu = tk.Menu(self.root)

        # 1. Menú Archivo
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", command=self.nuevo_archivo)
        menu_archivo.add_command(label="Abrir...", accelerator="Ctrl+O", command=self.abrir_archivo)
        menu_archivo.add_command(label="Guardar...", accelerator="Ctrl+S", command=self.guardar_archivo)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", accelerator="Ctrl+Q", command=self.root.quit)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        # 2. Menú Edición
        menu_edicion = tk.Menu(barra_menu, tearoff=0)
        menu_edicion.add_command(label="Cortar", command=lambda: self.txt_editor.event_generate("<<Cut>>"))
        menu_edicion.add_command(label="Copiar", command=lambda: self.txt_editor.event_generate("<<Copy>>"))
        menu_edicion.add_command(label="Pegar", command=lambda: self.txt_editor.event_generate("<<Paste>>"))
        menu_edicion.add_separator()
        menu_edicion.add_command(label="Seleccionar Todo", command=self.seleccionar_todo)
        barra_menu.add_cascade(label="Edición", menu=menu_edicion)

        # 3. Menú Ayuda
        menu_ayuda = tk.Menu(barra_menu, tearoff=0)
        menu_ayuda.add_command(label="Acerca de...", command=self.mostrar_acerca_de)
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.root.config(menu=barra_menu)

    def crear_area_texto(self):
        # Marco para el editor con scrollbar
        frame_editor = tk.Frame(self.root, bg="#1e1e2e")
        frame_editor.pack(fill="both", expand=True, padx=15, pady=10)

        self.scrollbar = tk.Scrollbar(frame_editor)
        self.scrollbar.pack(side="right", fill="y")

        self.txt_editor = tk.Text(
            frame_editor, 
            bg="#181825", 
            fg="#cdd6f4", 
            insertbackground="#f5c2e7",
            font=("Consolas", 11), 
            wrap="word", 
            yscrollcommand=self.scrollbar.set,
            padx=10, 
            pady=10
        )
        self.txt_editor.pack(fill="both", expand=True)
        self.scrollbar.config(command=self.txt_editor.yview)

        texto_inicial = (
            "✨ Bienvenido al demostrador de menús y atajos de Tkinter ✨\n\n"
            "Prueba las siguientes funciones:\n"
            "1. Haz CLIC DERECHO en cualquier parte de este texto para abrir el menú contextual.\n"
            "2. Usa los atajos de teclado:\n"
            "   - Ctrl + N : Nuevo documento\n"
            "   - Ctrl + S : Guardar documento\n"
            "   - Ctrl + Q : Salir de la aplicación\n"
            "3. Explora las opciones en la barra de menú superior (Archivo, Edición, Ayuda)."
        )
        self.txt_editor.insert("1.0", texto_inicial)

        # Barra de estado
        self.lbl_estado = tk.Label(
            self.root, 
            text="Listo | Atajos habilitados: Ctrl+N, Ctrl+S, Ctrl+Q", 
            bg="#11111b", 
            fg="#a6adc8", 
            anchor="w", 
            padx=12, 
            pady=4
        )
        self.lbl_estado.pack(fill="x", side="bottom")

    def crear_menu_contextual(self):
        # Menú flotante para clic derecho
        self.menu_contextual = tk.Menu(self.root, tearoff=0)
        self.menu_contextual.add_command(label="Cortar", command=lambda: self.txt_editor.event_generate("<<Cut>>"))
        self.menu_contextual.add_command(label="Copiar", command=lambda: self.txt_editor.event_generate("<<Copy>>"))
        self.menu_contextual.add_command(label="Pegar", command=lambda: self.txt_editor.event_generate("<<Paste>>"))
        self.menu_contextual.add_separator()
        self.menu_contextual.add_command(label="Seleccionar Todo", command=self.seleccionar_todo)

        # Asociar clic derecho en Windows (<Button-3>)
        self.txt_editor.bind("<Button-3>", self.mostrar_menu_contextual)

    def mostrar_menu_contextual(self, event):
        self.menu_contextual.post(event.x_root, event.y_root)

    def vincular_atajos(self):
        self.root.bind("<Control-n>", lambda e: self.nuevo_archivo())
        self.root.bind("<Control-s>", lambda e: self.guardar_archivo())
        self.root.bind("<Control-q>", lambda e: self.root.quit())

    def nuevo_archivo(self):
        self.txt_editor.delete("1.0", tk.END)
        self.lbl_estado.config(text="Nuevo documento creado.")

    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos", "*.*")])
        if ruta:
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
            self.txt_editor.delete("1.0", tk.END)
            self.txt_editor.insert("1.0", contenido)
            self.lbl_estado.config(text=f"Archivo abierto: {ruta}")

    def guardar_archivo(self):
        ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(self.txt_editor.get("1.0", tk.END))
            self.lbl_estado.config(text=f"Guardado exitosamente en: {ruta}")

    def seleccionar_todo(self):
        self.txt_editor.tag_add("sel", "1.0", tk.END)

    def mostrar_acerca_de(self):
        messagebox.showinfo("Acerca de", "Demostrador de Menús y Atajos en Tkinter\nRyan.ShopMx - Python GUI Series")

if __name__ == "__main__":
    root = tk.Tk()
    app = EditorConMenus(root)
    root.mainloop()
