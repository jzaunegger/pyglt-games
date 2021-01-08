import pyglet, os, sys, json
from pyglet.gl import *
from time import time, sleep

key = pyglet.window.key
mouse = pyglet.window.mouse
font = pyglet.font

#######################################################################################################################
class ArrowBox:
    def __init__(self, x, y, title):
        self.x = x
        self.y = y
        self.title = title

        self.images = [
            os.path.join(os.getcwd(), 'resources', 'Frame-Gold.png'),
            os.path.join(os.getcwd(), 'resources', 'Button.png'),
            os.path.join(os.getcwd(), 'resources', 'Arrow-L.png'),
            os.path.join(os.getcwd(), 'resources', 'Arrow-R.png')
        ]
        self.data = []
        self.selected = ''

        # Initalize the components
        self.frame_stream = open(self.images[0], 'rb')
        self.frame_img = pyglet.image.load(self.images[0], file=self.frame_stream)

        self.button_label = pyglet.text.Label( text=self.title,  
            font_name='Adventurer', font_size=24, x=self.x+150, 
            y=self.y-265, anchor_x='center', anchor_y='center')

        self.button_bg_stream = open(self.images[1], 'rb')
        self.button_bg = pyglet.image.load(self.images[1], file=self.button_bg_stream)

        self.arrow_l_stream = open(self.images[2], 'rb')
        self.arrow_l_img = pyglet.image.load(self.images[2], file=self.arrow_l_stream)

        self.arrow_r_stream = open(self.images[3], 'rb')
        self.arrow_r_img = pyglet.image.load(self.images[3], file=self.arrow_r_stream)


    def draw(self):
        self.frame_img.blit(self.x+25,  self.y-250)
        self.button_label.draw()
        self.button_bg.blit(self.x, self.y-390)
        self.arrow_l_img.blit(self.x+10, self.y-365 )
        self.arrow_r_img.blit(self.x+240, self.y-365 )
        

#######################################################################################################################
class Button():
    def __init__(self, pos, label_text):
        self.size = (300, 100)
        self.x = pos[0]
        self.y = pos[1]
        self.bg_x = pos[0] - int(self.size[0] / 2)
        self.bg_y = pos[1] - int(self.size[1] / 2)
        self.width = self.size[0]
        self.height = self.size[1]
        self.label_text = label_text

        self.background = pyglet.shapes.Rectangle(
            self.bg_x, 
            self.bg_y, 
            self.width, 
            self.height,
            color=(50, 50, 50)
        )

        self.button_text = pyglet.text.Label( text=self.label_text,  
            font_name='Adventurer', font_size=32, x=self.x, 
            y=self.y, anchor_x='center', anchor_y='center')

        self.images = [  os.path.join(os.getcwd(), 'resources', 'Button.png') ]
        self.button_stream = open(self.images[0], 'rb')
        self.button_img = pyglet.image.load(self.images[0], file=self.button_stream)

    def draw(self):
        self.button_img.blit(self.bg_x, self.bg_y)
        self.button_text.draw()

    def check_bounds(self, point):
        if point[0] > self.background.x and point[0] < self.background.x + self.width and point[1] > self.background.y and point[1] < self.background.y + self.height:
            return True
        else:
            return False

#######################################################################################################################
class CloseButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.button_path = os.path.join(os.getcwd(), 'resources', 'Close-Icon-Gold.png')
        self.button_stream = open(self.button_path, 'rb')
        self.button_img = pyglet.image.load(self.button_path, file=self.button_stream)

    def check_if_button_clicked(self, mouse_pos):
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + 50 and mouse_pos[1] > self.y and mouse_pos[1] < self.y + 50:
            return True
        else:
            return False

    def draw(self):
        self.button_img.blit(self.x, self.y)