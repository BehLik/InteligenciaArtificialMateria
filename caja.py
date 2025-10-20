# Requerimientos: pip install geneticalgorithm numpy
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

L = 50.0  # lado de la cartulina en cm

# función objetivo: minimizar -> devolvemos -V(x)
def objective(X):
    # X es un array de dimensión 1 (por la API de la librería)
    x = float(X[0])
    # Si x fuera inválido, dar un valor grande (seguridad)
    if x <= 0 or x >= L/2:
        return 1e6
    V = x * (L - 2*x)**2
    return -V  # minimizamos -V para maximizar V

# límites para la variable x: entre 0 y L/2
varbound = np.array([[0.0, L/2]])

# parámetros del algoritmo (ajusta según necesidad)
algorithm_params = {
    'max_num_iteration': 200,       # iteraciones máximas
    'population_size': 80,
    'mutation_probability': 0.1,
    'elit_ratio': 0.01,
    'crossover_probability': 0.5,
    'parents_portion': 0.3,
    'crossover_type': 'uniform',
    'max_iteration_without_improv': None
}

model = ga(
    function=objective,
    dimension=1,
    variable_type='real',
    variable_boundaries=varbound,
    algorithm_parameters=algorithm_params
)

# Ejecutar la búsqueda
model.run()

# Resultados (la API del paquete suele exponer output en model.output_dict)
print("Mejor solución encontrada (x en cm):", model.output_dict['variable'])
print("Volumen máximo encontrado (cm^3):", -model.output_dict['function'])  # negativo -> volver a positivo
