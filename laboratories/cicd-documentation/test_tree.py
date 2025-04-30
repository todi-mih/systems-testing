import pytest
from node import Node
from tree import Tree

@pytest.fixture
def setup_tree():
    """ Fixture to set up a tree for testing """
    tree = Tree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)
    tree.add(12)
    tree.add(18)
    return tree

def test_find_existing_node(setup_tree):
    """ Test that the find method returns the correct node when the data exists """
    node = setup_tree.find(7)
    assert node is not None 
    assert node.data == 7  

def test_find_non_existing_node(setup_tree):
    """ Test that the find method returns None when the data does not exist """
    node = setup_tree.find(20)
    assert node is None 
