import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class RyanShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ryan.ShopMx — Haute Parfumerie System")
        self.root.geometry("820x620")
        self.root.minsize(780, 560)
        self.root.config(bg="#121212")

        # Catálogo organizado con categorías y precios
        self.catalogo = {
            "Xerjoff Erba Pura (Nicho)": {"precio": 185.00, "cat": "Nicho"},
            "Tom Ford Black Orchid (Nicho)": {"precio": 145.00, "cat": "Nicho"},
            "Dior Sauvage Elixir (Diseñador)": {"precio": 125.50, "cat": "Diseñador"},
            "Jean Paul Gaultier Le Male (Diseñador)": {"precio": 95.00, "cat": "Diseñador"},
            "Decant 10ml - Afnan 9pm": {"precio": 18.00, "cat": "Decants"},
            "Decant 10ml - Lattafa Asad": {"precio": 16.00, "cat": "Decants"}
        }

        # Carrito estructurado: {nombre_perfume: {"precio": float, "cantidad": int}}
        self.carrito = {}
        self.contador_ordenes = 1001

        self.crear_interfaz()

    def crear_interfaz(self):
        # Título / Header
        lbl_header = tk.Label(
            self.root, 
            text="✨ RYAN.SHOPMX | HIGH PERFUMERY ✨", 
            font=("Helvetica", 16, "bold"), 
            bg="#121212", 
            fg="#d4af37"
        )
        lbl_header.pack(pady=(15, 8))

        # Marco Principal dividido en dos columnas
        frame_principal = tk.Frame(self.root, bg="#121212")
        frame_principal.pack(fill="both", expand=True, padx=20, pady=5)

        # --- Columna Izquierda: Catálogo ---
        frame_catalogo = tk.LabelFrame(
            frame_principal, 
            text=" Catálogo Exclusivo ", 
            font=("Helvetica", 11, "bold"), 
            bg="#1b1b1b", 
            fg="#e0e0e0", 
            bd=1, 
            relief="solid"
        )
        frame_catalogo.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # Filtro de categorías
        frame_filtro = tk.Frame(frame_catalogo, bg="#1b1b1b")
        frame_filtro.pack(fill="x", padx=15, pady=(10, 5))

        tk.Label(
            frame_filtro, 
            text="Filtrar por:", 
            font=("Helvetica", 9, "bold"), 
            bg="#1b1b1b", 
            fg="#aaaaaa"
        ).pack(side="left")

        self.filtro_var = tk.StringVar(value="Todas")
        combo_filtro = ttk.Combobox(
            frame_filtro, 
            textvariable=self.filtro_var, 
            values=["Todas", "Nicho", "Diseñador", "Decants"], 
            state="readonly",
            width=14
        )
        combo_filtro.pack(side="left", padx=8)
        combo_filtro.bind("<<ComboboxSelected>>", lambda e: self.actualizar_lista_productos())

        # Contenedor de Radiobuttons
        self.frame_radios = tk.Frame(frame_catalogo, bg="#1b1b1b")
        self.frame_radios.pack(fill="both", expand=True, padx=10, pady=5)

        self.perfume_var = tk.StringVar(value=list(self.catalogo.keys())[0])
        self.actualizar_lista_productos()

        # Selector de Cantidad y Botón Añadir
        frame_acciones_cat = tk.Frame(frame_catalogo, bg="#1b1b1b")
        frame_acciones_cat.pack(fill="x", pady=12, padx=15)

        tk.Label(
            frame_acciones_cat, 
            text="Cant:", 
            font=("Helvetica", 10, "bold"), 
            bg="#1b1b1b", 
            fg="#e0e0e0"
        ).pack(side="left")

        self.cant_var = tk.IntVar(value=1)
        spn_cant = tk.Spinbox(
            frame_acciones_cat, 
            from_=1, 
            to=50, 
            textvariable=self.cant_var, 
            width=4, 
            font=("Helvetica", 10),
            bg="#2a2a2a",
            fg="white",
            buttonbackground="#d4af37"
        )
        spn_cant.pack(side="left", padx=6)

        btn_agregar = tk.Button(
            frame_acciones_cat, 
            text="➕ Agregar al Carrito", 
            command=self.agregar_al_carrito, 
            font=("Helvetica", 10, "bold"), 
            bg="#d4af37", 
            fg="#121212", 
            relief="flat",
            cursor="hand2",
            padx=12, 
            pady=4
        )
        btn_agregar.pack(side="right", fill="x", expand=True)

        # --- Columna Derecha: Resumen de Orden ---
        frame_carrito = tk.LabelFrame(
            frame_principal, 
            text=" Resumen de Orden ", 
            font=("Helvetica", 11, "bold"), 
            bg="#1b1b1b", 
            fg="#e0e0e0", 
            bd=1, 
            relief="solid"
        )
        frame_carrito.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # Texto del Carrito (Solo Lectura)
        self.txt_carrito = tk.Text(
            frame_carrito, 
            font=("Consolas", 10), 
            bg="#0f0f0f", 
            fg="#00ffcc", 
            relief="flat",
            state="disabled",
            padx=10,
            pady=10
        )
        self.txt_carrito.pack(padx=15, pady=10, fill="both", expand=True)

        # Botones de Acción para Carrito
        frame_botones_orden = tk.Frame(frame_carrito, bg="#1b1b1b")
        frame_botones_orden.pack(fill="x", padx=15, pady=(0, 12))

        btn_vaciar = tk.Button(
            frame_botones_orden, 
            text="🗑️ Vaciar", 
            command=self.vaciar_carrito, 
            font=("Helvetica", 9, "bold"), 
            bg="#3a1c1c", 
            fg="#ff6b6b", 
            relief="flat",
            cursor="hand2",
            padx=8,
            pady=5
        )
        btn_vaciar.pack(side="left")

        btn_finalizar = tk.Button(
            frame_botones_orden, 
            text="💳 Finalizar Venta", 
            command=self.finalizar_venta, 
            font=("Helvetica", 10, "bold"), 
            bg="#28a745", 
            fg="white", 
            relief="flat",
            cursor="hand2",
            padx=14, 
            pady=5
        )
        btn_finalizar.pack(side="right", fill="x", expand=True, padx=(8, 0))

        # Barra de Estado Inferior
        self.lbl_toast = tk.Label(
            self.root, 
            text="Sistema listo. Seleccione sus fragancias.", 
            font=("Helvetica", 9, "italic"), 
            bg="#1b1b1b", 
            fg="#888888", 
            anchor="w", 
            padx=15, 
            pady=5
        )
        self.lbl_toast.pack(fill="x", side="bottom")

    def actualizar_lista_productos(self):
        for widget in self.frame_radios.winfo_children():
            widget.destroy()

        cat_filtro = self.filtro_var.get()
        productos_mostrados = []

        for perfume, info in self.catalogo.items():
            if cat_filtro == "Todas" or info["cat"] == cat_filtro:
                productos_mostrados.append(perfume)
                rb = tk.Radiobutton(
                    self.frame_radios, 
                    text=f"{perfume} — ${info['precio']:.2f}", 
                    variable=self.perfume_var, 
                    value=perfume, 
                    font=("Helvetica", 9), 
                    bg="#1b1b1b", 
                    fg="#f5f5f5", 
                    selectcolor="#2a2a2a",
                    activebackground="#1b1b1b",
                    activeforeground="#d4af37",
                    anchor="w"
                )
                rb.pack(anchor="w", padx=10, pady=5)

        if productos_mostrados and self.perfume_var.get() not in productos_mostrados:
            self.perfume_var.set(productos_mostrados[0])

    def refrescar_vista_carrito(self):
        self.txt_carrito.config(state="normal")
        self.txt_carrito.delete("1.0", tk.END)

        if not self.carrito:
            self.txt_carrito.insert(tk.END, "El carrito está vacío.\n")
            self.txt_carrito.config(state="disabled")
            return

        total = 0
        total_items = 0
        self.txt_carrito.insert(tk.END, f"{'CANT':<5} {'PRODUCTO':<24} {'TOTAL':>8}\n")
        self.txt_carrito.insert(tk.END, "-" * 40 + "\n")

        for prod, data in self.carrito.items():
            subtotal = data["precio"] * data["cantidad"]
            total += subtotal
            total_items += data["cantidad"]
            nombre_corto = (prod[:21] + "..") if len(prod) > 23 else prod
            self.txt_carrito.insert(tk.END, f"{data['cantidad']:<5} {nombre_corto:<24} ${subtotal:>7.2f}\n")

        self.txt_carrito.insert(tk.END, "=" * 40 + "\n")
        self.txt_carrito.insert(tk.END, f"Artículos: {total_items}\n")
        self.txt_carrito.insert(tk.END, f"TOTAL: ${total:.2f}\n")
        self.txt_carrito.config(state="disabled")

    def agregar_al_carrito(self):
        seleccion = self.perfume_var.get()
        if not seleccion or seleccion not in self.catalogo:
            return

        try:
            cant = int(self.cant_var.get())
            if cant <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Cantidad Inválida", "Por favor ingresa una cantidad válida mayor a 0.")
            return

        precio = self.catalogo[seleccion]["precio"]

        if seleccion in self.carrito:
            self.carrito[seleccion]["cantidad"] += cant
        else:
            self.carrito[seleccion] = {"precio": precio, "cantidad": cant}

        self.refrescar_vista_carrito()
        self.lbl_toast.config(text=f"Agregado: {cant}x {seleccion}", fg="#d4af37")

    def vaciar_carrito(self):
        if not self.carrito:
            return
        if messagebox.askyesno("Confirmar", "¿Deseas vaciar todo el carrito?"):
            self.carrito.clear()
            self.refrescar_vista_carrito()
            self.lbl_toast.config(text="Carrito vaciado.", fg="#888888")

    def finalizar_venta(self):
        if not self.carrito:
            messagebox.showwarning("Carrito Vacío", "No hay productos seleccionados en la orden.")
            return

        total = sum(d["precio"] * d["cantidad"] for d in self.carrito.values())
        folio = f"RS-{self.contador_ordenes}"
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        resumen_msg = (
            f"¡Venta registrada con éxito!\n\n"
            f"Folio: {folio}\n"
            f"Fecha: {fecha}\n"
            f"Total cobrado: ${total:.2f}\n\n"
            f"¿Deseas iniciar una nueva venta?"
        )

        messagebox.showinfo("Ticket Generado", resumen_msg)
        self.contador_ordenes += 1
        self.carrito.clear()
        self.refrescar_vista_carrito()
        self.lbl_toast.config(text=f"Venta {folio} finalizada exitosamente.", fg="#28a745")

if __name__ == "__main__":
    root = tk.Tk()
    app = RyanShopApp(root)
    root.mainloop()
