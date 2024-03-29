from task1 import *
from task2 import *
from task3 import *
from task4 import *
from trees import *

BST = BSTEmpty | BSTNode

def test_task1_1() -> None:
    s = StrNode("Hello, world!")
    assert s.is_const()
    assert s.num_nodes() == 1
    assert s.eval() == "Hello, world!"
    assert str(s) == '"Hello, world!"'

def test_task1_2() -> None:
    s1 = StrNode("Hello")
    s2 = StrNode(" World")
    op = Concatenate(s1, s2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert op.eval() == "Hello World"
    assert str(op) == 'Concatenate("Hello", " World")'

def test_task1_3() -> None:
    s1 = StrNode("Foo")
    s2 = StrNode("Bar")
    s3 = StrNode("Baz")
    op = Concatenate(s1, Concatenate(s2, s3))
    assert not op.is_const()
    assert op.num_nodes() == 5
    assert op.eval() == "FooBarBaz"
    assert str(op) == 'Concatenate("Foo", Concatenate("Bar", "Baz"))'

def test_task1_4() -> None:
    s = StrNode("hello")
    op = Upper(s)
    assert not op.is_const()
    assert op.num_nodes() == 2
    assert op.eval() == "HELLO"
    assert str(op) == 'Upper("hello")'

def test_task1_5() -> None:
    s = StrNode("Hello, world!")
    op = Upper(s)
    assert not op.is_const()
    assert op.num_nodes() == 2
    assert op.eval() == "HELLO, WORLD!"
    assert str(op) == 'Upper("Hello, world!")'

def test_task1_6() -> None:
    s1 = StrNode("Bye")
    op = Repeat(s1, 1)
    assert not op.is_const()
    assert op.num_nodes() == 2
    assert op.eval() == "Bye"
    assert str(op) == 'Repeat("Bye", 1)'

def test_task1_7() -> None:
    s1 = StrNode("Bye")
    op = Repeat(s1, 3)
    assert not op.is_const()
    assert op.num_nodes() == 2
    assert op.eval() == "ByeByeBye"
    assert str(op) == 'Repeat("Bye", 3)'

def test_task1_8() -> None:
    s1 = StrNode("cmsc")
    s2 = StrNode(" 142")
    s3 = StrNode("0")

    op = Concatenate(Upper(s1), Concatenate(s2, Repeat(s3, 2)))
    assert not op.is_const()
    assert op.num_nodes() == 7
    assert op.eval() == "CMSC 14200"
    assert str(op) == 'Concatenate(Upper("cmsc"), Concatenate(" 142", Repeat("0", 2)))'
    

def test_task2_1() -> None:
    bst = BSTEmpty()
    assert valid_bst(bst)

def test_task2_2() -> None:
    values = [1]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert valid_bst(bst)

def test_task2_3() -> None:
    values = [1, 2]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert valid_bst(bst)

def test_task2_4() -> None:
    values = [2, 1]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert valid_bst(bst)

def test_task2_5() -> None:
    values = [2, 1, 3]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert valid_bst(bst)

def test_task2_6() -> None:
    values = [1, 2, 3]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert valid_bst(bst)

def test_task2_7() -> None:
    values = [3, 2, 1]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert valid_bst(bst)

def test_task2_8() -> None:
    values = [4, 2, 6, 1, 3, 5, 7]
    bst: BST = BSTEmpty()
    for v in values:
        bst = bst.insert(v)
    assert valid_bst(bst)

def test_task2_9() -> None:
    empty = BSTEmpty()
    bst = BSTNode(0, BSTNode(1, empty, empty), empty)
    assert not valid_bst(bst)

def test_task2_10() -> None:
    empty = BSTEmpty()
    bst = BSTNode(0, empty, BSTNode(-1, empty, empty))
    assert not valid_bst(bst)

def test_task2_11() -> None:
    empty = BSTEmpty()
    bst = BSTNode(0,
            BSTNode(-2,
              BSTNode(10, empty, empty),
              BSTNode(-1, empty, empty)),
            BSTNode(2,
              BSTNode(1, empty, empty),
              BSTNode(3, empty, empty)))
    assert not valid_bst(bst)

def test_task2_12() -> None:
    empty = BSTEmpty()
    bst = BSTNode(0,
            BSTNode(-2,
              BSTNode(-3, empty, empty),
              BSTNode(-10, empty, empty)),
            BSTNode(2,
              BSTNode(1, empty, empty),
              BSTNode(3, empty, empty)))
    assert not valid_bst(bst)

def test_task2_13() -> None:
    empty = BSTEmpty()
    bst = BSTNode(0,
            BSTNode(-2,
              BSTNode(-3, empty, empty),
              BSTNode(-1, empty, empty)),
            BSTNode(2,
              BSTNode(10, empty, empty),
              BSTNode(3, empty, empty)))
    assert not valid_bst(bst)
    
def test_task2_14() -> None:
    empty = BSTEmpty()
    bst = BSTNode(0,
            BSTNode(-2,
              BSTNode(-3, empty, empty),
              BSTNode(-1, empty, empty)),
            BSTNode(2,
              BSTNode(1, empty, empty),
              BSTNode(-10, empty, empty)))
    assert not valid_bst(bst)
    
def test_task2_15() -> None:
    empty = BSTEmpty()
    bst = BSTNode(0,
            BSTNode(-2,
              BSTNode(-3, empty, empty),
              BSTNode(1, empty, empty)),
            BSTNode(2,
              BSTNode(1, empty, empty),
              BSTNode(3, empty, empty)))
    assert not valid_bst(bst)
    
def test_task2_16() -> None:
    empty = BSTEmpty()
    bst = BSTNode(0,
            BSTNode(-2,
              BSTNode(-3, empty, empty),
              BSTNode(-1, empty, empty)),
            BSTNode(2,
              BSTNode(-1, empty, empty),
              BSTNode(3, empty, empty)))
    assert not valid_bst(bst)


def test_task3_1() -> None:
    bst = BSTEmptyOpt()
    assert bst.span is None

def test_task3_2() -> None:
    values = [4, 2, 6, 1, 3, 5, 7]
    bst: BSTEmptyOpt | BSTNodeOpt = BSTEmptyOpt()
    for v in values:
        bst = bst.insert(v)
    assert bst.span == (1, 7)

def test_task3_3() -> None:
    values = [4, 2, 1, 3, 6, 5, 7]
    bst: BSTEmptyOpt | BSTNodeOpt = BSTEmptyOpt()
    for v in values:
        bst = bst.insert(v)
    assert bst.span == (1, 7)
    for v in values:
        assert bst.contains(v)
    assert not bst.contains(0)
    assert not bst.contains(8)

def test_task3_4() -> None:
    values = [4, 5, 6, 3]
    bst: BSTEmptyOpt | BSTNodeOpt = BSTEmptyOpt()
    for v in values:
        bst = bst.insert(v)
    assert bst.span == (3, 6)
    for v in values:
        assert bst.contains(v)
    assert not bst.contains(2)
    assert not bst.contains(7)

def test_task3_5() -> None:
    values = [2, 3, 4, 5, 6]
    bst: BSTEmptyOpt | BSTNodeOpt = BSTEmptyOpt()
    for v in values:
        bst = bst.insert(v)
    assert bst.span == (2, 6)
    for v in values:
        assert bst.contains(v)
    assert not bst.contains(1)
    assert not bst.contains(7)

def test_task3_6() -> None:
    values =[0, 3, 5, 2, 9, 4, 8, 6, 1, 7]
    bst: BSTEmptyOpt | BSTNodeOpt = BSTEmptyOpt()
    for v in values:
        bst = bst.insert(v)
    assert bst.span == (0, 9)
    for v in values:
        assert bst.contains(v)
    assert not bst.contains(-1)
    assert not bst.contains(10)

def test_task3_7() -> None:
    values =[6, 3, 2, 4, 9, 5, 7, 8]
    bst: BSTEmptyOpt | BSTNodeOpt = BSTEmptyOpt()
    for v in values:
        bst = bst.insert(v)
    assert bst.span == (2, 9)
    for v in values:
        assert bst.contains(v)
    assert not bst.contains(1)
    assert not bst.contains(10)
    
def test_task3_8() -> None:
    values = [2, 7, 6, 8, 3, 4, 5]
    bst: BSTEmptyOpt | BSTNodeOpt = BSTEmptyOpt()
    for v in values:
        bst = bst.insert(v)
    assert bst.span == (2, 8)
    for v in values:
        assert bst.contains(v)
    assert not bst.contains(1)
    assert not bst.contains(9)
    
def test_task3_9() -> None:
    values =[5, 3, 10, 6, 9, 8, 7, 2, 4]
    bst: BSTEmptyOpt | BSTNodeOpt = BSTEmptyOpt()
    for v in values:
        bst = bst.insert(v)
    assert bst.span == (2, 10)
    for v in values:
        assert bst.contains(v)
    assert not bst.contains(1)
    assert not bst.contains(11)
    
def test_task3_10() -> None:
    values = [8, 5, 7, 9, 6]
    bst: BSTEmptyOpt | BSTNodeOpt = BSTEmptyOpt()
    for v in values:
        bst = bst.insert(v)
    assert bst.span == (5, 9)
    for v in values:
        assert bst.contains(v)
    assert not bst.contains(4)
    assert not bst.contains(10)


def test_task4_1() -> None:
    b = Board(3, 3)
    assert b.is_consistent

def test_task4_2() -> None:
    b = Board(3, 3)
    b.location_of_pieces["Black"] = [(0, 0), (0, 1)]
    assert b.is_consistent

def test_task4_3() -> None:
    b = Board(3, 3)
    b.location_of_pieces["Black"] = [(0, 0), (0, 1), (2, 2)]
    b.location_of_pieces["White"] = [(1, 1), (1, 2), (0, 2), (2, 0)]
    assert b.is_consistent

def test_task4_4() -> None:
    b = Board(3, 3)
    b.location_of_pieces["Black"] = [(0, 0), (0, 1), (2, 2)]
    b.location_of_pieces["White"] = [(1, 1), (1, 2), (2, 0)]
    b.location_of_pieces["Red"] =   [(0, 2), (1, 0)]
    assert b.is_consistent

def test_task4_5() -> None:
    b = Board(3, 3)
    b.location_of_pieces["Black"] = [(0, 0), (0, 1), (2, 2)]
    b.location_of_pieces["White"] = [(1, 1), (1, 2), (2, 2), (2, 0)]
    assert not b.is_consistent

def test_task4_6() -> None:
    b = Board(3, 3)
    b.location_of_pieces["Black"] = [(0, 0), (0, 1), (2, 2)]
    b.location_of_pieces["White"] = [(1, 1), (2, 0), (0, 2), (2, 0)]
    assert not b.is_consistent
