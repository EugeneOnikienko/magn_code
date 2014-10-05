import numpy as np

#------------------------ Paramete initialization ----------------------------

# Period of oscilation
T 			= 3.0
# Ferromagnetic frequency
om_FM       = 2*np.pi /T
# Interlayer interection
d_om_int    = 10.0 * 2*np.pi /T
#  Gilbert damping
a_G         = 0.9
# Current in units of critical
I 			= 1.1


#----------------------- Timescales initialization ---------------------------

t_st    = 0.0
t_en    = 30*T
dt      = 0.001
t       = np.arange( t_st, t_en, dt )


#------------------------------ Initial values -------------------------------

theta0  = 0.01*np.pi
theta1	= 0.99*np.pi
d_phi  	= 1.*np.pi
angs0 	= np.array([ theta0, theta1, d_phi])


#-----------------------------------------------------------------------------

from rhs import RHS_safm_polar
safm = RHS_safm_polar( om_FM, d_om_int, a_G, I )

from scipy.integrate import odeint
angs = odeint( safm, angs0, t )


#-----------------------------------------------------------------------------

from plotters import *
draw_angles_2d(angs, t)
draw_angles_3d(angs)