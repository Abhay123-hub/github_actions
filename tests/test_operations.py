from src.math_operations import add,sub

def test_add():
    assert add(2,3) ==5
    assert add(5,2) == 7
    assert add(3,7) ==10

def test_sub():
    assert sub(3,2) ==1
    assert(6,3) ==3
    assert(8,4) == 4
