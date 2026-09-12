def find_peak_element(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            # Peak must be on the right
            left = mid + 1
        else:
            # Peak is at mid or on the left
            right = mid

    return left


numbers = [1, 2, 3, 1]

index = find_peak_element(numbers)

print("Peak index =", index)
print("Peak value =", numbers[index])




def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Maximum subarray sum =", max_subarray(numbers))







def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for current_amount in range(1, amount + 1):

        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


coins = [1, 2, 5]
amount = 11

print("Minimum number of coins =", coin_change(coins, amount))