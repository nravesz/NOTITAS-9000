def agregar_nota():
    """"Pide al usuario el texto y la etiqueta. Lo registra en notas.csv"""
    texto = input("Escriba el contenido de la nota: ")
    etiqueta = input("Ingrese la etiqueta de la nota: ")
    if etiqueta == "":
        etiqueta = "Sin etiqueta"
    contenido = "{}|{}{}".format(etiqueta,texto,"\n")
    with open("notas.csv","a") as archivo:
        archivo.write(contenido)