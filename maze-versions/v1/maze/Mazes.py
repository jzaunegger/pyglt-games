import pyglet, math, random

class Maze:
    # Function to construct a maze
    def __init__(self, window_size, cell_size, padding):
        self.playable_space = (window_size[0] - padding[0], window_size[1] - padding[1])
        self.cell_size = cell_size
        self.maze_padding = padding

        self.rows = int(self.playable_space[0] / self.cell_size)
        self.cols = int(self.playable_space[1] / self.cell_size)
        self.cells = []
        self.player = None

    # Return a copy of the maze cells
    def get_cells(self):
        return self.cells

    # Create an empty list of cells
    def initalize_cells(self):
        offset_x, offset_y = self.maze_padding[0], self.maze_padding[1]

        x = offset_x
        y = offset_y
        for j in range(self.rows):
            for i in range(self.cols):
                self.cells.append(Cell(x, y, i, j, self.cell_size))
                y += self.cell_size
            x += self.cell_size
            y = offset_y

    def index(self, i, j):
        if i < 0 or j < 0 or i > self.cols-1 or j > self.rows-1:
            return -1
        else:
            return i + j * self.cols

    def pick_neighbor(self, current_cell):
        neighbors = []

        top    = self.index(current_cell.i, current_cell.j+1)
        right  = self.index(current_cell.i+1, current_cell.j)
        bottom = self.index(current_cell.i, current_cell.j-1)
        left   = self.index(current_cell.i-1, current_cell.j)

        if top != -1 and self.cells[top].visited == False:
            neighbors.append(self.cells[top])

        if right != -1 and self.cells[right].visited == False:
            neighbors.append(self.cells[right])

        if bottom != -1 and self.cells[bottom].visited == False:
            neighbors.append(self.cells[bottom])

        if left != -1 and self.cells[left].visited == False:
            neighbors.append(self.cells[left])

        if len(neighbors) > 0:
            r = math.floor(random.randint(0, len(neighbors)-1))
            return neighbors[r]
        else:
            return None

    def remove_walls(self, current_cell, next_cell):
        x = current_cell.i - next_cell.i
        if x == 1:
            current_cell.walls[2] = False
            next_cell.walls[0] = False
        if x == -1:
            current_cell.walls[0] = False
            next_cell.walls[2] = False

        y = current_cell.j - next_cell.j
        if y == -1:
            current_cell.walls[1] = False
            next_cell.walls[3] = False
        if y == 1:
            current_cell.walls[3] = False
            next_cell.walls[1] = False

    def generate_maze(self):
        current_cell = self.cells[0]
        current_cell.visited = True
        attempts = 0
        self.isGen = False
        self.stack = []

        while self.isGen == False:
            next_cell = self.pick_neighbor(current_cell)

            if next_cell != None:
                next_cell.visited = True
                self.remove_walls(current_cell, next_cell)

                self.stack.append(current_cell)
                current_cell = next_cell
            elif len(self.stack) > 0:
                current_cell = self.stack.pop(len(self.stack)-1)
            else:
                self.isGen = False

            attempts += 1
            if attempts > 10000:
                self.isGen = True
        print("Generation completed in {} attempts.".format(attempts))     

    def create_player(self):
        start_cell = self.cells[0]
        player_pos = (start_cell.x + (self.cell_size / 2), start_cell.y + (self.cell_size / 2))
        self.player = Player(start_cell.i, start_cell.j, player_pos[0], player_pos[1], int(self.cell_size/2))

    def get_player(self):
        return self.player

    def remove_player(self):
        self.player = None




class Cell:
    # Construct a Cell
    def __init__(self, x, y, i, j, cell_size):
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.cell_size = cell_size
        self.visited = False
        self.walls = [True, True, True, True]
        
    # Display that cell
    def draw(self):
        pt1 = (self.x+self.cell_size, self.y )
        pt2 = (self.x+self.cell_size, self.y+self.cell_size )
        pt3 = (self.x, self.y+self.cell_size )
        pt4 = (self.x, self.y )

        bg = pyglet.shapes.Rectangle(pt4[0], pt4[1], self.cell_size, self.cell_size, color=(50, 50, 50))
        bg.draw()
    
        if self.walls[0] == True:
            top_line = pyglet.shapes.Line( pt2[0], pt2[1], pt3[0], pt3[1], width=1, color=(255, 255, 255))
            top_line.draw()

        if self.walls[1] == True:
            right_line =  pyglet.shapes.Line( pt1[0], pt1[1], pt2[0], pt2[1], width=1, color=(255, 255, 255))
            right_line.draw()

        if self.walls[2] == True:
            bottom_line = pyglet.shapes.Line( pt4[0], pt4[1], pt1[0], pt1[1], width=1, color=(255, 255, 255))
            bottom_line.draw()

        if self.walls[3] == True:
            left_line = pyglet.shapes.Line( pt3[0], pt3[1], pt4[0], pt4[1], width=1, color=(255, 255, 255))
            left_line.draw()


class Player:
    def __init__(self, i, j, x, y, radius):
        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.radius = radius
        self.step_size = 0
    
    def set_step_size(self, new_size):
        self.step_size = new_size

    def move(self, direction):
        pass

    def draw(self):
        player = pyglet.shapes.Circle(self.x, self.y, self.radius, segments=None, color=(255, 0, 0), batch=None, group=None)
        player.draw()