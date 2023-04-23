from copy import deepcopy


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        sorted_arr = deepcopy(arr)
        sorted_arr.sort()
        poz = 0
        visited_numbers = {}
        result = 0
        for i in sorted_arr:
            visited_numbers[i] = 0

        for i in range(len(arr)):
            visited_numbers[arr[i]] += 1

            while poz < len(arr) and visited_numbers[sorted_arr[poz]] > 0:
                visited_numbers[sorted_arr[poz]] -= 1
                poz += 1

            if i + 1 == poz:
                result += 1

        return result