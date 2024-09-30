import yaml
import argparse

def load_config(filename):
    with open(filename, 'r') as file:
        config = yaml.safe_load(file)
    return config

def parse_arguments():
    parser = argparse.ArgumentParser(description="Define los Argumentos de la Ejecución")
    parser.add_argument('--type', type=str, required=True, help='Type of Execution (all, simulacion_basica)')

    return parser.parse_args()
