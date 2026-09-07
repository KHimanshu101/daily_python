def find_missing_number(nums):
    n = len(nums)
    result = n

    for i, num in enumerate(nums):
        result ^= i
        result ^= num

    return result


numbers = [3, 0, 1]

print("Missing number =", find_missing_number(numbers))




def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    max_length = 0

    first_occurrence = {}

    for i, num in enumerate(nums):
        prefix_sum += num

        # Subarray from index 0 to i
        if prefix_sum == k:
            max_length = i + 1

        # Check whether prefix_sum - k appeared before
        if prefix_sum - k in first_occurrence:
            length = i - first_occurrence[prefix_sum - k]
            max_length = max(max_length, length)

        # Store only the first occurrence
        if prefix_sum not in first_occurrence:
            first_occurrence[prefix_sum] = i

    return max_length


numbers = [10, 5, 2, 7, 1, 9]
k = 15

print("Longest subarray length =", longest_subarray_sum_k(numbers, k))






def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        previous = merged[-1]

        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)

    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print("Merged intervals =", merge_intervals(intervals))