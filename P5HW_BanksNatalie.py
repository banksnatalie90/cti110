# Natalie Banks
# 07/14/2025
# P5LAB
# Use of loops, functions, and import to create a game



import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🛡️ Space Shield Defense ☄️")

# Colors and fonts
WHITE = (255, 255, 255)
RED = (255, 0, 0)
font = pygame.font.SysFont(None, 40)

# === Value-Returning Function ===
def create_alien():
    alien = {
        "name": "Zorg 👽",
        "health": 10,
        "score": 0
    }
    return alien

# === Function 1: Move Meteors ===
def move_meteors(meteors):
    for meteor in meteors:
        meteor["y"] += meteor["speed"]
        if meteor["y"] > HEIGHT:
            meteor["y"] = 0
            meteor["x"] = random.randint(50, WIDTH - 50)

# === Function 2: Check Collision ===
def check_collision(shield_rect, meteors, alien):
    for meteor in meteors:
        meteor_rect = pygame.Rect(meteor["x"], meteor["y"], 40, 40)
        if meteor_rect.colliderect(shield_rect):
            alien["score"] += 1
            meteor["y"] = 0
        elif meteor["y"] > HEIGHT - 50:
            alien["health"] -= 1
            meteor["y"] = 0

# === Main Function ===
def main():
    clock = pygame.time.Clock()
    alien = create_alien()
    shield_x = WIDTH // 2
    shield_speed = 8
    start_ticks = pygame.time.get_ticks()  # store the start time
    game_duration = 300  # game lasts 300 seconds

    # Create meteors
    meteors = []
    for _ in range(5):
        meteors.append({
            "x": random.randint(50, WIDTH - 50),
            "y": random.randint(-300, -40),
            "speed": random.randint(1, 2)
        })

    running = True
    while running:
        clock.tick(30)
        screen.fill((0, 0, 30))  # Space background
        # Calculate how many seconds have passed
        seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000

        # Display countdown timer on screen
        time_left = game_duration - seconds_passed
        timer_text = font.render(f"Time: {time_left} ⏱️", True, WHITE)
        screen.blit(timer_text, (20, 60))

        # End the game when time runs out
        if seconds_passed >= game_duration:
            running = False

    

    

        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and shield_x > 0:
            shield_x -= shield_speed
        if keys[pygame.K_RIGHT] and shield_x < WIDTH - 100:
            shield_x += shield_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw shield
        shield_rect = pygame.Rect(shield_x, HEIGHT - 50, 100, 20)
        pygame.draw.rect(screen, WHITE, shield_rect)

        # Move and draw meteors
        move_meteors(meteors)
        for meteor in meteors:
            pygame.draw.circle(screen, RED, (meteor["x"], meteor["y"]), 20)

        # Check collisions
        check_collision(shield_rect, meteors, alien)

        # Display stats
        stats_text = font.render(f"{alien['name']} | Health: {alien['health']} ❤️ | Score: {alien['score']} 🌟", True, WHITE)
        screen.blit(stats_text, (20, 20))

        pygame.display.flip()

        # End game if health is 0
        if alien["health"] <= 0:
            running = False

      


    # Game over screen
    screen.fill((0, 0, 0))
    game_over_text = font.render("Game Over 💀 Final Score: " + str(alien["score"]), True, RED)
    screen.blit(game_over_text, (WIDTH//2 - 200, HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()

# Run the game
main()
