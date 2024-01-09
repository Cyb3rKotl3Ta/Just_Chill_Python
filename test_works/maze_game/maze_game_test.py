import random
import time

class MazeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = self.generate_maze()
        self.player_pos = (1, 1)  # Starting position
        self.exit_pos = (width - 2, height - 2)  # Exit position
        self.obstacle_positions = self.generate_obstacles()
        self.start_time = None

    def generate_maze(self):
        maze = [[1 for _ in range(self.width)] for _ in range(self.height)]

        def is_valid(x, y):
            return 0 <= x < self.width and 0 <= y < self.height and maze[y][x] == 1

        def carve_path(x, y):
            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    maze[y + dy // 2][x + dx // 2] = 0  # Carve a path
                    maze[ny][nx] = 0
                    carve_path(nx, ny)

        start_x, start_y = random.randrange(0, self.width, 2), random.randrange(0, self.height, 2)
        carve_path(start_x, start_y)

        return maze

    def generate_obstacles(self, num_obstacles=5):
        obstacles = set()

        while len(obstacles) < num_obstacles:
            x, y = random.randint(1, self.width - 2), random.randint(1, self.height - 2)
            if (x, y) != self.player_pos and (x, y) != self.exit_pos:
                obstacles.add((x, y))

        return obstacles

    def print_maze(self):
        for row in range(self.height):
            for col in range(self.width):
                if (col, row) == self.player_pos:
                    print('P', end='')
                elif (col, row) == self.exit_pos:
                    print('X', end='')
                elif (col, row) in self.obstacle_positions:
                    print('#', end='')
                elif self.maze[row][col] == 1:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()

    def move_player(self, direction):
        x, y = self.player_pos
        new_x, new_y = x, y

        if direction == 'u' and y > 0:
            new_y -= 1
        elif direction == 'd' and y < self.height - 1:
            new_y += 1
        elif direction == 'l' and x > 0:
            new_x -= 1
        elif direction == 'r' and x < self.width - 1:
            new_x += 1

        # Check for wall collisions
        if (new_x, new_y) not in self.obstacle_positions and self.maze[new_y][new_x] != 1:
            self.player_pos = (new_x, new_y)

    def play_game(self):
        self.start_time = time.time()

        while self.player_pos != self.exit_pos:
            self.print_maze()
            direction = input("Enter direction (up[u]/down[d]/left[l]/right[r]): ").lower()
            self.move_player(direction)

        elapsed_time = time.time() - self.start_time
        print(f"Congratulations! You reached the exit in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    width, height = 21, 11  # Adjust the size of the maze as needed
    game = MazeGame(width, height)
    game.play_game()
