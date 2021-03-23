import unittest

from linked_list import LinkedListException, LinkedList, Empty, Cell


class TestIsEmptyAndLength(unittest.TestCase):

    def test_empty_is_empty(self):
        self.assertTrue(Empty().is_empty())

    def test_cell_is_empty(self):
        self.assertFalse(Cell(1, Empty()).is_empty())

    def test_empty_length(self):
        self.assertEqual(Empty().length(), 0)

    def test_cell_length(self):
        self.assertEqual(Cell(1, Cell(2, Empty())).length(), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
