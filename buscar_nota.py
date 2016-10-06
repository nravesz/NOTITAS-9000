def buscar_nota(diccionario):
    """Le pide al usuario un texto clave. Busca en los valores del diccionario dicho texto Le muestra al usuario en qué notas se encuentra la palabra"""
    clave = input("Ingrese el texto que desea buscar: ")
    clave_minus = clave.lower()
    for etiqueta,texto in diccionario.items():
        for casillero in texto:
            casillero_minus = casillero.lower()
            if clave_minus in casillero_minus:
                print("[{}]".format(etiqueta))
                print("-{}".format(casillero))
                print("\n")
    #Decirle al usuario que no existe lo que buscó
    #Hacer algo si el usuario ingresa un campo vacío