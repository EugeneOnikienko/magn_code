import numpy as np

class RHS_safm_polar( object ):
    """ RHS function, which describe two vectors of syntetic AFM."""
    def __init__( self, om_fm, om_int, a, I ):
        self.of  	= om_fm
        self.oi 	= om_int
        self.so 	= om_fm + om_int
        self.aof	= a * om_fm
        self.aoi	= a * om_int
        self.aa     = ( a*a + 1. )**-1
        self.i      = I*a*( om_fm + om_int )
        self.ai 	= a*self.i

    
    def __call__( self, angs, t ):
    	""" angs = { theta0, theta1, d_phi } """
    	s = np.sin( angs )
    	c = np.cos( angs )

    	return self.aa * np.array([
    		self.oi*s[1]*s[2] + self.i*s[0] - self.aof*s[0]*c[0] + self.aoi*( s[0]*c[1] - c[0]*s[1]*c[2] ),
    		-self.oi*s[0]*s[2] - self.i*s[1] - self.aof*s[1]*c[1] + self.aoi*( s[1]*c[0] - c[1]*s[0]*c[2] ),
    		self.so*(c[0]-c[1]) + 2*self.ai + ( self.oi*c[2]*(c[0]*s[1]**2 - c[1]*s[0]**2) + self.aoi*s[2]*(s[0]**2 + s[1]**2) ) / (s[0]*s[1])
    	])

