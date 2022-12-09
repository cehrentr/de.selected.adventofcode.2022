import unittest
from day03.solution import AdventOfCodePuzzleDay03


class TestAdventOfCodePuzzleDay03(unittest.TestCase):

    def setUp(self) -> None:
        self.input_day03_example = []
        with open("./testdata/input_day03_example.txt", "r") as fil:
            self.input_day03_example = [line.strip() for line in fil]

        self.input_day03 = []
        with open("./testdata/input_day03.txt", "r") as fil:
            self.input_day03 = [line.strip() for line in fil]

    def test_solution_day_01_puzzle_1_example(self):
        solution = AdventOfCodePuzzleDay03(self.input_day03_example).solve_puzzle_1()
        self.assertEqual(solution, 157)

    def test_solution_day_01_puzzle_1(self):
        solution = AdventOfCodePuzzleDay03(self.input_day03).solve_puzzle_1()
        self.assertEqual(solution, 8394)

    def test_solution_day_01_puzzle_2_example(self):
        solution = AdventOfCodePuzzleDay03(self.input_day03_example).solve_puzzle_2()
        self.assertEqual(solution, 70)

    def test_solution_day_01_puzzle_2(self):
        solution = AdventOfCodePuzzleDay03(self.input_day03).solve_puzzle_2()
        self.assertEqual(solution, 2413)


if __name__ == "__main__":
    unittest.main(verbosity=True)
