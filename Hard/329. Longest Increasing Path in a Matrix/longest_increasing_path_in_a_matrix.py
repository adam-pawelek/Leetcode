class Solution:

    def __init__(self):
        self.matrix = []
        self.visisted_places = []  # -2 never visited, -1 visiteed , >= 0 - number of larger numbers
        self.maxx_y = None
        self.maxx_x = None

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.maxx_y = len(matrix)
        self.maxx_x = len(matrix[0])

        for i in range(self.maxx_y):
            help_list = [-2] * self.maxx_x
            self.visisted_places.append(help_list)

        print(self.visisted_places)

        maxx = 0
        for y in range(self.maxx_y):
            for x in range(self.maxx_x):
                maxx = max(maxx, self.dfs(x, y, -1000))

        print(self.visisted_places)

        return maxx

    def dfs(self, x: int, y: int, last_value) -> int:
        if x >= self.maxx_x or y >= self.maxx_y or x < 0 or y < 0:
            return 0

        if self.matrix[y][x] <= last_value:
            return 0

        print(x)
        print(y)
        if self.visisted_places[y][x] >= 0:
            return self.visisted_places[y][x] + 1

        self.visisted_places[y][x] = 0
        maxx = 0

        maxx = max(maxx, self.dfs(x + 1, y, self.matrix[y][x]))
        maxx = max(maxx, self.dfs(x, y + 1, self.matrix[y][x]))
        maxx = max(maxx, self.dfs(x - 1, y, self.matrix[y][x]))
        maxx = max(maxx, self.dfs(x, y - 1, self.matrix[y][x]))

        self.visisted_places[y][x] = maxx

        return maxx + 1










