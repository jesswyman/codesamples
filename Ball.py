# name: T. Urness
# description: A Ball Class, inherits from Shape
# The Ball class keeps track of position, diameter, speed, and going_up values for a Ball

from tkinter import *
from Shape import *

class Ball(Shape):

    # initialization method
    # x -- x position of upper left corner of ball
    # y -- y poisition of upper left corner of ball
    # color -- string; color of ball to be drawn
    # diameter -- diameter of ball
    # canvas -- window canvas, part of tkinter
    def __init__(self, x, y, color, diameter, canvas, window):
        Shape.__init__(self,x,y,diameter, diameter, color, canvas)
        self.window = window
        self.speed_x = 6
        self.speed_y = 6
    
    #check if the ball is overlapping with anything, and runs the game over screen if it does
    def ball_overlap(self, w):
        overlap = Shape.overlap(self, w)
        if overlap == True:
            self.canvas.destroy()
            canvas = Canvas(self.window, bg="black", width = 800, height = 800)
            canvas.pack()
            canvas.create_text(400, 400, text="GAME OVER", font=("Helvetica", 100), fill="red")
            canvas.create_text(400, 600, text="(click anywhere to exit)", font=("Helvetica", 30), fill="white")
            canvas.bind("<Button-1>", self.callback)
    
    #lets the user click anywhere to exit the maze
    def callback(self, event):
        if event.x > 0 and event.x < 800 and event.y > 0 and event.y < 800:
            self.window.destroy()
    
        
    def hit_end(self):
        #checks if the ball hits the end of the maze, and shows the "you won" screen if it does
        if self.x + self.width > self.canvas.winfo_width():
            self.canvas.destroy()
            canvas = Canvas(self.window, bg="black", width = 800, height = 800)
            canvas.pack()
            canvas.create_text(400, 400, text="YOU WON!", font = ("Helvetica", 100), fill = "red")
            canvas.create_text(400, 600, text="(click anywhere to exit)", font=("Helvetica", 30), fill="white")
            canvas.bind("<Button-1>", self.callback)

    def draw(self):
        #draw the ball
        self.canvas.delete("ball"+str(self.id))
        self.canvas.create_oval(self.x, self.y,
                                self.x + self.width,
                                self.y+self.height,
                                fill=self.color,
                                tags="ball"+str(self.id))
                                