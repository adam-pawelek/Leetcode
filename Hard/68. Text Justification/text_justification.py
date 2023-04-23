class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        row_size = maxWidth
        result = []
        row_words = []
        row_sentence = ""
        words.append("")

        for i in words:
            if row_size == maxWidth and i != "":
                row_size -= len(i)
                row_words.append(i)
            elif row_size - len(i) - 1 >= 0 and i != "":
                row_size -= (len(i) + 1)
                row_words.append(i)
            elif i == "":
                print(row_words)
                row_sentence = " ".join(row_words)
                row_sentence += " " * (row_size)
                result.append(row_sentence)
            else:
                if len(row_words) == 1:
                    row_sentence = row_words[0] + " " * (row_size)
                else:
                    number_of_spaces = (row_size + (len(row_words) - 1))
                    print("number of spaces" + str(number_of_spaces))
                    modulo_spaces = number_of_spaces % (len(row_words) - 1)
                    number_of_spaces = number_of_spaces // (len(row_words) - 1)

                    for j in range(len(row_words) - 1):
                        row_sentence += row_words[j]
                        row_sentence += " " * (number_of_spaces)
                        row_sentence += " " if modulo_spaces > 0 else ""
                        modulo_spaces = modulo_spaces - 1 if modulo_spaces > 0 else 0

                    row_sentence += row_words[-1]
                print(row_words)
                print(len(row_words))
                result.append(row_sentence)

                row_words = []
                row_sentence = ""
                row_size = maxWidth

                row_size -= len(i)
                row_words.append(i)

        return result