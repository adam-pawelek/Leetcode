class Numbers:
    def __init__(self, value, position):
        self.value = value
        self.position = position

    def __lt__(self, other):
        return self.value < other.value


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        begin = 0
        end = len(nums) - 1

        numbers_list = []
        for i in range(len(nums)):
            numbers_list.append(Numbers(nums[i], i))

        numbers_list.sort()

        for i in numbers_list:
            print(i.value)

        begin = 0
        end = len(numbers_list) - 1

        while numbers_list[begin].value + numbers_list[end].value != target:
            if numbers_list[begin].value + numbers_list[end].value > target:
                end -= 1
            else:
                begin += 1

        return [numbers_list[begin].position, numbers_list[end].position]