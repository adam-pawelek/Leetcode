class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        count_letters_w1 = {}
        count_letters_w2 = {}

        for i in range(ord('a'), ord('z') + 1):
            count_letters_w1[chr(i)] = 0
            count_letters_w2[chr(i)] = 0

        for i in range(len(s)):
            count_letters_w1[s[i]] += 1
            count_letters_w2[t[i]] += 1

        for i in range(ord('a'), ord('z') + 1):
            if count_letters_w1[chr(i)] != count_letters_w2[chr(i)]:
                return False

        return True