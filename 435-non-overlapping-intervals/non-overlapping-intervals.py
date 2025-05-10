class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return 0
        
        intervals.sort(key=lambda x: x[1])
    
        end = intervals[0][1]
        count = 0
    
        for i in range(1, n):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
    
        return count
     
        