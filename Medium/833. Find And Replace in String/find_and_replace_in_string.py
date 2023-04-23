class Solution:

    def check_if_exist(self, indice, word, substring):
        for i in range(len(substring)):
            if i + indice >= len(word):
                return False

            if word[i + indice] != substring[i]:
                return False
        return True

    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        sources_position = []
        for i in range(len(sources)):
            if self.check_if_exist(indices[i], s, sources[i]):
                sources_position.append([indices[i], sources[i], targets[i]])

        sources_position.sort()
        word_position = 0
        list_position = 0
        ans_word = ""

        while word_position < len(s):

            if list_position == len(sources_position):
                ans_word = ans_word + s[word_position:]
                break

            if sources_position[list_position][0] == word_position:
                ans_word = ans_word + sources_position[list_position][2]
                word_position += len(sources_position[list_position][1])
                list_position += 1
            else:
                ans_word = ans_word + s[word_position]
                word_position += 1

        return ans_word




