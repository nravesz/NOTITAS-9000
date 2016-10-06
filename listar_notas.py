def listar_notas(diccionario):
    """Recibe un diccionario como parámetro. Imprime su contenido en forma de lista"""
    for etiqueta,texto in diccionario.items():
        print("[{}]".format(etiqueta))
        for casillero in texto:
            print("-{}".format(casillero))
        print("\n")
