def guardar_en_diccionarios():
    """Convierte los datos del archivo "notas.csv"" en un diccionario. La clave es la etiqueta de la nota y el valor una lista con el texto"""
    diccionario = {}
    with open("notas.csv","r") as f:
        for linea in f:
            oracion = linea.rstrip("\n")
            oracion = oracion.split("|")
            etiqueta,texto = oracion
            if etiqueta =="":
                etiqueta="sin etiqueta"
            diccionario[etiqueta] = diccionario.get(etiqueta,[]) + [texto]
    return diccionario

def elegir_etiqueta():
    """Pregunta al usuario la etiqueta deseada a modificar y valida, si esta es válida, devuelve la etiqueta correcta seleccionada"""
    etiqueta  = input("Ingrese una etiqueta: ")
    if etiqueta == "":
        etiqueta = "sin etiqueta"
    while True:
        validacion = es_etiqueta_valida(etiqueta)
        if validacion == True:
            return etiqueta
        else:
            print("La nota que ingresó no existe")
            etiqueta = input("Ingrese el nombre de la etiqueta que desea eliminar: ")
            continue

def es_etiqueta_valida(etiqueta):
    """Comprueba si la etiqueta existe. De no ser así, pide que se vuelva a ingresar hasta encontrar una coincidencia.
    Devuelve la clave perteneciente al diccionario que coincide con la etiqueta ingresada"""
    dic = guardar_en_diccionarios()
    lista = []
    for clave in dic:
        clave = clave.lower()
        lista.append(clave)
    etiqueta = etiqueta.lower()
    if etiqueta in lista:
        return True
    else:
        return False