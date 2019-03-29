# infinite jumper example
# modified from example by Prof. Mark Sherriff

import pygame
import gamebox


camera = gamebox.Camera(800, 600)
character = gamebox.from_color(50, 200, "yellow", 15, 40)
character.yspeed = 0
pillars = [
    gamebox.from_color(250, 50, "yellow", 10, 200),  # Pillar 1
    gamebox.from_color(250, 450, "yellow", 10, 300),  # Pillar 2
    gamebox.from_color(500, 50, "yellow", 10, 200),  # Pillar 3
    gamebox.from_color(500, 550, "yellow", 10, 200)  # Pillar 4
]

counter = 0


def tick(keys):
    # get access to the counter
    global counter
    if pygame.K_SPACE in keys:
        character.y += 30

    if pygame.K_RIGHT in keys:
        character.x += 10
    if pygame.K_LEFT in keys:
        character.x -= 10
    character.yspeed += 1
    character.y = character.y + character.yspeed
    camera.clear("cyan")
    camera.draw(character)

    # makes the screen scroll
    camera.x += 3

    # make random walls appear every time the counter hits a particular number
    # notice how I use the random.randint to vary the height of the platform
    # also I add in the camera.x to the x position because the screen keeps moving
    counter += 1
    if counter % 50 == 0:
        if pillar.x < 0:


    for pillar in pillars:
        if character.bottom_touches(pillar):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -20
        if character.touches(pillar):
            character.move_to_stop_overlapping(pillar)
        camera.draw(pillar)

    camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)

