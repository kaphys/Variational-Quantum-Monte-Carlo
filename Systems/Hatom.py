import numpy as np
""" This file contains the System information about the Hydrogen atom.
"""

# alpha values to compare with Jos Thijsen
alpha_jos = np.array([0.8, 0.9, 1, 1.1, 1.2])

# broader range of alphas to plot
alpha_broad = np.arange(0.5, 1.5, 0.05)

dimension = 3

def trial_wave_function(alpha, r):
    """ Trail wave function of the Hydrogen atom.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              numpy array of the position of the electron orbiting the atom


    Returns:
    --------
    np.exp(-alpha*r)
    """
    r = np.linalg.norm(r, axis = 1, keepdims = True)
    return np.exp(-alpha*r)

def E_loc(alpha, r):
    """ Local Energy of the Hydrogen atom.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              numpy array of the position of the electron orbiting the atom


    Returns:
    --------
    -1/r - 0.5*alpha*(alpha -2/r)
    """
    r = np.linalg.norm(r, axis = 1, keepdims = True)
    return (-1/r - 0.5*alpha*(alpha -2/r))

def deriv_wave_function(r):
    """ The derivative of the natural logarithm of the trail wave function. Needed for the minimal alpha finder.

    Parameters
    ----------
    r:              numpy array of the position of the electron orbiting the atom

    Returns:
    --------
    -r

    """
    r = np.linalg.norm(r, axis = 1, keepdims = True)
    return -r
