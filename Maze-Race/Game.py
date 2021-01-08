import pyglet, os, sys, json
from pyglet.gl import *
from time import time, sleep
from GUI import *

key = pyglet.window.key
mouse = pyglet.window.mouse
font = pyglet.font

#######################################################################################################################
class main(pyglet.window.Window):
    # Construct a new window
    def __init__(self):
        super(main, self).__init__(1200, 800, fullscreen=False)
        self.alive = 1
        self.refresh_rate = 60
        self.show_menu = True

        self.font_paths = [
            os.path.join(os.getcwd(), 'resources', 'Adventurer.ttf'),
            os.path.join(os.getcwd(), 'resources', 'alagard.ttf')
        ]

        # Load fonts
        for font_path in self.font_paths:
            font.add_file(font_path)

        self.menu_font = font.load('Adventurer', size=14, bold=False, italic=False, dpi=96)
        self.main_menu = MainMenu(1200, 800)


    # Draw Loop
    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.main_menu.check_if_button_clicked((x, y))

    # Render the application out to the screen 
    def render(self):
        # Clear the screen
        self.clear()
        glEnable(GL_BLEND)

        if self.show_menu == True:
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            self.main_menu.draw()

        # For the wiindow
        self.flip()

    # Function to run the application
    def run(self):
        while self.alive == 1:
            self.render()
            event = self.dispatch_events()
            sleep(1.0/self.refresh_rate)

#######################################################################################################################
x = main()
x.run()