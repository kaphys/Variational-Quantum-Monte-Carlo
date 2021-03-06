import numpy as np
""" This file contains the System information about the Harmonic oscillator.
"""

# alpha values to compare with Jos Thijsen
alpha_jos = np.array([0.4, 0.45, 0.5, 0.55, 0.6])

# broader range of alphas to plot
alpha_broad = np.arange(0.2, 0.8, 0.05)

dimension = 1

def trial_wave_function(alpha, r):
    """ Trail wave function of the harmonic oscillator.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be vaired
    r:              numpy array of the position of the oscillator


    Returns:
    --------
    np.exp(-alpha*r**2)
    """
    return np.exp(-alpha*r**2 )


def E_loc(alpha, r):
    """ Local Energy of the harmonic oscillator.

    Parameters
    ----------
    alpha:          int; parameter of the trail wave function to be varied
    r:              numpy array of the position of the oscillator


    Returns:
    --------
    alpha + (0.5-2*alpha**2)*r**(2)
    """
    return alpha + (0.5-2*alpha**2)*r**(2)

def deriv_wave_function(r):
    """ The derivative of the natural logarithm of the trail wave function. Needed for the minimal alpha finder.

    Parameters
    ----------
    r:              numpy array of the position of the oscillator

    Returns:
    --------
    -r**2

    """
    return -r**2
