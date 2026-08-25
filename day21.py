numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("There is no second largest unique number.")
else:
    largest = max(unique_numbers)

    unique_numbers.remove(largest)

    second_largest = max(unique_numbers)

    print("Largest number =", largest)
    print("Second largest number =", second_largest)