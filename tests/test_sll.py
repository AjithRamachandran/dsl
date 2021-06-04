import unittest
import numpy as np

from cdsl import sll, sllnode

class TestSll(unittest.TestCase):
    def test_sll(self):
        new_sll = sll()
        new_sll.insert(1, 0)
        new_sll.insert(2, 0)
        new_sll.insert(3, 0)
        new_sll.insert(4, 0)
        new_sll.insert(5, 0)
        new_sll.insert(6, 0)
        new_sll.insert(7, 0)
        new_sll.insert(6, 4)
        print(new_sll)
        print(new_sll.delete(4))
        print(new_sll, new_sll.length, new_sll.head, new_sll.tail)
        self.assertEqual(0, 0)

class TestSllNode(unittest.TestCase):
    def test_sll(self):
        new_sllnode = sllnode(10)
        print(new_sllnode, new_sllnode.value, new_sllnode.next )
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()