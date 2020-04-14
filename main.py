
# Jaden Hong
# ICS3U-02
#
# title screen don't starve together -> do fight together
# -types of animations :
# - idle, walking, jump?, attackUP,attackDOWN,attackLR,attackN,shield?,special, nair Leg attack
#
# -wilson l- projectile dart, wilson r- spear lunge, wilson up- fishing rod
#
#
#
# >fix bug with animations #########
#
# controls:
# PLAYER 1-
# arrow keys, n jump, m attack, comma shield
#
# PLAYER 2-
# WASD, x jump, c attack, v shield,0       ,    1       ,     2      ,     3       ,    4    ,        5  ,    6  ,   7
#playerAction=no action, up attack, down attack, left attack, right attack, n attack, air attack, shield, special

from pygame import *
font.init()
mixer.init()
width,height=1200,700
screen=display.set_mode((width,height))
screenRect=Rect(0,0,width,height)


def titleMenu():
    bg1=image.load('backgrounds/bg1.png').convert()
    word1=MyText('Do Fight', 150, CREAM, 0, 100, 100)
    word2=MyText('Together', 150, CREAM, 0, 90, 250)
    word3=MyText('press ENTER to continue', 50, WHITE, 0, 100, 500)
    word4=MyText('Do Fight', 75, CREAM, 0, 100, 200)
    word5=MyText('Do Fight Together', 75, CREAM, 0, 100, 325)
    word6=MyText('Controls', 75, CREAM, 0, 100, 450)
    word7=MyText('created by Jaden Hong', 25, CREAM, 255, 1050, 650)
    global optionSel
    myClock=time.Clock()
    myClock.tick(60)
    running=True
    menu='title'
    musicStop=False
    optionSel=4
    wordList=['',word1,word2,word3,word4,word5,word6,word7]
    mixer.music.play(-1)
    while running:
        for evt in event.get():
            if evt.type==KEYDOWN:
                if evt.key==K_RETURN:
                    menu='t main menu'
                    if optionSel==4: #singleplayer
                        #CSS('single')
                        print('single')
                    if optionSel==5: #multiplayer
                        menuClick.play()
                        mixer.music.stop()
                        musicStop=True
                        #time.wait(1000)
                        CSS('multi')
                    if optionSel==6: #controls
                        print('controls')
                if evt.key==K_DOWN:
                    if menu=='main menu':
                        optionSel+=1
                        if optionSel>6:
                            optionSel=4
                if evt.key==K_UP:
                    if menu=='main menu':
                        optionSel-=1
                        if optionSel<4:
                            optionSel=6
                if evt.key==K_ESCAPE:
                    if menu=='main menu':
                        menu='t title'
            if evt.type==QUIT:
                running=False
        if musicStop:
            mixer.music.play(-1)
            musicStop=False
        screen.blit(bg1,(0,0))
        if menu=='title':             #title
            for i in range(1,4,1):
                wordList[i].fadeIn()
                wordList[i].chosen(i,False)
        if menu=='t main menu':             #transition
            for i in range(1,4,1):
                wordList[i].fadeAway()
            if word3.alpha==0:
                #optionSel=4
                menu='main menu'
                menuClick.play()
        if menu=='main menu':             #main menu
            for i in range(4,7,1):
                wordList[i].chosen(i,True)
            for i in range(4,7,1):
                wordList[i].fadeIn()
        if menu=='t title':
            for i in range(4,7,1):
                wordList[i].fadeAway()
            word1.fadeAway()
            if word4.alpha==0:
                menu='title'
                menuClick.play()
        word7.basic()
        display.flip()


def CSS(mode):
    wilsonPortrait=image.load('portrait/wilson.png').convert_alpha()
    wendyPortrait=image.load('portrait/wendy.png').convert_alpha()
    woodiePortrait=image.load('portrait/woodie.png').convert_alpha()
    willowPortrait=image.load('portrait/willow.png').convert_alpha()
    word1=MyText('Choose your Fighter', 50, CREAM, 255, 100, 100)
    word2=MyText('ENTER to start', 100, CREAM, 255, 610, 500)
    p1word1=MyText('Player 1 - Choosing (m)', 35, CREAM, 255, 610, 400)
    p1word2=MyText('Player 1 - Ready', 35, CREAM, 255, 610, 400)
    p2word1=MyText('Player 2 - Choosing (c)', 35, CREAM, 255, 910, 400)
    p2word2=MyText('Player 2 - Ready', 35, CREAM, 255, 910, 400)
    myClock=time.Clock()
    myClock.tick(60)
    running=True
    player1=False
    player2=False
    player1Sel=0
    player2Sel=0
    playerPortrait=[wilsonPortrait,wendyPortrait,woodiePortrait,willowPortrait]
    while running:
        for evt in event.get():
            if evt.type==KEYDOWN:
                if evt.key==K_RETURN:
                    if player1 and player2:
                        game(mode)
                if evt.key==K_LEFT:
                    player1=False
                    player1Sel+=1
                    if player1Sel>3:
                        player1Sel=0
                if evt.key==K_RIGHT:
                    player1=False
                    player1Sel-=1
                    if player1Sel<0:
                        player1Sel=3
                if evt.key==K_m:
                    player1=True
                if evt.key==K_n:
                    player1=False

                if evt.key==K_x:
                    player2=False
                if evt.key==K_a:
                    player2=False
                    player2Sel+=1
                    if player2Sel>3:
                        player2Sel=0
                if evt.key==K_d:
                    player2=False
                    player2Sel-=1
                    if player2Sel<0:
                        player2Sel=3
                if evt.key==K_c:
                    player2=True
                if evt.key==K_ESCAPE:
                    running=False
            if evt.type==QUIT:
                quit()
        screen.blit(bg3,(0,0))
        screen.blit(playerPortrait[player1Sel],(600,100))
        screen.blit(playerPortrait[player2Sel],(900,100))
        word1.basic()
        if player1:
            p1word2.basic()
        else:
            p1word1.floating(25)
        if player2:
            p2word2.basic()
        else:
            p2word1.floating(25)
        if player1 and player2:
            word2.floating(25)
        # keys=key.get_pressed()
        display.flip()
        '''
          title          single    
        main title main menu  x single player  > story (player vs boss) > character select > game
                              > vs cpu if time
                              x multiplayer    > character select > season select(stage) > game

        game > result screen > rematch
                             > character select
                             > main menu
             > pause > reset
                     > character select
                     > main menu
        '''

def wordPic(txt,size,col,alpha):
    global font1
    font1=font.Font('fonts/belisa_plumilla.ttf',size)
    fontPic=font1.render(str(txt), True, col)
    alphaFont=Surface(fontPic.get_size(),SRCALPHA)
    alphaFont.fill((255,255,255,alpha))
    fontPic.blit(alphaFont,(0,0),special_flags=BLEND_RGBA_MULT)
    return fontPic

#movement functions
def friction(vx):
    if vx>3.5:
        vx-=3.5
    elif vx<-3.5:
        vx+=3.5
    else:
        vx=0
    return vx
def findHitbox(px,py,inputs,airborne,action):
    hitbox=Rect(px+20,py+5,60,145)
    if inputs[1] and airborne==False and action==1 or action==7:
        hitbox=Rect(px+20,py+20,60,130)
    elif airborne:
        hitbox=Rect(px+20,py,60,140)
    return hitbox

#classes
class MyText(object):
    def __init__(self,txt,size,col,alpha,locx,locy):
        self.txt=txt        #text
        self.size=size      #size
        self.col=col        #colour
        self.alpha=alpha    #alpha value
        self.mulVal=1
        self.locx=locx
        self.locy=locy
        self.speed=25
        self.menuNum=-1

    def chosen(self,menuNum,indent):
        self.menuNum=menuNum
        if optionSel==menuNum:
            self.speed+=self.mulVal
            if abs(self.speed)>300:
                self.mulVal*=-1
            if indent:
                screen.blit(wordPic(self.txt, self.size, self.col, self.alpha), (self.locx + 50, self.locy + self.speed // 25))
                screen.blit(beefalo,(self.locx,self.locy+self.size/5.5))
            else:
                screen.blit(wordPic(self.txt, self.size, self.col, self.alpha), (self.locx, self.locy + self.speed // 25))
        else:
            screen.blit(wordPic(self.txt, self.size, self.col, self.alpha), (self.locx, self.locy))
    def basic(self):
        screen.blit(wordPic(self.txt, self.size, self.col, self.alpha), (self.locx, self.locy))
    def floating(self,speed):
        self.speed+=self.mulVal
        if abs(self.speed)>300:
            self.mulVal*=-1
        screen.blit(wordPic(self.txt, self.size, self.col, self.alpha), (self.locx, self.locy + self.speed // 25))
    def fadeAway(self):
        if self.alpha-1>=0:
            self.alpha-=3
    def fadeIn(self):
        if self.alpha+1<=255:
            self.alpha+=3


def loadSprites(path):
    'loadSprites(path)- takes file path and returns list of each sprite in folder'
    picList=[]
    for i in range(50):
        try:
            picList.append(image.load(path+str(i)+'.png').convert_alpha())
        except:
            return picList

##                        #   0  ,    1     ,   2   ,     3   ,  4
##                        #sprite, increment, duration, damage, stun,
wilson=[[loadSprites('wilson/idle/'),15,59],             #-1,0
        [loadSprites('wilson/crouch/'),10,19],          #1
        [loadSprites('wilson/guard/'),8,47],            #2
        [loadSprites('wilson/walk/'),10,79],            #3
        [loadSprites('wilson/jump/'),16,45],            #4
        [loadSprites('wilson/nAttack/'),7,27],         #5
        [loadSprites('wilson/upAttack/'),5,19],       #6
        [loadSprites('wilson/downAttack/'),3,20],      #7
        [],                                                 #8  [loadSprites('wilson/leftAttack/')
        [loadSprites('wilson/rightAttack/'),5,39],    #9
        [],                   #10                               [loadSprites('wilson/special/')                   #10
        [loadSprites('wilson/airAttack/'),6,41],             #11
        [loadSprites('wilson/hurt/'),10,29],            #12
        [loadSprites('wilson/hurtair/'),10,19],           #13
        [loadSprites('wilson/collapse/'),7,69],    #14
        [loadSprites('wilson/death/'),20,139]]           #15

wilsonHitbox=[[0,0,0,0],             #-1,0
        [0,0,0,0],          #1
        [0,0,0,0],            #2
        [0,0,0,0],            #3
        [0,0,0,0],            #4
        [loadSprites('wilson/nAttack/hitbox/'),7,27,6,8],         #5
        [loadSprites('wilson/upAttack/hitbox/'),5,19,7,13],       #6
        [loadSprites('wilson/downAttack/hitbox/'),3,20,5,6],      #7
        [],                                                 #8  [loadSprites('wilson/leftAttack/')
        [loadSprites('wilson/rightAttack/hitbox/'),6,39,4,13],    #9
        [],                   #10                               [loadSprites('wilson/special/')                   #10
        [loadSprites('wilson/airAttack/hitbox/'),6,41,5,10],             #11
        [0,0,0,0],            #12
        [0,0,0,0],           #13
        [0,0,0,0],    #14
        [0,0,0,0]]          #15

class Player(sprite.Sprite):
    def __init__(self,n,char,charhit,inputs,px,py,vx,vy,direction,airborne,action,health):
        sprite.Sprite.__init__(self)
        self.n=n                    #player number (1,2)
        self.inputs=inputs          #player inputs [up,down,left,right,jump,attack,shield]
        self.char=char              #player character (0,1,2,3)
        self.charhit=charhit
        self.px=px                  #player pos x
        self.ex=0                   #enemy x
        self.ey=0                   #enemy y
        self.py=py                  #player pos y
        self.vx=vx                  #player velocity x
        self.vy=vy                  #player velocity y
        self.direction=direction    #player direction (rTrue,lFalse)
        self.airborne=airborne      #player airborne check (True False)
        self.inAction=False         #if player is taking an action
        self.action=action          #player action taken
        self.oAction=action
        self.hurtbox=Rect(self.px+20,self.py+5,60,145) #taking player hitbox
        self.cooldown=0             #animation timer cooldown
        self.ani=char[action][2]    #what frame limit player has per animation

        self.health=health          #player health
        self.hitstun=0                 #if player is unable to take action
        self.ouch=0
        self.lose=False
        #sprite class attributes
        self.image=self.char[self.action][0][self.cooldown//self.char[self.action][1]],(self.px-8,self.py)
        self.rect=Rect(self.px,self.py,100,150)

    def update(self):
##        if self.n==1:
##            print(self.health,self.ouch)
        self.ani=self.char[self.action][2]
        self.cooldown+=1
        if self.cooldown>self.ani:
            self.cooldown=0
            self.inAction=False
        if self.px<=avgpx:
            if self.action==6:
                self.rect=Rect(self.px-8,self.py,100,150)
                #check
            elif self.action==14:
                self.rect=Rect(self.px-90,self.py,100,150)
            else:
                self.rect=Rect(self.px,self.py,100,150)
            self.image=self.char[self.action][0][self.cooldown//self.char[self.action][1]]
            #check collision then return self image to normal

            self.direction=True
        else:
            if self.action==5:
                self.rect=Rect(self.px-22,self.py,100,150) #adjusting hitboxes
            elif self.action==6:
                self.rect=Rect(self.px-22,self.py,100,150)
            elif self.action==7:
                self.rect=Rect(self.px-28,self.py,100,150)
            elif self.action==9:
                self.rect=Rect(self.px-50,self.py,100,150)
            elif self.action==14:
                self.rect=Rect(self.px-10,self.py,100,150)
            elif self.action==15:
                self.rect=Rect(self.px-87,self.py,100,150)
            else:
                self.rect=Rect(self.px,self.py,100,150)
            self.image=transform.flip(self.char[self.action][0][self.cooldown//self.char[self.action][1]],True,False)
            self.direction=False
        # if self.action==13 or self.action==12:
        #     self.image

    def checkHit(self,image):
        pList=['',player1,player2]
        if self.n==1:
            oPlayer=2
        else:
            oPlayer=1
        if self.charhit[self.action][3]>0 and pList[oPlayer].action!=15:
            if self.direction:
                self.image=self.charhit[self.action][0][self.cooldown//self.charhit[self.action][1]]
            else:
                self.image=transform.flip(self.charhit[self.action][0][self.cooldown//self.charhit[self.action][1]],True,False)
            playerSprites.clear(screen,bg2)
            playerSprites.draw(screen)
            if sprite.collide_mask(pList[self.n],pList[oPlayer]) is not None and self.action!=14:
                if pList[oPlayer]!=12 or pList[oPlayer]!=13:
                    if pList[oPlayer].hitstun==0:
                        pList[oPlayer].hitstun=self.charhit[self.action][4]
                        if pList[oPlayer].inputs[2]:
                            pList[oPlayer].health-=self.charhit[self.action][3]/5
                        else:
                            pList[oPlayer].health-=self.charhit[self.action][3]
                        pList[oPlayer].ouch+=self.charhit[self.action][4]
                    if pList[oPlayer].direction:
                        pList[oPlayer].vx-=6
                    else:
                        pList[oPlayer].vx+=6
            self.image=image

    def showBoxes(self):
        if self.n==1:
            draw.rect(screen,GREEN,self.hurtbox,1)
        if self.n==2:
            draw.rect(screen,RED,self.hurtbox,1)

    def takeInput(self,n):
        'takeInput(n) - method which takes all inputs of a player)'
        p1InputList=[keys[K_UP],keys[K_DOWN],keys[K_LEFT],keys[K_RIGHT],keys[K_n],keys[K_m],keys[K_COMMA],keys[K_PERIOD]]
        p2InputList=[keys[K_w],keys[K_s],keys[K_a],keys[K_d],keys[K_x],keys[K_c],keys[K_v],keys[K_b]]
        pInputList=['',p1InputList,p2InputList]
        if self.health>0 and self.action!=14:
            for i in range(7):
                if pInputList[n][i]:
                    self.inputs[i]=True
                else:
                    self.inputs[i]=False
            if self.inputs[2] and self.inputs[3]:
                self.inputs[2]=False
                self.inputs[3]=False
            if self.action==12 or self.action==13:
                self.inputs[4]=False

    def findAction(self):
        if not self.direction:           #switching rightmost player inputs for left and right
            if self.inputs[2] or self.inputs[3]:
                temp=self.inputs[3]
                temp2=self.inputs[2]
                self.inputs[3]=temp2
                self.inputs[2]=temp
        if not self.inAction:
            if not self.airborne:
                if self.inputs[1]:
                    self.action=1
                elif self.inputs[2]:
                    self.action=2
                elif self.inputs[3]:
                    self.action=3
                elif self.inputs[0]:
                    self.action=0
                else:
                    self.action=0
            if self.inputs[4] and self.vy!=0 and self.inputs[5]==False:
                self.action=4
            elif self.inputs[5]:
                self.inAction=True
                if self.airborne:
                    self.action=11        #aerial attack
                elif self.action==0 and self.inputs[0]:
                    self.action=6
                elif self.action==1:
                    self.action=7
#                elif self.action==2: #back attack
#                    self.action=14
                elif self.action==3:
                    self.action=9
                else:
                    self.action=5        #n attack
        if self.hitstun>0:
            if self.action==2:
                self.hitstun-=2
                if self.hitstun<0:
                     self.hitstun=0
            else:
                if self.airborne:
                    self.action=13
                else:
                    self.action=12
                self.hitstun-=1

        self.ouch-=1/2
        if self.ouch<=0:
            self.ouch=0
        if self.ouch>25:
            self.action=14
            self.vx=0
            self.vy=0
            self.ouch=0
        if self.oAction==14 and self.cooldown!=69:
            self.action=14
        if self.oAction!=self.action: #cooldown timer resets whenever a new action is performed
            self.cooldown=0
        self.oAction=self.action
        if self.health<=0:
            self.action=15
            self.vx=0
            self.vy=0
            if self.cooldown==139:
                self.lose=True
#        if self.n==2:
#            print(self.oAction,self.action)
    def findVelocity(self):
        # avgpx=(player1.px+player2.px)/2
        i=1
        if self.inputs[2]: #section applies velocity left=-1, right=+1
            i=-1
        if self.inputs[3]:
            i=1
        if self.inputs[2] or self.inputs[3]:
            if not self.airborne:
                self.vx+=25*i
                if self.inputs[3]:
                    if abs(self.vx)>65:
                        self.vx=65*i
                else:
                    if abs(self.vx)>55:
                        self.vx=55*i
            else:
                self.vx+=35*i
                if abs(self.vx)>50:
                    self.vx=50*i
        if self.inputs[2] and self.inputs[3] or self.inputs[1]: #left and right input or crouch
            if not self.airborne:
                self.vx=0
        self.vx=friction(self.vx)
        if self.inputs[4] and self.airborne==False and self.inputs[1]==False:
            self.vy=275
            self.airborne=True
            if self.inAction:
                self.vy=0
                self.airborne=False
        if self.airborne:
            self.vy-=12
            if self.inputs[1]:
                if self.vy>-15:
                    self.vy=-25
                self.vy-=10
        if self.inAction:
            if not self.airborne:
                self.vx=0
                self.vy=0

    def updatePos(self): #updates all movement of a character
        self.px+=self.vx/dt
        self.py-=self.vy/dt
        self.hurtbox=findHitbox(self.px,self.py,self.inputs,self.airborne,self.action)
        if self.px+25>=1200-75:
            self.vx=0
            self.px=1100
        if self.px<0:
            self.vx=0
            self.px=0
        self.hurtbox=findHitbox(self.px,self.py,self.inputs,self.airborne,self.action)
        if self.hurtbox.colliderect(groundRect) or self.inputs[4] and self.airborne==False and self.inAction==False:
            self.airborne=False
            self.cooldown=0
            self.inAction=False
        elif self.py==400:
            self.airborne=False
        else:
            self.airborne=True
        if not self.airborne:
            self.vy=0
            self.py=400
            self.hurtbox=findHitbox(self.px,self.py,self.inputs,self.airborne,self.action)
        else:
            self.airborne=True
        if self.hurtbox.colliderect(Rect(self.ex+20,self.ey+5,60,145)):
            if self.direction:
                self.vx-=7.5
                self.vx=friction(self.vx)
            else:
                self.vx+=7.5
                self.vx=friction(self.vx)
        self.hurtbox=findHitbox(self.px,self.py,self.inputs,self.airborne,self.action)

class PlayerDisplay(object):
    def __init__(self,x,y,n):
        self.x=x
        self.y=y
        self.n=n
        self.health=100

    def healthBar(self,n,health):
        self.health=health
        if self.n==1:
            draw.rect(screen,BLACK,(150,40,400,50))
            rect=Rect(self.x+1,self.y-10,self.health*-2,50)
            rect.normalize()
            draw.rect(screen, BLUE, rect)
        if self.n==2:

            draw.rect(screen,BLACK,(650,40,400,50))
            draw.rect(screen,RED,(self.x-1,self.y-10,self.health*2,50))
        screen.blit(ui,(127,22))
        if player1.action==12 or player1.action==13 or player2.action==12 or player2.action==13 or player1.action==15 or player2.action==15:
            screen.blit(skull,(550,17))

def drawScreen(t):
    'drawScreen(n) - Displays everything need on screen, depending on type of game'
    playerSprites.clear(screen,bg2)
    screen.blit(bg4,(0,0))
    screen.blit(ground,groundRect)
    screen.blit(ground2,(0,525))
    #draw.rect(screen,(90,39,41),(groundRect))
    #draw.rect(screen,BLACK,(0,575,1200,125))
    playerSprites.draw(screen)
    player1.showBoxes()
    player2.showBoxes()
    health1.healthBar(1,player1.health)
    health2.healthBar(2,player2.health)


class projectile(sprite.Sprite):
    def __init__(self,n,px,py,vx,vy,direction):
        sprite.Sprite.__init__(self)
        self.n=n                    #player number (1,2)
        self.px=px                  #player pos x
        self.py=py                  #player pos y
        self.vx=vx                  #player velocity x
        self.vy=vy                  #player velocity y
        self.direction=direction    #player direction (rTrue,lFalse)

RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
CREAM=(245,242,208)

bg2=image.load('backgrounds/autumn2.png').convert()
bg3=image.load('backgrounds/bg3.png').convert()
bg4=image.load('backgrounds/autumn3.png').convert()
ground=image.load('backgrounds/ground.png').convert()
ground2=image.load('backgrounds/ground2.png').convert()
beefalo=image.load('icons/beefaloIcon.png').convert_alpha()
ui=image.load('backgrounds/ui.png').convert_alpha()
skull=image.load('icons/skull.png').convert_alpha()

music=mixer.music.load("music/Don't Starve Together - Main Theme2.wav")

menuClick=mixer.Sound('music/menuClick.wav')
#charList=[wilson,wendy,woodie,willow]
groundRect=Rect(0,550,1200,200)
playerSprites=sprite.Group()

player1=Player(1,wilson,wilsonHitbox,[False,False,False,False,False,False,False],400-50,400,0,0,True,False,-1,200)
player2=Player(2,wilson,wilsonHitbox,[False,False,False,False,False,False,False],800-50,400,0,0,False,False,-1,200)
playerSprites.add(player1)
playerSprites.add(player2)

health1=PlayerDisplay(550,50,1)
health2=PlayerDisplay(650,50,2)

myClock=time.Clock()
dt=myClock.tick(60)

running=True
def game(mode):
    myClock = time.Clock()
    myClock.tick(60)

    global keys
    global avgpx
    global evt
    pList=['',player1,player2]
    screen.blit(bg2,(0,0))

    player1.px,player1.px=350,400
    player2.px,player2.py=750,400
    running=True
    while running:
        for evt in event.get():
            if evt.type==KEYDOWN:
                if evt.key==K_ESCAPE:
                    running=False
            if evt.type==QUIT:
                quit()
        keys=key.get_pressed()
        for i in range(1,3,1):
            pList[i].takeInput(i)
            pList[i].checkHit(pList[i].image)
            pList[i].findVelocity()
            pList[i].findAction()
            pList[i].updatePos()
        avgpx=(player1.px+player2.px)/2
        player1.ex,player1.ey=player2.px,player2.py
        player2.ex,player2.ey=player1.px,player1.py

        #print(player1.lose,player2.lose)
        playerSprites.update()
        drawScreen(0)
        myClock.tick(60)
        display.flip()

titleMenu()
# CSS('multi')
# game(1)
quit()
