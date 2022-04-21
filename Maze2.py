from tkinter import *
from wall import *
from Animation import *
from BlinkingWall import *

class Maze2:
    
    def __init__(self):
        self.window = Tk()
        
        width = 800
        height = 800
        
        self.canvas = Canvas(self.window, bg="black", width = width, height = height)
        self.canvas.pack()
        
        a = "white"
        b = "blue"

        self.wall_list = []
        self.blinking_wall_list = []
        
        #creates all the walls for the maze
        wall1 = Wall(self.canvas, 0, 0, 800, 10, a, a)
        self.wall_list.append(wall1)
        
        wall2 = Wall(self.canvas, 0, 79, 10, 721, a, a)
        self.wall_list.append(wall2)
        
        wall3 = Wall(self.canvas, 10, 790, 790, 10, a, a)
        self.wall_list.append(wall3)
        
        wall4 = Wall(self.canvas, 790, 10, 10, 711, a, a)
        self.wall_list.append(wall4)
        
        wall5 = Wall(self.canvas, 158, 10, 10, 79, a, a)
        self.wall_list.append(wall5)
        
        wall6 = Wall(self.canvas, 395, 10, 10, 227, a, a)
        self.wall_list.append(wall6)
        
        wall7 = Wall(self.canvas, 711, 10, 10, 237, a, a)
        self.wall_list.append(wall7)
        
        wall8 = Wall(self.canvas, 10, 79, 69, 10, a, a)
        self.wall_list.append(wall8)
        
        wall9 = Wall(self.canvas, 168, 79, 79, 10, a, a)
        self.wall_list.append(wall9)
        
        wall10 = Wall(self.canvas, 474, 79, 158, 10, a, a)
        self.wall_list.append(wall10)
        
        wall11 = Wall(self.canvas, 79, 79, 10, 316, a, a)
        self.wall_list.append(wall11)
        
        wall12 = Wall(self.canvas, 89, 158, 227, 10, a, a)
        self.wall_list.append(wall12)
        
        wall13 = Wall(self.canvas, 316, 79, 10, 89, a, a)
        self.wall_list.append(wall13)
        
        wall14 = Wall(self.canvas, 79, 395, 247, 10, a, a)
        self.wall_list.append(wall14)
        
        wall15 = Wall(self.canvas, 237, 405, 10, 148, a, a)
        self.wall_list.append(wall15)
        
        wall16 = Wall(self.canvas, 10, 474, 158, 10, a, a)
        self.wall_list.append(wall16)
        
        wall17 = Wall(self.canvas, 79, 553, 247, 10, a, a)
        self.wall_list.append(wall17)
        
        wall18 = Wall(self.canvas, 158, 563, 10, 158, a, a)
        self.wall_list.append(wall18)
        
        wall19 = Wall(self.canvas, 79, 632, 10, 158, a, a)
        self.wall_list.append(wall19)
        
        wall20 = Wall(self.canvas, 316, 563, 10, 79, a, a)
        self.wall_list.append(wall20)
        
        wall21 = Wall(self.canvas, 711, 711, 79, 10, a, a)
        self.wall_list.append(wall21)
        
        wall22 = Wall(self.canvas, 632, 79, 10, 405, a, a)
        self.wall_list.append(wall22)
        
        wall23 = Wall(self.canvas, 642, 316, 79, 10, a, a)
        self.wall_list.append(wall23)
        
        wall24 = Wall(self.canvas, 711, 326, 10, 79, a, a)
        self.wall_list.append(wall24)
        
        wall25 = Wall(self.canvas, 642, 474, 79, 10, a, a)
        self.wall_list.append(wall25)
        
        wall26 = Wall(self.canvas, 711, 484, 10, 158, a, a)
        self.wall_list.append(wall26)
        
        wall27 = Wall(self.canvas, 632, 632, 79, 10, a, a)
        self.wall_list.append(wall27)
        
        wall28 = Wall(self.canvas, 632, 642, 10, 79, a, a)
        self.wall_list.append(wall28)
        
        wall29 = Wall(self.canvas, 474, 711, 158, 10, a, a)
        self.wall_list.append(wall29)
        
        wall30 = Wall(self.canvas, 474, 721, 10, 69, a, a)
        self.wall_list.append(wall30)
        
        wall31 = Wall(self.canvas, 158, 237, 326, 10, a, a)
        self.wall_list.append(wall31)
        
        wall32 = Wall(self.canvas, 158, 247, 10, 79, a, a)
        self.wall_list.append(wall32)
        
        wall33 = Wall(self.canvas, 168, 316, 237, 10, a, a)
        self.wall_list.append(wall33)
        
        wall34 = Wall(self.canvas, 474, 247, 10, 79, a, a)
        self.wall_list.append(wall34)
        
        wall35 = Wall(self.canvas, 395, 326, 10, 395, a, a)
        self.wall_list.append(wall35)
        
        wall36 = Wall(self.canvas, 316, 474, 79, 10, a, a)
        self.wall_list.append(wall36)
        
        wall37 = Wall(self.canvas, 237, 711, 158, 10, a, a)
        self.wall_list.append(wall37)
        
        wall38 = Wall(self.canvas, 237, 632, 10, 79, a, a)
        self.wall_list.append(wall38)
        
        wall39 = Wall(self.canvas, 405, 632, 148, 10, a, a)
        self.wall_list.append(wall39)
        
        wall40 = Wall(self.canvas, 553, 158, 10, 484, a, a)
        self.wall_list.append(wall40)
        
        wall41 = Wall(self.canvas, 563, 553, 79, 10, a, a)
        self.wall_list.append(wall41)
        
        wall42 = Wall(self.canvas, 474, 158, 79, 10, a, a)
        self.wall_list.append(wall42)
        
        wall43 = Wall(self.canvas, 474, 395, 79, 10, a, a)
        self.wall_list.append(wall43)
        
        wall44 = Wall(self.canvas, 474, 405, 10, 158, a, a)
        self.wall_list.append(wall44)
        
        wall45 = BlinkingWall(self.canvas, 158, 168, 10, 69, b, b)
        self.blinking_wall_list.append(wall45)
        
        wall46 = BlinkingWall(self.canvas, 316, 642, 10, 69, b, b)
        self.blinking_wall_list.append(wall46)
        
        wall47 = BlinkingWall(self.canvas, 642, 553, 69, 10, b, b)
        self.blinking_wall_list.append(wall47)
        
        wall48 = BlinkingWall(self.canvas, 711, 247, 10, 69, b, b)
        self.blinking_wall_list.append(wall48)
        
        #calls animation
        Animation(self.window, self.canvas, 24.5, 24.5, self.wall_list, self.blinking_wall_list)