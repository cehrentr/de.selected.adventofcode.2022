import unittest
from day05.solution import AdventOfCodePuzzleDay05


class TestAdventOfCodePuzzleDay05(unittest.TestCase):

    def setUp(self) -> None:
        self.input_day05_example = []
        with open("./testdata/input_day05_example.txt", "r") as fil:
            self.input_day05_example = [line.rstrip() for line in fil]

        self.input_day05 = []
        with open("./testdata/input_day05.txt", "r") as fil:
            self.input_day05 = [line.rstrip() for line in fil]

    def test_solution_day05_puzzle_1_example(self):
        solution = AdventOfCodePuzzleDay05(self.input_day05_example).solve_puzzle_1()
        self.assertEqual("CMZ", solution)

    def test_solution_day05_puzzle_1(self):
        solution = AdventOfCodePuzzleDay05(self.input_day05).solve_puzzle_1()
        self.assertEqual("LBLVVTVLP", solution)

    def test_solution_day05_puzzle_2_example(self):
        solution = AdventOfCodePuzzleDay05(self.input_day05_example).solve_puzzle_2()
        self.assertEqual("MCD", solution)

    def test_solution_day05_puzzle_2(self):
        solution = AdventOfCodePuzzleDay05(self.input_day05).solve_puzzle_2()
        self.assertEqual("TPFFBDRJD", solution)


if __name__ == "__main__":
    unittest.main(verbosity=True)
