from tkinter import *

class Description:
    
    def __init__(self):
        #creates the description screen and a back button to close the window
        self.window = Tk()
        self.window.title("Game Description")

        width=800
        height=800
        self.canvas = Canvas(self.window, bg="black", width = width, height = height)
        self.canvas.pack()
        
        self.canvas.create_text(400, 400, width = 600, text="This game is simple. Solve the maze, and don't let the ball hit anything! Use the arrow keys to move the ball.", font=("Helvetica", 40), fill="white")
        
        self.canvas.create_rectangle(690, 740, 790, 790, fill="red")
        self.canvas.create_text(740, 765, text="BACK", font=("Helvetica", 20))
        
        self.canvas.bind("<Button 1>", self.callback)
    
    #lets the user click the button to close the window
    def callback(self, event):
        if event.y >= 740 and event.y <= 790 and event.x >= 690 and event.x <= 790:
            self.window.destroy()