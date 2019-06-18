import os
from clases import *
import xml.etree.cElementTree as ET
import funciones

"""
Función: crearReporteListaCandidatos (genera el HTML del reporte lista de candidatos)
Entradas: listaCandidatos (list)
Salidas: vacía
"""
def crearReporteListaCandidatos(listaCandidatos):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Lista de candidatos"

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 60px 5px 60px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse}"  # Unir las celdas, que solo quede una línea entre ellas
    style.text = textoEstilo  # Se agregaTodo lo anterior dentro del nodo "style"

    # Nodos
    body = ET.SubElement(html, "body")
    center = ET.SubElement(body, "center")
    encabezado = ET.SubElement(center, "header")

    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p1 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Candidatos para rector"
    p1.text = textoInfo

    p2 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: 2019"  ###### Periodo - cambiar
    p2.text = textoInfo

    table = ET.SubElement(center, "table", border="1px", style="text-align:center", )  # Tabla
    cabeceraDeTabla = ET.SubElement(table, "thead")  # Nodo cabecera

    fila1 = ET.SubElement(cabeceraDeTabla, "tr", bgcolor="Gainsboro")  # Fila1(cabecera)

    columna = ET.SubElement(fila1, "td")  # Celda1
    columna.text = "Cédula"

    columna2 = ET.SubElement(fila1, "td")  # Celda2
    columna2.text = "Nombre Completo"

    columna3 = ET.SubElement(fila1, "td")  # Celda3
    columna3.text = "Teléfono"

    columna4 = ET.SubElement(fila1, "td")  # Celda4
    columna4.text = "Publicaciones"

    cuerpoTabla = ET.SubElement(table, "tbody")  # Resto de la tabla

    ##
    i = 0
    for candidato in listaCandidatos:  # Cantidad de filas a crear
        i += 1
        if i % 2 != 0:  # Asigna un color
            fila = ET.SubElement(cuerpoTabla, "tr")
        else:  # Asigna otro color
            fila = ET.SubElement(cuerpoTabla, "tr", bgcolor="Gainsboro")

        # Se crean las celdas de cada fila a crear
        columna = ET.SubElement(fila, "td")
        columna.text = str(candidato.getCedula())

        columna2 = ET.SubElement(fila, "td")
        columna2.text = candidato.getNombreCompleto()

        columna3 = ET.SubElement(fila, "td")
        columna3.text = str(candidato.getTelefono())

        columna4 = ET.SubElement(fila, "td")
        columna4.text = candidato.getPublicaciones()

    arbol = ET.ElementTree(html)
    nombreHTML = "ReportesHTML\lista_Candidatos.html"
    arbol.write(nombreHTML)  # Se escribeTodo
    abrirHTML(nombreHTML)


"""
Función: crearReporteSeguidoresPorCandidato (genera el HTML del reporte seguidores por candidato)
Entradas: listaPersonas (list), listaCandidatos (list)
Salidas: vacía
"""
def crearReporteSeguidoresPorCandidato(listaPersonas, listaCandidatos):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Seguidores por candidato"

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 75px 5px 75px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%; text-align: center}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse; margin:0% 17.5%}"  # Tabla, unir las celdas, que solo quede una línea entre ellas
    textoEstilo += "\np1{margin:0% 17.5%; font-family: Arial; font-size: 90%}"
    style.text = textoEstilo  # Se agregaTodo lo anterior dentro del nodo "style"

    # Nodos
    body = ET.SubElement(html, "body")

    encabezado = ET.SubElement(body, "header")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Seguidores por candidato"
    p.text = textoInfo

    p = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: 2019"  ###### Periodo - cambiar
    p.text = textoInfo

    j = 1
    for candidato in listaCandidatos:

        p1 = ET.SubElement(body, "p1")
        textoInfo = "Candidato: " + candidato.getNombreCompleto()
        p1.text = textoInfo

        table = ET.SubElement(body, "table", border="1px", style="text-align:center", )  # Tabla
        cabeceraDeTabla = ET.SubElement(table, "thead")  # Nodo cabecera

        fila1 = ET.SubElement(cabeceraDeTabla, "tr", bgcolor="Gainsboro")  # Fila1(cabecera)

        columna = ET.SubElement(fila1, "td")  # Celda1
        columna.text = "Cédula"

        columna2 = ET.SubElement(fila1, "td")  # Celda2
        columna2.text = "Nombre Completo"

        columna3 = ET.SubElement(fila1, "td")  # Celda3
        columna3.text = "Tipo (Est-Prof-Adm)"

        cuerpoTabla = ET.SubElement(table, "tbody")  # Resto de la tabla

        i = 1
        for persona in listaPersonas:  # Cantidad de filas a crear
            if persona.getVoto() == j:
                if i % 2 != 0:  # Asigna un color
                    fila = ET.SubElement(cuerpoTabla, "tr")
                else:  # Asigna otro color
                    fila = ET.SubElement(cuerpoTabla, "tr", bgcolor="Gainsboro")

                # Se crean las celdas de cada fila a introducir
                columna = ET.SubElement(fila, "td")
                columna.text = str(persona.getCedula())

                columna2 = ET.SubElement(fila, "td")
                columna2.text = persona.getNombreCompleto()

                columna3 = ET.SubElement(fila, "td")
                columna3.text = persona.getTipo()
                i += 1

        saltoDeLinea = ET.SubElement(body, "br/")
        saltoDeLinea = ET.SubElement(body, "br/")
        j += 1

    arbol = ET.ElementTree(html)
    nombreHTML = "ReportesHTML\lista_seguidores_por_candidato.html"
    arbol.write(nombreHTML)  # Se escribeTodo
    abrirHTML(nombreHTML)


"""
Función: crearReportePadronPorRol (genera el HTML del reporte padrón por rol)
Entradas: listaPersonas (list)
Salidas: vacía
"""
def crearReportePadronPorRol(listaPersonas):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Padrón por rol"

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 65px 5px 65px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%; text-align: center}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse; margin:0% 16.5%}"  # Tabla, unir las celdas, que solo quede una línea entre ellas
    textoEstilo += "\np1{margin:0% 16.5%; font-family: Arial; font-size: 90%}"
    style.text = textoEstilo  # Se agregaTodo lo anterior dentro del nodo "style"

    # Nodos
    body = ET.SubElement(html, "body")

    encabezado = ET.SubElement(body, "header")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Padrón por rol"
    p.text = textoInfo

    p = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: 2019"  ###### Periodo
    p.text = textoInfo

    listaAtributos = [["Estudiante", "Carnet", "Nombre", "Carrera"], ["Profesor", "Cédula", "Nombre"],
                      ["Administrativo", "Cédula", "Nombre", "Puesto"]]
    for atributos in listaAtributos:

        p1 = ET.SubElement(body, "p1")
        textoInfo = "Rol: " + atributos[0]
        p1.text = textoInfo

        table = ET.SubElement(body, "table", border="1px", style="text-align:center", )  # Tabla
        cabeceraDeTabla = ET.SubElement(table, "thead")  # Nodo cabecera

        fila1 = ET.SubElement(cabeceraDeTabla, "tr", bgcolor="Gainsboro")  # Fila1(cabecera)

        columna = ET.SubElement(fila1, "td")  # Celda1
        columna.text = atributos[1]

        columna2 = ET.SubElement(fila1, "td")  # Celda2
        columna2.text = atributos[2]

        if atributos[0] == "Estudiante" or atributos[0] == "Administrativo":
            columna3 = ET.SubElement(fila1, "td")  # Celda3
            columna3.text = atributos[3]

        cuerpoTabla = ET.SubElement(table, "tbody")  # Resto de la tabla

        i = 1
        tipo = atributos[0].lower()
        for persona in listaPersonas:  # Cantidad de filas a crear
            if persona.getTipo() == tipo:
                if i % 2 != 0:  # Asigna un color
                    fila = ET.SubElement(cuerpoTabla, "tr")
                else:  # Asigna otro color
                    fila = ET.SubElement(cuerpoTabla, "tr", bgcolor="Gainsboro")

                if tipo == "estudiante":
                    columna = ET.SubElement(fila, "td")
                    columna.text = str(persona.getCarnet())
                else:
                    columna = ET.SubElement(fila, "td")
                    columna.text = str(persona.getCedula())

                columna2 = ET.SubElement(fila, "td")
                columna2.text = persona.getNombreCompleto()

                if tipo != "profesor":
                    if tipo == "estudiante":
                        columna3 = ET.SubElement(fila, "td")
                        columna3.text = persona.getCarrera()
                    else:
                        columna3 = ET.SubElement(fila, "td")
                        columna3.text = persona.getPuesto()
                i += 1

        saltoDeLinea = ET.SubElement(body, "br/")
        saltoDeLinea = ET.SubElement(body, "br/")

    arbol = ET.ElementTree(html)
    nombreHTML = "ReportesHTML\lista_padron_por_rol.html"
    arbol.write(nombreHTML)  # Se escribeTodo
    abrirHTML(nombreHTML)


"""
Función: crearReporteVotantesPorRol (genera el HTML del reporte votantes por rol)
Entradas: listaCandidatos (list), listaPersonas (list)
Salidas: vacía
"""
def crearReporteVotantesPorRol(listaCandidatos, listaPersonas):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Votantes por rol"

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 60px 5px 60px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse}"  # Unir las celdas, que solo quede una línea entre ellas
    style.text = textoEstilo  # Se agregaTodo lo anterior dentro del nodo "style"

    # Nodos
    body = ET.SubElement(html, "body")
    center = ET.SubElement(body, "center")
    encabezado = ET.SubElement(center, "header")

    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p1 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Votantes por rol"
    p1.text = textoInfo

    p2 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: 2019"
    p2.text = textoInfo

    table = ET.SubElement(center, "table", border="1px", style="text-align:center", )  # Tabla
    cabeceraDeTabla = ET.SubElement(table, "thead")  # Nodo cabecera

    fila1 = ET.SubElement(cabeceraDeTabla, "tr", bgcolor="Gainsboro")  # Fila1(cabecera)

    columnas1 = ET.SubElement(fila1, "td")  # Celda1
    columnas1.text = "Rol"

    for candidato in listaCandidatos:
        columnas1 = ET.SubElement(fila1, "td")
        columnas1.text = candidato.getNombreCompleto()

    cuerpoTabla = ET.SubElement(table, "tbody")  # Resto de la tabla

    i = 0
    listaRoles = ["Estudiantes", "Profesores", "Administrativos"]
    for rol in listaRoles:  # Cantidad de filas a crear

        listaVotos = funciones.contarVotosPorRol(listaPersonas, funciones.obtenerRol(rol))
        i += 1

        if i % 2 != 0:  # Asigna un color
            fila = ET.SubElement(cuerpoTabla, "tr")
        else:  # Asigna otro color
            fila = ET.SubElement(cuerpoTabla, "tr", bgcolor="Gainsboro")

        columna = ET.SubElement(fila, "td")
        columna.text = rol

        j = 0
        for candidato in listaCandidatos:
            columna = ET.SubElement(fila, "td")
            columna.text = str(listaVotos[j])
            j += 1

    arbol = ET.ElementTree(html)
    nombreHTML = "ReportesHTML\lista_VotantesPorRol.html"
    arbol.write(nombreHTML)  # Se escribeTodo
    abrirHTML(nombreHTML)


"""
Función: crearReporteEstudiantesPorCarrera (genera el HTML del reporte estudiantes por carrera)
Entradas: listaEstudiantes (list)
Salidas: vacía
"""
def crearReporteEstudiantesPorCarrera(listaEstudiantes):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Estudiantes por carrera"

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 60px 5px 60px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse}"  # Unir las celdas, que solo quede una línea entre ellas
    style.text = textoEstilo  # Se agregaTodo lo anterior dentro del nodo "style"

    # Nodos
    body = ET.SubElement(html, "body")
    center = ET.SubElement(body, "center")
    encabezado = ET.SubElement(center, "header")

    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p1 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Estudiantes por carrera"
    p1.text = textoInfo

    p2 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: 2019"
    p2.text = textoInfo

    listaCarreras = ["IC-Ingeniería en Computación",
                     "ATI-Administración de la Información",
                     "E-Electrónica",
                     "AE-Administración de Empresas",
                     "CA-Ingeniería en Computadoras"]

    for carrera in listaCarreras:

        p3 = ET.SubElement(center, "p")  # Texto para el encabezado
        textoInfo = carrera
        p3.text = textoInfo

        table = ET.SubElement(center, "table", border="1px", style="text-align:center", )  # Tabla
        cabeceraDeTabla = ET.SubElement(table, "thead")  # Nodo cabecera

        fila1 = ET.SubElement(cabeceraDeTabla, "tr", bgcolor="Gainsboro")  # Fila1(cabecera)

        columna = ET.SubElement(fila1, "td")  # Celda1
        columna.text = "Carnet"

        columna2 = ET.SubElement(fila1, "td")  # Celda2
        columna2.text = "Nombre"

        columna3 = ET.SubElement(fila1, "td")  # Celda3
        columna3.text = "Voto emitido"

        cuerpoTabla = ET.SubElement(table, "tbody")  # Resto de la tabla

        ##
        i = 0
        for estudiante in listaEstudiantes:  # Cantidad de filas a crear
            if estudiante.getCarrera() == carrera:
                i += 1
                if i % 2 != 0:  # Asigna un color
                    fila = ET.SubElement(cuerpoTabla, "tr")
                else:  # Asigna otro color
                    fila = ET.SubElement(cuerpoTabla, "tr", bgcolor="Gainsboro")

                # Se crean las celdas de cada fila a crear
                columna = ET.SubElement(fila, "td")
                columna.text = str(estudiante.getCarnet())

                columna2 = ET.SubElement(fila, "td")
                columna2.text = estudiante.getNombreCompleto()

                columna3 = ET.SubElement(fila, "td")
                columna3.text = str(estudiante.getVoto())

    arbol = ET.ElementTree(html)
    nombreHTML = "ReportesHTML\lista_EstudiantesPorCarrera.html"
    arbol.write(nombreHTML)  # Se escribeTodo
    abrirHTML(nombreHTML)


"""
Función: crearReporteCargaAutomatica (genera el HTML del reporte carga automática)
Entradas: listaPersonas (list)
Salidas: vacía
"""
def crearReporteCargaAutomatica(listaPersonas):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Carga automática"

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 60px 5px 60px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse}"  # Unir las celdas, que solo quede una línea entre ellas
    style.text = textoEstilo  # Se agregaTodo lo anterior dentro del nodo "style"

    # Nodos
    body = ET.SubElement(html, "body")
    center = ET.SubElement(body, "center")
    encabezado = ET.SubElement(center, "header")

    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p1 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Carga automática"
    p1.text = textoInfo

    p2 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: 2019"
    p2.text = textoInfo

    table = ET.SubElement(center, "table", border="1px", style="text-align:center", )  # Tabla
    cabeceraDeTabla = ET.SubElement(table, "thead")  # Nodo cabecera

    fila1 = ET.SubElement(cabeceraDeTabla, "tr", bgcolor="Gainsboro")  # Fila1(cabecera)

    columna = ET.SubElement(fila1, "td")  # Celda1
    columna.text = "#"

    columna2 = ET.SubElement(fila1, "td")  # Celda2
    columna2.text = "Cédula"

    columna3 = ET.SubElement(fila1, "td")  # Celda3
    columna3.text = "Nombre"

    columna4 = ET.SubElement(fila1, "td")  # Celda4
    columna4.text = "Rol"

    cuerpoTabla = ET.SubElement(table, "tbody")  # Resto de la tabla

    ##
    i = 0
    for persona in listaPersonas:  # Cantidad de filas a crear
        i += 1
        if i % 2 != 0:  # Asigna un color
            fila = ET.SubElement(cuerpoTabla, "tr")
        else:  # Asigna otro color
            fila = ET.SubElement(cuerpoTabla, "tr", bgcolor="Gainsboro")

        # Se crean las celdas de cada fila a crear
        columna = ET.SubElement(fila, "td")
        columna.text = str(i)

        columna2 = ET.SubElement(fila, "td")
        columna2.text = str(persona.getCedula())

        columna3 = ET.SubElement(fila, "td")
        columna3.text = str(persona.getNombreCompleto())

        columna4 = ET.SubElement(fila, "td")
        columna4.text = persona.getTipo()

    arbol = ET.ElementTree(html)
    nombreHTML = "ReportesHTML\lista_CargaAutomatica.html"
    arbol.write(nombreHTML)  # Se escribeTodo
    abrirHTML(nombreHTML)


"""
Función: crearReporteListaNoVotantes (genera el HTML del reporte lista de no votantes)
Entradas: listaNoVotantes (list), porcentaje (float)
Salidas: vacía
"""
def crearReporteListaNoVotantes(listaNoVotantes, porcentaje):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Lista de no votantes"

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 60px 5px 60px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse}"  # Unir las celdas, que solo quede una línea entre ellas
    style.text = textoEstilo  # Se agregaTodo lo anterior dentro del nodo "style"

    # Nodos
    body = ET.SubElement(html, "body")
    center = ET.SubElement(body, "center")
    encabezado = ET.SubElement(center, "header")
    piePagina = ET.SubElement(body, "center")

    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p1 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Lista de no votantes."
    p1.text = textoInfo

    p2 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: 2019"
    p2.text = textoInfo

    table = ET.SubElement(center, "table", border="1px", style="text-align:center", )  # Tabla
    cabeceraDeTabla = ET.SubElement(table, "thead")  # Nodo cabecera

    fila1 = ET.SubElement(cabeceraDeTabla, "tr", bgcolor="Gainsboro")  # Fila1(cabecera)

    columna = ET.SubElement(fila1, "td")  # Celda1
    columna.text = "Cédula"

    columna2 = ET.SubElement(fila1, "td")  # Celda2
    columna2.text = "Nombre Completo"

    columna3 = ET.SubElement(fila1, "td")  # Celda3
    columna3.text = "Tipo (Est-Prof-Adm)"

    cuerpoTabla = ET.SubElement(table, "tbody")  # Resto de la tabla

    p3 = ET.SubElement(piePagina, "p")  # Texto para el encabezado
    textoInfo = "Porcentaje de abstencionismo: " + str(round(porcentaje, 2))
    p3.text = textoInfo
    ##
    i = 0
    for noVotante in listaNoVotantes:  # Cantidad de filas a crear
        i += 1
        if i % 2 != 0:  # Asigna un color
            fila = ET.SubElement(cuerpoTabla, "tr")
        else:  # Asigna otro color
            fila = ET.SubElement(cuerpoTabla, "tr", bgcolor="Gainsboro")

        # Se crean las celdas de cada fila a crear
        columna = ET.SubElement(fila, "td")
        columna.text = str(noVotante.getCedula())

        columna2 = ET.SubElement(fila, "td")
        columna2.text = noVotante.getNombreCompleto()

        columna3 = ET.SubElement(fila, "td")
        columna3.text = str(noVotante.getTipo())

    arbol = ET.ElementTree(html)
    nombreHTML = "ReportesHTML\lista_No_Votantes.html"
    arbol.write(nombreHTML)  # Se escribeTodo
    abrirHTML(nombreHTML)


"""
Función: crearReporteListaVotantesCandidato (genera el HTML del reporte votantes de candidato)
Entradas: listaVotantes (list), candidatoBuscar (str), cntEstudiantes (int), cntProfesores (int), cntAdministrativos (int)
Salidas: vacía
"""
def crearReporteListaVotantesCandidato(listaVotantes, candidatoBuscar, cntEstudiantes, cntProfesores,
                                       cntAdministrativos):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Lista de votantes por candidato"

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 60px 5px 60px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse}"  # Unir las celdas, que solo quede una línea entre ellas
    style.text = textoEstilo  # Se agregaTodo lo anterior dentro del nodo "style"

    # Nodos
    body = ET.SubElement(html, "body")
    center = ET.SubElement(body, "center")
    encabezado = ET.SubElement(center, "header")
    piePagina = ET.SubElement(body, "center")

    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p1 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Votantes de candidato."
    p1.text = textoInfo

    p2 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Candidato = " + candidatoBuscar
    p2.text = textoInfo

    p3 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: 2019"
    p3.text = textoInfo

    table = ET.SubElement(center, "table", border="1px", style="text-align:center", )  # Tabla
    cabeceraDeTabla = ET.SubElement(table, "thead")  # Nodo cabecera

    fila1 = ET.SubElement(cabeceraDeTabla, "tr", bgcolor="Gainsboro")  # Fila1(cabecera)

    columna = ET.SubElement(fila1, "td")  # Celda1
    columna.text = "Cédula"

    columna2 = ET.SubElement(fila1, "td")  # Celda2
    columna2.text = "Nombre Completo"

    columna3 = ET.SubElement(fila1, "td")  # Celda3
    columna3.text = "Tipo (Est-Prof-Adm)"

    cuerpoTabla = ET.SubElement(table, "tbody")  # Resto de la tabla

    p4 = ET.SubElement(piePagina, "p")  # Texto para el encabezado
    textoInfo = "Total estudiantes: " + str(cntEstudiantes)
    p4.text = textoInfo

    p5 = ET.SubElement(piePagina, "p")  # Texto para el encabezado
    textoInfo = "Total profesores: " + str(cntProfesores)
    p5.text = textoInfo

    p6 = ET.SubElement(piePagina, "p")  # Texto para el encabezado
    textoInfo = "Total Administrativos: " + str(cntAdministrativos)
    p6.text = textoInfo

    p7 = ET.SubElement(piePagina, "p")  # Texto para el encabezado
    textoInfo = "Total General: " + str(len(listaVotantes))
    p7.text = textoInfo
    ##
    i = 0
    for votante in listaVotantes:  # Cantidad de filas a crear
        i += 1
        if i % 2 != 0:  # Asigna un color
            fila = ET.SubElement(cuerpoTabla, "tr")
        else:  # Asigna otro color
            fila = ET.SubElement(cuerpoTabla, "tr", bgcolor="Gainsboro")

        # Se crean las celdas de cada fila a crear
        columna = ET.SubElement(fila, "td")
        columna.text = str(votante.getCedula())

        columna2 = ET.SubElement(fila, "td")
        columna2.text = votante.getNombreCompleto()

        columna3 = ET.SubElement(fila, "td")
        columna3.text = str(votante.getTipo())

    arbol = ET.ElementTree(html)
    nombreHTML = "ReportesHTML\lista_Votantes_Candidato.html"
    arbol.write(nombreHTML)  # Se escribeTodo
    abrirHTML(nombreHTML)


"""
Función: crearReporteListaCantidadVotantesCandidatos (genera el HTML del reporte cantidad de votantes por candidato)
Entradas: listaCandidatos (list), listaCantidadVotos (list), listaPorcentajes (list)
Salidas: vacía
"""
def crearReporteListaCantidadVotantesCandidatos(listaCandidatos, listaCantidadVotos, listaPorcentajes):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Cantidad de votantes por candidato."

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 60px 5px 60px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse}"  # Unir las celdas, que solo quede una línea entre ellas
    style.text = textoEstilo  # Se agregaTodo lo anterior dentro del nodo "style"

    # Nodos
    body = ET.SubElement(html, "body")
    center = ET.SubElement(body, "center")
    encabezado = ET.SubElement(center, "header")
    piePagina = ET.SubElement(body, "center")

    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p1 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Cantidad de votantes por candidato."
    p1.text = textoInfo

    p2 = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: 2019"
    p2.text = textoInfo

    table = ET.SubElement(center, "table", border="1px", style="text-align:center", )  # Tabla
    cabeceraDeTabla = ET.SubElement(table, "thead")  # Nodo cabecera

    fila1 = ET.SubElement(cabeceraDeTabla, "tr", bgcolor="Gainsboro")  # Fila1(cabecera)

    columna = ET.SubElement(fila1, "td")  # Celda1
    columna.text = "Nombre del candidato"

    columna2 = ET.SubElement(fila1, "td")  # Celda2
    columna2.text = "Cantidad de votantes"

    columna3 = ET.SubElement(fila1, "td")  # Celda3
    columna3.text = "Porcentaje de votos"

    cuerpoTabla = ET.SubElement(table, "tbody")  # Resto de la tabla

    ##
    i = 0
    for candidato in listaCandidatos:  # Cantidad de filas a crear
        i += 1
        if i % 2 != 0:  # Asigna un color
            fila = ET.SubElement(cuerpoTabla, "tr")
        else:  # Asigna otro color
            fila = ET.SubElement(cuerpoTabla, "tr", bgcolor="Gainsboro")

        # Se crean las celdas de cada fila a crear
        columna = ET.SubElement(fila, "td")
        columna.text = str(candidato.getNombreCompleto())

        columna2 = ET.SubElement(fila, "td")
        columna2.text = str(listaCantidadVotos[i - 1])

        columna3 = ET.SubElement(fila, "td")
        columna3.text = str(round(listaPorcentajes[i - 1], 2))

    arbol = ET.ElementTree(html)
    nombreHTML = "ReportesHTML\lista_cantidad_de_votantes_por_candidato.html"
    arbol.write(nombreHTML)  # Se escribeTodo
    abrirHTML(nombreHTML)


"""
Función: abrirHTML (abre el archivo HTML de acuerdo al nombre proporcionado)
Entradas: nombreHTML (str)
Salidas: vacía
"""
def abrirHTML(nombreHTML):
    os.popen(nombreHTML)
    return ""
