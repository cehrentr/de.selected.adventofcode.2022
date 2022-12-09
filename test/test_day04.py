import unittest
from day04.solution import AdventOfCodePuzzleDay04


class TestAdventOfCodePuzzleDay04(unittest.TestCase):

    def setUp(self) -> None:
        self.input_day04_example = []
        with open("./testdata/input_day04_example.txt", "r") as fil:
            self.input_day04_example = [line.strip() for line in fil]

        self.input_day04 = []
        with open("./testdata/input_day04.txt", "r") as fil:
            self.input_day04 = [line.strip() for line in fil]

    def test_solution_day04_puzzle_1_example(self):
        solution = AdventOfCodePuzzleDay04(self.input_day04_example).solve_puzzle_1()
        self.assertEqual(solution, 2)

    def test_solution_day04_puzzle_1(self):
        solution = AdventOfCodePuzzleDay04(self.input_day04).solve_puzzle_1()
        self.assertEqual(solution, 500)

    def test_solution_day04_puzzle_2_example(self):
        solution = AdventOfCodePuzzleDay04(self.input_day04_example).solve_puzzle_2()
        self.assertEqual(solution, 4)

    def test_solution_day04_puzzle_2(self):
        solution = AdventOfCodePuzzleDay04(self.input_day04).solve_puzzle_2()
        self.assertEqual(solution, 815)


if __name__ == "__main__":
    unittest.main(verbosity=True)
