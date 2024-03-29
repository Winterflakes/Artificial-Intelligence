import pygame
import sys

# Define constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BLOCK_SIZE = 20
PACMAN_COLOR = (255, 255, 0)
GHOST_COLOR = (255, 0, 0)
FOOD_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)
FOOD_POINTS = 10

class Character:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Pacman(Character):
    def __init__(self, x, y):
        super().__init__(x, y, PACMAN_COLOR)
        self.respawn_timer = 0

    def transform_to_ghost(self):
        return Ghost(self.x, self.y)

    def respawn(self):
        self.x = 5
        self.y = 5
        self.respawn_timer = pygame.time.get_ticks()

class Ghost(Character):
    def __init__(self, x, y):
        super().__init__(x, y, GHOST_COLOR)

    def transform_to_pacman(self):
        return Pacman(self.x, self.y)

class Food(Character):
    def __init__(self, x, y):
        super().__init__(x, y, FOOD_COLOR)

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def draw_character(character, screen):
    pygame.draw.circle(screen, character.color, (character.x * BLOCK_SIZE + BLOCK_SIZE // 2, character.y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pacman Game")
    clock = pygame.time.Clock()

    pacman = Pacman(5, 5)
    ghost = Ghost(15, 5)
    foods = [Food(10, 5), Food(12, 5), Food(14, 5), Food(16, 5)]  # Example: Food distribution

    start_time = pygame.time.get_ticks()
    total_time = 3000  # Total time allowed in seconds
    left_score = 0
    right_score = 0

    while True:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move characters
        ghost.move(-1, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            pacman.move(0, -1)
        if keys[pygame.K_DOWN]:
            pacman.move(0, 1)
        if keys[pygame.K_LEFT]:
            pacman.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            pacman.move(1, 0)

        # Check if Pacman crosses the mid of the game frame
        if pacman.x >= SCREEN_WIDTH // BLOCK_SIZE:
            ghost = pacman.transform_to_ghost()

        # Check if Ghost crosses the mid of the game frame
        if ghost.x <= SCREEN_WIDTH // BLOCK_SIZE:
            pacman = ghost.transform_to_pacman()

        # Check if Ghost catches Pacman
        if manhattan_distance(pacman.x, pacman.y, ghost.x, ghost.y) <= 5:
            print("Ghost caught Pacman! Respawn...")
            pacman.respawn()

        # Respawn Pacman after a certain time
        respawn_time_passed = (pygame.time.get_ticks() - pacman.respawn_timer) / 1000
        if respawn_time_passed >= 3:  # Respawn time in seconds
            pacman.respawn_timer = 0

        # Check for food eaten
        for food in foods:
            if pacman.x == food.x and pacman.y == food.y:
                foods.remove(food)
                if food.x <= SCREEN_WIDTH // (2 * BLOCK_SIZE):
                    left_score += FOOD_POINTS
                else:
                    right_score += FOOD_POINTS

        # Draw characters and food
        draw_character(pacman, screen)
        draw_character(ghost, screen)
        for food in foods:
            draw_character(food, screen)

        pygame.display.flip()
        clock.tick(10)

        # Check game end condition
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        if elapsed_time >= total_time:
            pygame.quit()
            if left_score > right_score:
                print("Left side wins!")
            elif right_score > left_score:
                print("Right side wins!")
            else:
                print("It's a tie!")
            sys.exit()

if __name__ == "__main__":
    main()
