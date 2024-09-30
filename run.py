import os
import yaml

from src import simulacion_basica
from src.funciones_basicas import *

def orden_de_ejecucion(args, config):
    if args.type == "all":
        simulacion_basica.main(config=config)
    elif args.type == "simulacion_basica":
        simulacion_basica.main(config=config)
    else:
        print("Tipo de Ejecución Invalido")


if __name__ == "__main__":

    ##############################
    #    CREACIÓN DE CARPETAS    #
    ##############################

    # Creamos una carpeta para resultados
    if not os.path.exists("resultados"):
        os.makedirs("resultados")  


    #################################
    #    OBTENCIÓN DE PARÁMETROS    #
    #################################

    # Obtenemos los argumentos de la ejecución
    args = parse_arguments()

    # Cargamos el archivo config.yaml
    config = load_config('config.yaml')


    ###############################
    #    ORDEN DE LA EJECUCIÓN    #
    ###############################

    orden_de_ejecucion(args=args,
                       config=config)