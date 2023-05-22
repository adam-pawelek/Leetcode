class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                new_word.append(word1[i])
            if i < len(word2):
                new_word.append(word2[i])
        
        return ''.join(new_word)
