class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        result = 0

        i = 2

        while i * (i + 1) / 2 <= n:
            if ((n - i * (i + 1) / 2) % i == 0):
                result += 1
            i += 1

        return result + 1