def answer():
    return(42)

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
        return("Cell(%d, %d)" % (self._x, self._y))

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
