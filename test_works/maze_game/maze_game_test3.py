import random
import time

class MazeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = None
        self.player_pos = None
        self.exit_pos = None
        self.obstacle_positions = None
        self.start_time = None
        self.generate_game()

    def generate_game(self):
        while True:
            self.player_pos = self.generate_random_position()
            self.exit_pos = self.generate_random_position(exclude_positions=[self.player_pos])

            self.maze = self.generate_maze(self.player_pos, self.exit_pos)
            self.obstacle_positions = self.generate_obstacles()

            # Check if there is a clear path from the starting point to the exit
            if self.has_clear_path(self.player_pos, self.exit_pos):
                break


    def generate_maze(self, player_pos, exit_pos):
        maze = [[1 for _ in range(self.width)] for _ in range(self.height)]

        def is_valid(x, y):
            return 0 <= x < self.width and 0 <= y < self.height and maze[y][x] == 1

        def carve_path(x1, y1, x2, y2):
            dx, dy = x2 - x1, y2 - y1
            nx, ny = x1, y1

            while (nx, ny) != (x2, y2):
                # Check if the new indices are within the valid range
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    maze[ny][nx] = 0

                nx += 2 * int(dx > 0) - 1
                ny += 2 * int(dy > 0) - 1



        # Carve a path from the player's position to the exit position
        carve_path(*player_pos, *exit_pos)

        return maze


    def has_clear_path(self, start, end):
        visited = set()

        def dfs(x, y):
            if (x, y) == end:
                return True

            visited.add((x, y))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in visited and self.maze[ny][nx] == 0:
                    if dfs(nx, ny):
                        return True

            return False

        return dfs(*start)

    def generate_random_position(self, exclude_positions=None):
        exclude_positions = exclude_positions or []
        
        while True:
            x, y = random.randrange(0, self.width, 2), random.randrange(0, self.height, 2)
            if (x, y) not in exclude_positions:
                return (x, y)


    def generate_obstacles(self, num_obstacles=5):
        obstacles = set()

        while len(obstacles) < num_obstacles:
            position = self.generate_random_position(exclude_positions=[self.player_pos, self.exit_pos])
            obstacles.add(position)

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
