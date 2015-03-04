
directions = {
    "up"    : [  0, -1 ],
    "down"  : [  0,  1 ],
    "left"  : [ -1,  0 ],
    "right" : [  1,  0 ]
}

class Creature:
    
    def __init__( self, char ):
        
        # Colored char
        self.char = char
        self.color = "white"
        
        # Position
        self.x = 0
        self.y = 0
    
    def move( self, direction ):
        self.x += directions[ direction ][ 0 ]
        self.y += directions[ direction ][ 1 ]
        return
    
    def draw( self, context ):
        
        return