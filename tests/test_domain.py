from gol import domain
from gol.domain import Cell
from gol.domain import State
from gol.domain import ClassicRules

def test_true():
    assert 42 == domain.answer()

def test_cell_candidates():
    cell = Cell(0, 0)
    candidates = cell.candidates()
    assert 9 == len(candidates)
    for n in candidates:
        assert abs(n.x()) <= 1
        assert abs(n.y()) <= 1

def test_cell_neighbors():
    cell = Cell(0, 0)
    neighbors = cell.neighbors()
    assert 8 == len(neighbors)
    for n in neighbors:
        assert abs(n.x()) <= 1
        assert abs(n.y()) <= 1
        assert not n == cell

def test_rules_for_alive_cells():
    rules = ClassicRules()
    assert State.dead == rules.next_state(State.alive, 0)
    assert State.dead == rules.next_state(State.alive, 1)
    assert State.alive == rules.next_state(State.alive, 2)
    assert State.alive == rules.next_state(State.alive, 3)
    assert State.dead == rules.next_state(State.alive, 4)
    assert State.dead == rules.next_state(State.alive, 5)
    assert State.dead == rules.next_state(State.alive, 6)
    assert State.dead == rules.next_state(State.alive, 7)
    assert State.dead == rules.next_state(State.alive, 8)

def test_rules_for_dead_cells():
    rules = ClassicRules()
    assert State.dead == rules.next_state(State.dead, 0)
    assert State.dead == rules.next_state(State.dead, 1)
    assert State.dead == rules.next_state(State.dead, 2)
    assert State.alive == rules.next_state(State.dead, 3)
    assert State.dead == rules.next_state(State.dead, 4)
    assert State.dead == rules.next_state(State.dead, 5)
    assert State.dead == rules.next_state(State.dead, 6)
    assert State.dead == rules.next_state(State.dead, 7)
    assert State.dead == rules.next_state(State.dead, 8)
