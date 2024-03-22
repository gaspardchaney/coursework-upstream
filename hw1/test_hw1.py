"""
CMSC 14200
Spring 2024

Test code for Homework #1
"""

import task1
import task2
import task3
import task4
import task5
import pytest

from tree import TreeNode


@pytest.mark.parametrize("list_of_dicts, expected",
                         [([{"b": 2}], ("b", 1)),
                          ([{"a": 1, "b": 2}, {"a": 3}], ("a", 2)),
                          ([{"b": 1, "c": 2}, {"a": 3, "c": 4}], ("c", 2)),
                          ([{"a": 1, "b": 2, "c": 3}, {"a": 3, "c": 1}, {"c": 4, "b": 2}], ("c", 3)),
                          ([{"a": 1, "b": 2}, {"a": 3}, {"c": 2}, {"a": 2, "b": 3}], ("a", 3)),
                          ([{"a": 1, "b": 2}, {"a": 3}, {"c": 2, "b": 3}, {"d": 2, "b": 3}], ("b", 3))])
def test_task1(list_of_dicts: list[dict[str, int]], expected: tuple[str, int]) -> None:
    """Do a single test for Task 1: count_words"""
    assert task1.most_common_key(list_of_dicts) == expected

def make_t1() -> TreeNode:
    """
         3
       /   \
      4     1
     / \   / \
    5   1 4   3
    """
    n1 = TreeNode(3)
    n2 = TreeNode(4); n3 = TreeNode(1)
    n4 = TreeNode(5); n5 = TreeNode(1); n6 = TreeNode(4); n7 = TreeNode(3)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    return n1

def make_t2() -> TreeNode:
    """
         1
       /   \
      2     3
     / \   / \
    4   1 3   2
    """
    n1 = TreeNode(1)
    n2 = TreeNode(2); n3 = TreeNode(3)
    n4 = TreeNode(4); n5 = TreeNode(1); n6 = TreeNode(3); n7 = TreeNode(2)

    n1.add_child(n2); n1.add_child(n3)
    n2.add_child(n4); n2.add_child(n5)
    n3.add_child(n6); n3.add_child(n7)

    return n1

def compare_paths_unordered(paths1: list[list[int]], paths2: list[list[int]]) -> bool:
    """
    Compares two lists of paths, ignoring the order of the paths
    """

    # hack for no-paths case
    if paths2 == [[]]:
        return (paths1 == []) or (paths1 ==[[]])

    if len(paths1) != len(paths2):
        return False

    for path in paths1:
        if path not in paths2:
            return False

    return True

    
@pytest.mark.parametrize("tree, weight, expected",
    [[TreeNode(4), 4, [[4]]],
     [TreeNode(4), 5, [[]]],
     [make_t1(), 7, [[3, 4], [3, 1, 3]]],
     [make_t1(), 8, [[3, 4, 1], [3, 1, 4]]],
     [make_t2(), 4, [[1, 2, 1], [1, 3]]],
     [make_t2(), 7, [[1, 2, 4], [1, 3, 3]]]])
def test_task3_get_paths(tree: TreeNode, weight: int, expected: list[list[int]])  -> None:
    """Do a single test for Task 3: get_paths"""
    assert tree is not None
    assert compare_paths_unordered(task3.get_paths(tree, weight), expected)


def test_task4_sphere_1() -> None:
    s = task4.Sphere(1)
    assert abs(s.surface_area() - 12.56636) < 0.1
    
def test_task4_sphere_2() -> None:
    s = task4.Sphere(2)
    assert abs(s.surface_area() - 50.26544) < 0.1
    
def test_task4_sphere_3() -> None:
    s = task4.Sphere(10)
    assert abs(s.surface_area() - 1256.636) < 0.1

def test_task4_sphere_4() -> None:
    s = task4.Sphere(1)
    assert abs(s.volume() - 4.188786666666667) < 0.1
    
def test_task4_sphere_5() -> None:
    s = task4.Sphere(2)
    assert abs(s.volume() - 33.510293333333333) < 0.1
    
def test_task4_sphere_6() -> None:
    s = task4.Sphere(10)
    assert abs(s.volume() - 4188.786666666666667) < 0.1

def test_task4_sphere_7() -> None:
    with pytest.raises(ValueError):
        s = task4.Sphere(-13)

def test_task4_box_1() -> None:
    b = task4.Box(1, 2, 3)
    assert abs(b.surface_area() - 22) < 0.1
    
def test_task4_box_2() -> None:
    b = task4.Box(4, 5, 6)
    assert abs(b.surface_area() - 148) < 0.1
    
def test_task4_box_3() -> None:
    b = task4.Box(7, 9, 11)
    assert abs(b.surface_area() - 478) < 0.1

def test_task4_box_4() -> None:
    b = task4.Box(1, 2, 3)
    assert abs(b.volume() - 6) < 0.1
    
def test_task4_box_5() -> None:
    b = task4.Box(4, 5, 6)
    assert abs(b.volume() - 120) < 0.1
    
def test_task4_box_6() -> None:
    b = task4.Box(7, 9, 11)
    assert abs(b.volume() - 693) < 0.1

def test_task4_box_7() -> None:
    with pytest.raises(ValueError):
        b = task4.Box(-13, 6, 8)

def test_task4_box_8() -> None:
    with pytest.raises(ValueError):
        b = task4.Box(4, -13, 8)
        
def test_task4_box_9() -> None:
    with pytest.raises(ValueError):
        b = task4.Box(4, 6, -13)


def test_task5_box_1() -> None:
    b = task5.OrientedBox(7, 9, 11, "HW", 13)
    assert abs(b.surface_area() - 478) < 0.1
    assert abs(b.volume() - 693) < 0.1
    
def test_task5_box_2() -> None:
    b = task5.OrientedBox(7, 9, 11, "HW", 13)
    assert abs(b.pressure() - 143) < 0.1
    
def test_task5_box_3() -> None:
    b = task5.OrientedBox(7, 9, 11, "HD", 13)
    assert abs(b.pressure() - 117) < 0.1

def test_task5_box_4() -> None:
    b = task5.OrientedBox(7, 9, 11, "WD", 13)
    assert abs(b.pressure() - 91) < 0.1

def test_task5_box_5() -> None:
    with pytest.raises(ValueError):
        b = task5.OrientedBox(-13, 6, 8, "HW", 13)
    with pytest.raises(ValueError):
        b = task5.OrientedBox(4, -13, 8, "HW", 13)
    with pytest.raises(ValueError):
        b = task5.OrientedBox(4, 6, -13, "HW", 13)

def test_task5_box_6() -> None:
    with pytest.raises(ValueError):
        b = task5.OrientedBox(4, 6, 8, "QZ", 13)
    with pytest.raises(ValueError):
        b = task5.OrientedBox(4, 6, 8, "HW", -13)

