marks = []

for i in range(5):
    mark = float(input(f"Enter marks of subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
percentage = (total / 500) * 100

passed = all(mark >= 40 for mark in marks)

print("\n----- Result -----")
print(f"Total Marks = {total}")
print(f"Average = {average:.2f}")
print(f"Percentage = {percentage:.2f}%")

if passed:
    print("Result = Pass")
else:
    print("Result = Fail")