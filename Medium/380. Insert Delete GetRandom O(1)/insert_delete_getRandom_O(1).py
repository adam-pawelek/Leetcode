class RandomizedSet:

    def __init__(self):

        self.values_position = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.values_position:
            return False
        self.values.append(val)
        self.values_position[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values_position:
            return False
        position = self.values_position[val]
        val_len = len(self.values) - 1
        self.values[position], self.values[val_len] = self.values[val_len], self.values[position]
        self.values_position[self.values[position]] = position
        self.values.pop()
        del (self.values_position[val])
        return True

    def getRandom(self) -> int:
        result = random.randint(0, len(self.values) - 1)
        return self.values[result]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()