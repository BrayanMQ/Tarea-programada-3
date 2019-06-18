from funcionesHTML import *
import random

"""
Función: validarCamposVacios (valida si los campos de información vienen vacíos)
Entradas: nombre (str), tipo (int), carrera (str)
Salidas: booleanas (True o False)
"""
def validarCamposVacios(nombre, tipo, carrera):
    if nombre == "" == "":
        return True
    if tipo == 1:
        if carrera == "":
            return True
    return False


"""
Función: validacionCedulaExistente (valida si la cédula recibida ya se encuentra registrada)
Entradas: cedula (int), listaPersonas (list)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validacionCedulaExistente(cedula, listaPersonas):
    for pCedula in listaPersonas:
        pCedula = pCedula.getCedula()
        if pCedula == cedula:
            return True, "La cédula ya se encuentra \nregistrada."
    return False, ""


"""
Función: validarTelefono (valida si el teléfono es del tipo de dato requerido)
Entradas: telefono (str)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validarTelefono(telefono):
    try:
        telefono = int(telefono)
        return False, ""
    except:
        return True, "El telefono solamente debe \ncontener dígitos."


"""
Función: validarLargoTelefono (valida si el teléfono es del tamaño requerido)
Entradas: telefono (str)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validarLargoTelefono(telefono):
    if len(telefono) == 8:
        return False, ""
    return True, "El telefono debe ser de \n8 dígitos."



def validarExtension(extension):
    """
    Función: validarExtension (valida si la extensión es del tipo de dato requerido)
    Entradas: extension (str)
    Salidas: tupla (booleana en el primer campo, string en el segundo)
    """
    try:
        extension = int(extension)
        return False, ""
    except:
        return True, "La extension solamente \ndebe contener dígitos."


"""
Función: validarLargoExtension (valida si la extensión es del tamaño requerido)
Entradas: extension (str)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validarLargoExtension(extension):
    if len(extension) == 4:
        return False, ""
    return True, "La extension debe ser \nde 4 dígitos."


"""
Función: validarCarnet (valida si el carnet es del tipo de dato requerido)
Entradas: carnet (str)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validarCarnet(carnet):
    try:
        carnet = int(carnet)
        return False, ""
    except:
        return True, "El carnet solamente debe \ncontener dígitos."


"""
Función: validarLargoCarnet (valida si el carnet es del tamaño requerido)
Entradas: carnet (str)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validarLargoCarnet(carnet):
    if len(carnet) == 10:
        return False, ""
    return True, "El carnet debe ser de \n10 dígitos."


"""
Función: validarCedula (valida si la cédula es del tipo de dato requerido)
Entradas: cedula (str)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validarCedula(cedula):
    try:
        cedula = int(cedula)
        return False, ""
    except:
        return True, "La cédula solamente debe \ncontener dígitos."


"""
Función: validarLargoCedula (valida si la cédula es del tamaño requerido)
Entradas: cedula (str)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validarLargoCedula(cedula):
    if len(cedula) == 9:
        return False, ""
    return True, "La cédula debe ser de \n9 dígitos."


"""
Función: validarTipoDatoCarga (valida si la cantidad a cargar es del tipo de dato requerido)
Entradas: cantidad (str)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validarTipoDatoCarga(cantidad):
    try:
        cantidad = int(cantidad)
        return False, ""
    except:
        return True, "Debe introducir un \nvalor numérico."


"""
Función: validarCantidadCarga (valida si la cantidad a cargar se encuentra dentro del rango disponible)
Entradas: cantidad (str)
Salidas: tupla (booleana en el primer campo, string en el segundo)
"""
def validarCantidadCarga(cantidad):
    cantidad = int(cantidad)
    if cantidad > 0 and cantidad <= 100:
        return False, ""
    return True, "Debe introducir un número \nentre 1 y 100."


"""
Función: votacionGenerada (revisa si la votación ya ha sido generada)
Entradas: listaPersonas (list)
Salidas: booleana (True o False)
"""
def votacionGenerada(listaPersonas):
    for persona in listaPersonas:
        if persona.getVoto() != 0:
            return True
    return False


"""
Función: candidatoGanador (revisa cuál de los candidatos fue el ganador y cuánto el porcentaje de votos)
Entradas: listaPersonas (list)
Salidas: tupla (string en el primer campo, flotante en el segundo)
"""
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

"""
Función: crearEstudiante (genera un objeto de la clase Estudiante)
Entradas: carnet (str), cedula (str)
Salidas: objeto (estudiante)
"""
def crearEstudiante(carnet, carrera):
    estudiante = Estudiante()
    estudiante.setCarnet(carnet)
    estudiante.setCarrera(carrera)
    return estudiante


"""
Función: crearProfesor (genera un objeto de la clase Profesor)
Entradas: publicaciones (str), candidato (str)
Salidas: objeto (profesor)
"""
def crearProfesor(publicaciones, candidato=""):
    profesor = Profesor()
    profesor.setPublicaciones(publicaciones)
    profesor.setCandidato(candidato)
    return profesor


"""
Función: crearAdministrativo (genera un objeto de la clase Administrativo)
Entradas: puesto (str), extension (str)
Salidas: objeto (administrativo)
"""
def crearAdministrativo(puesto, extension):
    administrativo = Administrativo()
    administrativo.setPuesto(puesto)
    administrativo.setExtension(extension)
    return administrativo


"""
Función: crearPersona (genera un objeto de la clase Persona, con algunos de sus atributos)
Entradas: persona (objeto), cedula (int), nombre (str), telefono (int)
Salidas: objeto (persona)
"""
def crearPersona(persona, cedula, nombre, telefono):
    persona.setCedula(int(cedula))
    persona.setNombreCompleto(nombre)
    persona.setTelefono(telefono)
    return persona


"""
Función: funcionRegitrarMiembro (prepara un objeto de la clase Persona, según su tipo, para poder ser registrado)
Entradas: cedula (int), nombre (str), telefono (int), tipo (str), carnet (str), publicaciones (str),
          extension (str), carrera (str), puesto (str)
Salidas: objeto (persona)
"""
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


"""
Función: obtenerCedula (genera cédulas aleatorias para realizar la carga de datos)
Entradas: listaPersonas (list)
Salidas: cedula (int)
"""
def obtenerCedula(listaPersonas):
    cedula = random.randint(100000000, 799999999)
    if validacionCedulaExistente(cedula, listaPersonas)[0]:
        while validacionCedulaExistente(cedula, listaPersonas)[0]:
            cedula = random.randint(100000000, 799999999)
    return cedula


"""
Función: obtenerContador (obtiene el contador de la última perspna generada por el sistema, para continuar la secuencia)
Entradas: listaPersonasCarga (list)
Salidas: nuevoContador (int)
"""
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


"""
Función: funcionCargarDatos (genera objetos de la clase Persona de tipo y atributos aleatorios, de acuerdo a 
                             una cantidad)
Entradas: cantidadACargar (str), listaPersonasCarga (list)
Salidas: listaPersonasCarga (list) - actualizada
"""
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


"""
Función: funcionCantidadCandidatos (obtiene la lista de las personas que han sido registradas como candidatos)
Entradas: listaPersonas (list)
Salidas: listaCandidatos (list)
"""
def funcionCantidadCandidatos(listaPersonas):
    listaCandidatos = []
    for persona in listaPersonas:
        if persona.getTipo() == "profesor":
            if not persona.getCandidato() == "":
                listaCandidatos.append(persona)
    return listaCandidatos


"""
Función: funcionObtenerEstudiantes (obtiene la lista de las personas que son de tipo estudiante)
Entradas: listaPersonas (list)
Salidas: listaEstudiantes (list)
"""
def funcionObtenerEstudiantes(listaPersonas):
    listaEstudiantes = []
    for persona in listaPersonas:
        if persona.getTipo() == "estudiante":
            listaEstudiantes.append(persona)
    return listaEstudiantes


"""
Función: funcionGenerarVotacion (genera selecciones aleatorias de uno de los candidatos registrados, de acuerdo a 
                                 la cantidad)
Entradas: listaPersonas (list)
Salidas: listaPersonas (list) - actualizada
"""
def funcionGenerarVotacion(listaPersonas):
    cntCandidatos = funcionCantidadCandidatos(listaPersonas)
    for persona in listaPersonas:
        voto = random.randint(0, len(cntCandidatos))
        persona.setVoto(voto)
    return listaPersonas


"""
Función: contarVotos (cuenta la cantidad de votos correspondientes a cada candidato y los guarda en una lista)
Entradas: listaPersonas (list)
Salidas: listaVotos (list)
"""
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


"""
Función: contarVotosPorRol (cuenta la cantidad de votos que corresponden a los candidatos, de acuerdo a los roles de 
                            las personas)
Entradas: listaPersonas (list), rol (str)
Salidas: listaVotos (list)
"""
def contarVotosPorRol(listaPersonas, rol):
    listaVotos = [0, 0, 0, 0]

    for i in range(1, 5):  # i representa el candidato
        for persona in listaPersonas:
            if persona.getVoto() == i and persona.getTipo() == rol:
                listaVotos[i - 1] += 1
    return listaVotos


"""
Función: obtenerRol (realiza una modificación con respecto a cómo viene dado el rol)
Entradas: rol (str)
Salidas: rol (str) - actualizado
"""
def obtenerRol(rol):
    if rol == "Estudiantes":
        rol = "estudiante"

    elif rol == "Profesores":
        rol = "profesor"

    elif rol == "Administrativos":
        rol = "administrativo"

    return rol


"""
Función: funcionHTMLListaCandidatos (obtiene la lista de candidatos y envía a realizar reporte de lista de candidatos)
Entradas: listaPersonas (list)
Salidas: crearReporteListaCandidatos (función (con entrada candidatos (list)))
"""
def funcionHTMLListaCandidatos(listaPersonas):
    candidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteListaCandidatos(candidatos)


"""
Función: funcionHTMLVotantesPorRol (obtiene la lista de candidatos y envía a realizar reporte de votantes por rol)
Entradas: listaPersonas (list)
Salidas: crearReporteVotantesPorRol (función (con entradas candidatos (list) y listaPersonas (list)))
"""
def funcionHTMLVotantesPorRol(listaPersonas):
    candidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteVotantesPorRol(candidatos, listaPersonas)


"""
Función: funcionHTMLEstudiantesPorCarrera (obtiene la lista de estudiantes y envía a realizar reporte de estudiantes 
                                           por carrera)
Entradas: listaPersonas (list)
Salidas: crearReporteEstudiantesPorCarrera (función (con entrada estudiantes (list)))
"""
def funcionHTMLEstudiantesPorCarrera(listaPersonas):
    estudiantes = funcionObtenerEstudiantes(listaPersonas)
    return crearReporteEstudiantesPorCarrera(estudiantes)


"""
Función: funcionHTMLSeguidoresPorCandidato (obtiene la lista de candidatos y envía a realizar reporte de 
                                            seguidores por candidato)
Entradas: listaPersonas (list)
Salidas: crearReporteSeguidoresPorCandidato (función (con entradas listaPersonas (list) y listaCandidatos (list)))
"""
def funcionHTMLSeguidoresPorCandidato(listaPersonas):
    listaCandidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteSeguidoresPorCandidato(listaPersonas, listaCandidatos)


"""
Función: obtenerNoVotantes (obtiene la lista de personas que no votaron)
Entradas: listaPersonas (list)
Salidas: listaNoVotante (list)
"""
def obtenerNoVotantes(listaPersonas):
    listaNoVotante = []
    for persona in listaPersonas:
        if persona.getVoto() == 0:
            listaNoVotante.append(persona)
    return listaNoVotante


"""
Función: funcionHTMLListaNoVotantes (obtiene la lista de no votantes y su porcentaje, y envía a realizar reporte de
                                     lista de no votantes)
Entradas: listaPersonas (list)
Salidas: crearReporteListaNoVotantes (función (con entradas noVotantes (list) y porcentaje (float)))
"""
def funcionHTMLListaNoVotantes(listaPersonas):
    noVotantes = obtenerNoVotantes(listaPersonas)
    porcentaje = (len(noVotantes) * 100) / len(listaPersonas)
    return crearReporteListaNoVotantes(noVotantes, porcentaje)


"""
Función: funcionHTMLListaVotantesCandidato (obtiene la lista votantes por cadidato, y la cantidad de estos por cada rol)
Entradas: candidatoBuscar (str), listaPersonas (list), posicion (int)
Salidas: crearReporteListaVotantesCandidato (función (con entradas listaVotantes (list), candidatoBuscar (str),
                                             cntEstudiantes (int), cntProfesores (int) y cntAdministrativos (int)))
"""
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


"""
Función: funcionHTMLListaCantidadVotantesPorCandidato (obtiene la lista de candidatos, la cantidad y el porcentaje de 
                                                       votos para cada uno, y envía a realizar reporte de votantes por
                                                       candidato)
Entradas: listaPersonas (list)
Salidas: crearReporteListaCantidadVotantesCandidatos (función (con entradas listaCandidatos (list), listaCantidadVotos 
                                                     (list) y listaPorcentajes (list)))
"""
def funcionHTMLListaCantidadVotantesPorCandidato(listaPersonas):
    listaCandidatos = funcionCantidadCandidatos(listaPersonas)
    listaCantidadVotos = contarVotos(listaPersonas)
    listaPorcentajes = []

    for i in range(len(listaCandidatos)):
        listaPorcentajes.append((listaCantidadVotos[i] * 100) / (len(listaPersonas)))

    return crearReporteListaCantidadVotantesCandidatos(listaCandidatos, listaCantidadVotos, listaPorcentajes)


"""
Función: funcionHTMLCargaAutomatica (envía a realizar reporte de carga automática)
Entradas: listaPersonas (list)
Salidas: crearReporteCargaAutomatica (función (con entrada listaPersonas (list))
"""
def funcionHTMLCargaAutomatica(listaPersonas):
    return crearReporteCargaAutomatica(listaPersonas)
