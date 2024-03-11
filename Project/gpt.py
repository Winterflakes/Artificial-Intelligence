import random

class Agent:
    def __init__(self, is_pacman, position):
        self.is_pacman = is_pacman
        self.position = position
        self.is_ghost = not is_pacman
        self.score = 0

class PacManGame:
    def __init__(self):
        self.board = [['.' for _ in range(10)] for _ in range(10)]  # Initialize a 10x10 empty board
        self.agents = [Agent(True, (0, 0)), Agent(True, (9, 9)), Agent(False, (4, 4)), Agent(False, (5, 5))]  # Initialize Pac-Man and Ghosts
        self.food_dots = {(i, j) for i in range(10) for j in range(10)}  # Add food dots to the board
        self.max_moves = 3000
        self.move_count = 0

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def move_agent(self, agent, direction):
        x, y = agent.position
        if direction == 'up':
            new_x, new_y = x - 1, y
        elif direction == 'down':
            new_x, new_y = x + 1, y
        elif direction == 'left':
            new_x, new_y = x, y - 1
        elif direction == 'right':
            new_x, new_y = x, y + 1
        else:
            return False  # Invalid move

        if 0 <= new_x < 10 and 0 <= new_y < 10:
            agent.position = (new_x, new_y)
            return True
        else:
            return False  # Out of bounds move

    def play(self):
        while self.move_count < self.max_moves:
            self.move_count += 1
            pacman_moves = [(random.choice(['up', 'down', 'left', 'right']), agent) for agent in self.agents if agent.is_pacman]
            ghost_moves = [(random.choice(['up', 'down', 'left', 'right']), agent) for agent in self.agents if agent.is_ghost]

            for move, agent in pacman_moves + ghost_moves:
                if not self.move_agent(agent, move):
                    continue  # Invalid move, try again

                if agent.is_pacman:  # Pac-Man eats food dot
                    if agent.position in self.food_dots:
                        self.food_dots.remove(agent.position)
                        agent.score += 1
                else:  # Ghost eats Pac-Man
                    pacman_agents = [pacman for pacman in self.agents if pacman.is_pacman]
                    for pacman in pacman_agents:
                        if pacman.position == agent.position:
                            pacman.position = (0, 0)  # Move Pac-Man back to starting position
                            break

                if len(self.food_dots) <= 2:  # Win condition
                    print("Game Over: All food dots eaten.")
                    return

        # Game ends due to move limit
        print("Game Over: Move limit reached.")

    def print_scores(self):
        for agent in self.agents:
            print(f"{'Pac-Man' if agent.is_pacman else 'Ghost'} {agent.position}: {agent.score} points")


if __name__ == "__main__":
    game = PacManGame()
    game.play()
    game.print_board()
    game.print_scores()
