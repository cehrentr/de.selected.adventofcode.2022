import unittest
from day02.solution import AdventOfCodePuzzleDay02


class TestAdventOfCodePuzzleDay02(unittest.TestCase):

    def setUp(self) -> None:
        self.input_day02_example = []
        with open("./testdata/input_day02_example.txt", "r") as fil:
            self.input_day02_example = [line.strip() for line in fil]

        self.input_day02 = []
        with open("./testdata/input_day02.txt", "r") as fil:
            self.input_day02 = [line.strip() for line in fil]

    def test_solution_day_01_puzzle_1_example(self):
        solution = AdventOfCodePuzzleDay02(self.input_day02_example).solve_puzzle_1()
        self.assertEqual(solution, 15)

    def test_solution_day_01_puzzle_1(self):
        solution = AdventOfCodePuzzleDay02(self.input_day02).solve_puzzle_1()
        self.assertEqual(solution, 9651)

    def test_solution_day_01_puzzle_2_example(self):
        solution = AdventOfCodePuzzleDay02(self.input_day02_example).solve_puzzle_2()
        self.assertEqual(solution, 12)

    def test_solution_day_01_puzzle_2(self):
        solution = AdventOfCodePuzzleDay02(self.input_day02).solve_puzzle_2()
        self.assertEqual(solution, 10560)


if __name__ == "__main__":
    unittest.main(verbosity=True)
