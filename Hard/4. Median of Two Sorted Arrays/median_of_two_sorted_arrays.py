class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        lenght1 = len(nums1)
        lenght2 = len(nums2)

        half = (len(nums1) + len(nums2)) // 2

        begin = -1
        end = lenght1

        nums1.append(float(inf))
        nums1.append(float(inf))
        nums2.append(float(inf))
        nums2.append(float(inf))

        print(half)

        while True:
            middle = (end + begin) // 2
            i = middle
            j = half - 2 - i
            print(i, j)
            elem1 = nums1[i] if i >= 0 else float("-inf")
            next1 = nums1[i + 1] if i + 1 >= 0 else float("-inf")

            if j >= lenght2:
                elem2 = float(inf)
                next2 = float(inf)
            else:
                elem2 = nums2[j] if j >= 0 else float("-inf")
                next2 = nums2[j + 1] if j + 1 >= 0 else float("-inf")

            print(elem1, next1, elem2, next2)

            if elem1 <= next2 and elem2 <= next1:
                if (lenght1 + lenght2) % 2 == 0:
                    maxx = max(elem1, elem2)
                    minn = min(next1, next2)
                    return ((minn + maxx) / 2)
                else:
                    return min(next1, next2)

            elif elem1 > next2:
                end = middle

            else:
                begin = middle



