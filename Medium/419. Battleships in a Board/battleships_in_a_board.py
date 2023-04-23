from collections import deque


class Solution(object):

    def __init__(self):
        self.visited_board = []

    def check_conditions(self, y, x, board):
        if x < 0 or y < 0 or y >= len(board) or x >= len(board[0]):
            return False

        if self.visited_board[y][x] == 1:
            return False

        if board[y][x] == ".":
            return False

        return True

    def bfs(self, y, x, board):
        if not self.check_conditions(y, x, board):
            return 0

        self.visited_board[y][x] = 1
        que = deque()
        que.append((y, x))

        while len(que) > 0:
            position = que.popleft()

            self.visited_board[position[0]][position[1]] = 1

            if self.check_conditions(position[0] + 1, position[1], board):
                que.append((position[0] + 1, position[1]))

            if self.check_conditions(position[0], position[1] + 1, board):
                que.append((position[0], position[1] + 1))

            if self.check_conditions(position[0] - 1, position[1], board):
                que.append((position[0] - 1, position[1]))

            if self.check_conditions(position[0], position[1] - 1, board):
                que.append((position[0], position[1] - 1))

        return 1

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        for i in range(len(board)):
            new_list = [0] * len(board[0])
            self.visited_board.append(new_list)

        result = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                result += self.bfs(i, j, board)

        return result
