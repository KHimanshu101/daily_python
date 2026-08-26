#problem 1
def move_zeros(nums):
    position = 0

    for num in nums:
        if num != 0:
            nums[position] = num
            position += 1

    while position < len(nums):
        nums[position] = 0
        position += 1

    return nums


numbers = [0, 1, 0, 3, 12]

print(move_zeros(numbers))


#problem 2
def first_non_repeating(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for index, char in enumerate(text):
        if frequency[char] == 1:
            return char, index

    return None, -1


text = input("Enter a string: ")

character, index = first_non_repeating(text)

if character is not None:
    print("Character =", character)
    print("Index =", index)
else:
    print("No non-repeating character")


#problem 3
def two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    return []


numbers = [2, 7, 11, 15]
target = 9

print(two_sum(numbers, target))