"""
Clase Persona

Atributos: cedula (int)
           nombreCompleto (str)
           telefono (int)
           voto (int)
           tipo (str)
"""
class Persona:

    def __init__(self, tipo):
        self.cedula = 0
        self.nombreCompleto = ""
        self.telefono = 0
        self.voto = 0
        self.tipo = tipo

    def setCedula(self, cedula):
        self.cedula = cedula

    def getCedula(self): # Método, obtiene el atributo cédula
        return self.cedula

    def setNombreCompleto(self, nombreCompleto):
        self.nombreCompleto = nombreCompleto

    def getNombreCompleto(self): # Método, obtiene el atributo nombreCompleto
        return self.nombreCompleto

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self): # Método, obtiene el atributo telefono
        return self.telefono

    def setVoto(self, voto):
        self.voto = voto

    def getVoto(self): # Método, obtiene el atributo voto
        return self.voto

    def getTipo(self): # Método, obtiene el atributo tipo
        return self.tipo

"""
Clase Estudiante, con herencia de Persona

Atributos: carnet (str)
           carrera (str)
"""
class Estudiante(Persona):

    def __init__(self):
        self.carnet = ""
        self.carrera = ""
        Persona.__init__(self, tipo="estudiante")

    def setCarnet(self, carnet):
        self.carnet = carnet

    def getCarnet(self): # Método, obtiene el atributo carnet
        return self.carnet

    def setCarrera(self, carrera):
        self.carrera = carrera

    def getCarrera(self): # Método, obtiene el atributo carrera
        return self.carrera

"""
Clase Profesor, con herencia de Persona

Atributos: publicaiones (str)
           candidato (str)
"""
class Profesor(Persona):

    def __init__(self):
        self.publicaciones = ""
        self.candidato = ""
        Persona.__init__(self, tipo="profesor")

    def setPublicaciones(self, publicaciones):
        self.publicaciones = publicaciones

    def getPublicaciones(self): # Método, obtiene el atributo publicaciones
        return self.publicaciones

    def setCandidato(self, candidato):
        self.candidato = candidato

    def getCandidato(self): # Método, obtiene el atributo candidato
        return self.candidato

"""
Clase Administrativo, con herencia de Persona

Atributos: puesto (str)
           extension (str)
"""
class Administrativo(Persona):

    def __init__(self):
        self.puesto = ""
        self.extension = ""
        Persona.__init__(self, tipo="administrativo")

    def setPuesto(self, puesto):
        self.puesto = puesto

    def getPuesto(self): # Método, obtiene el atributo puesto
        return self.puesto

    def setExtension(self, extension):
        self.extension = extension

    def getExtension(self): # Método, obtiene el atributo extension
        return self.extension
