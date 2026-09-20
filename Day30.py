def character_frequency(text):
    frequency = {}

    # Count each character
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    # Sort by frequency in descending order
    sorted_frequency = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_frequency


text = input("Enter a string: ")

result = character_frequency(text)

print("Character frequencies:")
for char, count in result:
    print(char, ":", count)







def longest_run(text):
    if not text:
        return 0

    current_count = 1
    max_count = 1

    for i in range(1, len(text)):

        if text[i] == text[i - 1]:
            current_count += 1
        else:
            current_count = 1

        max_count = max(max_count, current_count)

    return max_count


text = input("Enter a string: ")

print("Longest consecutive run =", longest_run(text))









def can_reach_end(nums):
    farthest = 0

    for i in range(len(nums)):

        # If current index cannot be reached
        if i > farthest:
            return False

        # Update the farthest reachable position
        farthest = max(farthest, i + nums[i])

        # We can already reach the end
        if farthest >= len(nums) - 1:
            return True

    return True


numbers = [2, 3, 1, 1, 4]

print("Can reach the last index?", can_reach_end(numbers))