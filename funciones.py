from clases import *

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo, showerror


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
    return True, "La cédula debe ser de 8 dígitos."


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
    persona.setCedula(int(cedula))
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
