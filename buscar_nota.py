def buscar_nota(diccionario):
    """Le pide al usuario un texto clave. Busca en los valores del diccionario dicho texto. Muestra al usuario en qué notas se encuentra la palabra"""
    resultados = {}
    clave = input("Ingrese el texto que desea buscar: ")
    clave_minus = clave.lower()
    for etiqueta,texto in diccionario.items():
        for casillero in texto:
            casillero_minus = casillero.lower()
            if clave_minus in casillero_minus:
                resultados[etiqueta] = resultados.get(etiqueta,[]) + [casillero]
    if clave == "":
        print("Ha ingresado un campo vacío")
    elif resultados == {}:
        print("No se han encontrado coincidencias")
    else:
        coincidencias = listar_notas.listar_notas(resultados)
