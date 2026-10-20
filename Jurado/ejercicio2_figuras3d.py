"""
Curso: Programación (213023) - UNAD
Fase 3: Modelos de herencia, polimorfismo y gestión de métodos
Ejercicio 2: Sistema Avanzado de Figuras 3D
Autor: Juan Pablo Jurado Vásquez
"""

# ==============================================================================
# IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import math  # Librería matemática estándar (nos permite usar el número Pi: math.pi)
from abc import ABC, abstractmethod  # Herramientas para crear Clases Abstractas (moldes)
import tkinter as tk  # Librería estándar de Python para crear ventanas gráficas (GUI)
from tkinter import ttk, messagebox  # Componentes modernos de Tkinter y ventanas de alerta


# ==============================================================================
# 1. CLASE BASE ABSTRACTA (MOLDE OBLIGATORIO)
# ==============================================================================
# Al poner (ABC) entre paréntesis, le decimos a Python que Figura3D es una Clase Abstracta.
# Esto significa que es solo una plantilla: no se puede crear un objeto "Figura3D" directo,
# sino que sirve de base para crear figuras reales (Cubo, Esfera, Cilindro).
class Figura3D(ABC):
    """Clase abstracta que obliga a todas las figuras 3D a tener los mismos métodos."""

    # __init__ es el método constructor: se ejecuta al crear cualquier figura.
    def __init__(self, nombre: str):
        # Guardamos el nombre de la figura (ej. "Cube", "Sphere", "Cylinder") dentro del objeto (self)
        self.nombre = nombre

    # @abstractmethod es un candado/regla: obliga a que cualquier clase hija (Cubo, Esfera, etc.)
    # tenga que escribir su propia fórmula para calcular_volumen().
    @abstractmethod
    def calcular_volumen(self) -> float:
        # "pass" significa "no hagas nada aquí". Como el molde general no tiene forma definida,
        # dejamos la fórmula vacía para que cada figura hija la rellene a su manera.
        pass

    # Segundo método obligatorio con simulación de SOBRECARGA (factor_escala = None).
    @abstractmethod
    def calcular_area_superficial(self, factor_escala: float = None) -> float:
        pass

    # Tercer método obligatorio y POLIMÓRFICO para mostrar la descripción de la figura.
    @abstractmethod
    def dibujar(self) -> str:
        pass


# ==============================================================================
# 2. SUBCLASES / CLASES HIJAS (HERENCIA, POLIMORFISMO Y SOBRECARGA)
# ==============================================================================

# --- SUBCLASE 1: CUBO ---
# Poner Cubo(Figura3D) indica HERENCIA: "Cubo es hijo de Figura3D".
class Cubo(Figura3D):
    """Representa un Cubo tridimensional."""

    # Constructor del Cubo: pide cuánto mide su lado.
    def __init__(self, lado: float):
        # super().__init__("Cube") llama al constructor de la clase padre (Figura3D)
        # y le entrega el texto "Cube" para que lo guarde en self.nombre.
        super().__init__("Cube")
        # Guardamos la medida del lado dentro de este cubo específico.
        self.lado = lado

    # POLIMORFISMO: Sobrescribimos calcular_volumen() con la fórmula exclusiva del Cubo.
    def calcular_volumen(self) -> float:
        # Fórmula matemática del volumen de un cubo: lado elevado a la 3 (lado³).
        # En Python, el doble asterisco (**) significa potencia.
        return self.lado ** 3

    # SOBRECARGA Y POLIMORFISMO:
    # factor_escala: float = None significa que el parámetro es OPCIONAL.
    # - Si llaman a calcular_area_superficial() vacío, factor_escala vale None.
    # - Si llaman a calcular_area_superficial(2.0), factor_escala vale 2.0.
    def calcular_area_superficial(self, factor_escala: float = None) -> float:
        # Si nos enviaron un factor_escala (no es None), usamos ese número;
        # de lo contrario (si no enviaron nada), usamos 1.0 (tamaño original sin cambios).
        escala = factor_escala if factor_escala is not None else 1.0
        
        # Calculamos el lado temporal escalado sin alterar el self.lado original del objeto.
        lado_escalado = self.lado * escala
        
        # Fórmula del área superficial de un cubo: 6 caras multiplicadas por (lado²).
        return 6 * (lado_escalado ** 2)

    # POLIMORFISMO: El cubo responde al método dibujar() con su propia descripción en inglés.
    def dibujar(self) -> str:
        # {self.lado:.2f} formatea el número para que muestre solo 2 decimales.
        return f"[3D Mesh: Cube] -> 6 square faces | Side = {self.lado:.2f} u"


# --- SUBCLASE 2: ESFERA ---
# Esfera también hereda de Figura3D.
class Esfera(Figura3D):
    """Representa una Esfera tridimensional."""

    # Constructor de la Esfera: pide cuánto mide su radio.
    def __init__(self, radio: float):
        # Llama al padre Figura3D para registrar el nombre "Sphere".
        super().__init__("Sphere")
        # Guarda el radio de la esfera.
        self.radio = radio

    # POLIMORFISMO: Fórmula de volumen exclusiva para la Esfera.
    def calcular_volumen(self) -> float:
        # Fórmula matemática: (4/3) * pi * radio³
        return (4.0 / 3.0) * math.pi * (self.radio ** 3)

    # SOBRECARGA: Calcula el área superficial normal (sin parámetros) o escalada (con parámetro).
    def calcular_area_superficial(self, factor_escala: float = None) -> float:
        # Define la escala (1.0 por defecto si no se pasa parámetro).
        escala = factor_escala if factor_escala is not None else 1.0
        
        # Multiplica el radio por el factor de escala de forma temporal.
        radio_escalado = self.radio * escala
        
        # Fórmula del área superficial de una esfera: 4 * pi * radio²
        return 4 * math.pi * (radio_escalado ** 2)

    # POLIMORFISMO: Descripción textual única de la esfera.
    def dibujar(self) -> str:
        return f"[3D Mesh: Sphere] -> Continuous curved surface | Radius = {self.radio:.2f} u"


# --- SUBCLASE 3: CILINDRO ---
# Cilindro también hereda de Figura3D.
class Cilindro(Figura3D):
    """Representa un Cilindro tridimensional."""

    # Constructor del Cilindro: requiere dos medidas (radio y altura).
    def __init__(self, radio: float, altura: float):
        # Registra el nombre "Cylinder" en la clase padre.
        super().__init__("Cylinder")
        # Guarda tanto el radio como la altura en el objeto.
        self.radio = radio
        self.altura = altura

    # POLIMORFISMO: Fórmula de volumen exclusiva para el Cilindro.
    def calcular_volumen(self) -> float:
        # Fórmula matemática: pi * radio² * altura
        return math.pi * (self.radio ** 2) * self.altura

    # SOBRECARGA: Permite escalar dinámicamente tanto el radio como la altura.
    def calcular_area_superficial(self, factor_escala: float = None) -> float:
        # Si no se recibe factor_escala, se mantiene en 1.0.
        escala = factor_escala if factor_escala is not None else 1.0
        
        # Escalamos temporalmente radio (r_esc) y altura (h_esc).
        r_esc = self.radio * escala
        h_esc = self.altura * escala
        
        # Fórmula del área superficial total de un cilindro: 2 * pi * r * (r + h)
        return 2 * math.pi * r_esc * (r_esc + h_esc)

    # POLIMORFISMO: Descripción textual única del cilindro.
    def dibujar(self) -> str:
        return (
            f"[3D Mesh: Cylinder] -> 2 circular bases | "
            f"Radius = {self.radio:.2f} u, Height = {self.altura:.2f} u"
        )


# ==============================================================================
# 3. INTERFAZ GRÁFICA DE USUARIO (TKINTER - DISEÑADA EN INGLÉS)
# ==============================================================================
class Shapes3DApp:
    """Clase que administra la ventana gráfica y conecta los botones con las figuras."""

    def __init__(self, root: tk.Tk):
        # Guardamos la ventana principal de Tkinter.
        self.root = root
        # Título de la ventana superior en inglés (requisito del Anexo 2).
        self.root.title("Advanced 3D Shapes Rendering & Math Module - UNAD")
        # Tamaño de la ventana: 820 píxeles de ancho por 580 de alto.
        self.root.geometry("820x580")
        # Bloqueamos el cambio de tamaño para que el diseño no se desordene.
        self.root.resizable(False, False)

        # LISTA HETEROGÉNEA (Lista de figuras mezcladas):
        # Aquí metemos un Cubo, una Esfera y un Cilindro dentro de la misma lista.
        # Aunque son clases distintas, conviven juntas porque todas son hijas de Figura3D.
        self.shapes_list: list[Figura3D] = [
            Cubo(4.0),          # Cubo de lado 4.0
            Esfera(3.5),        # Esfera de radio 3.5
            Cilindro(2.5, 7.0)  # Cilindro de radio 2.5 y altura 7.0
        ]

        # Llamamos a la función que dibuja los botones y cuadros de texto en la ventana.
        self._build_ui()
        # Ejecutamos la simulación inicial para que aparezcan resultados apenas abras el programa.
        self.run_polymorphic_simulation()

    def _build_ui(self):
        """Construye visualmente cada sección de la ventana gráfica."""
        
        # --- Encabezado principal ---
        header = ttk.Label(
            self.root,
            text="3D Digital Animation - Mathematical Geometry Engine",
            font=("Segoe UI", 14, "bold")
        )
        header.pack(pady=10)  # pack() coloca el título arriba con un margen vertical de 10px

        # --- SECCIÓN 1: Panel para agregar nuevas figuras a la lista ---
        input_frame = ttk.LabelFrame(self.root, text="Add New 3D Shape to Scene", padding=10)
        input_frame.pack(fill="x", padx=15, pady=5)

        # Etiqueta y menú desplegable (Combobox) para elegir entre Cube, Sphere o Cylinder
        ttk.Label(input_frame, text="Shape Type:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.shape_type_var = tk.StringVar(value="Cube")
        type_combo = ttk.Combobox(
            input_frame,
            textvariable=self.shape_type_var,
            values=["Cube", "Sphere", "Cylinder"],
            state="readonly",
            width=12
        )
        type_combo.grid(row=0, column=1, padx=5, pady=5)
        # Cuando el usuario cambia la opción del menú, se ejecuta _on_type_change
        type_combo.bind("<<ComboboxSelected>>", self._on_type_change)

        # Caja de texto 1: Para escribir el Lado (si es Cubo) o el Radio (si es Esfera/Cilindro)
        self.lbl_param1 = ttk.Label(input_frame, text="Side / Radius:")
        self.lbl_param1.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_param1 = ttk.Entry(input_frame, width=10)
        self.entry_param1.insert(0, "5.0")  # Valor por defecto: 5.0
        self.entry_param1.grid(row=0, column=3, padx=5, pady=5)

        # Caja de texto 2: Para escribir la Altura (solo se activa cuando se elige Cylinder)
        self.lbl_param2 = ttk.Label(input_frame, text="Height (Cylinder):")
        self.lbl_param2.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.entry_param2 = ttk.Entry(input_frame, width=10, state="disabled")
        self.entry_param2.grid(row=0, column=5, padx=5, pady=5)

        # Botón para agregar la figura a la lista mezclada
        btn_add = ttk.Button(input_frame, text="Add Shape", command=self.add_shape)
        btn_add.grid(row=0, column=6, padx=10, pady=5)

        # --- SECCIÓN 2: Panel para probar la Sobrecarga (Escalado Dinámico) ---
        scale_frame = ttk.LabelFrame(
            self.root,
            text="Dynamic Scaling Simulation (Method Overloading)",
            padding=10
        )
        scale_frame.pack(fill="x", padx=15, pady=5)

        # Caja para escribir el factor_escala (por defecto 2.0, es decir, el doble de tamaño)
        ttk.Label(scale_frame, text="Scale Factor (factor_escala):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_scale = ttk.Entry(scale_frame, width=10)
        self.entry_scale.insert(0, "2.0")
        self.entry_scale.grid(row=0, column=1, padx=5, pady=5)

        # Botón que dispara el ciclo polimórfico y muestra los cálculos
        btn_run = ttk.Button(
            scale_frame,
            text="Run Polymorphic Cycle & Overload Test",
            command=self.run_polymorphic_simulation
        )
        btn_run.grid(row=0, column=2, padx=15, pady=5)

        # Botón para reiniciar la lista a las 3 figuras originales
        btn_clear = ttk.Button(scale_frame, text="Reset Scene", command=self.reset_scene)
        btn_clear.grid(row=0, column=3, padx=5, pady=5)

        # --- SECCIÓN 3: Pantalla negra (Consola de resultados) ---
        output_frame = ttk.LabelFrame(self.root, text="Polymorphic Scene Render Log", padding=10)
        output_frame.pack(fill="both", expand=True, padx=15, pady=10)

        # Cuadro de texto amplio donde se imprimen todos los resultados matemáticos
        self.txt_output = tk.Text(output_frame, font=("Consolas", 10), bg="#1e1e1e", fg="#d4d4d4")
        self.txt_output.pack(fill="both", expand=True)

    def _on_type_change(self, event=None):
        """Activa la casilla de 'Height' únicamente si el usuario selecciona 'Cylinder'."""
        if self.shape_type_var.get() == "Cylinder":
            self.entry_param2.config(state="normal")
            self.entry_param2.delete(0, tk.END)
            self.entry_param2.insert(0, "8.0")
        else:
            self.entry_param2.delete(0, tk.END)
            self.entry_param2.config(state="disabled")

    def add_shape(self):
        """Lee los números escritos por el usuario, crea el objeto y lo mete en la lista."""
        try:
            shape_type = self.shape_type_var.get()
            # Convertimos el texto de la casilla 1 a número decimal (float)
            p1 = float(self.entry_param1.get())
            if p1 <= 0:
                raise ValueError("Dimensions must be greater than zero.")

            # Según lo elegido en el menú, instanciamos la subclase correspondiente
            if shape_type == "Cube":
                new_shape = Cubo(p1)
            elif shape_type == "Sphere":
                new_shape = Esfera(p1)
            else:
                p2 = float(self.entry_param2.get())
                if p2 <= 0:
                    raise ValueError("Height must be greater than zero.")
                new_shape = Cilindro(p1, p2)

            # Agregamos la nueva figura a nuestra lista heterogénea
            self.shapes_list.append(new_shape)
            # Actualizamos la pantalla de resultados
            self.run_polymorphic_simulation()

        except ValueError as e:
            # Si el usuario escribió letras o números negativos, mostramos alerta de error
            messagebox.showerror("Invalid Input", f"Please enter valid positive numbers.\nDetails: {e}")

    def reset_scene(self):
        """Vacía la lista y vuelve a poner las 3 figuras iniciales de prueba."""
        self.shapes_list.clear()
        self.shapes_list.extend([Cubo(4.0), Esfera(3.5), Cilindro(2.5, 7.0)])
        self.run_polymorphic_simulation()

    def run_polymorphic_simulation(self):
        """
        CORAZÓN DEL EJERCICIO 2:
        Recorre la lista mezclada con un solo ciclo for e invoca los métodos
        polimórficos y sobrecargados sin usar 'if' para preguntar qué figura es.
        """
        try:
            # Leemos el factor de escala escrito en la interfaz
            scale_factor = float(self.entry_scale.get())
            if scale_factor <= 0:
                raise ValueError("Scale factor must be positive.")
        except ValueError:
            messagebox.showerror("Scale Error", "Scale factor must be a valid positive number.")
            return

        # Limpiamos la consola negra antes de escribir nuevos resultados
        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert(tk.END, "=== STARTING POLYMORPHIC RENDERING ENGINE ===\n")
        self.txt_output.insert(tk.END, f"Total mixed objects in scene: {len(self.shapes_list)}\n")
        self.txt_output.insert(tk.END, f"Dynamic Scale Factor applied: x{scale_factor:.2f}\n")
        self.txt_output.insert(tk.END, "=" * 75 + "\n\n")

        # CICLO POLIMÓRFICO:
        # En cada vuelta del ciclo, la variable 'figura' toma un objeto de la lista
        # (primero el Cubo, luego la Esfera, luego el Cilindro, etc.).
        for idx, figura in enumerate(self.shapes_list, start=1):
            
            # 1. Llamada polimórfica a dibujar()
            representacion = figura.dibujar()
            
            # 2. Llamada polimórfica a calcular_volumen()
            volumen = figura.calcular_volumen()
            
            # 3. Llamada SOBRECARGADA #1: Sin argumentos (calcula el área con tamaño normal)
            area_base = figura.calcular_area_superficial()
            
            # 4. Llamada SOBRECARGADA #2: Enviando scale_factor (calcula el área escalada)
            area_escalada = figura.calcular_area_superficial(scale_factor)

            # Armamos el bloque de texto con los resultados de esa figura y lo mostramos en pantalla
            log_entry = (
                f"Object #{idx}: {representacion}\n"
                f"   -> Base Volume                 : {volumen:.2f} u³\n"
                f"   -> Base Surface Area (No Args) : {area_base:.2f} u²\n"
                f"   -> Scaled Surface Area (x{scale_factor:.2f}) : {area_escalada:.2f} u²\n"
                f"{'-' * 75}\n"
            )
            self.txt_output.insert(tk.END, log_entry)


# ==============================================================================
# 4. PUNTO DE ENTRADA DEL PROGRAMA (EJECUCIÓN PRINCIPAL)
# ==============================================================================
# Esta condición verifica que este archivo se esté ejecutando directamente.
if __name__ == "__main__":
    root = tk.Tk()          # Crea la ventana base de Tkinter
    app = Shapes3DApp(root) # Carga nuestra aplicación dentro de esa ventana
    root.mainloop()         # Mantiene la ventana abierta esperando clics del usuario