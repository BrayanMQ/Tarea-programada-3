from clases import *


def crearEstudiante(carnet, carrera):
    estudiante = Estudiante()
    estudiante.setCarnet(carnet)
    estudiante.setCarrera(carrera)
    return estudiante


def crearProfesor(publicaciones, candidato=False):
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
    persona.setCedula(cedula)
    persona.setNombreCompleto(nombre)
    persona.setTelefono(telefono)
    return persona


def funcionRegitrarMiembro(cedula, nombre, telefono, tipo,
                           carnet, publicaciones, extension, carrera, puesto):
    if tipo == 1:
        persona = crearEstudiante(carnet, carrera)
    elif tipo == 2:
        persona = crearProfesor(publicaciones)
    else:
        persona = crearAdministrativo(puesto, extension)

    persona = crearPersona(persona, cedula, nombre, telefono)

    return persona


def funcionBotonCargarDatos():
    return ""


def funcionBotonRegistrarCandidatos():
    return ""


def funcionBotonGenerarVotacion():
    return ""


def funcionBotonReportes():
    return ""
