def longest_unique_substring(s):
    characters = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in characters:
            characters.remove(s[left])
            left += 1

        characters.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


text = input("Enter a string: ")

result = longest_unique_substring(text)

print("Length of longest substring =", result)



def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Product of all elements to the left
    prefix = 1

    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Product of all elements to the right
    suffix = 1

    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


numbers = [1, 2, 3, 4]

print(product_except_self(numbers))




def is_valid_parentheses(s):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in "({[":
            stack.append(char)

        else:
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


text = input("Enter parentheses: ")

print(is_valid_parentheses(text))