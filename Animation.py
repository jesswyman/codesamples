# author: Jess Wyman & Prof. Urness
# description: Assignment #8 - a maze game where you can't let the ball hit the walls or objects within the game. This specific
    #file is the driver for the game and runs all the animation
#proposed points: 15/15 - I mean I kinda went way beyond the basic pong game so I think that merits full points

from Ball import *
from tkinter import *
from Boulder import *

class Animation:
    def __init__(self, window, canvas, start_x, start_y, wall_list, blinking_wall_list = [], boulder_list = []):
        #setting the window and canvas from the inputs, as well as setting other variables/lists from input
        self.window = window

        self.canvas = canvas
        
        self.boulder_list = boulder_list
        
        self.wall_list = wall_list
        self.blinking_wall_list = blinking_wall_list
        
        #binding key presses to the window
        self.pressed_keys = {}
        self.window.bind("<KeyPress>", self.key_press)
        self.window.bind("<KeyRelease>", self.key_release)
        
        # create an empty list for balls
        self.ball_list = []
        #creates the ball
        self.ball_create(start_x, start_y)
        # starts the animation loop
        self.animate()
    
    def key_press(self, event):
        self.pressed_keys[event.keysym] = True

    def key_release(self, event):
        self.pressed_keys.pop(event.keysym, None)
        
    def ball_create(self, start_x, start_y):
        # create a ball and add it to the list
        diameter = 40
        
        ball_color = "red"
        
        ball = Ball(start_x, start_y, ball_color, diameter, self.canvas, self.window)
        self.ball_list.append(ball)

    def process_movements(self):
        #loops through the ball list and moves ball based on what key is pressed (only arrow keys are accounted for)
        for b in self.ball_list:
            if 'Right' in self.pressed_keys:
                b.x += b.speed_x
            if 'Left' in self.pressed_keys:
                b.x -= b.speed_x
            if 'Down' in self.pressed_keys:
                b.y += b.speed_y
            if 'Up' in self.pressed_keys:
                b.y -= b.speed_y
    
    def draw_boulder(self):
        #draws the boulders (if the level has boulders)
        for d in self.boulder_list:
            self.canvas.delete("boulder"+str(d.id))
            self.canvas.create_oval(d.x, d.y, d.x+d.width, d.y+d.height, fill=d.color, tags="boulder"+str(d.id))
            
    def animate_boulder(self):
        #animates the boulder (they only go up and down so this only accounts for movement in the y direction)
        for d in self.boulder_list:
            d.y += d.speed_y
            
            #changes direction of the boulder if it hits its start or stop point
            if d.y + d.height >  d.stop_y:
                d.speed_y = -d.speed_y
            if d.y < d.start_y:
                d.speed_y = -d.speed_y
    
    def collision_detect(self, flag):
        #detects collisions from the standard ball list
        for b in self.ball_list:
            for w in self.wall_list:
                b.ball_overlap(w)

        #if walls are on, loops through the blinking wall list to detect collisions with those walls
        if flag == True:
            for b in self.ball_list:
                for w in self.blinking_wall_list:
                    b.ball_overlap(w)
        
        for b in self.ball_list:
            for w in self.boulder_list:
                b.ball_overlap(w)


    def win_detect(self):
        #detects if ball reaches the end of the maze
        for b in self.ball_list:
            b.hit_end()
    
    def animate(self):
        #main loop
        #counts frames for the blinking wall list
        frame = 1
        #sets walls on to true initially
        walls_on = True
        
        while True:
            self.canvas.after(20) # Sleep
            self.canvas.update() # Update self.canvas
            
            #adds one to the frame count every time
            frame += 1
            
            #calls the collision detect method
            self.collision_detect(walls_on)
            
            #makes the walls blink on and off in 50 frame intervals
            if frame % 50 == 0 and walls_on == True:
                walls_on = False
                for w in self.blinking_wall_list:
                    w.wall_delete()
            
            elif frame % 50 == 0 and walls_on == False:
                walls_on = True
                for w in self.blinking_wall_list:
                    w.wall_create()
            
            #calls the win detect method
            self.win_detect()
            
            # loop through all of the items in the list
            # move the ball and draw it
            for b in self.ball_list:
                self.process_movements()
                b.draw()

            self.draw_boulder()
            self.animate_boulder()