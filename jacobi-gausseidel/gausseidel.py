import numpy as np
import matplotlib.pyplot as plt

############# EXAMPLE #############
A = np.array([[-1, 2, 1],
            [1, 2, -3],
            [1, 1, 3]], dtype=float)
b = np.array([5, 11, -4], dtype=np.float64)
x_init = np.array([1, 2, 3], dtype=np.float64)
"""
Řešič soustav rovnic gausseidelovou metodou.
do proměnných A, b, x_init si nastavte hodnoty dle své soustavy. Přednastavané hodnoty odpovídají soustavě
-x_1 + 2x_2 + x_3 = 5
x_1 + 2x_2 - -x_3 = 11
x_1 + x_2 + 3x_3 = -4

s počátečním odhadem x_1 = 0; x_2 = 2; x_3 = 3



"""
def gauss_seidel_method(A: np.array, b: np.array, x_init: np.array = None, eps: float = 1e-9, max_iterations: int = 300, show_steps: bool = True, plot: bool = True):
    """
        Krom nutných parametrů popisující soustavu můžeme specifikovat:
        eps - mezní velikost změny, při které utnem další postup
        max_iterations - Když metoda nezkonverguje, tak po kolika krocích má přestat
        show_steps - True/False: jestli chceme vypsat řešení po každém kroku
        plot - True/False: jestli chceme vykreslit graf s výsledky po každé iteraci 
    """
    
    if x_init is None:
        x_init = np.zeros_like(b, dtype=np.float64)

    n = len(b)
    x = x_init
    history = [x.copy()]
    for iteration in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            sum_before = np.dot(A[i, :i], x[:i])  
            sum_after = np.dot(A[i, i+1:], x_old[i+1:])  

            x[i] = (b[i] - sum_before - sum_after) / A[i, i]
        history.append(x.copy())
        if show_steps == True:
            print(f"Odhad řešení: {x} po {iteration+1} iteracích")
        if np.linalg.norm(x - x_old, ord=np.inf) < eps:
            if plot == True:
                plot_iterations(history)
            return x, iteration + 1

    if plot == True:
        plot_iterations(history)
    raise ValueError("Gauss-Seidel nezkonvergoval :-(")





def plot_iterations(history):
    history = np.array(history)
    iterations = np.arange(len(history))
    
    plt.figure(figsize=(8, 5))
    for i in range(history.shape[1]):  
        plt.plot(iterations, history[:, i], marker='o', label=f"x{i+1}")
    
    plt.xlabel("# iterací")
    plt.ylabel("hodnota proměnných")
    plt.title("Gauss-Seidel ")
    plt.legend()
    plt.grid(True)
    plt.show()



# Example usage
if __name__ == "__main__":

    try:
        solution, num_iterations = gauss_seidel_method(A, b, x_init)
        print(f"Solution: {solution}")
        print(f"Number of iterations: {num_iterations}")
    except ValueError as e:
        print(e)