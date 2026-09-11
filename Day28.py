def rotate_array(nums, k):
    n = len(nums)

    k = k % n

    # Reverse the entire array
    nums.reverse()

    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])

    # Reverse the remaining elements
    nums[k:] = reversed(nums[k:])

    return nums


numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3

print("Rotated array =", rotate_array(numbers, k))



def merge_sorted_arrays(nums1, nums2):
    i = 0
    j = 0
    merged = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    return merged


nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]

print("Merged array =", merge_sorted_arrays(nums1, nums2))





def house_robber(nums):
    previous_two = 0
    previous_one = 0

    for money in nums:
        current = max(previous_one, previous_two + money)

        previous_two = previous_one
        previous_one = current

    return previous_one


houses = [2, 7, 9, 3, 1]

print("Maximum money =", house_robber(houses))