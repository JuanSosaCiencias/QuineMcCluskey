# QuineMcCluskey

## Descripción
Una implementación inicial del algoritmo de Quine McCLuskey para reducir  expresiones logicas.

## Uso

Ejecute el programa principal simplemente haciendo 'quine_mccluskey.py' le preguntara por 'Ingrese el número de variables:' le damos el numero de variables diferentes  y despues preguntara por 'Ingrese los minterminos separados por espacios:' finalmente regresara 'Implicantes primos esenciales:' con el formato '\<primos escenciales\> : (\<Minterminos que cubren\>)'.

Ejemplo:

```bash
    Ingrese el número de variables: 4   
    Ingrese los minterminos separados por espacios: 0 4 5 7 8 11 12 15
    Implicantes primos esenciales:
    --00 : (0, 4, 8, 12)
    01-1 : (5, 7)
    1-11 : (11, 15)
```

o en imagen:
![Logo de mi proyecto](imagenes/ejemplo.png)

