import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
x = 250
y = 250
running = True
while running:
    screen.fill('White')
    pygame.draw.circle(screen, 'Red', (x, y), 25)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and y <= 450:
                y = y + 20
            if event.key == pygame.K_UP and y >= 50:
                y = y - 20
            if event.key == pygame.K_LEFT and x >= 50:
                x = x - 20
            if event.key == pygame.K_RIGHT and x <= 450:
                x = x + 20