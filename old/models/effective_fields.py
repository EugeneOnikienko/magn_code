"""This module contains effective magnetic field models."""

import numpy as np
from numpy.linalg import norm

class MF_anisotropy_cart( object ):
    """ Anisotropy magnetic field in cartesian coorinats:
    H = k*(h,m)
    h: unit vector, directed along the anisotropy direction
    k: coefficient of proportionality; it defines the strength of the field
    m: vector of magnetization
    """

    def __init__( self, direction, constant ):
        """Initialize the MF_anisotropy_cart by the essential parameters

        Arguments
        ---------
        direction : ndarray
            arbitrary vector, the size doesn't metter
        constant : scalar
            the coefficient of proportionality

        Return
        ------
        None.
        """
        self.direct = np.array( direction ) / norm( direction )
        self.const = constant

    def __call__( self, m, t ):
        """

        Arguments
        ---------
        m : magnetizarion (vector);
        t : time (scalar).

        Return
        ------
        the value of magnetic field that acts on the magnetization m.
        """
        return self.const * np.dot( self.direct, m ) * self.direct


if __name__ == "__main__":
    print __doc__