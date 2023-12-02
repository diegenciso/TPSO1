import argparse
import shutil

def copiar_archivo(origen, destino):
    try:
        shutil.copy(origen, destino)
        print(f"Archivo copiado de {origen} a {destino}")
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado - {origen}")
    except PermissionError:
        print(f"Error: Permiso denegado para copiar - {origen}")

def main():
    parser = argparse.ArgumentParser(description='Script para copiar archivos.')
    parser.add_argument('origen', type=str, help='Ruta del archivo de origen')
    parser.add_argument('destino', type=str, help='Ruta del archivo de destino')

    #ESTE ES EL QUE VAMOS A USAR PARA SACAR LO DEL TECLADO
    #cadena1 = input("nombre ").split(sep = ' ')
    #print(f"cadena 1",cadena1[0],cadena1[1],cadena1[2])


    args = parser.parse_args()

    # Llamar a la función de copia con las rutas proporcionadas
    copiar_archivo(args.origen, args.destino)


if __name__ == "__main__":
    main()
    

"""
ACLARACION
Todo lo que se quiere probar tiene que ser creado con la terminal de abajo creado en el ubuntu con mkdir por ejemplo o touch 
Es como el redhat de las clases, el windows no tiene nada que ver aca

"""

"""SHELL:
La shell se debe ejecutar como:    python3 shell.py 

Luego va a un loop infinito donde puede ingresar las funciones de la siguiente manera:  comando "primer argumento" "segundo argumento"
que se guardan en: cadena = input(" ").split(sep = ' ')  respectivamente    #CADENA SEPARADA POR ESPACIOS CADA ESPACIO ES UN [NUMERO] DE 0 A X-1

#Esto es lo que tengo entendido hasta ahora

"""