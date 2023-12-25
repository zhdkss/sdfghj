import pygame
import sys
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
TARGET_RADIUS = 30
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Это окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
# Клок = FPS
clock = pygame.time.Clock()
# ФунКция которая генерирует место мишени
def generate_target_position():
    x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
    y = random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS)
    return x, y
# ОСновной цикл игры
def aim_trainer():
    score = 0
    target_position = generate_target_position()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                distance = ((mouse_x - target_position[0]) ** 2 + (mouse_y - target_position[1]) ** 2) ** 0.5
                if distance < TARGET_RADIUS:
                    score += 1
                    target_position = generate_target_position()

        # Тут я задал цвет фона
        screen.fill(WHITE)

        # Рисуем цвет мишени и задаем ее в функцию
        pygame.draw.circle(screen, RED, target_position, TARGET_RADIUS)

        # Очки которые мы зарабатываем во время игры
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: {}".format(score), True, RED)
        screen.blit(score_text, (10, 10))

        # Обновление диспеля
        pygame.display.flip()

        # Ограничиваем частоту кадров
        clock.tick(FPS)

if __name__ == "__main__":
    aim_trainer()
