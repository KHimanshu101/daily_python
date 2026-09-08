def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


numbers = [2, 2, 1, 1, 1, 2, 2]

print("Majority element =", majority_element(numbers))




def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]

print("Maximum profit =", max_profit(prices))




def group_anagrams(words):
    groups = {}

    for word in words:
        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))