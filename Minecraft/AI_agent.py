from pyglet.window import key, mouse
import random

class Agent(object):
    def __init__(self, Window):
        self.window = Window
        
    def jump(self):
        print "I'm going to jump!"
        self.window.on_key_press(32, 16)
        
        
    def move_right(self):
        print "I'm going to move right!"
        self.window.on_key_press(100, 16)
        
    def move_left(self):
        print "I'm going to move left!"
        self.window.on_key_press(97, 16)

    def move_forward(self):
        print "I'm going to move forward!"
        self.window.on_key_press(119, 16)

    def move_backward(self):
        print "I'm going to move backward!"
        self.window.on_key_press(115, 16)

    def turn_right(self):
        #Turn the agent 90 degrees to the right
        print "I'm going to turn right!"
        self.window.rotation = (self.window.rotation[0] + 90, self.window.rotation[1])

    def turn_left(self):
        #Turn the agent 90 degrees to the right
        print "I'm going to turn left!"
        self.window.rotation = (self.window.rotation[0] - 90, self.window.rotation[1])
        
    def stop(self):
        self.window.strafe[0] = 0
        self.window.strafe[1] = 0

    #The left click destroys a block
    def left_click(self):
        print "I'm going to click left!"
        #Clicks will always occur at the center of the screen
        x = self.window.width / 2
        y = self.window.height / 2
        button = 1
        modifiers = 16
        self.window.on_mouse_press(x, y, button, modifiers)

    #The right click makes a block
    def right_click(self):
        print "I'm going to click right!"
        #Clicks will always occur at the center of the screen
        x = self.window.width / 2
        y = self.window.height / 2
        button = 4
        modifiers = 16
        self.window.on_mouse_press(x, y, button, modifiers)

    def change_block_brick(self):
        print "Making blocks BRICK"
        self.window.block = self.window.inventory[0]
        
    def change_block_grass(self):
        print "Making blocks GRASS"
        self.window.block = self.window.inventory[1]

    def change_block_sand(self):
        print "Making blocks SAND"
        self.window.block = self.window.inventory[2]

        
    def get_move(self):
        #NN part
        #self.turn_right()
        #self.left_click()
        functions = [self.jump, self.move_right, self.move_left, self.move_forward, self.move_backward, self.turn_right, self.turn_left, self.left_click, self.right_click]
        random.choice(functions)()
        
        # move = random.randint(0,3)
        # if move == 0:
        #     self.move_right()
        # elif move == 1:
        #     self.move_left()
        # elif move == 2:
        #     self.move_forward()
        # else:
        #     self.move_backward()
