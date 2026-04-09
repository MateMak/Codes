import numpy as np
import matplotlib.pyplot as plt


##########################################################
############ Definujme funkci a její derivaci ############
##########################################################
def f(x):
    return x + np.sin(2 * x) - np.log(x + 2)


def df(x):
    return 1 + 2 * np.cos(2 * x) - 1 / (x + 2)


# ----------------------------------------------------------


def newton_tangents(f, df, x0, tol=1e-12, max_iter: int = 20, plot: bool = False):
    """
    Newtonova metoda.

    Parametry:
        f        ... funkce
        df       ... derivace funkce
        x0       ... počáteční bod
        tol      ... tolerance pro ukončení
        max_iter ... maximální počet iterací
        plot     ... pokud True, vykreslí funkci a Newtonovy body
    """
    results = []
    x_n = float(x0)

    for n in range(max_iter):
        # Error handling: dělení nulou, nekonečna a undef výrazy
        try:
            fx = float(f(x_n))
            dfx = float(df(x_n))
        except Exception as e:
            error_message = (
                f"V iteraci {n} nešlo vyhodnotit f nebo df v bodě x = {x_n}. "
                f"Původní chyba: {e}"
            )
            break

        if not np.isfinite(fx):
            error_message = f"V iteraci {n} není f({x_n}) konečné číslo: {fx}"
            break

        if not np.isfinite(dfx):
            error_message = f"V iteraci {n} není f'({x_n}) konečné číslo: {dfx}"
            break

        if abs(dfx) < 1e-14:
            error_message = f"V iteraci {n} je derivace příliš malá: f'({x_n}) = {dfx}"
            break

        # tečna: y = a*x + b
        a = dfx
        b = fx - dfx * x_n

        # Newtonův krok
        x_next = -b / a

        results.append(
            {
                "iterace": n,
                "x_n": x_n,
                "f_x_n": fx,
                "a": a,
                "b": b,
                "tecna": f"y = {a:.10f}x + {b:.10f}",
                "nulovy_bod": x_next,
            }
        )

        print(results[-1])

        if not np.isfinite(x_next):
            raise ValueError(
                f"V iteraci {n} vyšel nekonečný nebo nedefinovaný krok: {x_next}"
            )

        if abs(x_next - x_n) < tol:
            break

        x_n = x_next

    if plot:
        plot_newton_iterations(f, results)

    return results


#################################
############ Helpery ############
#################################


def safe_eval(f, x):
    """
    číslo nechá, nebo vratí nan aby to šlo vyhodnotit
    """
    try:
        y = f(float(x))
        y = float(y)
        if np.isfinite(y):
            return y
    except Exception:
        pass
    return np.nan


def sample_function_for_plot(f, x_left, x_right, num):
    """
    Navzorkuje funkci a infty body nahradí nánou
    """
    xs = np.linspace(x_left, x_right, num)
    ys = np.array([safe_eval(f, x) for x in xs], dtype=float)
    return xs, ys


def plot_newton_iterations(f, results):
    """
    kreslič grafu.
    """
    if not results:
        return

    x_points = np.array([r["x_n"] for r in results], dtype=float)
    y_points = np.array([r["f_x_n"] for r in results], dtype=float)
    x_next_points = np.array([r["nulovy_bod"] for r in results], dtype=float)

    x_all = np.concatenate([x_points, x_next_points])

    x_min = np.min(x_all)
    x_max = np.max(x_all)

    width = x_max - x_min
    margin = 0.25 * width

    x_left = x_min - margin
    x_right = x_max + margin

    xs, ys = sample_function_for_plot(f, x_left, x_right, num=1500)

    plt.figure(figsize=(10, 6))
    plt.plot(xs, ys, label="f(x)")
    plt.axhline(0, linewidth=1)

    cmap = plt.cm.viridis
    # gradient coloring bodů v grafu
    colors = cmap(np.linspace(0, 1, len(results)))

    for i, (x, y, x_next, c) in enumerate(
        zip(x_points, y_points, x_next_points, colors)
    ):
        # body na grafu funkce
        plt.scatter(x, y, color=c, s=70, zorder=3)
        plt.text(x, y, f"  {i}", color=c, fontsize=9)

        # body na ose x + úsečka
        if np.isfinite(x_next):
            plt.scatter(x_next, 0, color=c, s=40, marker="x", zorder=3)
            plt.plot([x, x_next], [y, 0], "--", color=c, alpha=0.7)

    plt.title("Newtonova metoda")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()


# --------------------------------------------------------------------------

########### RUN ###########

if __name__ == "__main__":
    vysledky = newton_tangents(f, df, x0=1, max_iter=10, plot=True)
