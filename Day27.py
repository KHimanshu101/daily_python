def max_water(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])

        area = width * current_height
        max_area = max(max_area, area)

        # Move the pointer with the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print("Maximum water =", max_water(heights))




def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:

        # Start only if num is the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


numbers = [100, 4, 200, 1, 3, 2]

print("Longest consecutive sequence =", longest_consecutive(numbers))



def search_rotated_array(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:

            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


numbers = [4, 5, 6, 7, 0, 1, 2]
target = 0

print("Target index =", search_rotated_array(numbers, target))