import random

def generate_maze(width, height):
    # Initialize maze with walls
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and maze[y][x] == 1

    def carve_path(x, y):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                maze[y + dy // 2][x + dx // 2] = 0  # Carve a path
                maze[ny][nx] = 0
                carve_path(nx, ny)

    start_x, start_y = random.randrange(0, width, 2), random.randrange(0, height, 2)
    carve_path(start_x, start_y)

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(["#" if cell == 1 else " " for cell in row]))

if __name__ == "__main__":
    width, height = 21, 11  # Adjust the size of the maze as needed
    maze = generate_maze(width, height)
    print_maze(maze)
