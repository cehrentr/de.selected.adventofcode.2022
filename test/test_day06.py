import unittest
from day06.solution import AdventOfCodePuzzleDay06


class TestAdventOfCodePuzzleDay06(unittest.TestCase):

    def setUp(self) -> None:
        self.input_day06_example = ""
        with open("./testdata/input_day06_example.txt", "r") as fil:
            self.input_day06_example = fil.read()

        self.input_day06 = ""
        with open("./testdata/input_day06.txt", "r") as fil:
            self.input_day06 = fil.read()

    def test_solution_day06_puzzle_1_example(self):
        solution = AdventOfCodePuzzleDay06(self.input_day06_example).solve_puzzle_1()
        self.assertEqual(7, solution)

    def test_solution_day06_puzzle_1(self):
        solution = AdventOfCodePuzzleDay06(self.input_day06).solve_puzzle_1()
        self.assertEqual(1100, solution)

    def test_solution_day06_puzzle_2_example(self):
        solution = AdventOfCodePuzzleDay06(self.input_day06_example).solve_puzzle_2()
        self.assertEqual(19, solution)

    def test_solution_day06_puzzle_2(self):
        solution = AdventOfCodePuzzleDay06(self.input_day06).solve_puzzle_2()
        self.assertEqual(2421, solution)


if __name__ == "__main__":
    unittest.main(verbosity=True)
