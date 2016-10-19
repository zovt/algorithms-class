import sys


class Board:
    def __init__(self, lines, board=None):
        if board is None:
            _lines = list(filter(lambda x: x != '\n', lines))
            self.__size__ = len(_lines)
            self.__board__ = [[] for i in range(self.__size__)]
            for (idx, line) in enumerate(_lines):
                if line == "\n":
                    continue

                split = line.split(' ')
                nums = map(lambda x: int(x), split)
                self.__board__[idx] = list(nums)
        else:
            self.__size__ = board.__size__
            self.__board__ = board.__board__[:]

    def __str__(self):
        return "\n".join(list(map(lambda xs: " ".join(list(map("{}".format, xs))),
            self.__board__)))

    def set(self, x, y, val):
        self.__board__[y][x] = val

    def get(self, x, y):
        return self.__board__[y][x]

    def enumerate_possibilities(self, x, y):
        nums_in_row = list(filter(lambda x: x != 0, self.__board__[y]))
        nums_in_col = list(filter(lambda x: x != 0,
            map(lambda row: row[x], self.__board__)))

        used = nums_in_row + nums_in_col
        return list(filter(lambda x: x not in used, range(1, self.__size__ + 1)))

    def try_solve(self, x, y):
        # we are finished when y is out of the array bounds
        if y == self.__size__:
            return self

        cur_val = self.get(x, y)

        next_x = (x + 1) % (self.__size__)
        next_y = y if next_x > x else y + 1

        # skip non-zero entries
        if cur_val != 0:
            return self.try_solve(next_x, next_y)

        # gather the possible values at [x, y]
        possibilities = self.enumerate_possibilities(x, y)

        # for every possibility, set [x, y] equal to it and try to
        # solve the puzzle from the next index on
        for possibility in possibilities:
            self.set(x, y, possibility)
            res = self.try_solve(next_x, next_y)
            if res is not None:
                return res

        # If we are out of possibilities, reset [x, y]
        self.set(x, y, cur_val)
        return None

    def solve(self):
        return self.try_solve(0, 0)


def main():
    lines = sys.stdin.readlines()
    board = Board(lines)
    solved = board.solve()

    print(solved)

main()
