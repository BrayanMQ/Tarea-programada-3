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
    arbol.write("lista_Candidatos.html")  # Se escribeTodo
