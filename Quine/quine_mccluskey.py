def representacion_binaria(num, num_vars):
    """
    Obtiene la representación binaria de un número con ceros a la izquierda.

    Args:
        num (int): El número entero a convertir en binario.
        num_vars (int): El número de variables en la representación binaria.

    Returns:
        str: La representación binaria del número con padding.
    """
    binario = bin(num)[2:]
    return '0' * (num_vars - len(binario)) + binario

def contar_unos(cadena_binaria):
    """
    Cuenta el número de unos en una cadena binaria.

    Args:
        cadena_binaria (str): La cadena binaria.

    Returns:
        int: El número de unos en la cadena binaria.
    """
    return cadena_binaria.count('1')

def combinar_terminos(terminos1, terminos2):
    """
    Combina dos términos binarios devolviendo None si no se pueden combinar.

    Args:
        terminos1 (str): El primer término binario.
        terminos2 (str): El segundo término binario.

    Returns:
        str: La combinación de los términos si se pueden combinar, None en caso contrario.
    """
    combinados = []
    diferencias = 0

    for i in range(len(terminos1)):
        if terminos1[i] != terminos2[i]:
            diferencias += 1
            combinados.append('-')
        else:
            combinados.append(terminos1[i])

    if diferencias == 1:
        return ''.join(combinados)
    else:
        return None

def obtener_implicantes_primos(minterminos, num_vars):
    """
    Obtiene los implicantes primos a partir de los minterminos, basicamente combinando a los minterminos
    para obtener los implicantes primos esto usando la cantidad de unos en la representación binaria de los minterminos.
    Despues obtiene los implicantes primos esenciales basicamente eliminando los implicantes primos que estan cubiertos.

    Args:
        minterminos (list): Lista de minterminos.
        num_vars (int): El número de variables en la representación binaria.

    Returns:
        list: Lista de implicantes primos esenciales.
    """
    implicantes_primos = set()

    for mintermino in minterminos:
        implicantes_primos.add((representacion_binaria(mintermino, num_vars), (mintermino,)))

    nuevos_implicantes_primos = implicantes_primos.copy()
    while True:
        nuevos_implicantes_primos = set()
        fusionados = set()

        for imp1 in implicantes_primos:
            for imp2 in implicantes_primos:
                combinado = combinar_terminos(imp1[0], imp2[0])
                if combinado:
                    fusionados.add(imp1[1][0])
                    fusionados.add(imp2[1][0])
                    nuevos_terminos = imp1[1] + imp2[1]
                    nuevos_implicantes_primos.add((combinado, tuple(sorted(nuevos_terminos))))

        for imp in implicantes_primos:
            if imp[1][0] not in fusionados:
                nuevos_implicantes_primos.add(imp)

        if nuevos_implicantes_primos == implicantes_primos:
            break

        implicantes_primos = nuevos_implicantes_primos.copy()

    # Identificar implicantes primos esenciales
    return encontrar_implicantes_primos_esenciales(implicantes_primos)

def encontrar_implicantes_primos_esenciales(implicantes_primos):
    """
    Encuentra los implicantes primos esenciales de un conjunto de implicantes primos.

    Un implicante primo es esencial si es el único que cubre al menos un mintermino. Esta función
    también verifica si, después de seleccionar los implicantes esenciales, hay minterminos que no están cubiertos.
    En tal caso, determina cuáles de los implicantes no esenciales son necesarios para cubrir todos los minterminos.

    Args:
    implicantes_primos (set of tuples): Un conjunto de implicantes primos, donde cada implicante
                                       es una tupla que contiene una representación binaria y
                                       una tupla de los minterminos que cubre.

    Returns:
    set: Un conjunto de implicantes primos esenciales.
    """

    # Diccionario para mapear cada mintermino a los implicantes que lo cubren
    # me di cuenta hasta despues
    cobertura_minterminos = {}

    # Llenar el diccionario con los minterminos y los implicantes que los cubren
    for implicante in implicantes_primos:
        for mintermino in implicante[1]:
            if mintermino not in cobertura_minterminos:
                cobertura_minterminos[mintermino] = set()
            cobertura_minterminos[mintermino].add(implicante)

    # Identificar implicantes primos esenciales
    implicantes_esenciales = set()
    for implicantes in cobertura_minterminos.values():
        if len(implicantes) == 1:
            implicante_esencial = next(iter(implicantes))
            implicantes_esenciales.add(implicante_esencial)

    # Verificar cobertura de minterminos por los esenciales
    minterminos_cubiertos = set()
    for implicante in implicantes_esenciales:
        minterminos_cubiertos.update(implicante[1])
    
    # Añadir implicantes necesarios si hay minterminos no cubiertos, me quitaba de mas
    if len(minterminos_cubiertos) < len(cobertura_minterminos):
        for implicante in (implicantes_primos - implicantes_esenciales):
            es_necesario = False
            for mintermino in implicante[1]:
                if mintermino not in minterminos_cubiertos:
                    es_necesario = True
                    break
            if es_necesario:
                implicantes_esenciales.add(implicante)
                minterminos_cubiertos.update(implicante[1])

    return implicantes_esenciales

def main():
    """
    Función principal del programa.
    """
    num_vars = int(input("Ingrese el número de variables: "))
    minterminos = list(map(int, input("Ingrese los minterminos separados por espacios: ").split()))

    implicantes_primos_esenciales = obtener_implicantes_primos(minterminos, num_vars)

    print("Implicantes primos esenciales:")
    for implicant in implicantes_primos_esenciales:
        print(f"{implicant[0]} : {implicant[1]}")

if __name__ == "__main__":
    main()
