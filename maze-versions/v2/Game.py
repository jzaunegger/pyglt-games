import pyglet, os, sys, json
from pyglet.gl import *
from time import time, sleep

key = pyglet.window.key
mouse = pyglet.window.mouse
font = pyglet.font

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
class GameSetup:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.cx = int(self.width/2)
        self.cy = int(self.height/2)
        self.is_visibile = False

        self.start_button = Button( (self.cx, self.height-575), 'Start')
        self.close_button = CloseButton(125, 670)

        self.theme_selection = ArrowBox(200, 675, 'Themes')
        self.player_selection = ArrowBox(700, 675, 'Player')

    def toggle_visibility(self):
        if self.is_visibile == True:
            self.is_visibile = False
        else:
            self.is_visibile = True

    def draw(self):
        self.theme_selection.draw()
        self.player_selection.draw()

        self.close_button.draw()
        self.start_button.draw()

#######################################################################################################################
class HighScores:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

        self.cx = int(self.width/2)
        self.cy = int(self.height/2)

        self.is_visibile = False

        self.batch = None

        self.load_scores()
        self.create_text()

    def toggle_visibility(self):
        if self.is_visibile == True:
            self.is_visibile = False
        else:
            self.is_visibile = True

    def load_scores(self):
        self.scores_path = os.path.join(os.getcwd(), 'scores.json')
        with open(self.scores_path) as json_file:
            self.scores = json.load(json_file)

    def create_text(self):
        self.header_text = pyglet.text.Label(
            text=' Rank    Player Name    Score ',
            font_name='Adventurer',
            font_size=18, 
            x=self.cx, 
            y=self.height-200,
            anchor_x='center',
            anchor_y='center',
            color=(0, 0, 0, 255)
        )

        self.score_labels = []
        for i in range(0, len(self.scores['default'])):
            current_score = self.scores['default'][i]
            label_y = self.height - 240 - (26 * i)

            rank_label =    pyglet.text.Label(text=str(i+1),              font_name='Alagard', font_size=14, x=self.cx - 140, y=label_y, anchor_x='center', anchor_y='center', color=(20, 20, 20, 255) )
            player_label =  pyglet.text.Label(text=current_score[0],      font_name='Alagard', font_size=14, x=self.cx,       y=label_y, anchor_x='center', anchor_y='center', color=(20, 20, 20, 255) )
            score_label =   pyglet.text.Label(text=str(current_score[1]), font_name='Adventurer', font_size=14, x=self.cx + 125, y=label_y, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255) )


            self.score_labels.append([rank_label, player_label, score_label])
            self.back_button = Button((self.cx, self.height-550), 'Back')

    def draw(self):
        # Draw Header
        self.header_text.draw()

        # Draw Scores
        for score_label in self.score_labels:
            for label in score_label:
                label.draw()

        self.back_button.draw()

    def check_if_button_clicked(self, mouse_pos):
        if self.back_button.check_bounds(mouse_pos) == True:
            self.toggle_visibility()


#######################################################################################################################
class MainMenu():
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.batch = None

        self.cx = int(self.width/2)
        self.cy = int(self.height/2)

        self.images = [  
            os.path.join(os.getcwd(), 'resources', 'Maze-Game-Menu.png'),
            os.path.join(os.getcwd(), 'resources', 'Setup-Screen.png')
        ]
        self.bg_stream1 = open(self.images[0], 'rb')
        self.bg_img1 = pyglet.image.load(self.images[0], file=self.bg_stream1)

        self.bg_stream2 = open(self.images[1], 'rb')
        self.bg_img2 = pyglet.image.load(self.images[1], file=self.bg_stream2)


        self.scores_menu = HighScores(self.width, self.height)
        self.game_setup = GameSetup(self.width, self.height)

        self.buttons = [
            Button((self.cx, self.height-250), 'Play'),
            Button((self.cx, self.height-400), 'High Scores'),
            Button((self.cx, self.height-550), 'Quit')
        ] 

    def draw(self):

        if self.game_setup.is_visibile == True:
            self.bg_img2.blit(0, 0)
            self.game_setup.draw()

    
        elif self.scores_menu.is_visibile == True:
            self.bg_img1.blit(0, 0)
            self.scores_menu.draw()


        # Draw main menu
        else:
            self.bg_img1.blit(0, 0)
            for button in self.buttons:
                button.draw()

    def check_if_button_clicked(self, mouse_pos):

        if self.game_setup.is_visibile == True:
            if self.game_setup.close_button.check_if_button_clicked(mouse_pos) == True:
                print("Closing Setup")
                self.game_setup.toggle_visibility()
            


        # Check if the back button was pressed when the scores menu is open
        if self.scores_menu.is_visibile == True:
            if self.scores_menu.check_if_button_clicked(mouse_pos) == True:
                print("Back button pressed")
                self.scores_menu.toggle_visibility()

        # Check for button press in the main menu screen
        else:

            for button in self.buttons:
                if button.check_bounds(mouse_pos) == True:
                    print('Button - {} was clicked.'.format(button.label_text))

                    if button.label_text == 'Play':
                        print('Showing Game Setup')
                        self.game_setup.toggle_visibility()

                    if button.label_text == 'High Scores':
                        print('Showing High Scores')
                        self.scores_menu.toggle_visibility()

                    if button.label_text == 'Quit':
                        print('Exiting application.')
                        pyglet.app.exit() 
                        sys.exit()


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