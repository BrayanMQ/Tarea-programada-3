from funcionesHTML import *
import random


def validarCamposVacios(nombre, tipo, carrera):
    if nombre == "" == "":
        return True
    if tipo == 1:
        if carrera == "":
            return True
    return False


def validacionCedulaExistente(cedula, listaPersonas):
    for pCedula in listaPersonas:
        pCedula = pCedula.getCedula()
        if pCedula == cedula:
            return True, "La cédula ya se encuentra \nregistrada."
    return False, ""


def validarTelefono(telefono):
    try:
        telefono = int(telefono)
        return False, ""
    except:
        return True, "El telefono solamente debe \ncontener dígitos."


def validarLargoTelefono(telefono):
    if len(telefono) == 8:
        return False, ""
    return True, "El telefono debe ser de \n8 dígitos."


def validarExtension(extension):
    try:
        extension = int(extension)
        return False, ""
    except:
        return True, "La extension solamente \ndebe contener dígitos."


def validarLargoExtension(extension):
    if len(extension) == 4:
        return False, ""
    return True, "La extension debe ser \nde 4 dígitos."


def validarCarnet(carnet):
    try:
        carnet = int(carnet)
        return False, ""
    except:
        return True, "El carnet solamente debe \ncontener dígitos."


def validarLargoCarnet(carnet):
    if len(carnet) == 10:
        return False, ""
    return True, "El carnet debe ser de \n10 dígitos."


def validarCedula(cedula):
    try:
        cedula = int(cedula)
        return False, ""
    except:
        return True, "La cédula solamente debe \ncontener dígitos."


def validarLargoCedula(cedula):
    if len(cedula) == 9:
        return False, ""
    return True, "La cédula debe ser de \n9 dígitos."


def validarTipoDatoCarga(cantidad):
    try:
        cantidad = int(cantidad)
        return False, ""
    except:
        return True, "Debe introducir un \nvalor numérico."


def validarCantidadCarga(cantidad):
    cantidad = int(cantidad)
    if cantidad > 0 and cantidad <= 100:
        return False, ""
    return True, "Debe introducir un número \nentre 1 y 100."


def votacionGenerada(listaPersonas):
    for persona in listaPersonas:
        if persona.getVoto() != 0:
            return True
    return False


def candidatoGanador(listaPersonas):
    votos = contarVotos(listaPersonas)
    votoMayor = 0
    i = 0
    for candidato in votos:
        if candidato > votoMayor:
            votoMayor = candidato
            i += 1

    listaCandidatos = funcionCantidadCandidatos(listaPersonas)
    nombreGanador = listaCandidatos[i-1]
    nombreCompleto = nombreGanador.getNombreCompleto()
    porcentaje = (votos[i-1] * 100) / len(listaPersonas)

    return nombreCompleto, porcentaje

def crearEstudiante(carnet, carrera):
    estudiante = Estudiante()
    estudiante.setCarnet(carnet)
    estudiante.setCarrera(carrera)
    return estudiante


def crearProfesor(publicaciones, candidato=""):
    profesor = Profesor()
    profesor.setPublicaciones(publicaciones)
    profesor.setCandidato(candidato)
    return profesor


def crearAdministrativo(puesto, extension):
    administrativo = Administrativo()
    administrativo.setPuesto(puesto)
    administrativo.setExtension(extension)
    return administrativo


def crearPersona(persona, cedula, nombre, telefono):
    persona.setCedula(int(cedula))
    persona.setNombreCompleto(nombre)
    persona.setTelefono(telefono)
    return persona


def funcionRegitrarMiembro(cedula, nombre, telefono, tipo,
                           carnet, publicaciones, extension, carrera, puesto):
    if tipo == 1:
        persona = crearEstudiante(int(carnet), carrera)
    elif tipo == 2:
        persona = crearProfesor(publicaciones)
    else:
        persona = crearAdministrativo(puesto, extension)

    persona = crearPersona(persona, cedula, nombre, telefono)

    return persona


def obtenerCedula(listaPersonas):
    cedula = random.randint(100000000, 799999999)
    if validacionCedulaExistente(cedula, listaPersonas)[0]:
        while validacionCedulaExistente(cedula, listaPersonas)[0]:
            cedula = random.randint(100000000, 799999999)
    return cedula


def obtenerContador(listaPersonasCarga):
    if listaPersonasCarga == []:
        nuevoContador = 1
    else:
        listaSecuencia = []
        for persona in listaPersonasCarga:
            numero = persona.getNombreCompleto().split()
            if numero[-1].isdigit():
                listaSecuencia += [int(numero[-1])]

        if listaSecuencia != []:
            contadorActual = max(listaSecuencia)
            nuevoContador = contadorActual + 1
        else:
            nuevoContador = 1

    return nuevoContador


def funcionCargarDatos(cantidadACargar, listaPersonasCarga):
    contador = obtenerContador(listaPersonasCarga)
    tipos = [1, 2, 3]

    for i in range(contador, int(cantidadACargar) + contador):
        cedula = obtenerCedula(listaPersonasCarga)
        nombreCompleto = ""
        telefono = random.randint(85000000, 89999999)
        tipoPersona = random.choice(tipos)
        carnet = ""
        publicacion = ""
        extension = ""
        carrera = ""
        puesto = ""

        if tipoPersona == 1:
            nombreCompleto = "Nombre Número " + str(i)
            carreras = ["IC-Ingeniería en Computación", "ATI-Administración de la Información", "E-Electrónica",
                        "AE-Administración de Empresas", "CA-Ingeniería en Computadoras"]
            carrera = random.choice(carreras)
            carnet = random.randint(2019000000, 2019999999)

        elif tipoPersona == 2:
            nombreCompleto = "Nombre Número " + str(i)
            publicacion = "Publicación Número " + str(i)

        else:
            nombreCompleto = "Nombre Número " + str(i)
            puestos = ["Secretaria", "Asistente administrativa", "Coordinador", "Director"]
            puesto = random.choice(puestos)
            extension = random.randint(1000, 9999)

        persona = funcionRegitrarMiembro(cedula, nombreCompleto, telefono, tipoPersona,
                                         carnet, publicacion, extension, carrera, puesto)
        listaPersonasCarga += [persona]
    return listaPersonasCarga


def funcionCantidadCandidatos(listaPersonas):
    listaCandidatos = []
    for persona in listaPersonas:
        if persona.getTipo() == "profesor":
            if not persona.getCandidato() == "":
                listaCandidatos.append(persona)
    return listaCandidatos


def funcionObtenerEstudiantes(listaPersonas):
    listaEstudiantes = []
    for persona in listaPersonas:
        if persona.getTipo() == "estudiante":
            listaEstudiantes.append(persona)
    return listaEstudiantes


def funcionGenerarVotacion(listaPersonas):
    cntCandidatos = funcionCantidadCandidatos(listaPersonas)
    for persona in listaPersonas:
        voto = random.randint(0, len(cntCandidatos))
        persona.setVoto(voto)
    return listaPersonas


def contarVotos(listaPersonas):
    listaVotos = [0, 0, 0, 0]
    for persona in listaPersonas:
        if persona.getVoto() == 1:
            listaVotos[0] += 1
        elif persona.getVoto() == 2:
            listaVotos[1] += 1
        elif persona.getVoto() == 3:
            listaVotos[2] += 1
        elif persona.getVoto() == 4:
            listaVotos[3] += 1
    return listaVotos


def contarVotosPorRol(listaPersonas, rol):
    listaVotos = [0, 0, 0, 0]

    for i in range(1, 5):  # i representa el candidato
        for persona in listaPersonas:
            if persona.getVoto() == i and persona.getTipo() == rol:
                listaVotos[i - 1] += 1
    return listaVotos


def obtenerRol(rol):
    if rol == "Estudiantes":
        rol = "estudiante"

    elif rol == "Profesores":
        rol = "profesor"

    elif rol == "Administrativos":
        rol = "administrativo"

    return rol


def funcionHTMLListaCandidatos(listaPersonas):
    candidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteListaCandidatos(candidatos)


def funcionHTMLVotantesPorRol(listaPersonas):
    candidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteVotantesPorRol(candidatos, listaPersonas)


def funcionHTMLEstudiantesPorCarrera(listaPersonas):
    estudiantes = funcionObtenerEstudiantes(listaPersonas)
    return crearReporteEstudiantesPorCarrera(estudiantes)


def funcionHTMLSeguidoresPorCandidato(listaPersonas):
    listaCandidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteSeguidoresPorCandidato(listaPersonas, listaCandidatos)


def obtenerNoVotantes(listaPersonas):
    listaNoVotante = []
    for persona in listaPersonas:
        if persona.getVoto() == 0:
            listaNoVotante.append(persona)
    return listaNoVotante


def funcionHTMLListaNoVotantes(listaPersonas):
    noVotantes = obtenerNoVotantes(listaPersonas)
    porcentaje = (len(noVotantes) * 100) / len(listaPersonas)
    return crearReporteListaNoVotantes(noVotantes, porcentaje)


def funcionHTMLListaVotantesCandidato(candidatoBuscar, listaPersonas, posicion):
    listaVotantes = []
    cntEstudiantes = 0
    cntProfesores = 0
    cntAdministrativos = 0
    for persona in listaPersonas:
        if persona.getVoto() == posicion + 1:
            listaVotantes.append(persona)
            if persona.getTipo() == "estudiante":
                cntEstudiantes += 1
            elif persona.getTipo() == "profesor":
                cntProfesores += 1
            else:
                cntAdministrativos += 1
    return crearReporteListaVotantesCandidato(listaVotantes, candidatoBuscar, cntEstudiantes, cntProfesores,
                                              cntAdministrativos)


def funcionHTMLListaCantidadVotantesPorCandidato(listaPersonas):
    listaCandidatos = funcionCantidadCandidatos(listaPersonas)
    listaCantidadVotos = contarVotos(listaPersonas)
    listaPorcentajes = []

    for i in range(len(listaCandidatos)):
        listaPorcentajes.append((listaCantidadVotos[i] * 100) / (len(listaPersonas)))

    return crearReporteListaCantidadVotantesCandidatos(listaCandidatos, listaCantidadVotos, listaPorcentajes)


def funcionHTMLCargaAutomatica(listaPersonas):
    return crearReporteCargaAutomatica(listaPersonas)
