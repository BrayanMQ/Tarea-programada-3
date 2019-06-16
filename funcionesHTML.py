from clases import *
import xml.etree.cElementTree as ET


def crearReporteListaCandidatos(listaCandidatos):
    html = ET.Element("html")  # Raiz, html
    head = ET.SubElement(html, "head")

    tituloPagina = ET.SubElement(head, "title")
    tituloPagina.text = "Lista de candidatos"

    style = ET.SubElement(head, "style", type="text/css")  # Estilo del texto y la tabla
    textoEstilo = "table td{padding: 5px 60px 5px 60px;}"  # "Bordes", espacios entre letra y celda
    textoEstilo += "\ntable tbody{text-align: center;}"  # Centrar el texto en la tabla
    textoEstilo += "\nheader{font-family: Arial; font-size: 90%; line-height: 40%}"  # Formato y estilo del encabezado
    textoEstilo += "\ntable{font-family: Arial; font-size: 85%; border-collapse: collapse}"  # Tabla, unir las celdas, que solo quede una línea entre ellas
    style.text = textoEstilo  # Se agrega todo lo anterior dentro del nodo "style"

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
    textoInfo = "Periodo: 2019" ###### Periodo - cambiar
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
    arbol.write("lista_Candidatos.html")  # Se escribe todo


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
    style.text = textoEstilo  # Se agrega todo lo anterior dentro del nodo "style"

    #Nodos
    body = ET.SubElement(html, "body")

    encabezado = ET.SubElement(body, "header")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Seguidores por candidato"
    p.text = textoInfo

    p = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Periodo: XXXXX"  ###### Periodo - cambiar
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
    arbol.write("Seguidores por candidato.html")  # Se escribe todo


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
    style.text = textoEstilo  # Se agrega todo lo anterior dentro del nodo "style"

    #Nodos
    body = ET.SubElement(html, "body")

    encabezado = ET.SubElement(body, "header")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")
    saltoDeLinea = ET.SubElement(encabezado, "br/")

    p = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "Padrón por rol"
    p.text = textoInfo

    p = ET.SubElement(encabezado, "p")  # Texto para el encabezado
    textoInfo = "XXXXX"  ###### Periodo
    p.text = textoInfo

    listaAtributos = [["Estudiante", "Carnet", "Nombre", "Carrera"], ["Profesor", "Cédula", "Nombre"], ["Administrativo", "Cédula", "Nombre", "Puesto"]]
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
    arbol.write("Padrón por rol.html")  # Se escribe todo
