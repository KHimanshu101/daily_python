def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # stores indexes

    for i, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print("Days to wait:", daily_temperatures(temperatures))




def spiral_order(matrix):
    if not matrix:
        return []

    result = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Left → Right
        for col in range(left, right + 1):
            result.append(matrix[top][col])

        top += 1

        # Top → Bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])

        right -= 1

        # Right → Left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])

            bottom -= 1

        # Bottom → Top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])

            left += 1

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Spiral order:", spiral_order(matrix))




def trap_rain_water(height):
    if not height:
        return 0

    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0

    water = 0

    while left < right:

        if height[left] <= height[right]:

            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1

        else:

            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -= 1

    return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print("Trapped rain water:", trap_rain_water(height))