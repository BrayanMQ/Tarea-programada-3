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
            return True, "La cédula ya se encuentra registrada."
    return False, ""


def validarTelefono(telefono):
    try:
        telefono = int(telefono)
        return False, ""
    except:
        return True, "El telefono solamente debe contener dígitos."


def validarLargoTelefono(telefono):
    if len(telefono) == 8:
        return False, ""
    return True, "El telefono debe ser de 8 dígitos."


def validarExtension(extension):
    try:
        extension = int(extension)
        return False, ""
    except:
        return True, "La extension solamente debe contener dígitos."


def validarLargoExtension(extension):
    if len(extension) == 4:
        return False, ""
    return True, "La extension debe ser de 4 dígitos."


def validarCarnet(carnet):
    try:
        carnet = int(carnet)
        return False, ""
    except:
        return True, "El carnet solamente debe contener dígitos."


def validarLargoCarnet(carnet):
    if len(carnet) == 10:
        return False, ""
    return True, "El carnet debe ser de 10 dígitos."


def validarCedula(cedula):
    try:
        cedula = int(cedula)
        return False, ""
    except:
        return True, "La cédula solamente debe contener dígitos."


def validarLargoCedula(cedula):
    if len(cedula) == 9:
        return False, ""
    return True, "La cédula debe ser de 9 dígitos."


def validarTipoDatoCarga(cantidad):
    try:
        cantidad = int(cantidad)
        return False, ""
    except:
        return True, "Debe introducir un valor numérico"


def validarCantidadCarga(cantidad):
    cantidad = int(cantidad)
    if cantidad > 0 and cantidad <= 100:
        return False, ""
    return True, "Debe introducir un número entre 1 y 100"


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
            nombreCompleto = "Estudiante: Persona Número " + str(i)
            carreras = ["IC-Ingeniería en Computación", "ATI-Administración de la Información", "E-Electrónica",
                        "AE-Administración de Empresas", "CA-Ingeniería en Computadoras"]
            carrera = random.choice(carreras)
            carnet = random.randint(2019000000, 2019999999)

        elif tipoPersona == 2:
            nombreCompleto = "Profesor: Persona Número " + str(i)
            publicacion = "Publicación Número " + str(i)

        else:
            nombreCompleto = "Administrativo: Persona Número " + str(i)
            puestos = ["Secretaria", "Asistente administrativa", "Coordinador", "Director"]
            puesto = random.choice(puestos)
            extension = random.randint(1000, 9999)

        persona = funcionRegitrarMiembro(cedula, nombreCompleto, telefono, tipoPersona,
                                         carnet, publicacion, extension, carrera, puesto)
        listaPersonasCarga += [persona]
    return listaPersonasCarga


def funcionCantidadCandidatos(listaPersonas):
    cantidad = 0
    listaPosiciones = []
    for persona in listaPersonas:
        if persona.getTipo() == "profesor":
            if not persona.getCandidato() == "":
                cantidad += 1
                listaPosiciones.append(persona)
    print("")
    return cantidad, listaPosiciones


def funcionGenerarVotacion(anno, listaPersonas):
    cntCandidatos = funcionCantidadCandidatos(listaPersonas)

    for persona in listaPersonas:
        voto = random.randint(1, cntCandidatos[0])
        persona.setVoto(voto)
    return listaPersonas


def funcionHTMLListaCandidatos(listaPersonas):
    candidatos = funcionCantidadCandidatos(listaPersonas)
    return crearReporteListaCandidatos(candidatos[1])


def funcionBotonReportes():
    return ""
