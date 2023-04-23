class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        time = 0
        new_nums = []
        for num in nums:
            if num > 0:
                new_nums.append(num)

        nums = new_nums

        while len(nums) > 0:
            new_nums = []
            minn = min(nums)
            for i in range(len(nums)):
                if nums[i] - minn > 0:
                    new_nums.append(nums[i] - minn)

            nums = new_nums
            time += 1
            # print(nums)

        return time





