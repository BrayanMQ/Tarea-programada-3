from funcionesHTML import *
import random
import re

def validacionCedulaExistente(cedula, listaPersonas):
    """
    Función: validacionCedulaExistente (valida si la cédula recibida ya se encuentra registrada)
    Entradas: cedula (int), listaPersonas (list)
    Salidas: tupla (booleana en el primer campo, string en el segundo)
    """
    for pCedula in listaPersonas:
        pCedula = pCedula.getCedula()
        if pCedula == cedula:
            return True, "La cédula ya se encuentra \nregistrada."
    return False, ""


def validarTelefono(telefono):
    """
    Función: validarTelefono (valida si el teléfono es del tipo de dato requerido)
    Entradas: telefono (str)
    Salidas: tupla (booleana en el primer campo, string en el segundo)
    """
    if re.match("(0){1}", telefono):
        return True, "El primer dígito del teléfono \nno debe ser 0."

    if not re.match("^\d{8}$", telefono):
        return True, "El teléfono debe solamente debe \ncontener 8 dígitos."

    return False, ""


def validarExtension(extension):
    """
    Función: validarExtension (valida si la extensión es del tipo de dato requerido)
    Entradas: extension (str)
    Salidas: tupla (booleana en el primer campo, string en el segundo)
    """
    if re.match("(0){1}", extension):
        return True, "El primer dígito de la \nextensión no debe ser 0."

    if not re.match("^\d{4}$", extension):
        return True, "La extensión debe solamente debe \ncontener 4 dígitos."

    return False, ""


def validarCarnet(carnet):
    """
    Función: validarCarnet (valida si el carnet es del tipo de dato requerido)
    Entradas: carnet (str)
    Salidas: tupla (booleana en el primer campo, string en el segundo)
    """
    if re.match("(0){1}", carnet):
        return True, "El primer dígito del carnet \nno debe ser 0."

    if not re.match("^\d{10}$", carnet):
        return True, "El carnet debe solamente debe \ncontener 10 dígitos."

    return False, ""


def validarCedula(cedula):
    """
    Función: validarCedula (valida si la cédula es del tipo de dato requerido)
    Entradas: cedula (str)
    Salidas: tupla (booleana en el primer campo, string en el segundo)
    """
    if not re.match("[1-7]{1}", cedula):
        return True, "El primer dígito de la cédula \ndebe ser entre 1-7."

    if not re.match("^\d{9}$", cedula):
        return True, "La cédula debe contener 9 dígitos."

    return False, ""


def validarTipoDatoCarga(cantidad):
    """
    Función: validarTipoDatoCarga (valida si la cantidad a cargar es del tipo de dato requerido)
    Entradas: cantidad (str)
    Salidas: tupla (booleana en el primer campo, string en el segundo)
    """
    try:
        cantidad = int(cantidad)
        return False, ""
    except:
        return True, "Debe introducir un \nvalor numérico."


def validarCantidadCarga(cantidad):
    """
    Función: validarCantidadCarga (valida si la cantidad a cargar se encuentra dentro del rango disponible)
    Entradas: cantidad (str)
    Salidas: tupla (booleana en el primer campo, string en el segundo)
    """
    cantidad = int(cantidad)
    if cantidad > 0 and cantidad <= 100:
        return False, ""
    return True, "Debe introducir un número \nentre 1 y 100."


def votacionGenerada(listaPersonas):
    """
    Función: votacionGenerada (revisa si la votación ya ha sido generada)
    Entradas: listaPersonas (list)
    Salidas: booleana (True o False)
    """
    for persona in listaPersonas:
        if persona.getVoto() != 0:
            return True
    return False


def candidatoGanador(listaPersonas):
    """
    Función: candidatoGanador (revisa cuál de los candidatos fue el ganador y cuánto el porcentaje de votos)
    Entradas: listaPersonas (list)
    Salidas: tupla (string en el primer campo, flotante en el segundo)
    """
    votos = contarVotos(listaPersonas)
    votoMayor = 0
    i = 0
    for candidato in votos:
        if candidato > votoMayor:
            votoMayor = candidato
            i += 1

    listaCandidatos = funcionCantidadCandidatos(listaPersonas)
    nombreGanador = listaCandidatos[i - 1]
    nombreCompleto = nombreGanador.getNombreCompleto()
    porcentaje = (votos[i - 1] * 100) / len(listaPersonas)

    return nombreCompleto, porcentaje


def crearEstudiante(carnet, carrera):
    """
    Función: crearEstudiante (genera un objeto de la clase Estudiante)
    Entradas: carnet (str), cedula (str)
    Salidas: objeto (estudiante)
    """
    estudiante = Estudiante()
    estudiante.setCarnet(carnet)
    estudiante.setCarrera(carrera)
    return estudiante


def crearProfesor(publicaciones, candidato=""):
    """
    Función: crearProfesor (genera un objeto de la clase Profesor)
    Entradas: publicaciones (str), candidato (str)
    Salidas: objeto (profesor)
    """
    profesor = Profesor()
    profesor.setPublicaciones(publicaciones)
    profesor.setCandidato(candidato)
    return profesor


def crearAdministrativo(puesto, extension):
    """
    Función: crearAdministrativo (genera un objeto de la clase Administrativo)
    Entradas: puesto (str), extension (str)
    Salidas: objeto (administrativo)
    """
    administrativo = Administrativo()
    administrativo.setPuesto(puesto)
    administrativo.setExtension(extension)
    return administrativo


def crearPersona(persona, cedula, nombre, telefono):
    """
    Función: crearPersona (genera un objeto de la clase Persona, con algunos de sus atributos)
    Entradas: persona (objeto), cedula (int), nombre (str), telefono (int)
    Salidas: objeto (persona)
    """
    persona.setCedula(int(cedula))
    persona.setNombreCompleto(nombre)
    persona.setTelefono(telefono)
    return persona


def funcionRegitrarMiembro(cedula, nombre, telefono, tipo,
                           carnet, publicaciones, extension, carrera, puesto):
    """
    Función: funcionRegitrarMiembro (prepara un objeto de la clase Persona, según su tipo, para poder ser registrado)
    Entradas: cedula (int), nombre (str), telefono (int), tipo (str), carnet (str), publicaciones (str),
              extension (str), carrera (str), puesto (str)
    Salidas: objeto (persona)
    """
    if tipo == 1:
        persona = crearEstudiante(int(carnet), carrera)
    elif tipo == 2:
        persona = crearProfesor(publicaciones)
    else:
        persona = crearAdministrativo(puesto, extension)

    persona = crearPersona(persona, cedula, nombre, telefono)

    return persona


def obtenerCedula(listaPersonas):
    """
    Función: obtenerCedula (genera cédulas aleatorias para realizar la carga de datos)
    Entradas: listaPersonas (list)
    Salidas: cedula (int)
    """
    cedula = random.randint(100000000, 799999999)
    if validacionCedulaExistente(cedula, listaPersonas)[0]:
        while validacionCedulaExistente(cedula, listaPersonas)[0]:
            cedula = random.randint(100000000, 799999999)
    return cedula


def obtenerContador(listaPersonasCarga):
    """
    Función: obtenerContador (obtiene el contador de la última perspna generada por el sistema, para continuar la secuencia)
    Entradas: listaPersonasCarga (list)
    Salidas: nuevoContador (int)
    """
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
    """
    Función: funcionCargarDatos (genera objetos de la clase Persona de tipo y atributos aleatorios, de acuerdo a
                                 una cantidad)
    Entradas: cantidadACargar (str), listaPersonasCarga (list)
    Salidas: listaPersonasCarga (list) - actualizada
    """
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
    """
    Función: funcionCantidadCandidatos (obtiene la lista de las personas que han sido registradas como candidatos)
    Entradas: listaPersonas (list)
    Salidas: listaCandidatos (list)
    """
    listaCandidatos = []
    for persona in listaPersonas:
        if persona.getTipo() == "profesor":
            if not persona.getCandidato() == "":
                listaCandidatos.append(persona)
    return listaCandidatos


def funcionObtenerEstudiantes(listaPersonas):
    """
    Función: funcionObtenerEstudiantes (obtiene la lista de las personas que son de tipo estudiante)
    Entradas: listaPersonas (list)
    Salidas: listaEstudiantes (list)
    """
    listaEstudiantes = []
    for persona in listaPersonas:
        if persona.getTipo() == "estudiante":
            listaEstudiantes.append(persona)
    return listaEstudiantes


def funcionGenerarVotacion(listaPersonas):
    """
    Función: funcionGenerarVotacion (genera selecciones aleatorias de uno de los candidatos registrados, de acuerdo a
                                     la cantidad)
    Entradas: listaPersonas (list)
    Salidas: listaPersonas (list) - actualizada
    """
    cntCandidatos = funcionCantidadCandidatos(listaPersonas)
    for persona in listaPersonas:
        voto = random.randint(0, len(cntCandidatos))
        persona.setVoto(voto)
    return listaPersonas


def contarVotos(listaPersonas):
    """
    Función: contarVotos (cuenta la cantidad de votos correspondientes a cada candidato y los guarda en una lista)
    Entradas: listaPersonas (list)
    Salidas: listaVotos (list)
    """
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
    """
    Función: contarVotosPorRol (cuenta la cantidad de votos que corresponden a los candidatos, de acuerdo a los roles de
                                las personas)
    Entradas: listaPersonas (list), rol (str)
    Salidas: listaVotos (list)
    """
    listaVotos = [0, 0, 0, 0]

    for i in range(1, 5):  # i representa el candidato
        for persona in listaPersonas:
            if persona.getVoto() == i and persona.getTipo() == rol:
                listaVotos[i - 1] += 1
    return listaVotos


def obtenerRol(rol):
    """
    Función: obtenerRol (realiza una modificación con respecto a cómo viene dado el rol)
    Entradas: rol (str)
    Salidas: rol (str) - actualizado
    """
    if rol == "Estudiantes":
        rol = "estudiante"

    elif rol == "Profesores":
        rol = "profesor"

    elif rol == "Administrativos":
        rol = "administrativo"

    return rol


def funcionHTMLListaCandidatos(listaPersonas):
    """
    Función: funcionHTMLListaCandidatos (obtiene la lista de candidatos y envía a realizar reporte de lista de candidatos)
    Entradas: listaPersonas (list)
    Salidas: crearReporteListaCandidatos (función (con entrada candidatos (list)))
    """
    candidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteListaCandidatos(candidatos)


def funcionHTMLVotantesPorRol(listaPersonas):
    """
    Función: funcionHTMLVotantesPorRol (obtiene la lista de candidatos y envía a realizar reporte de votantes por rol)
    Entradas: listaPersonas (list)
    Salidas: crearReporteVotantesPorRol (función (con entradas candidatos (list) y listaPersonas (list)))
    """
    candidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteVotantesPorRol(candidatos, listaPersonas)


def funcionHTMLEstudiantesPorCarrera(listaPersonas):
    """
    Función: funcionHTMLEstudiantesPorCarrera (obtiene la lista de estudiantes y envía a realizar reporte de estudiantes
                                               por carrera)
    Entradas: listaPersonas (list)
    Salidas: crearReporteEstudiantesPorCarrera (función (con entrada estudiantes (list)))
    """
    estudiantes = funcionObtenerEstudiantes(listaPersonas)
    return crearReporteEstudiantesPorCarrera(estudiantes)


def funcionHTMLSeguidoresPorCandidato(listaPersonas):
    """
    Función: funcionHTMLSeguidoresPorCandidato (obtiene la lista de candidatos y envía a realizar reporte de
                                                seguidores por candidato)
    Entradas: listaPersonas (list)
    Salidas: crearReporteSeguidoresPorCandidato (función (con entradas listaPersonas (list) y listaCandidatos (list)))
    """
    listaCandidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteSeguidoresPorCandidato(listaPersonas, listaCandidatos)


def obtenerNoVotantes(listaPersonas):
    """
    Función: obtenerNoVotantes (obtiene la lista de personas que no votaron)
    Entradas: listaPersonas (list)
    Salidas: listaNoVotante (list)
    """
    listaNoVotante = []
    for persona in listaPersonas:
        if persona.getVoto() == 0:
            listaNoVotante.append(persona)
    return listaNoVotante


def funcionHTMLListaNoVotantes(listaPersonas):
    """
    Función: funcionHTMLListaNoVotantes (obtiene la lista de no votantes y su porcentaje, y envía a realizar reporte de
                                         lista de no votantes)
    Entradas: listaPersonas (list)
    Salidas: crearReporteListaNoVotantes (función (con entradas noVotantes (list) y porcentaje (float)))
    """
    noVotantes = obtenerNoVotantes(listaPersonas)
    porcentaje = (len(noVotantes) * 100) / len(listaPersonas)
    return crearReporteListaNoVotantes(noVotantes, porcentaje)


def funcionHTMLListaVotantesCandidato(candidatoBuscar, listaPersonas, posicion):
    """
    Función: funcionHTMLListaVotantesCandidato (obtiene la lista votantes por cadidato, y la cantidad de estos por cada rol)
    Entradas: candidatoBuscar (str), listaPersonas (list), posicion (int)
    Salidas: crearReporteListaVotantesCandidato (función (con entradas listaVotantes (list), candidatoBuscar (str),
                                                 cntEstudiantes (int), cntProfesores (int) y cntAdministrativos (int)))
    """
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
    """
    Función: funcionHTMLListaCantidadVotantesPorCandidato (obtiene la lista de candidatos, la cantidad y el porcentaje de
                                                           votos para cada uno, y envía a realizar reporte de votantes por
                                                           candidato)
    Entradas: listaPersonas (list)
    Salidas: crearReporteListaCantidadVotantesCandidatos (función (con entradas listaCandidatos (list), listaCantidadVotos
                                                         (list) y listaPorcentajes (list)))
    """
    listaCandidatos = funcionCantidadCandidatos(listaPersonas)
    listaCantidadVotos = contarVotos(listaPersonas)
    listaPorcentajes = []

    for i in range(len(listaCandidatos)):
        listaPorcentajes.append((listaCantidadVotos[i] * 100) / (len(listaPersonas)))

    return crearReporteListaCantidadVotantesCandidatos(listaCandidatos, listaCantidadVotos, listaPorcentajes)


def funcionHTMLCargaAutomatica(listaPersonas):
    """
    Función: funcionHTMLCargaAutomatica (envía a realizar reporte de carga automática)
    Entradas: listaPersonas (list)
    Salidas: crearReporteCargaAutomatica (función (con entrada listaPersonas (list))
    """
    return crearReporteCargaAutomatica(listaPersonas)
