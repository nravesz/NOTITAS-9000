def pedir_etiqueta_a_eliminar():
    """"Le pide al usuario que ingrese el nombre de la etiqueta que desea ingresar."""
    #Pedir el nombre de la etiqueta
    datos_dic = guardar_en_diccionarios.guardar_en_diccionarios()
    etiqueta = input("Ingrese el nombre de la nota que desea eliminar: ")
    if etiqueta == "":
        etiqueta = "Sin etiqueta"
    etiqueta = validar_etiqueta(etiqueta)
    #Mostrarle al usuario las opciones a borrar
    for i,elem in enumerate(datos_dic[etiqueta]):
        print("{}-{}".format(i+1,elem))

def validar_etiqueta(etiqueta):
    """Comprueba si la etiqueta existe. De no ser así, pide que se vuelva a ingresar hasta encontrar una coincidencia. Devuelve la clave perteneciente al diccionario que coincide con la etiqueta ingresada"""
    diccionario = guardar_en_diccionarios.guardar_en_diccionarios()
    lista = []
    for clave in diccionario:
        clave = clave.lower()
        lista.append(clave)
    while not etiqueta.lower() in lista:
        print("La nota que ingresó no existe")
        etiqueta = input("Ingrese el nombre de la etiqueta que desea eliminar: ")
    for clave in diccionario:
        if etiqueta == clave.lower():
            etiqueta = clave
            return etiqueta