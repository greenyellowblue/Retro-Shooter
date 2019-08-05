Playerv1 = PVector(230, 600)
Playerv2 = PVector(250, 550)
Playerv3 = PVector(270, 600)
keysPressed = [False for _ in range(128)]
bgcoloura = 135
bgcolourb = 206
bgcolourc = 250
PlaySize = 30
HTPSize = 30
Menu = True
Play = False
HTP = False
img = None
img_2 = None
yimgA = 0
yimgB = -500
backSize = 30
score = 0
bullets = []
enemies = []
esize = []
hitCount = []
speedx = 0
speedy = 0
delay = 0
waves = 1
frames = 0
counter = 0
Defeat = False
mainMenuSize = 40
mainMenuX = 90
deathexplosion = 50
dead = False
customSize = 30
CSTM = False
pcoloura = 0
pcolourb = 128
pcolourc = 0
pcolourindex = 0
pcolour = ["Green", "Blue", "Red", "Purple", "Yellow"]
arrowA = 30
arrowB = 30
powerups = []
BOOST = False
boostcounter = 0


def setup():
    global img, img_2
    size(500, 700)
    # background stuff
    img = None
    img = createGraphics(width, height)
    img.beginDraw()
    for i in range(10):
        x = random(img.width)
        y = random(img.width)
        diameter = random(5, 15)
        img.fill(255, 69, 0)
        img.ellipse(x, y, diameter, diameter)
    img.endDraw()
    img_2 = None
    img_2 = createGraphics(width, height)
    img_2.beginDraw()
    for i in range(10):
        x = random(img_2.width)
        y = random(img_2.width)
        diameter = random(5, 15)
        img_2.fill(255, 69, 0)
        img_2.ellipse(x, y, diameter, diameter)
    img_2.endDraw()


def draw():
    global speedx, speedy, Playerv1, Playerv2, Playerv3, score
    global keysPressed, bullets, enemies, delay, powerups
    global esize, frames, waves, counter, hitCount, BOOST
    global bgcoloura, bgcolourb, bgcolourc, boostcounter
    global PlaySize, HTPSize, HTP, Menu, Play, Defeat
    global img, yimgA, yimgB, backSize, mainMenuSize
    global mainMenuX, deathexplosion, dead, customSize
    global pcoloura, pcolourb, pcolourc, pcolourindex, pcolour
    global arrowA, arrowB
    if pcolourindex == 0:
            pcoloura = 0
            pcolourb = 128
            pcolourc = 0
    elif pcolourindex == 1:
        pcoloura = 0
        pcolourb = 0
        pcolourc = 255
    elif pcolourindex == 2:
        pcoloura = 255
        pcolourb = 0
        pcolourc = 0
    elif pcolourindex == 3:
        pcoloura = 128
        pcolourb = 0
        pcolourc = 128
    elif pcolourindex == 4:
        pcoloura = 255
        pcolourb = 255
        pcolourc = 0
    # background
    if Play:
        if bgcoloura > 0:
            bgcoloura -= 0.1
        if bgcolourb > 0:
            bgcolourb -= 0.1
        if bgcolourc > 100:
            bgcolourc -= 0.1
    background(bgcoloura, bgcolourb, bgcolourc)
    img.background(bgcoloura, bgcolourb, bgcolourc)
    img_2.background(bgcoloura, bgcolourb, bgcolourc)
    if Play:
        imgspeed = 1
        yimgA += imgspeed
        yimgB += imgspeed
        if yimgA >= img.height:
            yimgA = -height
        elif yimgB >= img.height:
            yimgB = -height
        image(img, 0, yimgA)
        image(img_2, 0, yimgB)

    # Player
    if Menu or Play:
        fill(pcoloura, pcolourb, pcolourc)
        strokeWeight(3)
        stroke(255)
        triangle(Playerv1.x, Playerv1.y,
                 Playerv2.x, Playerv2.y,
                 Playerv3.x, Playerv3.y)
    # menu screen
    if Menu:
        textSize(50)
        fill(34, 139, 34)
        text("<Retro Shooter>", 30, 100)

        textSize(HTPSize)
        fill(0, 128, 0)
        text("<HOW TO PLAY>", 20, 200)
        if mouseX >= 20 and mouseX <= 250 and mouseY >= 170 and mouseY <= 200:
            HTPSize = 40
        else:
            HTPSize = 30

        textSize(PlaySize)
        fill(0, 128, 0)
        text("<PLAY>", 20, 250)
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 220 and mouseY <= 250:
            PlaySize = 40
        else:
            PlaySize = 30

        textSize(customSize)
        fill(0, 128, 0)
        text("<CUSTOMIZATION>", 20, 300)
        if mouseX >= 20 and mouseX <= 300 and mouseY >= 270 and mouseY <= 300:
            customSize = 40
        else:
            customSize = 30
    # How To Play
    if HTP:
        textSize(20)
        fill(0, 128, 0)
        text("ARROW KEYS - Up, Down, Left, Right", 20, 100)
        text("SPACE - Shoot", 20, 140)
        text("Destroy incoming asteroids to gain points!", 20, 160, 480, 300)
        text("Score as many points as you can!", 20, 240, 480, 300)
        text("Squares dropped from enemies are a boost", 20, 280, 480, 300)
        textSize(backSize)
        text("<BACK>", 20, 650)
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 620 and mouseY <= 650:
            backSize = 40
        else:
            backSize = 30
    # Customization
    if CSTM:
        textSize(40)
        fill(0, 128, 0)
        text("CUSTOMIZATION", 80, 100)
        textSize(30)
        fill(0)
        text("Player Colour:      " + pcolour[pcolourindex], 25, 200)
        textSize(arrowA)
        text("<-", 230, 200)
        if mouseX >= 230 and mouseX <= 270 and mouseY >= 170 and mouseY <= 200:
            arrowA = 40
        else:
            arrowA = 30
        textSize(arrowB)
        text("->", 380, 200)
        if mouseX >= 380 and mouseX <= 420 and mouseY >= 170 and mouseY <= 200:
            arrowB = 40
        else:
            arrowB = 30
        textSize(backSize)
        text("<BACK>", 20, 650)
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 620 and mouseY <= 650:
            backSize = 40
        else:
            backSize = 30
        fill(pcoloura, pcolourb, pcolourc)
        strokeWeight(3)
        stroke(255)
        triangle(Playerv1.x, Playerv1.y,
                 Playerv2.x, Playerv2.y,
                 Playerv3.x, Playerv3.y)
    if Play:
        textSize(50)
        fill(0)
        text(score, 225, 350)
        if keysPressed[37]:
            if BOOST:
                speedx = -10
            else:
                speedx = -5
        elif keysPressed[39]:
            if BOOST:
                speedx = 10
            else:
                speedx = 5
        if keysPressed[38]:
            if BOOST:
                speedy = -10
            else:
                speedy = -5
        elif keysPressed[40]:
            if BOOST:
                speedy = 10
            else:
                speedy = 5
        if keysPressed[32] and delay == 5 and BOOST is False:
            bullets.append(PVector(Playerv2.x, Playerv2.y))
            delay = 0
        elif keysPressed[32] and delay == 5 and BOOST:
            bullets.append(PVector(Playerv2.x - 20, Playerv2.y))
            bullets.append(PVector(Playerv2.x, Playerv2.y))
            bullets.append(PVector(Playerv2.x + 20, Playerv2.y))
            delay = 0
        elif keysPressed[32] and delay != 5:
            delay += 1
        if frames >= 60 and waves == 1:
            enemies.append(PVector(random(50, 450), 0))
            esize.append(random(30, 70))
            hitCount.append(0)
            frames = 0
            counter += 1
        elif frames >= 40 and waves == 2:
            enemies.append(PVector(random(50, 450), 0))
            esize.append(random(30, 70))
            hitCount.append(0)
            frames = 0
            counter += 1
        elif frames >= 20 and waves == 3:
            enemies.append(PVector(random(50, 450), 0))
            esize.append(random(30, 70))
            hitCount.append(0)
            frames = 0
            counter += 1
        elif frames >= 10 and waves == 4:
            enemies.append(PVector(random(50, 450), 0))
            esize.append(random(30, 70))
            hitCount.append(0)
            frames = 0
            counter += 1
        else:
            frames += 1
        if counter >= 20 and waves == 1:
            waves = 2
        elif counter >= 50 and waves == 2:
            waves = 3
        elif counter >= 100 and waves == 3:
            waves = 4
        for i in range(len(enemies)):
            if esize[i] >= 50:
                enemies[i].y += 7
            elif esize >= 40:
                enemies[i].y += 6
            elif esize >= 30:
                enemies[i].y += 5
            strokeWeight(1)
            fill(128, 128, 128)
            Size = esize[i]
            ellipse(enemies[i].x, enemies[i].y, Size, Size)
        for i in range(len(bullets)):
            bullets[i].y -= 10
            noStroke()
            fill(250, 129, 0)
            rect(bullets[i].x, bullets[i].y, 5, 15)
        count = 0
        for i in range(len(bullets)):
            if bullets[i].y <= -100:
                del bullets[i]
                bullets.append(PVector(0, 1000))
                count += 1
            for k in range(len(enemies)):
                if (bullets[i].x >= enemies[k].x - esize[k]/2 and
                    bullets[i].x <= enemies[k].x + esize[k]/2 and
                    bullets[i].y >= enemies[k].y - esize[k]/2 and
                        bullets[i].y <= enemies[k].y + esize[k]/2):
                    del bullets[i]
                    bullets.append(PVector(0, 1000))
                    count += 1
                    hitCount[k] += 1
                    noStroke()
                    fill(249, 139, 0)
                    ellipse(enemies[k].x, enemies[k].y, esize[k], esize[k])
        for i in range(count):
            bullets.pop()
        count = 0
        for i in range(len(enemies)):
            if enemies[i].y >= 800:
                del enemies[i]
                del hitCount[i]
                del esize[i]
                hitCount.append(0)
                enemies.append(PVector(0, -100))
                esize.append(0)
                count += 1
            if hitCount[i] >= 10 and esize[i] >= 50:
                n = random(100)
                if n > 85:
                    powerups.append(PVector(enemies[i].x, enemies[i].y))
                del enemies[i]
                del hitCount[i]
                del esize[i]
                hitCount.append(0)
                enemies.append(PVector(0, -100))
                esize.append(0)
                count += 1
                score += 3
            elif hitCount[i] >= 7 and esize[i] >= 40 and esize[i] <= 49:
                n = random(100)
                if n > 90:
                    powerups.append(PVector(enemies[i].x, enemies[i].y))
                del enemies[i]
                del hitCount[i]
                del esize[i]
                hitCount.append(0)
                enemies.append(PVector(0, -100))
                esize.append(0)
                count += 1
                score += 2
            elif hitCount[i] >= 5 and esize[i] >= 30 and esize[i] <= 39:
                n = random(100)
                if n > 95:
                    powerups.append(PVector(enemies[i].x, enemies[i].y))
                del enemies[i]
                del hitCount[i]
                del esize[i]
                hitCount.append(0)
                enemies.append(PVector(0, -100))
                esize.append(0)
                count += 1
                score += 1
        for i in range(count):
            hitCount.pop()
            enemies.pop()
            esize.pop()
        for i in range(len(powerups)):
            fill(0, 128, 0)
            stroke(255)
            strokeWeight(1)
            rect(powerups[i].x, powerups[i].y, 30, 30)
            powerups[i].y += 1
        count = 0
        for k in range(len(powerups)):
            if (Playerv2.x >= powerups[k].x - 15 and
                Playerv2.x <= powerups[k].x + 15 and
                Playerv2.y >= powerups[k].y - 15 and
                    Playerv2.y <= powerups[k].y + 15):
                BOOST = True
                del powerups[k]
                powerups.append(PVector(0, -100))
                count += 1
            if (Playerv1.x >= powerups[k].x - 15 and
                Playerv1.x <= powerups[k].x + 15 and
                Playerv1.y >= powerups[k].y - 15 and
                    Playerv1.y <= powerups[k].y + 15):
                BOOST = True
                del powerups[k]
                powerups.append(PVector(0, -100))
                count += 1
            if (Playerv3.x >= powerups[k].x - 15 and
                Playerv3.x <= powerups[k].x + 15 and
                Playerv3.y >= powerups[k].y - 15 and
                    Playerv3.y <= powerups[k].y + 15):
                BOOST = True
                del powerups[k]
                powerups.append(PVector(0, -100))
                count += 1
        for i in range(count):
            powerups.pop()
        if BOOST:
            boostcounter += 1
        if boostcounter >= 900:
            boostcounter = 0
            BOOST = False
        for k in range(len(enemies)):
            if (Playerv2.x >= enemies[k].x - esize[k]/2 and
                Playerv2.x <= enemies[k].x + esize[k]/2 and
                Playerv2.y >= enemies[k].y - esize[k]/2 and
                    Playerv2.y <= enemies[k].y + esize[k]/2):
                dead = True
                del enemies[k]
                del esize[k]
                del hitCount[k]
                break
            elif (Playerv1.x >= enemies[k].x - esize[k]/2 and
                  Playerv1.x <= enemies[k].x + esize[k]/2 and
                  Playerv1.y >= enemies[k].y - esize[k]/2 and
                    Playerv1.y <= enemies[k].y + esize[k]/2):
                dead = True
                del enemies[k]
                del esize[k]
                del hitCount[k]
                break
            elif (Playerv3.x >= enemies[k].x - esize[k]/2 and
                  Playerv3.x <= enemies[k].x + esize[k]/2 and
                  Playerv3.y >= enemies[k].y - esize[k]/2 and
                    Playerv3.y <= enemies[k].y + esize[k]/2):
                dead = True
                del enemies[k]
                del esize[k]
                del hitCount[k]
                break
        deadx = False
        if dead and deathexplosion <= 1000:
            deathexplosion += 10
            fill(238, 232, 170)
            noStroke()
            ellipse(Playerv2.x, Playerv2.y, deathexplosion, deathexplosion)
            keysPressed = [False for _ in range(128)]
        if deathexplosion >= 1000:
            deadx = True
        if dead and deadx:
            Defeat = True
            Play = False
        if Playerv1.x <= 0 and keysPressed[37]:
            Playerv1.x -= speedx
            Playerv2.x -= speedx
            Playerv3.x -= speedx
        elif Playerv3.x >= 500 and keysPressed[39]:
            Playerv1.x -= speedx
            Playerv2.x -= speedx
            Playerv3.x -= speedx
        else:
            Playerv1.x += speedx
            Playerv2.x += speedx
            Playerv3.x += speedx
        if Playerv1.y >= 700 and keysPressed[40]:
            Playerv1.y -= speedy
            Playerv2.y -= speedy
            Playerv3.y -= speedy
        else:
            Playerv1.y += speedy
            Playerv2.y += speedy
            Playerv3.y += speedy
        speedx = 0
        speedy = 0
    if Defeat:
        textSize(50)
        fill(128, 0, 0)
        text("DEFEAT", 150, 100)
        textSize(30)
        fill(255)
        text("Your Final Score: " + str(score), 100, 200)
        textSize(mainMenuSize)
        fill(0)
        text("<MAIN MENU>", mainMenuX, 350)
        if mouseX >= 90 and mouseX <= 350 and mouseY >= 310 and mouseY <= 350:
            mainMenuSize = 50
            mainMenuX = 70
        else:
            mainMenuSize = 40
            mainMenuX = 90


def keyPressed():
    keysPressed[keyCode] = True


def keyReleased():
    keysPressed[keyCode] = False


def mouseReleased():
    global Menu, Play, HTP, Defeat, CSTM
    global dead, deathexplosion, counter
    global bgcoloura, bgcolourb, bgcolourc
    global score, waves, powerups, BOOST
    global enemies, bullets, Playerv1
    global Playerv2, Playerv3, pcolourindex
    if Menu:
        if mouseX >= 50 and mouseX <= 150 and mouseY >= 220 and mouseY <= 250:
            Play = True
            Menu = False
        if mouseX >= 50 and mouseX <= 150 and mouseY >= 170 and mouseY <= 200:
            Menu = False
            HTP = True
        if mouseX >= 20 and mouseX <= 300 and mouseY >= 270 and mouseY <= 300:
            CSTM = True
            Menu = False
    if HTP:
        if mouseX >= 50 and mouseX <= 150 and mouseY >= 620 and mouseY <= 650:
            HTP = False
            Menu = True
    if Defeat:
        if mouseX >= 90 and mouseX <= 300 and mouseY >= 310 and mouseY <= 350:
            Menu = True
            Defeat = False
            dead = False
            BOOST = False
            deathexplosion = 50
            bgcoloura = 135
            bgcolourb = 206
            bgcolourc = 250
            score = 0
            waves = 1
            counter = 0
            enemies = []
            bullets = []
            powerups = []
            Playerv1 = PVector(230, 600)
            Playerv2 = PVector(250, 550)
            Playerv3 = PVector(270, 600)
    if CSTM:
        if mouseX >= 230 and mouseX <= 270 and mouseY >= 170 and mouseY <= 200:
            if pcolourindex == 0:
                pcolourindex = 4
            else:
                pcolourindex -= 1
        if mouseX >= 380 and mouseX <= 420 and mouseY >= 170 and mouseY <= 200:
            if pcolourindex == 4:
                pcolourindex = 0
            else:
                pcolourindex += 1
        if mouseX >= 20 and mouseX <= 150 and mouseY >= 620 and mouseY <= 650:
            CSTM = False
            Menu = True
