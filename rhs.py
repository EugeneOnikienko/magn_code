class RHS_safm_polar( object ):
    """ RHS function, which describe two vectors of syntetic AFM."""
    def __init__( self, om_fm, om_int, a, I ):
        self.om_fm  = om_fm
        self.om_int = om_int
        self.a      = a
        self.i      = I*a*( om_fm + om_int )

    
    def __call__( self, angs, t ):
        
        
        
