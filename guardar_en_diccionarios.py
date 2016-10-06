def guardar_en_diccionarios():
    """Convierte los datos de notas.csv en un diccionario. La clave es la etiqueta de la nota y el valor una lista con el texto"""
    diccionario = {}
    with open("notas.csv","r") as f:
        for linea in f:
            oracion = linea.rstrip("\n") 
            oracion = oracion.split("|")
            etiqueta,texto = oracion
            diccionario[etiqueta] = diccionario.get(etiqueta,[]) + [texto]
    return diccionario
