from scipy.optimize import minimize as min
import numpy as np

def Problem151():
    #Función Objetivo
    def func_obj(x):
        Sum1 = sum((x-1)**2)
        Sum2 = sum(x[:-1] *  x[1:])

        return Sum1 - Sum2
    
    #Solución inicial
    x0 = np.zeros(10)

    bounds = [(-100,100)] * 10

    #Minimizar
    Solution = min(func_obj, x0 = x0, bounds = bounds)

    #Mostrar los resultados
    print(f'Valor minimo de la funcion: {Solution.fun}')
    print(f'Numero de iteraciones: {Solution.nit}')

#Llamar a la función de optimización
Problem151()