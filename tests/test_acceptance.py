from gol import domain
from gol.domain import Generation
from gol.domain import ClassicRules

def test_rotating_bar():
    bar = Generation.horizontal_bar()
    assert Generation.vertical_bar() == bar.evolve(ClassicRules())
    assert bar == Generation.vertical_bar().evolve(ClassicRules())

def test_block():
    assert Generation.block() == Generation.block().evolve(ClassicRules())
