# Katie Sabo (kbs5fp) and Nolan Harris (nph2tx)
# pykart with start screen(s)
# we still have to add the enemies and figure out the multiplayer
# also have to fix the lap counter
# and how to get the game to quit
# and a few aesthetic things

import pygame
from pygame.locals import*
import sys
import gamebox
import random

pygame.init()

size = [800, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("PyKart")
CAMERA_WIDTH, CAMERA_HEIGHT = 800, 600
BOX_WIDTH, BOX_HEIGHT = 10, 10
camera = gamebox.Camera(CAMERA_WIDTH, CAMERA_HEIGHT)

FPS = 30
fpsClock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

mario = gamebox.from_color(100, 100, "red", BOX_WIDTH, BOX_HEIGHT)
peach = gamebox.from_color(111, 100, "pink", BOX_WIDTH, BOX_HEIGHT)
luigi = gamebox.from_color(122, 100, "green", BOX_WIDTH, BOX_HEIGHT)
waluigi = gamebox.from_color(133, 100, "purple", BOX_WIDTH, BOX_HEIGHT)

walls = [
    gamebox.from_color(400, 10, "black", 800, 100),
    gamebox.from_color(400, 590, "black", 800, 100),
    gamebox.from_color(10, 300, "black", 100, 600),
    gamebox.from_color(790, 300, "black", 100, 600),
    gamebox.from_color(400, 300, "black", 300, 200)
]

finishLine = gamebox.from_color(270, 130, "white", 10, 140)

coins = [gamebox.from_color(300, 450, "yellow", 10, 10)]
time = 9000
direction_x = 1
direction_y = 1
speed = 5
coinCount = 0
peachCoinCount = 0
luigiCoinCount = 0
waluigiCoinCount = 0
laps = 0


done = False

font = pygame.font.Font(None, 36)

display_start = True
page = 1

while not done and display_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            page += 1
            if page == 4:
                display_start = False

    screen.fill(BLACK)

    if page == 1:
        backgroundImage = pygame.image.load('Slide1.jpg')
        screen.blit(pygame.transform.scale(backgroundImage, (800, 600)), (0, 0))

        text = font.render("Click to Start", True, BLACK)
        screen.blit(text, [325, 250])

    if page == 2:
        backgroundImage2 = pygame.image.load('Slide2.jpg')
        screen.blit(pygame.transform.scale(backgroundImage2, (800, 600)), (0, 0))

        text2 = font.render("Controls", True, BLACK)
        screen.blit(text2, [10, 10])

    if page == 3:
        backgroundImage3 = pygame.image.load('Slide3.jpg')
        screen.blit(pygame.transform.scale(backgroundImage3, (800, 600)), (0, 0))

    fpsClock.tick(FPS)

    pygame.display.flip()


while not done:
    def tick(keys):
        global direction_x, direction_y
        global speed, time, laps
        global coinCount, peachCoinCount, luigiCoinCount, waluigiCoinCount

        camera.clear("grey")

        time -= 1
        seconds = str(int((time / ticks_per_second))).zfill(3)

        # movement
        if pygame.K_RIGHT in keys:
            mario.x += speed * direction_x
        if pygame.K_LEFT in keys:
            mario.x -= speed * direction_x
        if pygame.K_UP in keys:
            mario.y -= speed * direction_y
        if pygame.K_DOWN in keys:
            mario.y += speed * direction_y

        if pygame.K_d in keys:
            peach.x += speed * direction_x
        if pygame.K_a in keys:
            peach.x -= speed * direction_x
        if pygame.K_w in keys:
            peach.y -= speed * direction_y
        if pygame.K_s in keys:
            peach.y += speed * direction_y

        if pygame.K_h in keys:
            luigi.x += speed * direction_x
        if pygame.K_f in keys:
            luigi.x -= speed * direction_x
        if pygame.K_t in keys:
            luigi.y -= speed * direction_y
        if pygame.K_g in keys:
            luigi.y += speed * direction_y

        if pygame.K_l in keys:
            waluigi.x += speed * direction_x
        if pygame.K_j in keys:
            waluigi.x -= speed * direction_x
        if pygame.K_i in keys:
            waluigi.y -= speed * direction_y
        if pygame.K_k in keys:
            waluigi.y += speed * direction_y

        # boundaries
        for wall in walls:
            if mario.touches(wall):
                mario.move_to_stop_overlapping(wall)
            if peach.touches(wall):
                peach.move_to_stop_overlapping(wall)
            if luigi.touches(wall):
                luigi.move_to_stop_overlapping(wall)
            if waluigi.touches(wall):
                waluigi.move_to_stop_overlapping(wall)
            camera.draw(wall)

        # removing coins
        for coin in coins:
            if mario.touches(coin):
                coinCount += 1
                coins.remove(coin)
            if peach.touches(coin):
                peachCoinCount += 1
                coins.remove(coin)
            if luigi.touches(coin):
                luigiCoinCount += 1
                coins.remove(coin)
            if waluigi.touches(coin):
                waluigiCoinCount += 1
                coins.remove(coin)
            camera.draw(coin)

        # adding coins
        if time % 100 == 0:
            coin_x = random.randint(70, 170)
            coin_y = random.randint(70, 520)

            coins.append(gamebox.from_color(coin_x, coin_y, "yellow", 10, 10))
        if time % 150 == 0:
            coin_x = random.randint(550, 730)
            coin_y = random.randint(70, 520)

            coins.append(gamebox.from_color(coin_x, coin_y, "yellow", 10, 10))

        # lap counting
        if mario.touches(finishLine):
            laps += 1
        camera.draw(finishLine)

        lap_box = gamebox.from_text(300, 30, "lap: " + str(laps // 5), 24, "white")
        time_box = gamebox.from_text(475, 30, "Time: " + seconds, 24, "white")
        score_box = gamebox.from_text(75, 30, "Mario-Coins: " + str(coinCount), 24, "white")
        score_box_2 = gamebox.from_text(75, 570, "Peach-Coins: " + str(peachCoinCount), 24, "white")
        score_box_3 = gamebox.from_text(650, 30, "Luigi-Coins: " + str(luigiCoinCount), 24, "white")
        score_box_4 = gamebox.from_text(650, 570, "Waluigi-Coins: " + str(waluigiCoinCount), 24, "white")

        camera.draw(lap_box)
        camera.draw(time_box)
        camera.draw(score_box)
        camera.draw(score_box_2)
        camera.draw(score_box_3)
        camera.draw(score_box_4)

        camera.draw(luigi)
        camera.draw(peach)
        camera.draw(mario)
        camera.draw(waluigi)
        camera.display()


    ticks_per_second = 30
    gamebox.timer_loop(ticks_per_second, tick)

for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

    fpsClock.tick(FPS)

    pygame.display.flip()

pygame.quit()
