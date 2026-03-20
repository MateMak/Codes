import numpy as np
import matplotlib.pyplot as plt
A = np.array([
                [2, 1, 1],
                [1, 3, -1],
                [-1, 1, 2]], dtype=np.float64)

b = np.array([6, 4, 1], dtype=np.float64)

x_init = np.array([0, 0, 0], dtype=np.float64)


"""
Řešič soustav rovnic gausseidelovou metodou.
do proměnných A, b, x_init si nastavte hodnoty dle své soustavy. Přednastavané hodnoty odpovídají soustavě
2x_1 + x_2 + x_3 = 6
x_1 + 3x_2 - -x_3 = 4
-x_1 + x_2 + 2x_3 = 1

s počátečním odhadem x_1 = 0; x_2 = 0; x_3 = 0
"""



def jacobi(A: np.array, b: np.array, x_init: np.array = None, eps: float =1e-9, max_iterations: int = 100, show_steps: bool = True, plot: bool = True):
   
    """
        Krom nutných parametrů popisující soustavu můžeme specifikovat:
        eps - mezní velikost změny, při které utnem další postup
        max_iterations - Když metoda nezkonverguje, tak po kolika krocích má přestat
        show_steps - True/False: jestli chceme vypsat řešení po každém kroku
        plot - True/False: jestli chceme vykreslit graf s výsledky po každé iteraci 
    """

    # Initialize variables   
    if x_init is None:
        x_init = np.zeros_like(b, dtype=np.float64)

    n = len(b)
    x = x_init
    x_new = np.zeros_like(x)
    history = [x.copy()]
    #  A = D + R
    D = np.diag(A)
    R = A - np.diagflat(D)

    for iteration in range(max_iterations):
        x_new = (b - np.dot(R, x)) / D
        if show_steps == True:
            print(f"Odhad řešení: {x_new} po {iteration+1} iteracích")
        
        if np.linalg.norm(x_new - x) < eps:
            if plot == True:
                plot_iterations(history)
            return x_new, iteration + 1
        
        x = x_new
        history.append(x.copy())
    if plot == True:
        plot_iterations(history)
    raise ValueError("Jacobi nezkonevergoval. :-(")


def plot_iterations(history):
    history = np.array(history)
    iterations = np.arange(len(history))
    
    plt.figure(figsize=(8, 5))
    for i in range(history.shape[1]):  
        plt.plot(iterations, history[:, i], marker='o', label=f"x{i+1}")
    
    plt.xlabel("# iterací")
    plt.ylabel("hodnota proměnných")
    plt.title("Jacobi ")
    plt.legend()
    plt.grid(True)
    plt.show()



# Example usage
if __name__ == "__main__":
    
    try:
        solution, num_iterations = jacobi(A, b, x_init)
        print(f"Solution: {solution}")
        print(f"Number of iterations: {num_iterations}")
    except ValueError as e:
        print(e)
