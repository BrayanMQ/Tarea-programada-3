from tkinter import *
from tkinter import ttk


def pantallaRegistrarMiembro():
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

    Radiobutton(pantallaRegistrarMiembro, variable=rb_variable, value=1).grid(row=3, column=0, padx=10, pady=5,
                                                                              sticky="W")
    Label(pantallaRegistrarMiembro, text="Estudiante").grid(row=3, column=0, padx=10, pady=5, sticky="E")

    Radiobutton(pantallaRegistrarMiembro, variable=rb_variable, value=2).grid(row=4, column=0, padx=10, pady=5,
                                                                              sticky="W")
    Label(pantallaRegistrarMiembro, text="Profesor").grid(row=4, column=0, padx=10, pady=5, sticky="E")

    Radiobutton(pantallaRegistrarMiembro, variable=rb_variable, value=3).grid(row=5, column=0, padx=10, pady=5,
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
                                      "CA-Ingeniería en Computadoras"]).grid(row=8, column=1, padx=10, pady=5,
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
                             values=["Asistente administrativa",
                                     "Coordinador",
                                     "Director"]).grid(row=11, column=1, padx=10, pady=5, sticky="W")

    Label(pantallaRegistrarMiembro, text="Extensión:").grid(row=12, column=0, padx=10, pady=5, sticky="E")
    txt_Extension = Entry(pantallaRegistrarMiembro)
    txt_Extension.grid(row=12, column=1, padx=10, pady=5, sticky="W")

    lbl_Errores = Label(pantallaRegistrarMiembro, text="Errores xd", fg="red").grid(row=13, column=0, padx=10, pady=5)


def pantallaCargarDatos():
    pantallaCargarDatos = Toplevel(root)
    pantallaCargarDatos.title("Cargar datos")
    pantallaCargarDatos.geometry("350x170")
    pantallaCargarDatos.resizable(False, False)

    Label(pantallaCargarDatos, text="Carga Automática Aleatoria").grid(row=0, column=0, padx=10, pady=5)

    Label(pantallaCargarDatos, text="Cantidad a crear:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
    txt_Cantidad = Entry(pantallaCargarDatos)
    txt_Cantidad.grid(row=1, column=1, padx=10, pady=5, sticky="W")

    btn_Crear = Button(pantallaCargarDatos, text="Cargar")
    btn_Crear.grid(row=2, column=0, padx=5, pady=5)
    btn_Crear.config(font="Helvetica")

    btn_Limpiar = Button(pantallaCargarDatos, text="Limpiar")
    btn_Limpiar.grid(row=2, column=1, padx=5, pady=5)
    btn_Limpiar.config(font="Helvetica")

    lbl_Errores = Label(pantallaCargarDatos, text="Error :v", fg="red")
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
    pantallaGenerarVotacion.title("Generar votación")
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

root.mainloop()
