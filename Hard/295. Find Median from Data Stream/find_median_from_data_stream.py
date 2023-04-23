from queue import PriorityQueue


class MedianFinder:

    def __init__(self):
        self.maxqueue = PriorityQueue()  # store smallest elements (sorted bigger first)
        self.minqueue = PriorityQueue()  # store bigger elements ( sorted smallest first)
        self.count_numbers = 0
        self.count_max = 0
        self.count_min = 0

    def addNum(self, num: int) -> None:
        self.count_numbers += 1
        self.count_max += 1
        self.maxqueue.put((-num, num))
        if self.count_max - self.count_min > 1:
            take_number = self.maxqueue.get()
            put_number = (take_number[1], take_number[1])
            self.minqueue.put(put_number)
            self.count_max -= 1
            self.count_min += 1

        if self.minqueue.empty():
            return 0
        take_max = self.maxqueue.get()
        take_min = self.minqueue.get()
        print(take_max)
        print(take_min)

        if (take_max[1] > take_min[1]):
            self.maxqueue.put((-take_min[1], take_min[1]))
            self.minqueue.put((take_max[1], take_max[1]))

        else:
            self.maxqueue.put(take_max)
            self.minqueue.put(take_min)

        return None

    def findMedian(self) -> float:
        take_max = None
        take_min = None
        result = 0
        if self.count_numbers % 2 == 0:
            take_max = self.maxqueue.get()
            take_min = self.minqueue.get()
            result = (take_max[1] + take_min[1]) / 2
        else:
            take_max = self.maxqueue.get()
            result = take_max[1]

        if take_max:
            self.maxqueue.put(take_max)
        if take_min:
            self.minqueue.put(take_min)

        return result

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()