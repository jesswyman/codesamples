#Boulder class

from Shape import *
from tkinter import *

class Boulder(Shape):
    
    #makes the boulders
    def __init__(self, x, y, diameter, color, stop_y, canvas, window):
        Shape.__init__(self, x, y, diameter, diameter, color, canvas)
        self.window = window
        self.speed_y = 4
        self.stop_y = stop_y
        self.start_y = y