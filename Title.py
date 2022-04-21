#main title page

from tkinter import *
from Description import *
from Maze1 import *
from Maze2 import *
from Maze3 import *

class Title:
    
    def __init__(self, window):
        self.window = window
        
        width=800
        height=800
        self.canvas = Canvas(self.window, bg="black", width = width, height = height)
        self.canvas.pack()
        
        #creates all the objects for the title page
        self.canvas.create_text(400, 200, text="MAZE CRAWLER", font=("Helvetica", 50), fill="white")
        
        self.canvas.create_rectangle(360, 360, 440, 440, fill = "white")
        self.canvas.create_text(400, 400, text="2", font=("Helvetica", 30), activefill="red")
        
        self.canvas.create_rectangle(260, 360, 340, 440, fill = "white")
        self.canvas.create_text(300, 400, text="1", font=("Helvetica", 30), activefill="red")
        
        self.canvas.create_rectangle(460, 360, 540, 440, fill = "white")
        self.canvas.create_text(500, 400, text="3", font=("Helvetica", 30), activefill="red")

        self.canvas.create_rectangle(300, 575, 500, 625, fill = "white")
        self.canvas.create_text(400, 600, text="Description", font=("Helvetica", 25), activefill="red")
        
        #binds the mouse to the canvas
        self.canvas.bind("<Button-1>", self.callback)
    
    #callback method to call certain classes when certain spots on the canvas are clicked
    def callback(self, event):
        if event.y >= 360 and event.y <= 440 and event.x >= 360 and event.x <= 440:
            Maze2()
        elif event.y >= 360 and event.y <= 440 and event.x >= 260 and event.x<= 340:
            Maze1()
        elif event.y >= 360 and event.y <= 440 and event.x >= 460 and event.x <= 540:
            Maze3()
        elif event.y >= 575 and event.y <= 625 and event.x >= 300 and event.x <= 500:
            Description()

