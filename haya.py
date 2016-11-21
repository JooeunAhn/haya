import random
from resource import *


game_over = False

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
siri_list = pygame.sprite.Group()
candle_list = pygame.sprite.Group()

background_image_path = "assets/background.png"

backgroundImageOne = pygame.image.load(background_image_path)
backgroundImageOne_position = [0, 0]

backgroundImageTwo = pygame.image.load(background_image_path)
backgroundImageTwo_position = [0, -560]


player = Rocket("assets/rocket.png", 320, 390)
all_sprites.add(player)

font = pygame.font.SysFont("monospace", 40)

# Game Loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player.move(-5)

            elif event.key == pygame.K_RIGHT:
                player.move(5)

            if event.key == pygame.K_SPACE and player.ammo > 0:
                player.ammo -= 1
                candle = Candle("assets/candle.png", player.rect.x+22,
                                player.rect.y-35)
                candle_list.add(candle)
                all_sprites.add(candle)

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player.move(5)

            elif event.key == pygame.K_RIGHT:
                player.move(-5)

    sirispawn_intervalOne = random.randrange(0, 200)
    sirispawn_intervalTwo = random.randrange(0, 200)

    if sirispawn_intervalOne == sirispawn_intervalTwo:

        for i in range(random.randrange(3, 6)):

            siri = Siri("assets/choi3.png", random.randrange(1, 5))
            siri.rect.x = random.randint(55, 585)
            siri.rect.y = random.randint(-400, -70)
            siri_list.add(siri)
            all_sprites.add(siri)

    all_sprites.update()

    screen.fill(DARKBLUE)

    screen.blit(backgroundImageOne, backgroundImageOne_position)
    screen.blit(backgroundImageTwo, backgroundImageTwo_position)

    if backgroundImageOne_position[1] < 560:
        backgroundImageOne_position[1] += 0.5
    if backgroundImageOne_position[1] >= 560:
        backgroundImageOne_position[1] = -560

    if backgroundImageTwo_position[1] < 560:
        backgroundImageTwo_position[1] += 0.5
    if backgroundImageTwo_position[1] >= 560:
        backgroundImageTwo_position[1] = -560

    for candle in candle_list:

        if candle.rect.y <= -40:
            candle.kill()

        for siri in siri_list:
            if candle.rect.y <= siri.rect.y + 50 \
            and siri.rect.x - 5 <= candle.rect.x <= siri.rect.x + 60:
                siri.kill()
                candle.kill()

    siri_hit_list = pygame.sprite.spritecollide(player, siri_list, True)

    if len(siri_hit_list) > 0:
        player.loseHealth(len(siri_hit_list))

    player.healthBar()

    if player.ammo < 10:
        player.ammo += 0.05

    player.shotsFired()

    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()