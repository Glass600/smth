from pygame import *
window = display.set_mode((700,500))
display.set_caption('Бред сумашедшего')
bg = transform.scale(image.load('background.jpg'), (700,500))

x1 = 100
x2 = 300
y1 = 300
y2 = 300

s1 = transform.scale(image.load('sprite1.jpg'),(100, 100))
s2 = transform.scale(image.load('sprite2.jpeg'),(100, 100))
speed = 25

run = True
clock = time.Clock()
FPS = 60

while run:
    window.blit(bg,(0,0))
    window.blit(s1,(x1,y1))
    window.blit(s2,(x2,y2))

    for e in event.get():
        if e.type ==QUIT:
            run = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1>5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and y1<395:
        x1 += speed
    if keys_pressed[K_UP] and y1>5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1<395:
        y1 += speed

    if keys_pressed[K_a] and x2>5:
        x2 -= speed
    if keys_pressed[K_d] and x2<595:
        x2 += speed
    if keys_pressed[K_w] and y2>5:
        y2 -= speed
    if keys_pressed[K_s] and y2<395:
        y2 += speed
    display.update()
    clock.tick(FPS)