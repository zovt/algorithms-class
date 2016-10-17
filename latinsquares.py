import sys

class Board:
    def __init__(self, lines, board = None):
        if board == None:
            self.__size__ = len(lines)
            self.__board__ = [[] for i in range(self.__size__)]
            for (idx, line) in enumerate(lines):
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

    def enumerate_possibilities(self, x, y):
        nums_in_row = list(filter(lambda x: x != 0, self.__board__[y]))
        nums_in_col = list(filter(lambda x: x != 0, 
            map(lambda row: row[x], self.__board__)))

        used = nums_in_row + nums_in_col
        return list(filter(lambda x: x not in used, range(1, self.__size__ + 1)))

    def try_solve(self, x, y):
        # print("---------------------")
        # print("{}".format(self))
        # print("x: {}".format(x))
        # print("y: {}".format(y))

        if x == self.__size__ - 1 and y == self.__size__ - 1:
            return

        next_x = (x + 1) % (self.__size__)
        next_y = y if next_x > x else y + 1

        if self.__board__[y][x] != 0:
            self.try_solve(next_x, next_y)

        # print(" --- zero! --- ")

        possibilities = self.enumerate_possibilities(x, y)
        # print(possibilities)
        for possibility in possibilities:
            self.set(x, y, possibility)
            self.try_solve(next_x, next_y)

        self.set(x, y, 0)

    def solve(self):
        return self.try_solve(0, 0)


def main():
    lines = sys.stdin.readlines()
    board = Board(lines)
    print(board)
    board.solve()
    
    print(board)

main()
