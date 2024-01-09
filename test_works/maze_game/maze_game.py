import random
import time
import os
import platform

class MazeGame:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.player_pos = None
        self.exit_pos = None
        self.obstacle_positions = set()
        self.path_positions = set()
        self.generate_maze()
        self.generate_obstacles()

    @staticmethod
    def clear_screen():
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def generate_maze(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i == 0:
                    self.maze[i][j] = '_'
                elif i == self.rows - 1:
                    self.maze[i][j] = '_'
                elif j == 0:
                    self.maze[i][j] = '|'
                elif j == self.cols - 1:
                    self.maze[i][j] = '|'
                else:
                    self.maze[i][j] = ' '

        self.player_pos = self.place_random('E')
        self.exit_pos = self.place_random('X')
        self.generate_path()

    def generate_path(self):
        start_row, start_col = self.player_pos
        end_row, end_col = self.exit_pos
        current_row, current_col = start_row, start_col

        while (current_row, current_col) != (end_row, end_col):
            self.path_positions.add((current_row, current_col))
            direction = random.choice(['u', 'd', 'l', 'r'])

            if direction == 'u' and current_row > 1:
                current_row -= 1
            elif direction == 'd' and current_row < self.rows - 2:
                current_row += 1
            elif direction == 'l' and current_col > 1:
                current_col -= 1
            elif direction == 'r' and current_col < self.cols - 2:
                current_col += 1

            # Draw the path in the maze
            self.maze[current_row][current_col] = '#'

    def generate_obstacles(self, num_obstacles=5):
        for _ in range(num_obstacles):
            obstacle_pos = self.place_random('#', exclude_positions=self.path_positions)
            self.obstacle_positions.add(obstacle_pos)

    def place_random(self, symbol, exclude_positions=None):
        while True:
            row = random.randint(1, self.rows - 2)
            col = random.randint(1, self.cols - 2)
            if exclude_positions and (row, col) in exclude_positions:
                continue
            if self.maze[row][col] == ' ':
                self.maze[row][col] = symbol
                return (row, col)

    def display_maze(self):
        for row in self.maze:
            print(' '.join(map(str, row)))
        print()

    def move_player(self, direction):
        row, col = self.player_pos

        self.clear_screen()
        self.display_maze()

        if direction == 'u' and row > 1:
            row -= 1
        elif direction == 'd' and row < self.rows - 2:
            row += 1
        elif direction == 'l' and col > 1:
            col -= 1
        elif direction == 'r' and col < self.cols - 2:
            col += 1

        new_pos = (row, col)

        if new_pos in self.obstacle_positions:
            print("You hit an obstacle! Game over.")
            return False

        self.maze[self.player_pos[0]][self.player_pos[1]] = ' '
        self.maze[row][col] = 'P'
        self.player_pos = new_pos

        if self.player_pos == self.exit_pos:
            print("Congratulations! You reached the exit.")
            return True

        return True

def main():
    rows = 20
    cols = 20
    game = MazeGame(rows, cols)

    while True:
        game.display_maze()
        direction = input("Enter direction (up[u]/down[d]/left[l]/right[r]): ").lower()

        if direction in ['u', 'd', 'l', 'r']:
            if not game.move_player(direction):
                break
        else:
            print("Invalid direction. Please enter up/down/left/right.")

if __name__ == "__main__":
    main()
