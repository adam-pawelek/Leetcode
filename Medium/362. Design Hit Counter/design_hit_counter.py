from collections import deque

class HitCounter:

    def __init__(self):
        self.timestamp_queue = deque()
        self.counter = 0

    def hit(self, timestamp: int) -> None:
        self.timestamp_queue.append(timestamp)
        self.counter += 1

    def getHits(self, timestamp: int) -> int:
        # print(self.timestamp_queue[0])
        while (self.counter > 0 and timestamp - self.timestamp_queue[0] >= 300):
            self.timestamp_queue.popleft()
            self.counter -= 1
        return self.counter

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)