def merge_intervals(intervals:list)->list:
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals

    
    def get_start(interval):
        return interval[0]

   
    intervals.sort(key=get_start)

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])  
        else:
            merged.append(current)

    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))


intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))