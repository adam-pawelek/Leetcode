from queue import PriorityQueue


class Solution:
    def __init__(self):
        self.count_num = {}
        self.current_num = []
        self.prio_queue = PriorityQueue()
        self.result = []

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        for i in range(k):
            self.prio_queue.put((-nums[i], nums[i]))
            if nums[i] in self.count_num:
                self.count_num[nums[i]] += 1
            else:
                self.count_num[nums[i]] = 1

        maxx = self.prio_queue.get()[1]
        self.prio_queue.put((-maxx, maxx))

        self.result.append(maxx)

        for i in range(k, len(nums)):
            self.prio_queue.put((-nums[i], nums[i]))

            self.count_num[nums[i - k]] -= 1
            if nums[i] in self.count_num:
                self.count_num[nums[i]] += 1
            else:
                self.count_num[nums[i]] = 1

            maxx = self.prio_queue.get()[1]
            while self.count_num[maxx] == 0:
                maxx = self.prio_queue.get()[1]

            self.prio_queue.put((-maxx, maxx))
            self.result.append(maxx)

        return self.result
