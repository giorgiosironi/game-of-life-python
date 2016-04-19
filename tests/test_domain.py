from gol import domain
from gol.domain import Cell

def test_true():
    assert 42 == domain.answer()

def test_cell_neighbors():
    cell = Cell(0, 0)
    neighbors = cell.neighbors()
    assert 8 == len(neighbors)
    for n in neighbors:
        assert abs(n.x()) <= 1
        assert abs(n.y()) <= 1
        assert not n == cell

