def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):

        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicate values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


numbers = [-1, 0, 1, 2, -1, -4]

print("Triplets:", three_sum(numbers))






import heapq


def top_k_frequent(nums, k):
    frequency = {}

    # Count frequencies
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # Create a min-heap
    heap = []

    for num, count in frequency.items():
        heapq.heappush(heap, (count, num))

        # Keep only k elements
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]


numbers = [1, 1, 1, 2, 2, 3]
k = 2

print("Top", k, "frequent elements:", top_k_frequent(numbers, k))





def word_break(s, word_dict):
    word_set = set(word_dict)

    dp = [False] * (len(s) + 1)

    # Empty string can always be formed
    dp[0] = True

    for i in range(1, len(s) + 1):

        for j in range(i):

            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]


s = "leetcode"
word_dict = ["leet", "code"]

print("Can the string be segmented?", word_break(s, word_dict))