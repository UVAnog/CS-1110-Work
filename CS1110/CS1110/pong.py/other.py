import pygame
import gamebox
import random
camera = gamebox.Camera(800, 600)
bird = gamebox.from_color(200, 200, 'yellow', 40, 50)
bird.yspeed = 0
counter = 0
pillars = []
clear_pillars = []
score = 0
adder = 0
start = True


def tick(keys):
    global counter, pillars, score, adder
    if pygame.K_SPACE in keys:
        bird.yspeed = -7
    current_score = gamebox.from_text(50 + adder, 50, str(score), 50, 'white')
    adder += 5
    bird.yspeed += 1
    bird.y = bird.y + bird.yspeed
    camera.clear('cyan')
    camera.draw(bird)

    bird.xspeed = 5
    bird.move_speed()
    camera.x += 5
    counter += 1

    if counter % 50 == 0:
        rand = random.randint(0, 600)
        hole = 70
        new_pillar_top = gamebox.from_color(camera.x + 400, 0, 'pink', 60, rand)
        new_pillar_bottom = gamebox.from_color(camera.x + 400, 600, 'pink', 60, 950 - hole - rand)
        clear_pillar = gamebox.from_color(camera.x + 400 + 100, 300, 'black', 1, 600)
        clear_pillars.append(clear_pillar)
        pillars.append(new_pillar_bottom)
        pillars.append(new_pillar_top)
    for pillar in pillars:
        global start
        if bird.touches(pillar):
            gamebox.pause()
            camera.clear('black')

        camera.draw(pillar)
        if pillar.x < camera.x - 500:
            pillars.remove(pillar)

    for pillar in clear_pillars:
        if bird.touches(pillar):
            score += 1
            clear_pillars.remove(pillar)





    camera.draw(current_score)
    current_score.xspeed = 5
    current_score.move_speed()
    camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)



