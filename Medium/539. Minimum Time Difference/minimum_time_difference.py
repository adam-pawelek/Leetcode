class Solution:

    def minimal_time_diffrence(self,a: str,b: str) -> int:
        midnight  = 24 *60 

        a_h = int(a[0:2])
        a_min = int(a[3:])
        b_h = int(b[0:2])
        b_min = int(b[3:])

        a = a_h * 60 + a_min
        b = b_h * 60 + b_min
        val1 = abs(a-b) 
        val2 = midnight  - max(a,b) + min (a,b)
        return min(val1,val2)


    def findMinDifference(self, timePoints: List[str]) -> int:
        min_value = 10**9
        timePoints.sort()
        print()
        
        for i in range(len(timePoints)):
            min_value = min(min_value, self.minimal_time_diffrence(timePoints[i], timePoints[(i+1) % len(timePoints)])) 

        return min_value
