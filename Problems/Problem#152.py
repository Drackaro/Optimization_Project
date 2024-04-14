from scipy.optimize import differential_evolution
from math import sin, e

def Problem152():
    #Función Objetivo
    def func_obj(x):
        return e ** sin(50 * x[0]) + sin(60 * e ** x[1]) + sin(70 * sin(x[0])) + sin(sin(80 * x[1])) - sin(10 * (x[0] + x[1])) + 1/4 * (x[0] ** 2 + x[1] ** 2)
    
    #Límites de las variables
    bounds = [(-10, 10), (-10, 10)]

    #Minimizar
    Solution = differential_evolution(func_obj, bounds)
    x1 = Solution.x[0]
    x2 = Solution.x[1]

    #Mostrar los resultados
    print(f'Minimo Global en:{x1}, {x2}')
    print(f'Valor minimo de la funcion: {func_obj([x1,x2])}')
    print(f'Numero de iteraciones: {Solution.nit}')


#Invocar el método de optimización
Problem152()

