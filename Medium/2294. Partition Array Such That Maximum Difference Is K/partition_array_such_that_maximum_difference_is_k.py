class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()
        minn = nums[0]
        maxx = nums[0]
        result = 1

        for num in nums:
            minn = min(minn, num)
            maxx = max(maxx, num)

            if maxx - minn > k:
                result += 1
                minn = num
                maxx = num

        if maxx - minn > k:
            result += 1

        return result



