
"""THis module contains right hand side (RHS) functors for solving dynamic \
equations of magnetization vector"""

import numpy as np
from numpy.linalg import norm

#-------------------------------------------------------------------------------

# 3D cartesian models
class RHS_LL_cart( object ):
    """RHS of the Landau-Lifshitz equation in cartesian coordinate system
    dM/dt = g [ M x H_eff ]:
    M       - 3d vector of magnetization
    g       - hyromagnetic ratio
    H_eff   - 3d vector of effective magnetic field
    """
    def __init__( self, hyro, H_eff ):
        """Initialize the RHS_LL_cart by the essential parameters

        Arguments:
        hyro    -- hyromagnetic ratio (scalar);
        H_eff   -- function of the magnetization and the time, H_eff = f( M, t ) (functor).

        Returns:
        None.

        """
        self.hyro = hyro
        self.H_eff = H_eff

    def __call__( self, m, t ):
        """

        Arguments:
        m       -- magnetization (vector);
        t       -- time (scalar).


        Return:
        time derivation of the magnetization, dM/dt (vector).
        """

        h_eff = self.H_eff( m, t )
        return self.hyro * np.cross( h_eff, m )

#-------------------------------------------------------------------------------

class RHS_LLG_cart( RHS_LL_cart ):
    """RHS of the Landau-Lifshitz equation with Gilbert damping in cartesian \
    coordinate system.
    dM/dt = g [ M x H_eff ] + (a * g / |M|) [ M x [ M x H_eff ] ]
    M       -- 3D vector of magnetization
    g       -- hyromagnetic ratio
    H_eff   -- 3d vector of effective magnetic field
    a       -- damping coefficient
    """
    def __init__( self, hyro, alpha, H_eff ):
        """ Initialize the RHS_LLG_cart by the essential parameters

        Arguments:
        hyro    -- hyromagnetic ratio (scalar);
        alpha   -- damping coefficient (scalar);
        H_eff   -- function of the magnetization and the time, H_eff = f( M, t ) (sunctor).

        Return:
        None.
        """

        super( RHS_LLG_cart, self ).__init__( hyro, H_eff )
        self.alpha = alpha

    def __call__( self, m, t ):
        """

        Arguments:
        m       -- magnetization (vector);
        t       -- time (scalar).

        Return:
        time derivation of the magnetization, dM/dt (vector).
        """
        self.norm_m = norm(m)
        dmdt_ndamp = super( RHS_LLG_cart, self ).__call__( m, t )
        return dmdt_ndamp + self.alpha / self.norm_m * np.cross( m, dmdt_ndamp )

#-------------------------------------------------------------------------------

class RHS_LLGS_cart( RHS_LLG_cart ):
    """RHS of the Landau-Lifshitz equation with Gilbert damping and Slonczewski \
    additional term in cartesian coordinate system.
    dM/dt = g [ M x H_eff ] + (a * g / |M|) [ M x [ M x H_eff ] ] + \
    (s*I/|M|)[ M x [M x e] ]
    M       -- 3D vector of magnetization
    g       -- hyromagnetic ratio
    H_eff   -- 3d vector of effective magnetic field
    a       -- damping coefficient
    s       -- sigma0 ???
    I       -- current magnitude
    e       -- unit vector directed along the current polarization direction
    """
    def __init__( self, hyro, alpha, sigma, curr, pol_dir, H_eff ):
        """ Initialize the RHS_LLGS_cart by the essential parameters

        Arguments:
        hyro    -- hyromagnetic ratio (scalar);
        alpha   -- damping coefficient (scalar);
        sigma   -- ??? (scalar);
        curr    -- magnitude of current (scalar);
        pol_dir -- polarization direction< the size doesn't metter (vector)
        H_eff   -- function of the magnetization and the time, H_eff = f( M, t ) (sunctor).

        Return:
        None.
        """

        super( RHS_LLGS_cart, self ).__init__( hyro, alpha, H_eff )
        self.sigma = sigma
        self.I = curr
        self.p = np.array( pol_dir ) / norm( pol_dir )

        self.k = sigma*curr     # for the sake of convenient

    def __call__( self, m, t ):
        """

        Arguments:
        m       -- magnetization (vector);
        t       -- time (scalar).

        Return:
        time derivation of the magnetization, dM/dt (vector).
        """

        dmdt_damp = super( RHS_LLGS_cart, self ).__call__( m, t )
        return dmdt_damp + ( self.k / self.norm_m ) * np.cross( m, np.cross( m, self.p ) )


################################################################################

if __name__ == "__main__":
    print __doc__