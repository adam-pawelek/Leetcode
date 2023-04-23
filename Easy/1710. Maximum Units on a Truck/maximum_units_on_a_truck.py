class TruckBox:

    def __init__(self, box_value, number_of_boxes):
        self.box_value = box_value
        self.number_of_boxes = number_of_boxes

    def __lt__(self, other):
        return self.box_value > other.box_value


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        box_list = []
        for i in range(len(boxTypes)):
            box = TruckBox(boxTypes[i][1], boxTypes[i][0])
            box_list.append(box)

        box_list.sort()

        result = 0

        while len(box_list) > 0:
            if box_list[0].number_of_boxes < truckSize:
                result += box_list[0].number_of_boxes * box_list[0].box_value
                truckSize -= box_list[0].number_of_boxes
                box_list.pop(0)
            else:
                result += box_list[0].box_value * truckSize
                return result

        return result