# 🐍 Guía Práctica y Colección de Funcionalidades de Tkinter en Python

Este repositorio contiene una colección estructurada, didáctica y progresiva de scripts en **Python** que demuestran las capacidades y componentes de la biblioteca de interfaz gráfica de usuario (GUI) **Tkinter** y su extensión moderna **TTK (Themed Tk)**.

El proyecto abarca desde los componentes visuales elementales hasta la integración de eventos del sistema, manejo de archivos, lienzos de dibujo bidimensional y una aplicación completa de escritorio orientada a objetos (POO).

---

## 📂 Estructura del Repositorio

```text
ryan-shop-pos/
│
├── 01_widgets_basicos.py             # Widgets elementales y variables de control
├── 02_administradores_geometria.py   # Comparativa de pack(), grid() y place()
├── 03_dialogos_y_ventanas.py         # Diálogos, archivos, colores y Toplevel
├── 04_ttk_avanzado.py                # Tablas (Treeview), Combobox y Progressbar
├── 05_canvas_y_eventos.py            # Gráficos 2D, mouse bindings y Mini Paint
├── 06_menus_y_atajos.py              # Barra de menús, clic derecho y atajos de teclado
├── main.py                           # Proyecto Integrador: Haute Parfumerie POS
│
├── requirements.txt                  # Archivo de dependencias del entorno
├── .gitignore                        # Reglas de exclusión para Git
└── README.md                         # Documentación detallada del proyecto
```

---

## 📖 Descripción Detallada de Cada Archivo

### 1. `01_widgets_basicos.py` — Widgets Elementales y Variables de Control
* **Objetivo:** Introducir los componentes gráficos primarios de interacción y el enlace reactivo de datos mediante variables de control de Tkinter.
* **Componentes y Conceptos Demostrados:**
  * `tk.Label`: Etiquetas de texto estático y formateo con fuentes personalizadas.
  * `tk.Entry`: Cajas de texto de una sola línea para captura de datos del usuario.
  * `tk.Button`: Botones con comandos asociados (`command=funcion`).
  * `tk.Checkbutton`: Casillas de verificación para valores booleanos.
  * `tk.Radiobutton`: Botones de selección excluyente con grupos de opciones.
  * `tk.Scale`: Control deslizante numérico (slider) horizontal.
  * `StringVar`, `IntVar`, `BooleanVar`: Variables especiales de Tkinter que sincronizan los datos con los widgets en tiempo real.
* **Lo que hace:** Despliega un formulario interactivo de preferencias de usuario. Al presionar *Enviar / Actualizar*, recopila el estado de todos los widgets y actualiza una etiqueta de resumen con formato de consola.
* **Ejecución:**
  ```bash
  python 01_widgets_basicos.py
  ```

---

### 2. `02_administradores_geometria.py` — Métodos de Posicionamiento y Layout
* **Objetivo:** Comprender y comparar los tres administradores de geometría que ofrece Tkinter para diseñar interfaces adaptables y ordenadas.
* **Componentes y Conceptos Demostrados:**
  * `pack()`: Posicionamiento por bloques y laterales (`side="top|bottom|left|right"`), distribución de espacio (`fill="x|y|both"`), y expansión proporcional (`expand=True`).
  * `grid()`: Sistema matricial basado en filas y columnas (`row`, `column`), unión de celdas (`columnspan`, `rowspan`), alineación (`sticky="nsew"`), y pesos de redimensionamiento (`columnconfigure`).
  * `place()`: Control de coordenadas exactas tanto absolutas en píxeles (`x`, `y`) como relativas/porcentuales respecto al tamaño de la ventana (`relx`, `rely`, `relwidth`).
  * `ttk.Notebook`: Pestañas para alternar entre las tres demostraciones sin recargar la ventana.
* **Lo que hace:** Muestra una ventana con 3 pestañas visuales interactivas, cada una dedicada a ilustrar el comportamiento visual y las propiedades clave de cada administrador de geometría.
* **Ejecución:**
  ```bash
  python 02_administradores_geometria.py
  ```

---

### 3. `03_dialogos_y_ventanas.py` — Cuadros de Diálogo del Sistema y Modales
* **Objetivo:** Aprender a comunicarse con el usuario a través de alertas del sistema operativo, selectores nativos y ventanas secundarias.
* **Componentes y Conceptos Demostrados:**
  * `tkinter.messagebox`: Despliegue de ventanas emergentes estándar de Información (`showinfo`), Advertencia (`showwarning`), Error (`showerror`) y Pregunta booleana (`askyesno`).
  * `tkinter.filedialog`: Explorador de archivos nativo del sistema para abrir (`askopenfilename`) o guardar archivos (`asksaveasfilename`) con filtros de extensión.
  * `tkinter.colorchooser`: Paleta nativa para selección de color interactivo (`askcolor`), devolviendo tuplas RGB y códigos hexadecimales.
  * `tk.Toplevel`: Creación de ventanas secundarias independientes con capacidad de bloqueo modal mediante `grab_set()`.
* **Lo que hace:** Ofrece un panel de control con botones que detonan cada tipo de diálogo del sistema y registra en pantalla las rutas, respuestas o colores elegidos por el usuario.
* **Ejecución:**
  ```bash
  python 03_dialogos_y_ventanas.py
  ```

---

### 4. `04_ttk_avanzado.py` — Tablas de Datos, Combobox y Barra de Progreso
* **Objetivo:** Usar la biblioteca `ttk` (Themed Tkinter) para crear interfaces modernas, estilizadas y profesionales.
* **Componentes y Conceptos Demostrados:**
  * `ttk.Treeview`: Renderizado de tablas de datos multidimensionales con cabeceras configurables, alineación de columnas y soporte para selección de filas.
  * `ttk.Scrollbar`: Barra de desplazamiento vertical vinculada bidireccionalmente con la tabla.
  * `ttk.Combobox`: Menú desplegable con autocompletado y captura de eventos de selección (`<<ComboboxSelected>>`).
  * `ttk.Progressbar`: Barra de carga animada mediante temporizadores (`root.after`).
  * `ttk.Style`: Personalización de temas visuales (`theme_use("clam")`) y estilos de cabecera.
* **Lo que hace:** Presenta una tabla con inventario de productos (ID, categoría, nombre, precio, existencias) que se filtra dinámicamente al seleccionar opciones en el Combobox, además de una barra de progreso interactiva con botones para simular o reiniciar una tarea pesada.
* **Ejecución:**
  ```bash
  python 04_ttk_avanzado.py
  ```

---

### 5. `05_canvas_y_eventos.py` — Gráficos 2D, Eventos del Ratón y Mini Paint
* **Objetivo:** Manipular el lienzo de dibujo de Tkinter y capturar eventos de entrada del usuario en tiempo real.
* **Componentes y Conceptos Demostrados:**
  * `tk.Canvas`: Área de gráficos vectoriales 2D.
  * Métodos de dibujo: `create_rectangle`, `create_oval`, `create_line`, `create_text`.
  * Eventos del ratón vinculados con `bind()`:
    * `<Button-1>`: Clic izquierdo presionado (registro del punto de inicio).
    * `<B1-Motion>`: Arrastre del ratón con el clic presionado (trazo continuo de líneas).
    * `<ButtonRelease-1>`: Clic izquierdo liberado.
    * `<Motion>`: Seguimiento en tiempo real de las coordenadas (X, Y) del puntero.
* **Lo que hace:** Proporciona una pizarra digital interactiva (Mini Paint) donde el usuario puede elegir colores de una paleta, variar el grosor del pincel, ver figuras geométricas de demostración, dibujar a mano alzada y borrar el lienzo.
* **Ejecución:**
  ```bash
  python 05_canvas_y_eventos.py
  ```

---

### 6. `06_menus_y_atajos.py` — Barra de Menús, Menú Contextual y Atajos de Teclado
* **Objetivo:** Crear una experiencia de aplicación de escritorio completa con navegación jerárquica y atajos de productividad.
* **Componentes y Conceptos Demostrados:**
  * `tk.Menu`: Barra de menús superior con menús desplegables (Archivo, Edición, Ayuda) y separadores visuales.
  * Menú Contextual (Clic derecho): Menú flotante que aparece en la posición exacta del cursor mediante el método `.post(x, y)`.
  * Atajos de Teclado (Accelerators & Binds): Enlace de atajos como `Ctrl+N` (Nuevo), `Ctrl+S` (Guardar) y `Ctrl+Q` (Salir).
  * `tk.Text`: Área de texto enriquecido multilinea con soporte para operaciones de portapapeles (`<<Cut>>`, `<<Copy>>`, `<<Paste>>`).
* **Lo que hace:** Implementa un editor de notas funcional que permite redactar texto, abrir y guardar archivos en disco, realizar operaciones de edición desde la barra de menú o con clic derecho, y controlar la aplicación mediante atajos de teclado.
* **Ejecución:**
  ```bash
  python 06_menus_y_atajos.py
  ```

---

### 7. `main.py` — Proyecto Integrador: Sistema POS de Alta Perfumería
* **Objetivo:** Integrar múltiples widgets, gestión de estado y diseño estético en una aplicación del mundo real utilizando Programación Orientada a Objetos (POO).
* **Componentes y Conceptos Demostrados:**
  * Arquitectura orientada a objetos (`class RyanShopApp`).
  * Paleta visual personalizada estilo *Dark Luxury* (`#121212`, `#1b1b1b` y dorado `#d4af37`).
  * Organización de pantalla a dos columnas con `LabelFrame`.
  * Filtro dinámico de catálogo por categorías (Nicho, Diseñador, Decants).
  * Control de cantidades con `Spinbox` y validación de enteros.
  * Carrito de compras reactivo con cálculo de subtotales, totales y recuento de artículos.
  * Finalización de venta con generación de folio único (`RS-1001`), marca de tiempo y reseteo de orden.
* **Lo que hace:** Simula el sistema de punto de venta para la boutique de fragancias **Ryan.ShopMx**, permitiendo seleccionar productos, ajustar cantidades, revisar la orden en tiempo real y emitir tickets de compra.
* **Ejecución:**
  ```bash
  python main.py
  ```

---

## 📊 Matriz Comparativa de Widgets y Módulos

| Widget / Módulo | Propósito Principal | Archivo(s) de Demostración |
| :--- | :--- | :--- |
| `tk.Label` | Textos, títulos e indicadores | Todos |
| `tk.Button` | Acciones y disparadores de eventos | `01`, `02`, `03`, `04`, `05`, `main.py` |
| `tk.Entry` | Entrada de texto de una sola línea | `01_widgets_basicos.py` |
| `tk.Checkbutton` | Selección booleana (Verdadero / Falso) | `01_widgets_basicos.py` |
| `tk.Radiobutton` | Selección exclusiva entre opciones | `01_widgets_basicos.py`, `main.py` |
| `tk.Scale` | Selector de rango numérico / slider | `01_widgets_basicos.py`, `05_canvas_y_eventos.py` |
| `tk.Spinbox` | Selector de cantidad numérica paso a paso | `main.py` |
| `tk.Text` | Editor de texto multilínea / resumen | `06_menus_y_atajos.py`, `main.py` |
| `tk.Canvas` | Dibujo vectorial 2D y captura de mouse | `05_canvas_y_eventos.py` |
| `tk.Menu` | Menú superior y menú contextual | `06_menus_y_atajos.py` |
| `tk.Toplevel` | Creación de ventanas secundarias modales | `03_dialogos_y_ventanas.py` |
| `ttk.Treeview` | Tablas de datos con columnas | `04_ttk_avanzado.py` |
| `ttk.Combobox` | Listas desplegables con eventos | `04_ttk_avanzado.py`, `main.py` |
| `ttk.Progressbar`| Barras de progreso de carga | `04_ttk_avanzado.py` |
| `ttk.Notebook` | Pestañas de navegación | `02_administradores_geometria.py` |
| `messagebox` | Alertas del sistema y confirmaciones | `03`, `04`, `06`, `main.py` |
| `filedialog` | Selector de archivos del sistema operativo | `03_dialogos_y_ventanas.py`, `06_menus_y_atajos.py` |
| `colorchooser` | Selector interactivo de color RGB/HEX | `03_dialogos_y_ventanas.py` |

---

## 🚀 Requisitos e Instalación

### Requisitos Previos
* **Python 3.8 o superior**.
* `Tkinter` viene incluido por defecto en las instalaciones oficiales de Python para Windows y macOS. En sistemas Linux (Ubuntu/Debian) se puede instalar mediante:
  ```bash
  sudo apt-get install python3-tk
  ```

### Clonar el Repositorio
```bash
git clone https://github.com/ryanmontiel26-jpg/ryan-shop-pos.git
cd ryan-shop-pos
```

### Ejecutar Cualquier Módulo
Para probar un archivo específico, ejecuta su comando en la terminal:
```bash
# Ejemplo: probar los widgets básicos
python 01_widgets_basicos.py

# Ejemplo: probar la aplicación completa
python main.py
```

---

## 👤 Autor
* **Ryan Montiel** — [@ryanmontiel26-jpg](https://github.com/ryanmontiel26-jpg)
* **Correo:** ryanmontiel26@gmail.com

---

## 📄 Licencia
Este repositorio se encuentra publicado bajo la licencia **MIT**, permitiendo su uso libre tanto para fines educativos como comerciales.
