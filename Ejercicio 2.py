import tkinter

# Clase usuario


class Usuario:
    def __init__(self):
        self.usuario = "programacion"
        self.password = "programacion"
# Metodo para validar el usuario y la contraseña

    def validar(self, usuario_ingresado, password_ingresado):
        if self.usuario == usuario_ingresado and self.password == password_ingresado:
            return True
        else:
            return False


# Clase ComputadorMantenimiento

class ComputadorMantenimiento:

    def __init__(self, _codigo, _hora_entrada, _valor_hora):
        self.codigo = _codigo
        self.hora_entrada = _hora_entrada
        self.valor_hora = _valor_hora
        self.hora_salida = 0

# Método registrar_entrada(hora)
    def registrar_entrada(self, hora):
        self.hora_entrada = hora

# Método registrar_salida(hora)
    def registrar_salida(self, hora):
        self.hora_salida = hora

# Método calcular_valor(hora_salida)
    def calcular_valor(self, hora_salida):
        self.hora_salida = hora_salida
        horas_totales = self.hora_salida - self.hora_entrada
        valor_final = horas_totales*self.valor_hora
        return valor_final

# Método obtener_codigo()
    def obtener_codigo(self):
        return self.codigo


class AppMantenimiento:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("600x500")

        # variable para asignar un consecutivo a cada computador como su codigo
        self.contador_computador = 0
        # variable para almacenar los computadores en una lista
        self.matriz_computadores = []
        # instanciamos la clase usuario para poder usarla
        self.usuario = Usuario()

        # Creamos un frame de login para manejar la interfaz grafica por frames
        self.frame_login = tkinter.Frame(self.ventana)
        self.frame_login.pack(pady=40)

        # etiquetas y cajas de texto para el login
        tkinter.Label(self.frame_login, text="User:").pack()
        self.caja_usuario = tkinter.Entry(self.frame_login)
        self.caja_usuario.pack()

        tkinter.Label(self.frame_login, text="Password:").pack()
        self.caja_contraseña = tkinter.Entry(self.frame_login, show="*")
        self.caja_contraseña.pack()

        # botón de inicio de sesión
        tkinter.Button(self.frame_login, text="Login",
                       command=self.iniciar_sesion).pack(pady=10)
        self.mensaje_error_login = tkinter.Label(
            self.frame_login, text="", fg="red")
        self.mensaje_error_login.pack()

        # Creamos el frame registro de entrada, que estará oculto hasta que el usuario inicie sesión correctamente
        self.frame_registro_entrada = tkinter.Frame(self.ventana)

        tkinter.Label(self.frame_registro_entrada,
                      text="Computer Maintenance System App", fg="green").pack(pady=30)
        tkinter.Label(self.frame_registro_entrada,
                      text="Computer Registration", fg="blue").pack(pady=20)
        tkinter.Label(self.frame_registro_entrada,
                      text="Entrance Hour (Only Integers)", fg="red").pack()
        self.caja_hora = tkinter.Entry(self.frame_registro_entrada)
        self.caja_hora.pack()
        tkinter.Label(self.frame_registro_entrada,
                      text="Hour Cost (Only Integers)", fg="red").pack()
        self.caja_valor = tkinter.Entry(self.frame_registro_entrada)
        self.caja_valor.pack()
        tkinter.Button(self.frame_registro_entrada, text="Submit",
                       command=self.registrar_pc_GUI).pack(pady=10)
        self.etiqueta_estado_registro = tkinter.Label(
            self.frame_registro_entrada, text="", fg="black")
        self.etiqueta_estado_registro.pack()
        tkinter.Button(self.frame_registro_entrada, text="Menu",
                       command=self.mostrar_menu_registro_entrada).pack(pady=10)

        # Creamos el frame del menú, que estará oculto hasta que el usuario haga clic en el botón "Menu"
        self.frame_menu = tkinter.Frame(self.ventana)
        tkinter.Label(self.frame_menu, text="Menu", fg="blue").pack(pady=20)
        tkinter.Label(self.frame_menu, text="1. Register Entrance").pack()
        tkinter.Button(self.frame_menu, text="Register Entrance",
                       command=self.mostrar_registro_entrada).pack(pady=5)
        tkinter.Label(self.frame_menu,
                      text="2. View Registered Computers").pack()
        tkinter.Button(self.frame_menu, text="View Registered Computers",
                       command=self.mostrar_ver_computadores).pack(pady=5)
        tkinter.Label(self.frame_menu, text="3. Register Exit").pack()
        tkinter.Button(self.frame_menu, text="Register Exit",
                       command=self.mostrar_registro_salida).pack(pady=5)

        # Creamos el frame para ver los computadores registrados, que estará oculto hasta que el usuario haga clic en la opción correspondiente del menú
        self.frame_ver_computadores = tkinter.Frame(self.ventana)

        # Creaamos el frame para registrar la salida de los computadores, que estará oculto hasta que el usuario haga clic en la opción correspondiente del menú
        self.frame_registro_salida = tkinter.Frame(self.ventana)

        tkinter.Label(self.frame_registro_salida,
                      text="Computer Exit Registration", fg="red").pack(pady=20)
        tkinter.Label(self.frame_registro_salida,
                      text="Enter the code of the computer to register exit:").pack()
        self.caja_codigo_salida = tkinter.Entry(self.frame_registro_salida)
        self.caja_codigo_salida.pack()
        tkinter.Label(self.frame_registro_salida,
                      text="Enter the exit hour:").pack()
        self.caja_hora_salida = tkinter.Entry(self.frame_registro_salida)
        self.caja_hora_salida.pack()
        tkinter.Button(self.frame_registro_salida, text="Submit",
                       command=self.registrar_salida_GUI).pack(pady=10)
        self.etiqueta_estado_salida = tkinter.Label(
            self.frame_registro_salida, text="", fg="red")
        self.etiqueta_estado_salida.pack()

        tkinter.Button(self.frame_registro_salida, text="Menu",
                       command=self.mostrar_menu_registro_entrada).pack(pady=10)

    def iniciar_sesion(self):
        usuario_ingresado = self.caja_usuario.get()
        password_ingresado = self.caja_contraseña.get()

        if self.usuario.validar(usuario_ingresado, password_ingresado):
            self.frame_login.pack_forget()  # Ocultar el frame de login
            self.frame_registro_entrada.pack(
                pady=5)  # Mostrar el frame principal
        else:
            self.mensaje_error_login.config(
                text="Incorrect username or password. Please try again.")

    def registrar_pc_GUI(self):
        hora_entrada = self.caja_hora.get()
        valor_hora = self.caja_valor.get()

        if 0 <= int(hora_entrada) <= 23 and 0 < float(valor_hora):
            try:
                hora_entrada = int(hora_entrada)
                valor_hora = float(valor_hora)
                self.contador_computador += 1
                nuevo_computador = ComputadorMantenimiento(
                    self.contador_computador, hora_entrada, valor_hora)
                self.matriz_computadores.append(nuevo_computador)
                self.etiqueta_estado_registro.config(
                    text=f"Computer {self.contador_computador} registered successfully!", fg="green")
            except ValueError:
                self.etiqueta_estado_registro.config(
                    text="Please enter valid numbers for hour and cost.", fg="red")
        else:
            self.etiqueta_estado_registro.config(
                text="Please fill in all fields with valid values.", fg="red")

    def mostrar_menu_registro_entrada(self):
        # Ocultar el frame de registro de entrada
        self.frame_registro_entrada.pack_forget()
        # Ocultar el frame de ver computadores
        self.frame_ver_computadores.pack_forget()
        # Ocultar el frame de registro de salida
        self.frame_registro_salida.pack_forget()
        self.frame_menu.pack(pady=5)  # Mostrar el frame del menú

    def mostrar_registro_entrada(self):
        self.frame_menu.pack_forget()  # Ocultar el frame del menú
        # Mostrar el frame de registro de entrada
        self.frame_registro_entrada.pack(pady=5)

    def mostrar_ver_computadores(self):
        self.frame_menu.pack_forget()  # Ocultar el frame del menú
        # Mostrar el frame de ver computadores
        self.frame_ver_computadores.pack(pady=5)

        for widget in self.frame_ver_computadores.winfo_children():
            widget.destroy()

        tkinter.Label(self.frame_ver_computadores, text="Registered Computers List", font=(
            "Arial", 12, "bold"), fg="blue").pack(pady=10)

        if len(self.matriz_computadores) == 0:
            tkinter.Label(self.frame_ver_computadores,
                          text="No computers registered yet.", fg="red").pack(pady=10)
        else:
            for pc in self.matriz_computadores:
                texto_pc = f"Code: {pc.obtener_codigo()} | Entry Hour: {pc.hora_entrada} | Hour Cost: ${pc.valor_hora}"
                tkinter.Label(self.frame_ver_computadores,
                              text=texto_pc).pack(pady=2)

        tkinter.Button(self.frame_ver_computadores, text="Menu",
                       command=self.mostrar_menu_registro_entrada).pack(pady=10)

    def mostrar_registro_salida(self):
        self.frame_menu.pack_forget()  # Ocultar el frame del menú
        # Mostrar el frame de registro de salida
        self.frame_registro_salida.pack(pady=5)

    def registrar_salida_GUI(self):
        codigo_salida = self.caja_codigo_salida.get()
        hora_salida = self.caja_hora_salida.get()

        if codigo_salida and hora_salida:
            try:
                codigo_salida = int(codigo_salida)
                hora_salida = int(hora_salida)

                # Buscar el computador por su código
                computador_encontrado = None
                for pc in self.matriz_computadores:
                    if pc.obtener_codigo() == codigo_salida:
                        computador_encontrado = pc
                        break

                if computador_encontrado and computador_encontrado.hora_entrada < hora_salida:
                    valor_final = computador_encontrado.calcular_valor(
                        hora_salida)
                    self.etiqueta_estado_salida.config(
                        text=f"Exit registered successfully! Total cost: ${valor_final:.2f}", fg="green")
                else:
                    self.etiqueta_estado_salida.config(
                        text="Computer code not found or invalid exit hour.", fg="red")
            except ValueError:
                self.etiqueta_estado_salida.config(
                    text="Please enter valid numbers for code and exit hour.", fg="red")
        else:
            self.etiqueta_estado_salida.config(
                text="Please fill in all fields.", fg="red")


raiz = tkinter.Tk()
app = AppMantenimiento(raiz)
raiz.mainloop()
