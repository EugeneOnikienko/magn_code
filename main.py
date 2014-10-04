import numpy as np


#------------------------ Paramete initialization ----------------------------

# Period of oscilation
T 			= 3.0
# Ferromagnetic frequency
om_FM       = 2*np.pi /T
# Interlayer interection
d_om_int    = 0.7 * 2*np.pi /T
#  Gilbert damping
a_G         = 0.01
# Current in units of critical
I 			= 3.0


#----------------------- Timescales initialization ---------------------------

t_st    = 0.0
t_en    = 30*T
dt      = 0.001
t       = np.arange( t_st, t_en, dt )


#------------------------------ Initial values -------------------------------

theta0  = 0.1*np.pi
theta1	= np.pi - theta0
d_phi  	= np.pi
angs0 	= np.array([ theta0, theta1, d_phi])


#-----------------------------------------------------------------------------

from rhs import RHS_safm_polar
safm = RHS_safm_polar( om_FM, d_om_int, a_G, I )

from scipy.integrate import odeint
angs = odeint( safm, angs0, t )


#-----------------------------------------------------------------------------
# from plotters import draw_angls_3D
# draw_angls_3D( angs )

from matplotlib import pyplot as pp

max2 = angs[:, 0].max()
min2 = angs[:, 0].min()
yticks2 = np.linspace(min2, max2, 5)
yt_labels2 = [ '$'+str(round(num, 1))+'\pi$' for num in yticks2 / np.pi]
	
max0 = angs[:, 0].max()
min0 = angs[:, 0].min()
	
max1 = angs[:, 1].max()
min1 = angs[:, 1].min()
	
mi = min(min0, min1)
ma = max(max0, max1)
yticks = np.linspace(mi, ma, 5)
yt_labels = [ '$'+str(round(num, 1))+'\pi$' for num in yticks / np.pi]
	
fig = pp.figure()
pp.subplot(211)
pp.plot(t, angs[:, 2], 'g', label='$\Delta\phi$')
pp.xlabel(r'time')
pp.ylabel(r'$\Delta\phi$')
pp.yticks(yticks2, yt_labels2)
pp.grid(True)

pp.subplot(212)
pp.plot(t, angs[:, 0], 'r', label='$M_1$')
pp.plot(t, angs[:, 1], 'b', label='$M_2$')
pp.xlabel(r'time')
pp.ylabel(r'$\theta$')
pp.yticks(yticks, yt_labels)
pp.legend(loc=7)
pp.grid(True)

pp.show()