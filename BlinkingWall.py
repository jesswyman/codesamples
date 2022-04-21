from tkinter import *
from Shape import *
import time

class BlinkingWall(Shape):
    def __init__(self, canvas, x, y, width, height, fill, outline):
        Shape.__init__(self, x, y, width, height, fill, canvas)
        self.outline = outline
        self.wall_create()
        
    def wall_create(self):
        #creates the wall
        self.canvas.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill=self.color, outline=self.outline, tags="wall"+str(self.id))
    
    def wall_delete(self):
        self.canvas.delete("wall"+str(self.id))