from funciones import *
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pickle
from tkinter.messagebox import showinfo, showerror

# Variables globales
listaPersonas = []
nomArch = "personas_backUp"

def grabar(nomArchGrabar, lista):
    #Función que graba un archivo con una lista de personas
    try:
        f = open(nomArchGrabar, "wb")
        pickle.dump(lista, f)
        f.close()
    except:
        showerror("Error", "No se encontró backUp.")

def leer(nomArchLeer):
    #Función que lee un archivo con una lista de personas
    lista = []
    try:
        f = open(nomArchLeer, "rb")
        lista = pickle.load(f)
        f.close()
        showinfo("Back up", "Se cargó con éxito el back up.")
    except:
        showerror("Error", "Error al cargar el back up")
    return lista

def deshabilitarMenuPrincipal():
    btn_RegistrarMiembro.config(state="disabled")
    btn_CargarDatos.config(state="disabled")
    btn_RegistrarCandidatos.config(state="disabled")
    btn_GenerarVotacion.config(state="disabled")
    btn_Reportes.config(state="disabled")


def habilitarMenuPrincipal():
    btn_RegistrarMiembro.config(state="normal")
    btn_CargarDatos.config(state="normal")
    btn_RegistrarCandidatos.config(state="normal")
    btn_GenerarVotacion.config(state="normal")
    btn_Reportes.config(state="normal")


def pantallaRegistrarMiembro():
    def ver():
        if rb_variable.get() == 1:
            txtBox_Publicaciones.config(state="disabled")
            cb_Puesto.config(state="disabled")
            txt_Extension.config(state="disabled")
            txt_Carnet.config(state="normal")
            cb_Carrera.config(state="normal")
        elif rb_variable.get() == 2:
            txt_Carnet.config(state="disabled")
            cb_Carrera.config(state="disabled")
            cb_Puesto.config(state="disabled")
            txt_Extension.config(state="disabled")
            txtBox_Publicaciones.config(state="normal")
        elif rb_variable.get() == 3:
            txt_Carnet.config(state="disabled")
            cb_Carrera.config(state="disabled")
            txtBox_Publicaciones.config(state="disabled")
            cb_Puesto.config(state="normal")
            txt_Extension.config(state="normal")

    # def validar

    def validarDatos():
        listaPersonas = leer(nomArch)
        if rb_variable.get() == 1:
            validacionCarnet = validarCarnet(txt_Carnet.get())
            if validacionCarnet[0]:
                mensajeError.set(validacionCarnet[1])
                return ""

            validacionLenCarnet = validarLargoCarnet(txt_Carnet.get())
            if validacionLenCarnet[0]:
                mensajeError.set(validacionLenCarnet[1])
                return ""

        if rb_variable == 2:
            if txtBox_Publicaciones == "":
                mensajeError.set("De ingresar como mínimo una publicación.")
                return ""

        if rb_variable == 3:
            validacionLenExtension = validarLargoExtension(txt_Extension.get())
            if validacionLenExtension[0]:
                mensajeError.set(validacionLenExtension[1])
                return ""

            validacionExtension = validarExtension(txt_Extension.get())
            if validacionExtension[0]:
                mensajeError.set(validacionExtension[1])
                return ""

            if cb_Puesto == "":
                mensajeError.set("Debe seleccionar un puesto.")
                return ""

        validacionLenCedula = validarLargoCedula(txt_Cedula.get())
        if validacionLenCedula[0]:
            mensajeError.set(validacionLenCedula[1])
            return ""

        validacionCedula = validarCedula(txt_Cedula.get())
        if validacionCedula[0]:
            mensajeError.set(validacionCedula[1])
            return ""

        validacionCedulaExist = validacionCedulaExistente(int(txt_Cedula.get()), listaPersonas)
        if validacionCedulaExist[0]:
            mensajeError.set(validacionCedulaExist[1])
            return ""

        validacionLenTelefono = validarLargoTelefono(txt_Telefono.get())
        if validacionLenTelefono[0]:
            mensajeError.set(validacionLenTelefono[1])
            return ""

        validacionTelefono = validarTelefono(txt_Telefono.get())
        if validacionTelefono[0]:
            mensajeError.set(validacionTelefono[1])
            return ""

        camposVacios = validarCamposVacios(txt_NombreCompleto.get(),
                                           txt_Extension.get(),
                                           carrera=cb_Carrera.get())
        if camposVacios:
            mensajeError.set("Debe ingresar toda la información requerida.")
            return ""
        mensajeError.set("")
        return funcionBtnRegistrarPantallaRM()

    def funcionBtnRegistrarPantallaRM():

        mensaje = tk.messagebox.askquestion("Confirmación", "El miembro se registrará en el sistema. ¿Está de acuerdo?",
                                            icon="warning")

        if mensaje == 'yes':
            persona = funcionRegitrarMiembro(int(txt_Cedula.get()),
                                             txt_NombreCompleto.get(),
                                             int(txt_Telefono.get()),
                                             rb_variable.get(),
                                             int(txt_Carnet.get()),
                                             txtBox_Publicaciones.get(1.0, END),
                                             txt_Extension.get(),
                                             carrera=cb_Carrera.get(),
                                             puesto=cb_Puesto.get(), )
            listaPersonas.append(persona)
            grabar(nomArch, listaPersonas) #Graba el archivo en memoria secundaria

    def funcionBtnLimpiarPantallaRM():
        txt_Cedula.delete(0, len(txt_Cedula.get()))
        txt_NombreCompleto.delete(0, len(txt_NombreCompleto.get()))
        txt_Telefono.delete(0, len(txt_Telefono.get()))
        rb_variable.set(0)
        txt_Carnet.delete(0, len(txt_Carnet.get()))
        txtBox_Publicaciones.delete(1.0, END)
        txt_Extension.delete(0, len(txt_Extension.get()))

    pantallaRegistrarMiembro = Toplevel(root)
    pantallaRegistrarMiembro.title("Registrar miembro")
    pantallaRegistrarMiembro.geometry("400x600")
    pantallaRegistrarMiembro.resizable(False, False)

    # Primera sección
    Label(pantallaRegistrarMiembro, text="Cédula:").grid(row=0, column=0, padx=10, pady=5, sticky="E")
    Label(pantallaRegistrarMiembro, text="Nombre completo:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
    Label(pantallaRegistrarMiembro, text="Teléfono:").grid(row=2, column=0, padx=10, pady=5, sticky="E")

    txt_Cedula = Entry(pantallaRegistrarMiembro)
    txt_Cedula.grid(row=0, column=1, padx=10, pady=5, sticky="W")

    txt_NombreCompleto = Entry(pantallaRegistrarMiembro)
    txt_NombreCompleto.grid(row=1, column=1, padx=10, pady=5, sticky="W")

    txt_Telefono = Entry(pantallaRegistrarMiembro)
    txt_Telefono.grid(row=2, column=1, padx=10, pady=5, sticky="W")

    rb_variable = IntVar()
    rb_variable.set(1)

    Radiobutton(pantallaRegistrarMiembro, variable=rb_variable, value=1, command=ver).grid(row=3, column=0, padx=10,
                                                                                           pady=5,
                                                                                           sticky="W")
    Label(pantallaRegistrarMiembro, text="Estudiante").grid(row=3, column=0, padx=10, pady=5, sticky="E")

    Radiobutton(pantallaRegistrarMiembro, variable=rb_variable, value=2, command=ver).grid(row=4, column=0, padx=10,
                                                                                           pady=5,
                                                                                           sticky="W")
    Label(pantallaRegistrarMiembro, text="Profesor").grid(row=4, column=0, padx=10, pady=5, sticky="E")

    Radiobutton(pantallaRegistrarMiembro, variable=rb_variable, value=3, command=ver).grid(row=5, column=0, padx=10,
                                                                                           pady=5,
                                                                                           sticky="W")
    Label(pantallaRegistrarMiembro, text="Administrativo").grid(row=5, column=0, padx=10, pady=5, sticky="E")

    # Segunda sección
    Label(pantallaRegistrarMiembro, text="Carnet:").grid(row=7, column=0, padx=10, pady=5, sticky="E")

    txt_Carnet = Entry(pantallaRegistrarMiembro)
    txt_Carnet.grid(row=7, column=1, padx=10, pady=5, sticky="W")

    Label(pantallaRegistrarMiembro, text="Carrera:").grid(row=8, column=0, padx=10, pady=5, sticky="E")
    cb_Carrera = ttk.Combobox(pantallaRegistrarMiembro, state="readonly",
                              values=["IC-Ingeniería en Computación",
                                      "ATI-Administración de la Información",
                                      "E-Electrónica",
                                      "AE-Administración de Empresas",
                                      "CA-Ingeniería en Computadoras"])
    cb_Carrera.grid(row=8, column=1, padx=10, pady=5,
                    sticky="W")

    # Tercera sección
    Label(pantallaRegistrarMiembro, text="Publicaciones: ").grid(row=9, column=0, padx=10, pady=5, sticky="E")
    txtBox_Publicaciones = Text(pantallaRegistrarMiembro, width=25, height=5)
    txtBox_Publicaciones.grid(row=9, column=1, padx=10, pady=5)

    # Creación scroll bar vertical del Text
    scrollVertical = Scrollbar(pantallaRegistrarMiembro, orient=VERTICAL, command=txtBox_Publicaciones.yview)
    scrollVertical.grid(row=9, column=2, sticky='nsew')
    txtBox_Publicaciones['yscrollcommand'] = scrollVertical.set

    # Creación scroll bar horizontal del Text
    scrollHorizontal = Scrollbar(pantallaRegistrarMiembro, orient=HORIZONTAL, command=txtBox_Publicaciones.xview)
    scrollHorizontal.grid(row=10, column=1, sticky='nsew')
    txtBox_Publicaciones['xscrollcommand'] = scrollHorizontal.set

    # Cuarta sección
    Label(pantallaRegistrarMiembro, text="Puesto:").grid(row=11, column=0, padx=10, pady=5, sticky="E")
    cb_Puesto = ttk.Combobox(pantallaRegistrarMiembro, state="readonly",
                             values=["Secretaria",
                                     "Asistente administrativa",
                                     "Coordinador",
                                     "Director"])
    cb_Puesto.grid(row=11, column=1, padx=10, pady=5, sticky="W")

    Label(pantallaRegistrarMiembro, text="Extensión:").grid(row=12, column=0, padx=10, pady=5, sticky="E")
    txt_Extension = Entry(pantallaRegistrarMiembro)
    txt_Extension.grid(row=12, column=1, padx=10, pady=5, sticky="W")

    mensajeError = StringVar()
    mensajeError.set("")
    lbl_Errores = Label(pantallaRegistrarMiembro, textvariable=mensajeError, fg="red")
    lbl_Errores.grid(row=13, column=1, padx=10, pady=5)

    # Quinta sección
    btn_RegistrarRM = Button(pantallaRegistrarMiembro, text="Registrar", command=validarDatos)
    btn_RegistrarRM.grid(row=14, column=0, padx=0, pady=0)
    btn_RegistrarRM.config(font="Helvetica")

    btn_LimpiarRM = Button(pantallaRegistrarMiembro, text="Limpiar", command=funcionBtnLimpiarPantallaRM)
    btn_LimpiarRM.grid(row=14, column=1, padx=0, pady=0)
    btn_LimpiarRM.config(font="Helvetica")

    # Este método es para habilitar un valor por defecto en los radio botones
    ver()


def pantallaCargarDatos():
    def funcionBtnCargarDatosConfirmacion():
        mensaje = tk.messagebox.askquestion("Confirmación", "Se cargarán los datos aleatorios. ¿Desea continuar?",
                                            icon="warning")
        if mensaje == 'yes':
            cargaListaPersonas = leer(nomArch)
            nuevaCarga = funcionCargarDatos(txt_Cantidad.get(), cargaListaPersonas)
            grabar(nomArch, nuevaCarga)  # Graba el archivo en memoria secundaria

    def funcionBtnLimpiarPantallaCargarDatos():
        txt_Cantidad.delete(0, len(txt_Cantidad.get()))

    def validarCarga():
        validacionTipoDato = validarTipoDatoCarga(txt_Cantidad.get())
        if validacionTipoDato[0]:
            mensajeError.set(validacionTipoDato[1])
            return ""

        validacionCantidadCarga = validarCantidadCarga(txt_Cantidad.get())
        if validacionCantidadCarga[0]:
            mensajeError.set(validacionCantidadCarga[1])
            return ""

        mensajeError.set("")
        return funcionBtnCargarDatosConfirmacion()

    pantallaCargarDatos = Toplevel(root)
    pantallaCargarDatos.title("Cargar datos")
    pantallaCargarDatos.geometry("350x170")
    pantallaCargarDatos.resizable(False, False)

    Label(pantallaCargarDatos, text="Carga Automática Aleatoria").grid(row=0, column=0, padx=10, pady=5)

    Label(pantallaCargarDatos, text="Cantidad a crear:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
    txt_Cantidad = Entry(pantallaCargarDatos)
    txt_Cantidad.grid(row=1, column=1, padx=10, pady=5, sticky="W")

    btn_Crear = Button(pantallaCargarDatos, text="Cargar", command=validarCarga)
    btn_Crear.grid(row=2, column=0, padx=5, pady=5)
    btn_Crear.config(font="Helvetica")

    btn_Limpiar = Button(pantallaCargarDatos, text="Limpiar", command=funcionBtnLimpiarPantallaCargarDatos)
    btn_Limpiar.grid(row=2, column=1, padx=5, pady=5)
    btn_Limpiar.config(font="Helvetica")

    mensajeError = StringVar()
    mensajeError.set("")
    lbl_Errores = Label(pantallaCargarDatos, textvariable=mensajeError, fg="red")
    lbl_Errores.place(x=125, y=125)


def pantallaRegistrarCandidato():
    pantallaRegistrarCandidato = Toplevel(root)
    pantallaRegistrarCandidato.title("Registrar candidato")
    pantallaRegistrarCandidato.geometry("350x170")
    pantallaRegistrarCandidato.resizable(False, False)

    Label(pantallaRegistrarCandidato, text="Cédula:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
    txt_Cedula = Entry(pantallaRegistrarCandidato)
    txt_Cedula.grid(row=1, column=1, padx=10, pady=5, sticky="W")

    btn_Crear = Button(pantallaRegistrarCandidato, text="Buscar")
    btn_Crear.grid(row=2, column=0, padx=5, pady=5)
    btn_Crear.config(font="Helvetica")

    btn_Limpiar = Button(pantallaRegistrarCandidato, text="Limpiar")
    btn_Limpiar.grid(row=2, column=1, padx=5, pady=5)
    btn_Limpiar.config(font="Helvetica")

    lbl_Errores = Label(pantallaRegistrarCandidato, text="Error :v", fg="red")
    lbl_Errores.place(x=125, y=100)


def pantallaGenerarVotacion():
    pantallaGenerarVotacion = Toplevel(root)
    pantallaGenerarVotacion.title("Generar votación")
    pantallaGenerarVotacion.geometry("275x85")
    pantallaGenerarVotacion.resizable(False, False)

    Label(pantallaGenerarVotacion, text="Indicar año:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
    cb_Anno = ttk.Combobox(pantallaGenerarVotacion, state="readonly",
                           values=["2019",
                                   "2023",
                                   "2027",
                                   "2031"]).grid(row=1, column=1, padx=10, pady=5, sticky="W")

    btn_Elegir = Button(pantallaGenerarVotacion, text="Elegir")
    btn_Elegir.grid(row=2, column=0, padx=5, pady=5)
    btn_Elegir.config(font="Helvetica")

    btn_Regresar = Button(pantallaGenerarVotacion, text="Regresar")
    btn_Regresar.grid(row=2, column=1, padx=5, pady=5)
    btn_Regresar.config(font="Helvetica")


def pantallaReportes():
    pantallaGenerarVotacion = Toplevel(root)
    pantallaGenerarVotacion.title("Reportes")
    pantallaGenerarVotacion.resizable(False, False)

    btn_ListaCandidatos = Button(pantallaGenerarVotacion, text="1. Lista de candidatos.", width=20, height=1)
    btn_ListaCandidatos.grid(row=0, column=1, padx=50, pady=5)
    btn_ListaCandidatos.config(font="Helvetica", fg="#0E9F00")

    btn_CantidadVotantesPorCandidato = Button(pantallaGenerarVotacion, text="2. Cantidad de votantes por candidato.",
                                              width=30, height=1)
    btn_CantidadVotantesPorCandidato.grid(row=1, column=1, padx=50, pady=5)
    btn_CantidadVotantesPorCandidato.config(font="Helvetica", fg="#0E9F00")

    btn_SeguidoresPorCandidato = Button(pantallaGenerarVotacion, text="3. Seguidores por candidato.", width=23,
                                        height=1)
    btn_SeguidoresPorCandidato.grid(row=2, column=1, padx=50, pady=5)
    btn_SeguidoresPorCandidato.config(font="Helvetica", fg="#0E9F00")

    btn_VotantesPorRol = Button(pantallaGenerarVotacion, text="4. Votantes por rol.", width=20, height=1)
    btn_VotantesPorRol.grid(row=3, column=1, padx=50, pady=5)
    btn_VotantesPorRol.config(font="Helvetica", fg="#0E9F00")

    btn_ListaNoVotantes = Button(pantallaGenerarVotacion, text="5. Lista de no votantes.", width=20, height=1)
    btn_ListaNoVotantes.grid(row=4, column=1, padx=50, pady=5)
    btn_ListaNoVotantes.config(font="Helvetica", fg="#0E9F00")

    btn_EstudiantesPorCarrera = Button(pantallaGenerarVotacion, text="6. Estudiantes por carrera.", width=21, height=1)
    btn_EstudiantesPorCarrera.grid(row=5, column=1, padx=50, pady=5)
    btn_EstudiantesPorCarrera.config(font="Helvetica", fg="#0E9F00")

    btn_PadronPorRol = Button(pantallaGenerarVotacion, text="7. Padrón por rol.", width=20, height=1)
    btn_PadronPorRol.grid(row=6, column=1, padx=50, pady=5)
    btn_PadronPorRol.config(font="Helvetica", fg="#0E9F00")

    btn_VotantesDeCandidato = Button(pantallaGenerarVotacion, text="8. Votantes de candidato.", width=21, height=1)
    btn_VotantesDeCandidato.grid(row=7, column=1, padx=50, pady=5)
    btn_VotantesDeCandidato.config(font="Helvetica", fg="#0E9F00")

    btn_CargaAutomatica = Button(pantallaGenerarVotacion, text="9. Carga automática.", width=20, height=1)
    btn_CargaAutomatica.grid(row=8, column=1, padx=50, pady=5)
    btn_CargaAutomatica.config(font="Helvetica", fg="#0E9F00")


# Definición de la ventana principal
root = Tk()
root.title("Elecciones")
root.resizable(False, False)

# Definición del frame
frame = Frame(root, bg="black")
frame.pack()

# Definición de los botones

btn_RegistrarMiembro = Button(frame, text="Registrar miembro", command=pantallaRegistrarMiembro, width=20, height=1)
btn_RegistrarMiembro.grid(row=0, column=1, padx=50, pady=5)
btn_RegistrarMiembro.config(font="Helvetica", fg="#0E9F00")

btn_CargarDatos = Button(frame, text="Cargar datos", command=pantallaCargarDatos, width=20, height=1)
btn_CargarDatos.grid(row=1, column=1, padx=50, pady=5)
btn_CargarDatos.config(font="Helvetica", fg="#0E9F00")

btn_RegistrarCandidatos = Button(frame, command=pantallaRegistrarCandidato, text="Registrar candidatos", width=20,
                                 height=1)
btn_RegistrarCandidatos.grid(row=2, column=1, padx=50, pady=5)
btn_RegistrarCandidatos.config(font="Helvetica", fg="#0E9F00")

btn_GenerarVotacion = Button(frame, text="Generar votación", command=pantallaGenerarVotacion, width=20, height=1)
btn_GenerarVotacion.grid(row=3, column=1, padx=50, pady=5)
btn_GenerarVotacion.config(font="Helvetica", fg="#0E9F00")

btn_Reportes = Button(frame, text="Reportes", command=pantallaReportes, width=20, height=1)
btn_Reportes.grid(row=4, column=1, padx=50, pady=5)
btn_Reportes.config(font="Helvetica", fg="#0E9F00")

leer(nomArch) #Leer el backUp

root.mainloop()
