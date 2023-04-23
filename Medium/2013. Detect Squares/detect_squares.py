class DetectSquares:
    def __init__(self):
        self.points = []
        self.point_exist = {}

    def add(self, point: List[int]) -> None:
        point = (point[0], point[1])
        self.points.append(point)

        if point not in self.point_exist:
            self.point_exist[point] = 1
        else:
            self.point_exist[point] += 1

    def count(self, point: List[int]) -> int:
        result = 0
        for p in self.points:
            if p[0] == point[0] or p[1] == point[1]:
                continue

            if (p[0], point[1]) in self.point_exist and (point[0], p[1]) in self.point_exist:
                if abs(p[0] - point[0]) == abs(p[1] - point[1]):
                    result += self.point_exist[(p[0], point[1])] * self.point_exist[(point[0], p[1])]

        return result

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)