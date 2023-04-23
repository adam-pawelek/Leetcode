class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        max_result = 0

        while (start != end):
            result = min(height[start], height[end]) * (end - start)
            max_result = max(max_result, result)

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_result
