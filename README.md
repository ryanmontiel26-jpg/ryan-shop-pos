# ✨ Haute Parfumerie System — Colección de Módulos Tkinter en Python

Este repositorio contiene una suite completa y didáctica de aplicaciones y módulos desarrollados en **Python** utilizando la librería gráfica **Tkinter** y su versión avanzada **TTK (Themed Tk)**.

Todo el proyecto está ambientado en el fascinante universo de la **Alta Perfumería y Fragancias de Lujo (Haute Parfumerie / Ryan.ShopMx)**. A través de este hilo temático, cada script demuestra de forma práctica y visual diferentes componentes, layouts, eventos y técnicas de desarrollo de interfaces de escritorio.

---

## 📂 Estructura del Repositorio

```text
ryan-shop-pos/
│
├── 01_widgets_basicos.py             # Asesor de fragancias y perfil olfativo
├── 02_administradores_geometria.py   # Diseño de vitrinas (pack, grid, place)
├── 03_dialogos_y_ventanas.py         # Consultas de tienda y pirámide olfativa modal
├── 04_ttk_avanzado.py                # Inventario de fragancias y maceración en laboratorio
├── 05_canvas_y_eventos.py            # Taller de grabado y personalización de frascos
├── 06_menus_y_atajos.py              # Bitácora de fórmulas maestras y reseñas de notas
├── main.py                           # Sistema POS completo para Ryan.ShopMx
│
├── requirements.txt                  # Dependencias del entorno
├── .gitignore                        # Archivos excluidos por Git
└── README.md                         # Documentación detallada del proyecto
```

---

## 📖 Explicación Detallada de Cada Archivo de Código

### 1. `01_widgets_basicos.py` — Asesor de Fragancias y Perfil Olfativo
* **Tema en Perfumería:** Asesor interactivo de la boutique para diagnosticar el gusto olfativo de un cliente y recomendarle una fragancia adecuada.
* **Componentes de Tkinter Utilizados:**
  * `tk.Label`: Títulos y membrete elegante en negro y dorado.
  * `tk.Entry`: Entrada de texto para capturar el nombre del cliente.
  * `tk.Radiobutton`: Selector exclusivo de familia olfativa (Amaderada, Oriental, Cítrica / Fresca, Gourmand / Dulce).
  * `tk.Checkbutton`: Opciones de servicio adicional (muestra decant 2ml de cortesía, caja con sello lacrado).
  * `tk.Scale`: Control deslizante (slider) para determinar la concentración de esencia deseada (% de aceite).
  * `tk.Button`: Botones de acción (*Descubrir Fragancia* y *Reiniciar*).
  * `StringVar`, `BooleanVar`: Variables reactivas de Tkinter que actualizan la vista en tiempo real.
* **Lo que hace el programa:** Permite al usuario configurar sus preferencias de perfume. Al hacer clic en el botón dorado, el programa procesa los datos y emite una recomendación personalizada con precio y detalles en una tarjeta con formato de consola.
* **Comando para ejecutar:**
  ```bash
  python 01_widgets_basicos.py
  ```

---

### 2. `02_administradores_geometria.py` — Diseño de Vitrinas y Estanterías
* **Tema en Perfumería:** Organización espacial y maquetación de mostradores, estanterías matriciales y escaparates VIP para exhibir perfumes.
* **Componentes de Tkinter Utilizados:**
  * `pack()`: Demuestra distribución por lados (`side="top"`, `side="bottom"`, `side="left"`, `side="right"`) y expansión proporcional (`fill="both"`, `expand=True`).
  * `grid()`: Demuestra cuadrículas estructuradas en filas (`row`) y columnas (`column`), expansión de columnas (`columnspan=3`) y configuración de pesos (`columnconfigure`).
  * `place()`: Demuestra coordenadas milimétricas exactas (`x`, `y`) y relativas porcentuales (`relx`, `rely`, `relwidth`, `anchor="center"`).
  * `ttk.Notebook`: Sistema de navegación por pestañas para alternar entre las tres vitrinas interactivamente.
* **Lo que hace el programa:** Presenta tres salas de exhibición:
  1. *Vitrina Lineal (pack):* Muestra un lanzamiento estrella arriba (Baccarat Rouge 540), decants económicos abajo y colecciones Nicho/Diseñador en los laterales.
  2. *Estantería Modular (grid):* Muestra una matriz ordenada por categorías de lujo con un banner publicitario inferior.
  3. *Escaparate VIP (place):* Coloca frascos en las esquinas y un frasco estelar (*Clive Christian No. 1*) flotando en el centro exacto del cristal.
* **Comando para ejecutar:**
  ```bash
  python 02_administradores_geometria.py
  ```

---

### 3. `03_dialogos_y_ventanas.py` — Centro de Consultas y Pirámide Olfativa Modal
* **Tema en Perfumería:** Gestión de alertas operativas de boutique (stock, pagos, envolturas) y visualizador de fichas técnicas olfativas.
* **Componentes de Tkinter Utilizados:**
  * `tkinter.messagebox`: Despliegue de ventanas emergentes estándar del sistema operativo:
    * `showinfo`: Confirmación de ubicación de stock en bodega.
    * `showwarning`: Alerta de inventario crítico (últimas 2 piezas).
    * `showerror`: Fallo de conexión de terminal bancaria.
    * `askyesno`: Pregunta de confirmación para empaque de lujo con satín dorado.
  * `tkinter.filedialog`:
    * `asksaveasfilename`: Exportación de lista de deseos (*Wishlist*) a un archivo de texto `.txt`.
    * `askopenfilename`: Importación de catálogo externo desde el disco duro.
  * `tkinter.colorchooser`:
    * `askcolor`: Selector de color nativo para cambiar el tono del frasco o fondo en vivo.
  * `tk.Toplevel` y `.grab_set()`: Ventana emergente secundaria con bloqueo modal que impide interactuar con la ventana principal hasta cerrarla.
* **Lo que hace el programa:** Proporciona un tablero interactivo con botones que disparan cada tipo de diálogo. Al abrir la ficha técnica, se despliega una ventana modal con la pirámide olfativa completa de *Xerjoff Erba Pura* desglosada en Notas de Salida, Corazón y Fondo.
* **Comando para ejecutar:**
  ```bash
  python 03_dialogos_y_ventanas.py
  ```

---

### 4. `04_ttk_avanzado.py` — Inventario de Fragancias y Laboratorio de Maceración
* **Tema en Perfumería:** Control de existencias de perfumes y monitoreo del proceso de añejamiento/maceración de aceites en laboratorio.
* **Componentes de Tkinter Utilizados:**
  * `ttk.Treeview`: Tabla interactiva con cabeceras de columnas, anchos específicos, alineación de texto y soporte para selección de filas.
  * `ttk.Scrollbar`: Barra de desplazamiento vertical acoplada dinámicamente a la tabla.
  * `ttk.Combobox`: Menú desplegable con captura del evento `<<ComboboxSelected>>` para filtrar el catálogo en tiempo real.
  * `ttk.Progressbar`: Barra de carga animada que simula el avance de días de reposo.
  * `ttk.Style`: Personalización del tema visual (*clam*) con colores dorado y grafito.
  * `root.after()`: Temporizador asíncrono que actualiza la animación del laboratorio sin congelar la ventana.
* **Lo que hace el programa:** Permite filtrar una tabla con 8 fragancias de alta gama por Casa (Xerjoff, Tom Ford, Dior, Jean Paul Gaultier, Perfumería Árabe). En la parte inferior, permite simular el proceso de maceración química de 45 días con una barra animada y porcentaje en vivo.
* **Comando para ejecutar:**
  ```bash
  python 04_ttk_avanzado.py
  ```

---

### 5. `05_canvas_y_eventos.py` — Taller de Grabado y Personalización de Frascos
* **Tema en Perfumería:** Servicio VIP de personalización donde el cliente graba sus iniciales o dedicatoria directamente en la placa dorada del frasco.
* **Componentes de Tkinter Utilizados:**
  * `tk.Canvas`: Lienzo gráfico donde se dibuja un frasco tridimensional vectorial con tapón dorado, atomizador plateado, vidrio reflectante y placa central.
  * Métodos gráficos: `create_rectangle`, `create_oval`, `create_line`, `create_text`.
  * Eventos del Mouse (`bind`):
    * `<Button-1>`: Clic inicial del puntero láser sobre el frasco.
    * `<B1-Motion>`: Arrastre para realizar el trazo a mano alzada.
    * `<Motion>`: Lectura en tiempo real de las coordenadas (X, Y) del puntero.
* **Lo que hace el programa:** El usuario puede cambiar el color del líquido del perfume (Dorado Erba Pura, Azul Sauvage, Rubí Baccarat o Ámbar Oud), ajustar el grosor del puntero y dibujar o firmar libremente sobre la etiqueta del frasco.
* **Comando para ejecutar:**
  ```bash
  python 05_canvas_y_eventos.py
  ```

---

### 6. `06_menus_y_atajos.py` — Bitácora de Fórmulas y Reseñas Olfativas
* **Tema en Perfumería:** Cuaderno digital de laboratorio para que el perfumista diseñe pirámides olfativas y fórmulas maestras de fragancias.
* **Componentes de Tkinter Utilizados:**
  * `tk.Menu`: Barra superior con menús desplegables:
    * *Archivo:* Nueva Bitácora, Cargar Fórmula, Guardar Fórmula, Salir.
    * *Acordes Olfativos:* Inserción automática de plantillas de notas cítricas, orientales y amaderadas.
    * *Edición:* Operaciones estándar de portapapeles (`<<Cut>>`, `<<Copy>>`, `<<Paste>>`).
    * *Ayuda:* Glosario técnico de términos de perfumería (*Sillage*, *Longevidad*, *Decant*).
  * Menú Contextual Flotante: Menú que aparece en la posición exacta del cursor al hacer **clic derecho** sobre el texto (`menu.post(x, y)`).
  * Atajos de Teclado (Accelerators): Vinculación de combinaciones rápidas mediante `bind`:
    * <kbd>Ctrl</kbd> + <kbd>N</kbd> : Nueva bitácora en blanco.
    * <kbd>Ctrl</kbd> + <kbd>S</kbd> : Guardar fórmula en archivo de texto `.txt`.
    * <kbd>Ctrl</kbd> + <kbd>Q</kbd> : Cerrar la aplicación.
  * `tk.Text` con `Scrollbar`: Área de edición multilinea con soporte para caracteres especiales y formato de notas.
* **Lo que hace el programa:** Es un editor de texto especializado para perfumistas. Incluye una plantilla predefinida con la fórmula de *Golden Elixir No. 7*, permite guardar y abrir fórmulas desde el disco duro y agregar acordes rápidamente con clic derecho.
* **Comando para ejecutar:**
  ```bash
  python 06_menus_y_atajos.py
  ```

---

### 7. `main.py` — Proyecto Integrador: Sistema POS Ryan.ShopMx
* **Tema en Perfumería:** Sistema de punto de venta (POS) y caja registradora para la boutique física de fragancias de lujo.
* **Componentes de Tkinter Utilizados:**
  * Arquitectura completa en Programación Orientada a Objetos (`class RyanShopApp`).
  * Interfaz a dos columnas (Catálogo a la izquierda, Resumen de Orden a la derecha).
  * Filtrado dinámico por categorías (Nicho, Diseñador, Decants).
  * `tk.Spinbox` para control y validación de cantidades de piezas.
  * `tk.Text` configurado en modo solo lectura (`state="disabled"`) para proteger el ticket de manipulaciones accidentales.
  * Botones de vaciado de orden y finalización de venta con emisión de folio correlativo (`RS-1001`), fecha/hora y total acumulado.
* **Lo que hace el programa:** Permite al cajero seleccionar perfumes, ingresar la cantidad deseada, ver el desglose en tiempo real y emitir el ticket de compra con confirmación interactiva.
* **Comando para ejecutar:**
  ```bash
  python main.py
  ```

---

## 📊 Matriz de Widgets y Funcionalidades de Tkinter

| Widget / Módulo | Demostración en el Proyecto | Archivo Principal |
| :--- | :--- | :--- |
| `tk.Label` | Títulos, indicadores y fichas técnicas | Todos los archivos |
| `tk.Button` | Disparador de funciones y acciones interactivas | Todos los archivos |
| `tk.Entry` | Captura de texto del cliente | `01_widgets_basicos.py` |
| `tk.Radiobutton` | Elección exclusiva de familia olfativa / perfumes | `01_widgets_basicos.py`, `main.py` |
| `tk.Checkbutton` | Selección de muestras y empaques de regalo | `01_widgets_basicos.py` |
| `tk.Scale` | Sliders de concentración de esencia y grosor | `01`, `05_canvas_y_eventos.py` |
| `tk.Spinbox` | Selector numérico de unidades por perfume | `main.py` |
| `tk.Text` | Editor de fórmulas olfativas y ticket de compra | `06_menus_y_atajos.py`, `main.py` |
| `tk.Canvas` | Renderizado de frascos y grabado con mouse | `05_canvas_y_eventos.py` |
| `tk.Menu` | Barra de menús y menú contextual con clic derecho | `06_menus_y_atajos.py` |
| `tk.Toplevel` | Ventana secundaria modal de pirámide olfativa | `03_dialogos_y_ventanas.py` |
| `ttk.Notebook` | Pestañas para comparar pack, grid y place | `02_administradores_geometria.py` |
| `ttk.Treeview` | Tabla de inventario de perfumes con columnas | `04_ttk_avanzado.py` |
| `ttk.Combobox` | Menús desplegables para filtrar fragancias | `04_ttk_avanzado.py`, `main.py` |
| `ttk.Progressbar`| Barra de progreso para maceración de aceites | `04_ttk_avanzado.py` |
| `messagebox` | Alertas de stock, errores de cobro y avisos | `03`, `04`, `06`, `main.py` |
| `filedialog` | Guardado de fórmulas y exportación de listas | `03_dialogos_y_ventanas.py`, `06_menus_y_atajos.py` |
| `colorchooser` | Selector de tono del líquido y cristal del frasco | `03_dialogos_y_ventanas.py` |

---

## 🚀 Requisitos e Instalación

### Requisitos
* **Python 3.8 o superior** instalado.
* `Tkinter` viene preinstalado por defecto en Python en Windows y macOS.

### Clonar el Proyecto desde GitHub
```bash
git clone https://github.com/ryanmontiel26-jpg/ryan-shop-pos.git
cd ryan-shop-pos
```

### Probar los Módulos
Cada archivo es completamente independiente y autocontenido. Puedes ejecutar cualquiera de ellos:

```bash
# Probar el asesor olfativo
python 01_widgets_basicos.py

# Probar el grabador interactivo de frascos
python 05_canvas_y_eventos.py

# Probar la caja registradora / POS
python main.py
```

---

## 👤 Autor
* **Ryan Montiel** — [@ryanmontiel26-jpg](https://github.com/ryanmontiel26-jpg)
* **Contacto:** ryanmontiel26@gmail.com

---

## 📄 Licencia
Este proyecto está publicado bajo la licencia **MIT**, permitiendo su uso libre tanto para fines académicos como comerciales.
