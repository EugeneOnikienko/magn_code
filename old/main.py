from scipy.integrate import odeint
from numpy import *
from models.right_hand_sides import RHS_LL_cart, RHS_LLG_cart, RHS_LLGS_cart
from models.effective_fields import MF_anisotropy_cart
from matplotlib import pyplot as pp

#-------------------------------------------------------------------------------
# time scales definitions
t_st    = 0.0
t_en    = 200.0
dt      = 0.001
t       = arange( t_st, t_en, dt )

#-------------------------------------------------------------------------------
# stt parameters
sigma0  = 0.03
I       = 1.0
pol_dir = array( [0.0, 0.0, 1.0 ] )

#-------------------------------------------------------------------------------
# Initial value of the magnetization vector definition
m0      = array( [ 0.0, 0.5, 0.5*3**0.5 ] )

#-------------------------------------------------------------------------------
# effective magnetic field and rhs of dynamic equation definitions
h_eff   = MF_anisotropy_cart( [0, 0, 1], 10.0 )
rhs     = RHS_LLGS_cart( 0.3, 0.01, sigma0, I, pol_dir, h_eff )

#-------------------------------------------------------------------------------
# Solving the dynamic equation
m   = odeint( rhs, m0, t )

mx  = m[:, 0]
my  = m[:, 1]
mz  = m[:, 2]

#-------------------------------------------------------------------------------
# Drawing

def plot_style( x_lab, y_lab ):
    pp.xlabel( x_lab )
    pp.ylabel( y_lab )
    a = pp.gca()
    a.grid(True)

pp.figure()
pp.subplot(311); pp.plot( t, mx, 'r' ); plot_style( 'time', 'Mx' );
pp.subplot(312); pp.plot( t, my, 'b' ); plot_style( 'time', 'My' );
pp.subplot(313); pp.plot( t, mz, 'g' ); plot_style( 'time', 'Mz' );

pp.show()


