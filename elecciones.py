from tkinter import *

#Definición de la ventana principal
root = Tk()
root.title("Elecciones")
root.resizable(False, False)

#Definición del frame
frame = Frame(root, bg="black")
frame.pack()

#Definición de los botones

btn_RegistrarMiembro = Button(frame, text="Registrar miembro", width=20, height=1)
btn_RegistrarMiembro.grid(row=0, column=1, padx=50, pady=5)
btn_RegistrarMiembro.config(font="Helvetica", fg="#0E9F00")

btn_CargarDatos = Button(frame, text="Cargar datos", width=20, height=1)
btn_CargarDatos.grid(row=1, column=1, padx=50, pady=5)
btn_CargarDatos.config(font="Helvetica", fg="#0E9F00")

btn_RegistrarCandidatos = Button(frame, text="Registrar candidatos", width=20, height=1)
btn_RegistrarCandidatos.grid(row=2, column=1, padx=50, pady=5)
btn_RegistrarCandidatos.config(font="Helvetica", fg="#0E9F00")

btn_GenerarVotacion = Button(frame, text="Generar votación", width=20, height=1)
btn_GenerarVotacion.grid(row=3, column=1, padx=50, pady=5)
btn_GenerarVotacion.config(font="Helvetica", fg="#0E9F00")

btn_Reportes = Button(frame, text="Reportes", width=20, height=1)
btn_Reportes.grid(row=4, column=1, padx=50, pady=5)
btn_Reportes.config(font="Helvetica", fg="#0E9F00")

root.mainloop()