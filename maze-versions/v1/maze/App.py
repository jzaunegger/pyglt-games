import pyglet
from Mazes import *

window = pyglet.window.Window(width=1200, height=800)
maze = Maze((1200, 800), 25, (12, 12))
maze.initalize_cells()
maze.generate_maze()
maze.create_player()
player = maze.get_player()
maze_cells = maze.get_cells()

# Keyboard Handler
def on_key_press(symbol, modifiers):
    print(modifiers, symbol)

@window.event
def on_draw():
    window.clear()

    for cell in maze_cells:
        cell.draw()
    
    player.draw()

# Run the app
def main():
    pyglet.app.run()

# When file loads, run main function
if __name__ == '__main__':
    main()