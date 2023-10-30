def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals by their start values
    merged_intervals = [list(intervals[0])]  # Convert the first interval to a list

    for i in range(1, len(intervals)):
        current_interval = list(intervals[i])  # Convert the current interval to a list
        last_merged = merged_intervals[-1]

        # Check for overlap and merge intervals if necessary
        if current_interval[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current_interval[1])
        else:
            merged_intervals.append(current_interval)

    total_length = sum(end - start for start, end in merged_intervals)
    return total_length

def sum_of_intervals2(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s

# Example usage:
intervals = [[1, 4], [7, 10], [3, 5]]
result = sum_of_intervals2(intervals)
print(result)  # Output: 7
