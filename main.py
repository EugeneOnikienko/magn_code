import numpy as np

#----------------------- Timescales initialization ---------------------------

t_st    = 0.0
t_en    = 200.0
dt      = 0.001
t       = arange( t_st, t_en, dt )

#------------------------ Paramete initialization ----------------------------

# Ferromagnetic frequency
om_FM       =
# Interlayer interection
d_om_int    =
#  Gilbert damping
a_G         =

#------------------------------ Initial values -------------------------------

theta0  = 0.01*np.pi
phi0    = 0.1*np.pi
ang = np.array([ theta0, phi0, np.pi - theta0, phi0,
                 0., 0., 0., 0.  ])




