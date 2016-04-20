class Cell:
    def __init__(self, x, y):
        # TODO: idiomatic usage of fields and their scope
        self._x = x
        self._y = y

    def neighbors(self):
        # TODO: use list comprehension
        return frozenset([
            Cell(self._x-1, self._y-1),
            Cell(self._x-1, self._y),
            Cell(self._x-1, self._y+1),
            Cell(self._x, self._y-1),
            Cell(self._x, self._y+1),
            Cell(self._x+1, self._y-1),
            Cell(self._x+1, self._y),
            Cell(self._x+1, self._y+1),
        ])

    def candidates(self):
        return self.neighbors() | frozenset([self])

    def __eq__(self, another):
        return(self._x == another._x and self._y == another._y)

    def __hash__(self):
        return(self._x * 31 + self._y)

    def __str__(self):
        return("Cell({}, {})".format(self._x, self._y))

    def __repr__(self):
        return(self.__str__())

    def x(self):
        return(self._x)

    def y(self):
        return(self._y)

class State:
    alive = True
    dead = False

class ClassicRules:
    def next_state(self, state, alive_neighbors):
        if (state == State.alive):
            if (alive_neighbors >= 2 and alive_neighbors <= 3):
                return(State.alive)
        else:
            if (alive_neighbors == 3):
                return(State.alive)
        return(State.dead)

class Generation:
    @staticmethod
    def horizontal_bar():
        return(Generation(frozenset([Cell(-1, 0), Cell(0, 0), Cell(1, 0)])))
    @staticmethod
    def vertical_bar():
        return(Generation(frozenset([Cell(0, -1), Cell(0, 0), Cell(0, 1)])))
    @staticmethod
    def block():
        return(Generation(frozenset([Cell(0, 0), Cell(0, 1), Cell(1, 0), Cell(1, 1)])))
    def __init__(self, alive_cells):
        self._alive_cells = alive_cells
    def __eq__(self, another):
        return(self._alive_cells == another._alive_cells)
    def __repr__(self):
        return "Generation({})".format(self._alive_cells)
    def evolve(self, rules):
        # TODO: list comprehensions?
        candidates = frozenset()
        for cell in self._alive_cells:
            candidates = candidates.union(cell.candidates())
        alive = {c for c in candidates if (State.alive == rules.next_state(self._state(c), self._alive_neighbors(c)))}
        return Generation(frozenset(alive))
    def _state(self, cell):
        if cell in self._alive_cells:
            return(State.alive)
        else:
            return(State.dead)
    def _alive_neighbors(self, cell):
        return(len({n for n in cell.neighbors() if n in self._alive_cells}))
