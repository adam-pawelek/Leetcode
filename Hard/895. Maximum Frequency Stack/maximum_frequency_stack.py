from queue import PriorityQueue

class FreqStack:

    def __init__(self):
        self.count_on_stack = {}
        self.prio_queue = PriorityQueue()
        self.time = 0
        self.data_time = {}

    def push(self, val: int) -> None:
        if val not in self.count_on_stack:
            self.count_on_stack[val] = 1
        else:
            self.count_on_stack[val] += 1

        self.prio_queue.put((-self.count_on_stack[val], -self.time, val))
        self.data_time[val] = self.time
        self.time += 1

    def pop(self) -> int:

        my_data = self.prio_queue.get()
        self.count_on_stack[my_data[2]] -= 1

        return my_data[2]

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()