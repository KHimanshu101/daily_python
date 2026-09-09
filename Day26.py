def max_product_subarray(nums):
    current_max = nums[0]
    current_min = nums[0]
    result = nums[0]

    for num in nums[1:]:
        # A negative number swaps the roles of max and min
        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        result = max(result, current_max)

    return result


numbers = [2, 3, -2, 4]

print("Maximum product =", max_product_subarray(numbers))






def longest_palindrome(s):
    if not s:
        return ""

    start = 0
    end = 0

    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    for i in range(len(s)):
        # Odd-length palindrome
        left1, right1 = expand_from_center(i, i)

        # Even-length palindrome
        left2, right2 = expand_from_center(i, i + 1)

        if right1 - left1 > end - start:
            start = left1
            end = right1

        if right2 - left2 > end - start:
            start = left2
            end = right2

    return s[start:end + 1]


text = input("Enter a string: ")

print("Longest palindromic substring =", longest_palindrome(text))







def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0

    frequency = {
        0: 1
    }

    for num in nums:
        prefix_sum += num

        required = prefix_sum - k

        if required in frequency:
            count += frequency[required]

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    return count


numbers = [1, 1, 1]
k = 2

print("Number of subarrays =", subarray_sum(numbers, k))