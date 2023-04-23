class Solution:

    def __init__(self):
        self.substring_dict = {}
        self.word_dict = {}
        self.result_dict = {}
        self.result = []
        self.matrix = None
        self.input_word = None
        self.m = None
        self.n = None
        self.was_already = []
        self.first_letters = {}

    def check_if_substring(self, created_word):
        is_substring = False
        if created_word in self.substring_dict:
            is_substring = True

        if created_word in self.word_dict and created_word not in self.result_dict:
            self.result.append(created_word)
            self.result_dict[created_word] = 1
            self.input_word.remove(created_word)

        return is_substring

    def word_backtracking(self, y, x, created_word):
        if x >= self.m or y >= self.n or x < 0 or y < 0 or self.was_already[y][x]:
            return 0

        created_word += self.matrix[y][x]
        if not self.check_if_substring(created_word):
            return 0

        self.was_already[y][x] = True

        self.word_backtracking(y + 1, x, created_word)
        self.word_backtracking(y - 1, x, created_word)
        self.word_backtracking(y, x + 1, created_word)
        self.word_backtracking(y, x - 1, created_word)

        self.was_already[y][x] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.matrix = board
        self.input_word = words

        self.m = len(self.matrix[0])
        self.n = len(self.matrix)

        for i in range(self.n):
            self.was_already.append([False] * self.m)

        for i in words:
            self.word_dict[i] = 1
            self.first_letters[i[0]] = 1
            for j in range(len(i)):
                self.substring_dict[i[0:(j + 1)]] = 1

        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j] in self.first_letters:
                    self.word_backtracking(i, j, "")

        return self.result

