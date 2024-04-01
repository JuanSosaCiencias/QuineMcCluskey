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
    Despues obtiene los implicantes primos esenciales basicamente eliminando los implicantes primos que estan cubiertos
    por otros implicantes primos, aprovechandose de que los implicantes primos son una tupla con si mismos y los minterminos
    que cubren.

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
    implicantes_primos_ordenados = sorted(implicantes_primos, key=lambda x: x[0]) # Ordenar por número de unos
    implicantes_primos_esenciales = [] 

    for imp in implicantes_primos_ordenados: 
        mintermino_cubierto = imp[1][0] 
        cubierto_por_otro = False   

        for otro_imp in implicantes_primos_ordenados: 
            if otro_imp != imp and mintermino_cubierto in otro_imp[1]: 
                cubierto_por_otro = True
                break

        if not cubierto_por_otro:
            implicantes_primos_esenciales.append(imp)

    return implicantes_primos_esenciales

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
