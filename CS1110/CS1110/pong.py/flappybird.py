# Nolan Harris
# Nph2tx


import pygame
import gamebox
import random


# The following code block generates the screen and adds some global
# variables to add to and change throughout the game
camera = gamebox.Camera(800, 600)
bird = gamebox.from_color(200, 200, 'yellow', 40, 50)
logo = gamebox.from_text(600, 200, 'Flappy Pygame! Created by Nolan Harris November 2018', 60, 'white')
bird.yspeed = 0
counter = 0
pillars = []
clear_pillars = []
score = 0
adder = 0


# The tick function is for movement through the game and adding to the score


def tick(keys):
    global counter, pillars, score, adder
    if pygame.K_SPACE in keys:
        bird.yspeed = -7
    current_score = gamebox.from_text(50 + adder, 50, str(score), 50, 'white')  # Displays the score
    adder += 5
    bird.yspeed += 1
    bird.y = bird.y + bird.yspeed
    camera.clear('cyan')  # Colors the background
    camera.draw(bird)
    camera.draw(logo)

# The following is for movement of the bird and the camera
    bird.xspeed = 5
    bird.move_speed()
    camera.x += 5
    counter += 1

# The next code block is for the generation of new pillars on the top and the bottom.
# the clear pillar is so the flapper can fly through it and signal an addition to the score
    if counter % 50 == 0:
        rand = random.randint(0, 600)
        hole = 70
        new_pillar_top = gamebox.from_color(camera.x + 400, 0, 'pink', 60, rand)
        new_pillar_bottom = gamebox.from_color(camera.x + 400, 600, 'pink', 60, 950 - hole - rand)
        clear_pillar = gamebox.from_color(camera.x + 400 + 100, 300, 'black', 1, 600)
        clear_pillars.append(clear_pillar)
        pillars.append(new_pillar_bottom)
        pillars.append(new_pillar_top)
    #
    # This series of statements is to check for if the flapper touches the pillars,
    # and ends the game should it touch a non clear pillar
    #
    for pillar in pillars:

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
