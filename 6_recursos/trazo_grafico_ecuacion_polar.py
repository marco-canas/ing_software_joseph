import numpy as np

import matplotlib.pyplot as plt

def plot_polar_equation(equation, theta_range, filename):
    """
    Genera y guarda un gráfico de una ecuación polar.

    Args:
        equation (callable): Función que define la ecuación polar r(θ).
        theta_range (tuple): Rango de valores de θ en radianes (inicio, fin).
        filename (str): Nombre del archivo donde se guardará el gráfico.
    """
    # Generar valores de θ
    theta = np.linspace(theta_range[0], theta_range[1], 1000)
    
    # Calcular valores de r usando la ecuación polar
    r = equation(theta)
    
    # Crear el gráfico polar
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, label='Ecuación polar')
    
    # Configurar título y leyenda
    ax.set_title('Gráfico de la ecuación polar', va='bottom')
    ax.legend(loc='upper right')
    
    # Guardar el gráfico
    plt.savefig(filename, bbox_inches='tight')
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Definir la ecuación polar r(θ)
    def polar_equation(theta):
        return 3*np.cos(theta)
    
    # Rango de θ en radianes
    theta_range = (0, 2 * np.pi)
    
    # Nombre del archivo de salida
    filename = "polar_plot.png"
    
    # Llamar a la función para graficar y guardar
    plot_polar_equation(polar_equation, theta_range, filename)