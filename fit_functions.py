import numpy as np
from scipy.optimize import curve_fit
from magnetism import curie_weiss

def fit_curie_weiss(T, M):
    initial_guess = [1.0, 0.0]
    try:
        popt = curve_fit(curie_weiss, T, M, p0=initial_guess, bounds=(0, [np.inf, 1000]))
        return popt
    except Exception as e:
        print(f"Error in fitting: {e}")
        return None
