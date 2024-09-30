import os
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from tqdm import tqdm

def main(config):    
    
    ##################################
    #    DEFINICIÓN DE PARÁMETROS    #
    ##################################
    
    # Nivel de significancia para las pruebas
    alpha = 0.05

    # Definimos el número de simulaciones que vamos a hacer
    numero_de_simulaciones = 1000

    # Definimos los rangos de las diferencias entre las medias
    min_dif = -1
    max_dif = 1
    num_points = 200

    ####################
    #    SIMULACIÓN    #
    ####################

    # Definimos un vector para guardar las probabilidades
    probabilidades = []

    # Definimos una grilla de las diferencias
    grilla_de_diferencias = np.linspace(min_dif, max_dif, num_points)
    total_pasos = len(grilla_de_diferencias)


    print("#"*50)
    print("Progreso Simulación Básica")
    print("#"*50)
    for delta in tqdm(grilla_de_diferencias, desc="Progreso", unit="paso"):

        # Definimos un vector para guardar los resultados de cada prueba
        resultados_pruebas = []

        for _ in range(numero_de_simulaciones):

            # Definimos los parámetros de cada simulación
            mu_1 = 0
            mu_2 = mu_1 + delta 
            sigma2_1 = 1
            sigma2_2 = 1
            n_1 = 20
            n_2 = 20

            # Simulamos las muestras
            muestra1 = np.random.normal(mu_1, np.sqrt(sigma2_1), n_1)
            muestra2 = np.random.normal(mu_2, np.sqrt(sigma2_2), n_2)

            # Hacemos la prueba t-student
            t_stat, p_value = stats.ttest_ind(muestra1, muestra2)

            # Vemos si se rechaza la prueba
            resultados_pruebas.append(int( p_value < alpha ))

        # Calculamos la probabilidad de rechazar la hipótesis nula
        probabilidades.append( np.mean(resultados_pruebas) )

    plt.style.use("ggplot")
    plt.figure(figsize=(13,8))
    plt.plot(grilla_de_diferencias, probabilidades, color = "blue")
    plt.axvline(mu_1, color="red", label=r"$\mu = 0$")
    plt.legend()
    plt.xlabel("Diferencia " + r"$ \Delta = \mu_1 - \mu_2$")
    plt.ylabel("Potencia")
    plt.title("Potencia de la Prueba t-student \n Normal " + rf"$ \mu={mu_1}, \sigma^2 = {sigma2_1}, n = {n_1}$" + f" \n Número de Simulaciones = {numero_de_simulaciones}")
    plt.savefig(os.path.dirname(__file__)+"/../resultados/grafica1.png")
    plt.close()