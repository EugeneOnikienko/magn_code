from models.effective_fields import MF_anisotropy_cart
import numpy as np
from matplotlib import pyplot as pp
from math import pi

_2pi = 2*pi

def main():
    # field function
    h_eff = MF_anisotropy_cart( [0, 0, 1], 10.0 )

    # time scale
    t_st = 0.0
    t_en = 10.0
    dt = 0.1
    t = np.arange( t_st, t_en, dt )

    # magnetization
    omega = _2pi / (50*dt)
    mx = np.sin( omega*t ).reshape(-1, 1)
    my = np.zeros( t.size ).reshape(-1, 1)
    mz = np.cos( omega*t ).reshape(-1, 1)

    m = np.concatenate( [mx, my, mz], axis=1 )
    h = np.array([ h_eff(x, tau) for x, tau in zip( m, t ) ])
    print h

    hx = h[:, 0]
    hy = h[:, 1]
    hz = h[:, 2]
    #draw

    pp.figure()

    print mx.size
    print t

    pp.subplot(211)
    pp.plot( t, mx, 'r' )
    pp.plot( t, my, 'g' )
    pp.plot( t, mz, 'b' )

    pp.subplot(212)
    pp.plot( t, hx, 'r' )
    pp.plot( t, hy, 'g' )
    pp.plot( t, hz, 'b' )

    pp.show()

if __name__ == "__main__":
    main()

