from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
while True:
    x = 400
    while(x < 770):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x+4
        delay(0.01)

    y = 90
    while(y<550):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y+4
        delay(0.01)

    x = 770
    while(x > 30):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x-4
        delay(0.01)

    y = 550
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y-4
        delay(0.01)

    x = 30
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x+4
        delay(0.01)

    x = 0
    while(x < 360):
        dx = 400+240*math.sin(x/360*2*math.pi)
        dy = 320+240*math.cos(x/360*2*math.pi)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(dx,dy)
        x = x+2
        delay(0.01)

close_canvas()
