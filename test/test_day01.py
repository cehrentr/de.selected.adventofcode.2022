import unittest
from day01.solution import AdventOfCodePuzzleDay01


class TestAdventOfCodePuzzleDay01(unittest.TestCase):

    def setUp(self) -> None:
        self.input_day01_example = []
        with open("./testdata/input_day01_example.txt", "r") as fil:
            self.input_day01_example = [line.strip() for line in fil]

        self.input_day01 = []
        with open("./testdata/input_day01.txt", "r") as fil:
            self.input_day01 = [line.strip() for line in fil]

    def test_solution_day01_puzzle_1_example(self):
        solution = AdventOfCodePuzzleDay01(self.input_day01_example).solve_puzzle_1()
        self.assertEqual(solution, 24000)

    def test_solution_day01_puzzle_1(self):
        solution = AdventOfCodePuzzleDay01(self.input_day01).solve_puzzle_1()
        self.assertEqual(solution, 70374)

    def test_solution_day01_puzzle_2_example(self):
        solution = AdventOfCodePuzzleDay01(self.input_day01_example).solve_puzzle_2()
        self.assertEqual(solution, 45000)

    def test_solution_day01_puzzle_2(self):
        solution = AdventOfCodePuzzleDay01(self.input_day01).solve_puzzle_2()
        self.assertEqual(solution, 204610)


if __name__ == "__main__":
    unittest.main(verbosity=True)
