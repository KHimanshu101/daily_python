def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def dfs(row, col):
        # Check boundaries and water
        if (
            row < 0 or row >= rows or
            col < 0 or col >= cols or
            grid[row][col] == "0"
        ):
            return

        # Mark the land as visited
        grid[row][col] = "0"

        # Explore four directions
        dfs(row + 1, col)  # Down
        dfs(row - 1, col)  # Up
        dfs(row, col + 1)  # Right
        dfs(row, col - 1)  # Left

    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == "1":
                islands += 1
                dfs(row, col)

    return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print("Number of islands =", num_islands(grid))





from collections import deque


def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    # Build graph
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    # Courses with no prerequisites
    queue = deque()

    for course in range(num_courses):
        if indegree[course] == 0:
            queue.append(course)

    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        # Remove this course as a prerequisite
        for next_course in graph[course]:
            indegree[next_course] -= 1

            if indegree[next_course] == 0:
                queue.append(next_course)

    return completed == num_courses


num_courses = 2
prerequisites = [[1, 0]]

print("Can finish all courses?", can_finish(num_courses, prerequisites))