class Solution:

    def __init__(self):
        self.word_dict = {}

    def is_in_list(self, word) -> bool:
        dp = [False] * (len(word) + 1)
        dp[0] = True
        for i in range(len(word)):
            if (dp[i] == 1):
                for j in range(i, len(word) + 1):
                    if (word[i:j] in self.word_dict and j - i != len(word)):
                        dp[j] = True
        return dp[-1]

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        for i in words:
            if len(i) > 0:
                self.word_dict[i] = 1

        result = []

        for i in words:
            if len(i) > 0 and self.is_in_list(i):
                result.append(i)

        return result