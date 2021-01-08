import pyglet
from Mazes import *

class main(pyglet.window.Window):
    # Construct a new window
    def __init__(self):
        super(main, self).__init__(1200, 800, fullscreen=False)
        self.alive = 1
        self.current_maze = None
        self.player = None
        self.maze_cells = []
        self.current_score = 0

    def generate_maze(self):
        self.current_maze = Maze( (1200, 750), 25, (1, 1) )
        self.current_maze.initalize_cells()
        self.current_maze.generate_maze()
        self.maze_cells = self.current_maze.get_cells()

    # Draw Loop
    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = 0

    # Keyboard Handler
    def on_key_press(self, symbol, modifiers):
        print(symbol)

    # Draw GUI
    def draw_HUD(self):
        gui_bg = pyglet.shapes.Rectangle(0, 750, 1200, 50, color=(120, 120, 120))
        gui_bg.draw()

        gui_level_text = pyglet.text.Label(text='Level 1', font_name='Sans Serif', font_size=16, x=50, y=775, anchor_x='center', anchor_y='center')
        gui_level_text.draw()

        gui_time_text = pyglet.text.Label(text='00:00:01', font_name='Sans Serif', font_size=16, x=600, y=775, anchor_x='center', anchor_y='center')
        gui_time_text.draw()

        gui_score_text = pyglet.text.Label(text='Score', font_name='Sans Serif', font_size=16, x=1000, y=775, anchor_x='center', anchor_y='center')
        gui_score_text.draw()
        
    # Render the application out to the screen 
    def render(self):
        # Clear the screen
        self.clear()

        # Draw the HUD
        self.draw_HUD()

        # Draw the maze
        if len(self.maze_cells) > 0:
            for cell in self.maze_cells:
                cell.draw()

        # For the wiindow
        self.flip()

    # Function to run the application
    def run(self):
        self.generate_maze()
        while self.alive == 1:
            self.render()
            event = self.dispatch_events()

x = main()
x.run()
