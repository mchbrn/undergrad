import numpy as np
from random import seed
from random import randrange

class Automaton:
    def __init__(self, number, name, x, y, population, edges):
        self.number = number
        self.name = name
        self.x = x - 1
        self.y = y - 1
        self.coordinates = np.zeros((x,y), dtype=object)
        self.state = 1
        self.population = population
        self.capacity = round(((x * y) / 3.0))
        self.edges = edges
        self.edges_number_of = len(edges)

    def getHost(self, x, y):
        host = self.coordinates[x][y]
        return host

    def setHost(self, host):
        empty_cells = np.where(self.coordinates == 0)
        seed()
        index = randrange(0, len(empty_cells[0]), 1)
        x = empty_cells[0][index]
        y = empty_cells[1][index]
        self.coordinates[x][y] = host
        self.population += 1
        location_new = [x, y]
        return location_new

    def atCapacity(self):
        if self.population >= self.capacity:
            return True
        else:
            return False

    def getEdges(self):
        return self.edges

    def getEdgesNumberOf(self):
        return self.edges_number_of

    def move(self, x_current, y_current):
        cell_current = x_current, y_current
        cells_available, cells_taken = self.getNeighbourhood(cell_current)

        if cells_available:
            location_new = self.changeCell(x_current, y_current, cells_available)
            return location_new
        else:
            location_current = [x_current, y_current]
            return location_current

    def changeCell(self, x_current, y_current, cells_available):
        seed()
        cells_available_number_of = len(cells_available)
        cell_new_index = randrange(0, cells_available_number_of)
        cell_new = cells_available[cell_new_index]
        x_new, y_new = cell_new
        # move host to new cell
        self.coordinates[x_new][y_new] = self.coordinates[x_current][y_current]
        # set old cell to empty
        self.coordinates[x_current][y_current] = 0
        location_new = [x_new, y_new]
        return location_new

    def removeHost(self, x_current, y_current):
        self.coordinates[x_current][y_current] = 0
        self.population -= 1

    def transmit(self, x_current, y_current):
        infections = []
        cell = [x_current, y_current]
        cells_available, cells_taken = self.getNeighbourhood(cell)
        for cell in cells_taken:
            x, y = cell
            host = self.getHost(x, y)
            host_state = host.state
            if host_state == 0:
                infection = host.infect()
                if infection:
                    infection.append(self.number)
                    infections.append(infection)

        return infections

    def getNeighbourhood(self, cell):
        x, y = cell
        cells_available = []
        cells_taken = []
        neighbourhood = []

        # bottom left corner
        if x == 0 and y == 0:
            for i in range(x, x+2, 1):
                for j in range(y, y+2, 1):
                    if not self.coordinates[i][j]:
                        cells_available.append([i,j])
                    else:
                        cells_taken.append([i,j])
        # top left corner
        elif x == 0 and y == self.y:
            for i in range(x, x+2, 1):
                for j in range(y-1, y+1, 1):
                    if not self.coordinates[i][j]:
                        cells_available.append([i,j])
                    else:
                        cells_taken.append([i,j])
        # top right corner
        elif x == self.x and y == self.y:
            for i in range(x-1, x+1, 1):
                for j in range(y-1, y+1, 1):
                    if not self.coordinates[i][j]:
                        cells_available.append([i,j])
                    else:
                        cells_taken.append([i,j])
        # bottom right corner
        elif x == self.x and y == 0:
            for i in range(x-1, x+1, 1):
                for j in range(y, y+2, 1):
                    if not self.coordinates[i][j]:
                        cells_available.append([i,j])
                    else:
                        cells_taken.append([i,j])
        # bottom middle
        elif y == 0:
            for i in range(x-1, x+2, 1):
                for j in range(y, y+2, 1):
                    if not self.coordinates[i][j]:
                        cells_available.append([i,j])
                    else:
                        cells_taken.append([i,j])
        # left middle
        elif x == 0:
            for i in range(x, x+2, 1):
                for j in range(y-1, y+2, 1):
                    if not self.coordinates[i][j]:
                        cells_available.append([i,j])
                    else:
                        cells_taken.append([i,j])
        # top middle
        elif y == self.y:
            for i in range(x-1, x+2, 1):
                for j in range(y-1, y+1, 1):
                    if not self.coordinates[i][j]:
                        cells_available.append([i,j])
                    else:
                        cells_taken.append([i,j])
        # right middle
        elif x == self.x:
            for i in range(x-1, x+1, 1):
                for j in range(y-1, y+2, 1):
                    if not self.coordinates[i][j]:
                        cells_available.append([i,j])
                    else:
                        cells_taken.append([i,j])
        # middle
        else:
            for i in range(x-1, x+2, 1):
                for j in range(y-1, y+2, 1):
                    if not self.coordinates[i][j]:
                        cells_available.append([i,j])
                    else:
                        cells_taken.append([i,j])

        neighbourhood.append(cells_available)
        neighbourhood.append(cells_taken)
        return neighbourhood


    def unlock(self):
        self.state = 1

    def lock(self):
        self.state = 0

