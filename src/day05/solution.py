import re
from itertools import zip_longest


class AdventOfCodePuzzleDay05:
    """
    --- Day 5: Supply Stacks ---
    The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies
    are stored in stacks of marked crates, but because the needed supplies are buried under many other
    crates, the crates need to be rearranged.

    The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates
    get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps.
    After the crates are rearranged, the desired crates will be at the top of each stack.

    The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to
    ask her which crate will end up where, and they want to be ready to unload them as soon as possible, so they
    can embark.

    They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your
    puzzle input). For example:

            [D]
        [N] [C]
        [Z] [M] [P]
         1   2   3

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2

    In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom,
    and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D.
    Finally, stack 3 contains a single crate, P.

    Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved
    from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is
    moved from stack 2 to stack 1, resulting in this configuration:

        [D]
        [N] [C]
        [Z] [M] [P]
         1   2   3

    In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the
    first crate to be moved (D) ends up below the second and third crates:

                [Z]
                [N]
            [C] [D]
            [M] [P]
         1   2   3

    Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C
    ends up below crate M:

                [Z]
                [N]
        [M]     [D]
        [C]     [P]
         1   2   3

    Finally, one crate is moved from stack 1 to stack 2:

                [Z]
                [N]
                [D]
        [C] [M] [P]
         1   2   3

    The Elves just need to know which crate will end up on top of each stack; in this example, the top
    crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give
    the Elves the message CMZ.

    After the rearrangement procedure completes, what crate ends up on top of each stack?

    --- Part Two ---
    As you watch the crane operator expertly rearrange the crates, you notice the process isn't following
    your prediction.

    Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't
    a CrateMover 9000 - it's a CrateMover 9001.

    The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an
    extra cup holder, and the ability to pick up and move multiple crates at once.

    Again considering the example above, the crates begin in the same configuration:

            [D]
        [N] [C]
        [Z] [M] [P]
         1   2   3

    Moving a single crate from stack 2 to stack 1 behaves the same as before:

        [D]
        [N] [C]
        [Z] [M] [P]
         1   2   3

    However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay
    in the same order, resulting in this new configuration:

                [D]
                [N]
            [C] [Z]
            [M] [P]
         1   2   3

    Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

                [D]
                [N]
        [C]     [Z]
        [M]     [P]
         1   2   3

    Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

                [D]
                [N]
                [Z]
        [M] [C] [P]
         1   2   3

    In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

    Before the rearrangement process finishes, update your simulation so that the Elves know where they
    should stand to be ready to unload the final supplies. After the rearrangement procedure completes,
    what crate ends up on top of each stack?
    """

    CREATE_SIZE = 3

    def __init__(self, puzzle_input: list):
        self.stacks = puzzle_input

    def solve_puzzle_1(self) -> str:
        stacks, moves = self._get_stacks_and_moves()

        for move in moves:
            how_much = int(move[0])

            for i in range(how_much):
                stacks = self._move_one_crate(
                    stacks=stacks,
                    start=int(move[1]) - 1,
                    dest=int(move[2]) - 1
                )

        return "".join([stack[-1].replace("[", "").replace("]", "") for stack in stacks])

    def solve_puzzle_2(self) -> str:
        stacks, moves = self._get_stacks_and_moves()

        for move in moves:
            self._move_multiple_crate(
                stacks=stacks,
                start=int(move[1]) - 1,
                dest=int(move[2]) - 1,
                number_of_crates=int(move[0])
            )

        return "".join([stack[-1].replace("[", "").replace("]", "") for stack in stacks])

    def _get_stacks_and_moves(self) -> tuple:
        stacks = self._get_stack_informations(stacks=self.stacks)
        max_len_sublist = len(max(stacks, key=len))
        moves = self._get_stack_instructions(stacks=self.stacks, start=max_len_sublist + 2)

        return stacks, moves

    @staticmethod
    def _get_stack_instructions(stacks: list, start: int) -> list:
        result = []

        for item in stacks[start:]:
            instruction = re.sub("[^0-9 ]", "", item)
            result.append(instruction.strip().replace("  ", " ").split(" "))

        return result

    def _get_stack_informations(self, stacks: list) -> list:
        result = []

        for stack in stacks:
            if stack:
                j = 0
                line = []

                while j <= len(stack):
                    line.append(stack[j:j+3])
                    j += 4

                result.append(line)
            else:
                break

        return self._transpose(result[:-1])

    @staticmethod
    def _transpose(stacks: list) -> list:
        result = []
        mapped = list(map(list, zip_longest(*stacks)))

        for stack in mapped:
            line = []
            for crate in stack:
                if crate and crate.replace(" ", "") != "":
                    line.append(crate)
            line.reverse()
            result.append(line)

        return result

    @staticmethod
    def _move_one_crate(stacks: list, start: int, dest: int) -> list:
        crate = stacks[start].pop()
        stacks[dest].append(crate)

        return stacks

    @staticmethod
    def _move_multiple_crate(stacks: list, start: int, dest: int, number_of_crates: int) -> list:
        crates = stacks[start][number_of_crates*-1:]
        del stacks[start][number_of_crates*-1:]
        stacks[dest].extend(crates)

        return stacks
