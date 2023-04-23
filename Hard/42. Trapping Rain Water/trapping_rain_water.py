class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        arr_size = len(height)
        right_max[arr_size - 1] = height[arr_size - 1]

        for i in range(arr_size - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        result = 0

        for i in range(arr_size):
            result += min(left_max[i], right_max[i]) - height[i]

        return result