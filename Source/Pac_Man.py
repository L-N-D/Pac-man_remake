from Specification import *

class Pacman:
    
    ##################### CORE ##############################
    def __init__(self, context, pos, cell = None ):
        
        self.context = context
        self.pos = [pos[0], pos[1]]
        