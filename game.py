WIDTH = 1024
HEIGHT = 384

ascending = False

alien = Actor('alien')
joker = Actor('cat')
alien.pos = (50, 320)
joker.pos = (WIDTH-50, 320)
jokertwo = Actor('cat')
jokertwo.pos = (WIDTH/2, 320/2)

def draw():
    screen.clear()
    alien.draw()
    joker.draw()
    jokertwo.draw()

beep = tone.create('A3', 0.5)
beeptwo = tone.create('D5', 0.25)

def update():
    global ascending
    if keyboard[keys.UP] and not ascending and alien.y == 320:
        ascending = True
    #elif alien.y < 320:
        #alien.y += 3
    if keyboard[keys.LEFT] and alien.left > 0:
        alien.x -= 2
    if keyboard[keys.RIGHT] and alien.right < WIDTH:
        alien.x += 2
    if ascending:
            if alien.y > 160:
                alien.y -= 2
            else:
                ascending = False
    if not ascending and alien.y < 320:
        alien.y += 2
    joker.x -= 4
    if joker.x < 0:
        joker.x = WIDTH-50
    if joker.colliderect(alien):
        beep.play()
    jokertwo.x -= 6
    if jokertwo.x < 0:
        jokertwo.x = WIDTH-50
    if jokertwo.colliderect(alien):
        beeptwo.play()