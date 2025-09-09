def is_path_clear(grid, start_x, start_y, end_x, end_y):
    """
    Checks if a direct path in a simple grid is clear (no obstacles).
    (Simplified example, actual pathfinding uses more complex algorithms like A*)
    Args:
        grid (list of lists): The grid representing the environment.
        start_x (int): Starting X coordinate.
        start_y (int): Starting Y coordinate.
        end_x (int): Ending X coordinate.
        end_y (int): Ending Y coordinate.
    Returns:
        bool: True if the path is clear, False otherwise.
    """
    # For simplicity, let's assume a straight line path for this example
    # In a real scenario, this would involve a pathfinding algorithm
    if start_x == end_x:
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            if grid[y][start_x] == 0: # Obstacle
                return False
    elif start_y == end_y:
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            if grid[start_y][x] == 0: # Obstacle
                return False

    return True
robot_environment_grid = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1]
]
path_1_clear = is_path_clear(robot_environment_grid, 0, 0, 0, 2)
print(f"Path from (0,0) to (0,2) clear: {path_1_clear}") # Should be True

path_2_clear = is_path_clear(robot_environment_grid, 0, 0, 3, 0)
print(f"Path from (0,0) to (3,0) clear: {path_2_clear}") # Should be False due to obstacle at (3,0)
