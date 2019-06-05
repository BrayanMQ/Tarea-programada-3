class Persona:

    def __init__(self, tipo):
        self.cedula = 0
        self.nombreCompleto = ""
        self.telefono = 0
        self.voto = 0
        self.tipo = tipo

    def setCedula(self, cedula):
        self.cedula = cedula

    def getCedula(self):
        return self.cedula

    def setNombreCompleto(self, nombreCompleto):
        self.nombreCompleto = nombreCompleto

    def getNombreCompleto(self):
        return self.nombreCompleto

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono

    def setVoto(self, voto):
        self.voto = voto

    def getVoto(self):
        return self.voto

    def getTipo(self):
        return self.tipo

class Estudiante(Persona):

    def __init__(self):
        self.carnet = ""
        self.carrera = ""
        Persona.__init__(self, tipo="estudiante")

    def setCarnet(self, carnet):
        self.carnet = carnet

    def getCarnet(self):
        return self.carnet

    def setCarrera(self, carrera):
        self.carrera = carrera

    def getCarrera(self):
        return self.carrera

class Profesor(Persona):

    def __init__(self):
        self.publicaciones = ""
        self.candidato = ""
        Persona.__init__(self, tipo="profesor")

    def setPublicaciones(self, publicaciones):
        self.publicaciones = publicaciones

    def getPublicaciones(self):
        return self.publicaciones

    def setCandidato(self, candidato):
        self.candidato = candidato

    def getCandidato(self):
        return self.candidato

class Administrativo(Persona):

    def __init__(self):
        self.puesto = ""
        self.extension = ""
        Persona.__init__(self, tipo="administrativo")

    def setPuesto(self, puesto):
        self.puesto = puesto

    def getPuesto(self):
        return self.puesto

    def setExtension(self, extension):
        self.extension = extension

    def getExtension(self):
        return self.extension
