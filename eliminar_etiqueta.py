import guardar_en_diccionarios
def pedir_etiqueta_a_eliminar():
    """"Le pide al usuario que ingrese el nombre de la etiqueta que desea eliminar. La elimina"""
    #Pedir el nombre de la etiqueta
    diccionario = guardar_en_diccionarios.guardar_en_diccionarios()
    etiqueta = input("Ingrese el nombre de la nota que desea eliminar: ")
    if etiqueta == "":
        etiqueta = "Sin etiqueta"
    etiqueta = validar_etiqueta(etiqueta)
    #Mostrarle al usuario las opciones a borrar
    for i,elem in enumerate(diccionario[etiqueta]):
        print("{}-{}".format(i+1,elem))
    cantidad = len(diccionario[etiqueta])
    #Preguntar qué opciones quiere borrar e imprimirla
    texto_a_borrar = input("Ingrese el número de la opción que desea borrar: ")
    texto_a_borrar = validar_numero(texto_a_borrar,cantidad)
    print("[{}]".format(etiqueta))
    print("-{}".format(diccionario[etiqueta][int(texto_a_borrar)-1]))
    eliminar = input("Eliminar [s/n]: ")
    #Llamar función para que elimine el valor
    eliminar_etiqueta(etiqueta,texto_a_borrar,eliminar)

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
        if etiqueta.lower() == clave.lower():
            return clave

def validar_numero(texto_a_borrar,cantidad):
    """Comprueba si el texto a borrar hace una referencia a un número y comprueba que no esté fuera de rango"""
    while True:
        if (not texto_a_borrar.isdigit()) or (int(texto_a_borrar)<=0) or (int(texto_a_borrar)>cantidad):
            print("El número ingresado es inválido")
            texto_a_borrar = input("Ingrese la opción que desea eliminar: ")
        else:
            break
    return texto_a_borrar

def eliminar_etiqueta(etiqueta,texto_a_borrar,eliminar):
    """Elimina la etiqueta del diccionario con los datos de notas.csv y llama a una función para que reescriba el archivo"""
    diccionario = guardar_en_diccionarios.guardar_en_diccionarios()
    posicion = int(texto_a_borrar)-1
    while True:
        if eliminar.lower()=="s":
            lista = diccionario.pop(etiqueta)
            lista.pop(posicion)
            diccionario[etiqueta]= lista
            reescribir_notas(diccionario)
            print("La nota ha sido eliminada")
            break
        elif eliminar.lower() == "n" or eliminar.lower() == "no" :
            print("La nota no se ha eliminado")
            break
        else:
            eliminar= input("Ingrese nuevamente la opción que desea eliminar: ")

def reescribir_notas(diccionario):
    """Recibe como parámetro un diccionario y reescribe el contenido de un archivo.csv"""
    with open("notas.csv",'w') as archivo:
        for etiqueta,textos in diccionario.items():
            for elem in textos:
                texto = elem
                contenido = "{}|{}{}".format(etiqueta,texto,"\n")
                archivo.write(contenido)
