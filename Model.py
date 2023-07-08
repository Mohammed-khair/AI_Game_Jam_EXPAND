import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRID_SIZE = 10
BOX_SIZE = SCREEN_WIDTH // GRID_SIZE
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid of Boxes")

# Font
font = pygame.font.Font(None, 36)

# Game state
grid = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
grid[0][0] = True

# Specific points to make red boxes
points = [(0, 9), (8, 8), (5, 5)]

# Function for checking connectivity
def dfs(row, col, visited):
    visited[row][col] = True

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row = row + dr
        new_col = col + dc
        if (
                0 <= new_row < GRID_SIZE
                and 0 <= new_col < GRID_SIZE
                and not visited[new_row][new_col]
                and grid[new_row][new_col]
        ):
            dfs(new_row, new_col, visited)


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            col = mouse_pos[0] // BOX_SIZE
            row = (mouse_pos[1] - 100) // BOX_SIZE
            if 0 <= row < GRID_SIZE:
                if (
                        (col > 0 and grid[row][col - 1])
                        or (col < GRID_SIZE - 1 and grid[row][col + 1])
                        or (row > 0 and grid[row - 1][col])
                        or (row < GRID_SIZE - 1 and grid[row + 1][col])
                ) and not (col == 0 and row == 0):  # Additional condition for top-right box
                    grid[row][col] = not grid[row][col]

    # Update grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if (
                    (col > 0 and not grid[row][col - 1])
                    and (col < GRID_SIZE - 1 and not grid[row][col + 1])
                    and (row > 0 and not grid[row - 1][col])
                    and (row < GRID_SIZE - 1 and not grid[row + 1][col])
            ):
                grid[row][col] = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Perform connectivity check and update grid
    visited = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    dfs(0, 0, visited)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] and not visited[row][col]:
                grid[row][col] = False

    # Draw the header
    header_text = font.render("Expand!!!", True, (255, 255, 255))
    header_rect = header_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(header_text, header_rect)

    # Draw the grid of boxes
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * BOX_SIZE, row * BOX_SIZE + 100, BOX_SIZE, BOX_SIZE)
            if grid[row][col]:
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)

            if (row, col) in points:
                if grid[row][col] and (
                        (col > 0 and grid[row][col - 1])
                        or (col < GRID_SIZE - 1 and grid[row][col + 1] if col < GRID_SIZE - 1 else False)
                        or (row > 0 and grid[row - 1][col])
                        or (row < GRID_SIZE - 1 and grid[row + 1][col] if row < GRID_SIZE - 1 else False)
                ):
                    pygame.draw.rect(screen, YELLOW, rect)
                else:
                    pygame.draw.rect(screen, RED, rect)



    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
