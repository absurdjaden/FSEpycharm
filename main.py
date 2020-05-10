# Jaden Hong
# ICS3U-02
#
# title screen don't starve together -> do fight together
# -types of animations :
# - idle, walking, jump?, attackUP,attackDOWN,attackLR,attackN,shield?,special, nair Leg attack
#
# controls:
# PLAYER 1-
# arrow keys, n jump, m attack, comma shield
#
# PLAYER 2-
# WASD, x jump, c attack, v shield,


from pygame import *
from random import *
font.init()
mixer.init()
width,height=1200,700
screen=display.set_mode((width,height))
screenRect=Rect(0,0,width,height)

def TITLEMENU():
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
    optionSel=3
    wordList=['',word1,word2,word3,word4,word5,word6,word7]
    mixer.music.play(-1)
    while running:
        for evt in event.get():
            if evt.type==KEYDOWN:
                if evt.key==K_RETURN:
                    menu='t main menu'
                    if optionSel==4: #singleplayer
                        menuClick.play()
                        mixer.music.stop()
                        musicStop=True
                        optionSel=CSS('single')
                    if optionSel==5: #multiplayer
                        menuClick.play()
                        mixer.music.stop()
                        musicStop=True
                        optionSel=CSS('multi')
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
                quit()
        if musicStop:
            mixer.music.play(-1)
            musicStop=False
        screen.blit(titleBG,(0,0))
        if menu=='title':             #title
            for i in range(1,4,1):
                wordList[i].fadeIn()
                wordList[i].chosen(i,False)
        if menu=='t main menu':             #transition
            for i in range(1,4,1):
                wordList[i].fadeAway()
            if word3.alpha==0:
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
            optionSel=3
            word1.fadeAway()
            if word4.alpha==0:
                menu='title'
                menuClick.play()
        word7.basic()
        display.flip()

def CSS(mode):
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
    p1InputList=[False,False,False,False,False,False,False]
    p2InputList=[False,False,False,False,False,False,False]
    pInputList=['',p1InputList,p2InputList]
    pList=[0,player1,player2]
    pListSel=[0,player1Sel,player2Sel]
    playerPortrait=[wilsonPortrait,wendyPortrait,woodiePortrait,willowPortrait]
    charList=[[wilson,wilsonHitbox,0,100,150,50],
              [wilson,wilsonHitbox,0,100,150,50],
              [wilson,wilsonHitbox,0,100,150,50],
              [wilson,wilsonHitbox,0,100,150,50]]

    while running:
        for evt in event.get():
            if evt.type==KEYDOWN:
                for i in range(1,3):
                    if evt.key==pInputList[i][2]:
                        pListSel[i]+=1
                        if pListSel[i]>3:
                            pListSel[i]=0
                    if evt.key==pInputList[i][3]:
                        pListSel[i]-=1
                        if pListSel[i]<0:
                            pListSel[i]=3
                    if evt.key==pInputList[i][5]:
                        pList[i]=True
                    if evt.key==pInputList[i][4]:
                        pList[i]=False
                if evt.key==K_RETURN:
                    if pList[1] and pList[2]:
                        one=pListSel[1]
                        two=pListSel[2]
                        game(mode,Player(1,charList[one][0],charList[one][1],charList[one][2],charList[one][3],
                                        charList[one][4],charList[one][5],[False,False,False,False,False,False,False],
                                         400,700,0,0,True,False,0,200),
                                  Player(2,charList[two][0],charList[two][1],charList[two][2],charList[two][3],
                                        charList[two][4],charList[two][5],[False,False,False,False,False,False,False],
                                         700,700,0,0,True,False,0,200))
                if evt.key==K_ESCAPE:
                    running=False
            if evt.type==QUIT:
                quit()

        p1InputList=[K_UP,K_DOWN,K_LEFT,K_RIGHT,K_n,K_m,K_COMMA]
        p2InputList=[K_w,K_s,K_a,K_d,K_x,K_c,K_v,K_b]
        pInputList=['',p1InputList,p2InputList]

        screen.blit(cssBG,(0,0))
        screen.blit(playerPortrait[pListSel[1]],(600,100))
        screen.blit(playerPortrait[pListSel[2]],(900,100))
        word1.basic()
        if pList[1]:
            p1word2.basic()
        else:
            p1word1.floating(25)
        if pList[2]:
            p2word2.basic()
        else:
            p2word1.floating(25)
        if pList[1] and pList[2]:
            word2.floating(25)
        display.flip()
    return 3

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
def VICTORY(mode,char1,char2):
    myClock=time.Clock()
    myClock.tick(60)
    running=True
    charQuotes=[['Your existence is an affront to the laws of science, Wilson!',
                 'Murderer!',
                 "Murder! Bring me an axe and we'll get in the swing of things!",
                 'Murderer! Arsonist!',
                 'This was really gross!',
                 "I don't know exactly what that thing was.",
                 "That was one fly dragon!",
                 "What a bear of a badger."],                #wilson quotes
                ["You've gone mad, scientist.",
                 "Have we not seen enough death, Wendy?",
                 "I'll send you someplace much nicer than this, Woodie.",
                 "You've made a terrible error, Willow.",
                 "Death incarnate!",
                 "It was an abomination.",
                 "It was burning on the inside",
                 "It smelt like death."], #wendy quotes
                ['Enemy of the Forest!',
                 "Hereeee's Woodie!",
                 "Hey, c'mere Woodie! I've gotta AXE you question!",
                 "Here comes the wildfire!",
                 "That was a big moose!",
                 "Whatever it was, it was definitely Canadian!",
                 "He would've burn down all the trees before I chopped them",
                 "That was a big bear!"], #woodie quotes
                ["Hey Wilson! Your hair is dumb! Raaaugh!",
                 "She's gone nuts! Murderer!",
                 "Murderer. BURN!",
                 "Murderer! Burn the impostor!",
                 "Holy Crap!",
                 "What in the world was that...",
                 "It was filled with fire.",
                 "It's fur all the way down."]] #willow quotes,,,


    if mode=='multi':
        if char1.points==2:
            word1=MyText(charQuotes[char1.charType][char2.charType],40,CREAM,255,100,500)
            word2=MyText(charList[char1.charType]+' WINS!',100,WHITE,255,100,100)
        else:
            word1=MyText(charQuotes[char2.charType][char2.charType],40,CREAM,255,100,500)
            word2=MyText(charList[char2.charType]+' WINS!',100,WHITE,255,100,100)
    else:
        if char1.points==2:
            word1=MyText(charQuotes[char1.charType][char2.charType],40,CREAM,255,100,500)
            word2=MyText(charList[char1.charType]+' WINS!',100,WHITE,255,100,100)
        else:
            word1=MyText(('Day '+str(randint(0,100))+' Everyone is dead'),40,CREAM,255,100,500)
            word2=MyText(charList[char2.charType]+' WINS!',100,WHITE,255,100,100)

    draw.rect(screen,BLACK,(0,0,1200,700))
    screen.blit(skull,(600-50,300))
    while running:
        for evt in event.get():
            if evt.type==KEYDOWN:
                if evt.key==K_RETURN:
                    TITLEMENU()
            if evt.type==QUIT:
                quit()
        draw.rect(screen,BLACK,(0,0,1200,700))
        word1.basic()
        word2.basic()
        display.flip()

def updateCamera(mode,player1,player2,leftpx,cameraRect):
    pList=[0,player1,player2]
    if player1.push:
        i=1
    elif player2.push:
        i=2

    if pList[i].px <= leftpx:  # p1[   p2]
        leftpx = pList[i].px
    elif pList[i].px >= leftpx + 720 - pList[i].width:  # [p2   ]p1
        leftpx = pList[i].px - 720 + pList[i].width

    if leftpx<0:
        leftpx=0
    elif leftpx>480:
        leftpx=480

    if mode=='single':
        cameraRect=Rect(leftpx,150,720,420)
    if mode=='multi':
        cameraRect=Rect(leftpx,150,720,420)
    return cameraRect,leftpx


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
def findHitbox(n,pList):
    pList[n].hurtbox=Rect(pList[n].px+20,pList[n].py+5,60,145)
    if pList[n].charType<4:
        if pList[n].inputs[1] and pList[n].airborne==False and pList[n].action==1 or pList[n].action==7:
            pList[n].hurtbox=Rect(pList[n].px+20,pList[n].py+20,60,130)
        if pList[n].airborne:
            pList[n].hurtbox=Rect(pList[n].px+20,pList[n].py,60,140)
    else:
        if pList[n].direction:
            pList[n].hurtbox=Rect(pList[n].px+10,pList[n].py+30,230,320)
        else:
            pList[n].hurtbox=Rect(pList[n].px+10,pList[n].py+30,230,320)


#classes
class ScreenDisplay(object):
    def __init__(self,n,effect,selection):
        self.n=n
        self.effect=effect
        self.selection=selection
        self.confirm=False
        self.inputs=[False,False,False,False,False,False,False]
        self.basicList=[]
        self.floatingList=[]

    def takeInput(self):
        p1InputList=[keys[K_UP],keys[K_DOWN],keys[K_LEFT],keys[K_RIGHT],keys[K_n],keys[K_m],keys[K_COMMA],keys[K_RETURN]]
        p2InputList=[keys[K_w],keys[K_s],keys[K_a],keys[K_d],keys[K_x],keys[K_c],keys[K_v],keys[K_RETURN]]
        pInputList=['',p1InputList,p2InputList]
        for i in range(7):
            if pInputList[self.n][i]:
                self.inputs[i]=True
            else:
                self.inputs[i]=False

    def choose(self,evt,bounds):
        for i in range(1,3):
            if evt.key==self.inputs[2]:
                self.selection+=1
                if self.selection>bounds[1]:
                    self.selection=bounds[0]
            if evt.key==self.inputs[3]:
                self.selection-=1
                if self.selection<bounds[0]:
                    self.selection=bounds[1]
            if evt.key==self.inputs[5]:
                self.confirm=True
            if evt.key==self.inputs[4]:
                self.confirm=False

    def drawScreenDisplay(self,x,y,w,h,bg):
        screen.blit(bg,(x,y,w,h))
        for w in self.basicList:
            self.basicList[w].basic()
        for w in self.floatingList:
            self.floatingList[w].floating()

    def openMenu(self):

    def closeMenu(self):
		#fade screen to black
		#
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
        [loadSprites('wilson/walk/'),8,63],            #3
        [loadSprites('wilson/jump/'),16,45],            #4
        [loadSprites('wilson/nAttack/'),7,27],         #5
        [loadSprites('wilson/upAttack/'),5,19],       #6
        [loadSprites('wilson/downAttack/'),3,20],      #7
        [loadSprites('wilson/leftAttack/'),10,29],        #8
        [loadSprites('wilson/rightAttack/'),5,39],    #9
        # [],                   #10                               [loadSprites('wilson/special/')                   #10
        [loadSprites('wilson/airAttack/'),6,41],             #11
        [loadSprites('wilson/hurt/'),10,29],            #12
        [loadSprites('wilson/hurtair/'),10,19],           #13
        [loadSprites('wilson/collapse/'),7,69],    #14
        [loadSprites('wilson/death/'),20,139]]           #15

wilsonHitbox=[[0,0,0,0],             #-1,0
              [0,0,0,0],          #1
              [0,0,0,0],            #2
              [0,0,0,0],            #3
              [0,0,0,0],            #4              inc,tot,damage,hitstun
              [loadSprites('wilson/nAttack/hitbox/'),7,27,15,10],         #5
              [loadSprites('wilson/upAttack/hitbox/'),5,19,12,6],       #6
              [loadSprites('wilson/downAttack/hitbox/'),3,20,10,10],      #7
              [loadSprites('wilson/leftAttack/hitbox/'),10,29,15,5],             #8
              [loadSprites('wilson/rightAttack/hitbox/'),5,39,15,17],    #9
              # [],                   #10                               [loadSprites('wilson/special/')                   #10
              [loadSprites('wilson/airAttack/hitbox/'),6,41,15,14],             #11
              [0,0,0,0],            #12
              [0,0,0,0],           #13
              [0,0,0,0],    #14
              [0,0,0,0]]          #15


#boss data
deerclops=[[loadSprites('deerclops/idle/'),20,79],              #0      x
           [loadSprites('deerclops/walk/'),7,41],              #1       x
           [loadSprites('deerclops/iceAttack/'),15,104],         #2
           [loadSprites('deerclops/slashAttack/'),20,79],       #3
           [loadSprites('deerclops/hurt/'),5,19],              #4       x
           [loadSprites('deerclops/death/'),14,139],]            #5
#
deerclopsHitbox=[[0,0,0,0],
                 [0,0,0,0],
                 [loadSprites('deerclops/iceAttack/hitbox/'),15,104,100,25],
                 [loadSprites('deerclops/slashAttack/hitbox/'),34,25],
                 [0,0,0,0],
                 [0,0,0,0]]


class Player(sprite.Sprite):
    def __init__(self,n,char,charhit,charType,width,height,speed,inputs,px,py,vx,vy,direction,airborne,action,health):
        sprite.Sprite.__init__(self)

        self.n=n                    #player number (1,2)
        self.inputs=inputs          #player inputs [up,down,left,right,jump,attack,shield]
        self.char=char              #player character (0,1,2,3)
        self.charhit=charhit
        self.charType=charType
        self.width=width
        self.height=height
        self.px=px                  #player pos x
        self.speed=speed

        self.push=False

        if n==1:
            self.oPlayer=2
        else:
            self.oPlayer=1

        self.py=py                  #player pos y
        self.vx=vx                  #player velocity x
        self.vy=vy                  #player velocity y
        self.direction=direction    #player direction (rTrue,lFalse)
        self.airborne=airborne      #player airborne check (True False)
        self.inAction=False         #if player is taking an action
        self.action=action          #player action taken
        self.oAction=action
        self.hurtbox=Rect(self.px+20,self.py+5,60,height) #taking player hitbox
        self.cooldown=0             #animation timer cooldown
        self.ani=char[action][2]    #what frame limit player has per animation

        self.health=health          #player health
        self.hitstun=0                 #if player is unable to take action
        self.hitten=False
        self.pHitten=False
        self.superArmor=False

        self.ouch=0
        self.lose=False
        self.points=0
        self.projectileCount=0
        self.proj=0

        #sprite class attributes
        self.image=char[action][0][self.cooldown//char[action][1]],(px-8,py)

        self.rect=Rect(px,py,width,height)
    def update(self,pList):
        self.ani=self.char[self.action][2]
        self.cooldown+=1
        if self.charType<4:
            adjustListL=[0,0,0,0,0,-22,-22,-28,0,-50,0,0,0,-10,-87]
            adjustListR=[0,0,0,0,0,0,-8,0,0,0,0,0,0,-90,0]
            adjustListU=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        else:
            adjustListL=[0,0,-250,0,0,0]
            adjustListR=[0,0,-100,0,0,0]
            adjustListU=[0,-5,-50,0,-60,0]
        if self.cooldown>self.ani:
            self.cooldown=0
            self.inAction=False
        if self.px+self.width/2<=avgpx:
            self.rect=Rect(self.px+adjustListR[self.action],self.py+adjustListU[self.action],self.width,self.height)
            self.image=self.char[self.action][0][self.cooldown//self.char[self.action][1]]
            self.direction=True
        else:
            self.rect=Rect(self.px+adjustListL[self.action],self.py+adjustListU[self.action],self.width,self.height)
            self.image=transform.flip(self.char[self.action][0][self.cooldown//self.char[self.action][1]],True,False)
            self.direction=False

    def checkHit(self,image,pList,playerSprites):
        attackd=False
        if pList[self.n].charType>3:
            if self.anger>2:
                self.superArmor=True
            else:
                self.superArmor=False
        if pList[self.oPlayer].action!=14 and pList[self.oPlayer].superArmor==False:
            if self.charhit[self.action][2]>0:
                if self.direction:
                    self.image=self.charhit[self.action][0][self.cooldown//self.charhit[self.action][1]]
                else:
                    self.image=transform.flip(self.charhit[self.action][0][self.cooldown//self.charhit[self.action][1]],True,False)
                playerSprites.clear(screen,autumnBG)
                playerSprites.draw(screen)
                if sprite.collide_mask(pList[self.n],pList[self.oPlayer]) is not None and pList[self.oPlayer].action<13:
                    if not pList[self.n].hitten:
                        if pList[self.oPlayer]!=11 or pList[self.oPlayer]!=12:
                            if pList[self.oPlayer].hitstun==0:
                                pList[self.oPlayer].hitstun=self.charhit[self.action][4]
                                if pList[self.oPlayer].inputs[2] and pList[self.n].charType<4:
                                    pList[self.oPlayer].health-=self.charhit[self.action][3]/5
                                else:
                                    pList[self.oPlayer].health-=self.charhit[self.action][3]
                                pList[self.oPlayer].ouch+=self.charhit[self.action][4]
                            pList[self.n].hitten=True
                            if pList[self.oPlayer].charType>3:
                                pList[self.oPlayer].anger+=1
                attackd=True

        if self.projectileCount>0 and self.superArmor==False: #checking for projectile collision
            if sprite.collide_mask(pList[self.n].proj,pList[self.oPlayer]) is not None and pList[self.oPlayer].action<13:
                if not pList[self.n].pHitten:
                    if pList[self.oPlayer].hitstun==0:
                        pList[self.oPlayer].hitstun=self.charhit[8][4]
                        if pList[self.oPlayer].inputs[2]:
                            pList[self.oPlayer].health -= self.charhit[8][3]/5
                        else:
                            pList[self.oPlayer].health -= self.charhit[8][3]
                        pList[self.oPlayer].ouch += self.charhit[8][4]
                    pList[self.n].pHitten=True
                    if pList[self.oPlayer].charType>3:
                        pList[self.oPlayer].anger+=1
                attackd=True
        #giving super armor to bosses
        if attackd and self.cooldown==self.char[self.action][2]:
            if self.superArmor:
                self.superArmor=False
                self.anger=0

        self.image=image

    def takeInput(self,n,pList):
        'takeInput(n) - method which takes all inputs of a player)'
        p1InputList=[keys[K_UP],keys[K_DOWN],keys[K_LEFT],keys[K_RIGHT],keys[K_n],keys[K_m],keys[K_COMMA],keys[K_PERIOD]]
        p2InputList=[keys[K_w],keys[K_s],keys[K_a],keys[K_d],keys[K_x],keys[K_c],keys[K_v],keys[K_b]]
        pInputList=['',p1InputList,p2InputList]
        print(pInputList)
        if self.health>0 and self.action!=13:
            for i in range(7):
                if pInputList[n][i]:
                    self.inputs[i]=True
                else:
                    self.inputs[i]=False
            if self.inputs[2] and self.inputs[3]:
                self.inputs[2]=False
                self.inputs[3]=False
            if self.action==11 or self.action==12:
                self.inputs[4]=False

    def findAction(self,projectileSprites,pList):
        if self.action!=13:
            if not self.direction:           #switching rightmost player inputs for left and right
                if self.action!=14:
                    if self.inputs[2] or self.inputs[3]:
                        temp=self.inputs[3]
                        temp2=self.inputs[2]
                        self.inputs[3]=temp2
                        self.inputs[2]=temp
            if not self.inAction:
                if self.action!=14:
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
                elif self.inputs[5] and self.action!=13:
                    self.hitten=False
                    self.inAction=True
                    if self.airborne:
                        self.action=10        #aerial attack
                    elif self.action==0 and self.inputs[0]:
                        self.action=6
                    elif self.action==1:
                        self.action=7
                    elif self.action==2: #back attack
                        self.action=8
                        if self.projectileCount<1:
                            if self.char==wilson:
                                self.proj = Projectile(self.n, blowdart, self.px, self.py, 7, 0, self.direction)
                                projectileSprites.add(self.proj)
                                self.projectileCount+=1
                    elif self.action==3:
                        self.action=9
                    else:
                        self.action=5        #n attack
        else:
            if self.cooldown==69:
                self.action=0
        #check hitstun animation
        if self.hitstun>0 and self.action!=5 and self.action!=13:
            self.vx=0
            self.vy=0
            if self.action==2:
                self.hitstun-=2
                if self.hitstun<0:
                    self.hitstun=0
            else:
                if self.airborne:
                    self.action=12
                else:
                    self.action=11
                self.hitstun-=1
        self.ouch-=0.25
        if self.ouch<=0:
            self.ouch=0
        if self.ouch>40:
            self.cooldown=0
            self.action=13
            self.oAction=13
            self.vx=0
            self.vy=0
            self.ouch=0
            self.hitstun=0

        if self.oAction!=self.action and self.oAction!=14: #cooldown timer resets whenever a new action is performed
            if self.action!=0 or self.oAction!=13:
                self.cooldown=0
                pList[self.n].hitten=False
        self.oAction = self.action
        if self.health<=0 and self.airborne==False:
            self.action=14
            self.vx=0
            self.vy=0
            if self.cooldown==self.char[14][2]:
                self.lose=True

    def findVelocity(self,charSpeed):
        i=1
        if self.inputs[2]: #section applies velocity left=-1, right=+1
            i=-1
        if self.inputs[3]:
            i=1
        if self.action!=13 and (self.inputs[2] or self.inputs[3]):
            if not self.airborne:
                self.vx+=(charSpeed-25)*i
                if abs(self.vx)>charSpeed+15:
                    self.vx=(charSpeed+20)*i
                    if (self.inputs[2] and self.direction) or (self.inputs[3] and self.direction==False):
                        self.vx=(charSpeed+10)*i
            else:
                self.vx+=(charSpeed-15)*i
                if abs(self.vx)>50:
                    self.vx=charSpeed*i
        if self.inputs[2] and self.inputs[3] or self.inputs[1]: #left and right input or crouch
            if not self.airborne:
                self.vx=0
        self.vx=friction(self.vx)
        if self.inputs[4] and self.airborne==False and self.inputs[1]==False and self.action<4:
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

    def updatePos(self,mode,pList,cameraRect,leftpx): #updates all movement of a character
        opx=self.px
        self.px+=round(self.vx/dt)
        self.py-=round(self.vy/dt)
        if abs(pList[1].px-pList[2].px)>720-self.width:
            self.px=opx
            self.vx=0
        if self.push and abs(pList[1].px-pList[2].px)<=720-self.width:
            cameraRect, leftpx = updateCamera(mode, pList[1], pList[2], leftpx, cameraRect)
        self.push=False
        pList[self.oPlayer].oPush=False
        if self.px <= leftpx or self.px>=leftpx+720-self.width:
            if cameraRect.collidepoint(self.px-self.width,self.py)==False or cameraRect.collidepoint(self.px+self.width,self.py)==False:
                self.push=True

        if self.px>1200-self.width:
            self.vx=0
            self.px=1200-self.width
        if self.px<0:
            self.vx=0
            self.px=0

        findHitbox(self.n,pList)

        if self.hurtbox.colliderect(groundRect) or self.inputs[4] and self.airborne==False and self.inAction==False:
            if self.action!=14:
                self.airborne=False
                self.cooldown=0
                self.inAction=False

        elif self.py==550-self.height:
            self.airborne=False
        else:
            self.airborne=True
        if not self.airborne:
            self.vy=0
            self.py=550-self.height
            findHitbox(self.n,pList)
        else:
            self.airborne=True
        if self.hurtbox.colliderect(pList[self.oPlayer].hurtbox) and self.hitstun<=0:
            if self.direction:
                self.vx-=7.5
                self.vx=friction(self.vx)
            else:
                self.vx+=7.5
                self.vx=friction(self.vx)
        findHitbox(self.n,pList)
        return cameraRect, leftpx

class Boss(Player):
    def __init__(self,n,char,charhit,charType,width,height,speed,inputs,px,py,vx,vy,direction,airborne,action,health):
        Player.__init__(self,n,char,charhit,charType,width,height,speed,inputs,px,py,vx,vy,direction,airborne,action,health)
        self.inRange=False
        self.py=py
        self.hurtbox=Rect(self.px+10,self.py+30,230,320) #taking boss hitbox
        self.anger=0





    def takeInput(self,n,pList):
        'takeInput(n) - method which takes all inputs of a boss'
        radius=0
        rng=randint(0,100)
        avgpx=(pList[1].px+pList[2].px)/2

        #walking towards player
        self.inputs[3],self.inputs[2]=False,False #left and right
        if not pList[1].hurtbox.colliderect(pList[2].hurtbox) and pList[self.oPlayer].action<14:          #Rect(self.px-radius,self.py+30,230+2*radius,320)
            if self.px<=avgpx:
                self.inputs[3]=True
            else:
                self.inputs[2]=True
            self.inRange=False
            self.inputs[5]=False

        else:
            self.inRange=True

        if self.inRange: #boss in range for attack
            if pList[self.oPlayer].health>0:
                if rng<50:
                    self.inputs[5]=True
                elif rng<85:
                    self.inputs[5]=True
                else:
                    self.inputs[5]=True

    def findAction(self,projectileSprites,pList):
        # print(self.action,self.anger,self.inputs[5])
        if self.action!=5: #not dead
            if not self.direction:           #switching rightmost player inputs for left and right
                if self.action!=14:
                    if self.inputs[2] or self.inputs[3]:
                        temp=self.inputs[3]
                        temp2=self.inputs[2]
                        self.inputs[3]=temp2
                        self.inputs[2]=temp
            if not self.inAction:
                if not self.airborne:
                    if self.inputs[1]:
                        self.action=0
                    elif self.inputs[2]:
                        self.action=1
                    elif self.inputs[3]:
                        self.action=1
                    elif self.inputs[0]:
                        self.action=0
                    else:
                        self.action=0
                if self.inputs[5] and self.action!=13:
                    self.hitten=False
                    self.inAction=True
                    self.action=2
        else:
            if self.cooldown==69 and self.action!=5:
                self.action=0

        if self.hitstun>0:
            self.vx=0
            self.vy=0
            self.hitstun-=1
            self.action=4
            self.inAction=True
        #comment out later
        self.ouch-=0.25
        if self.ouch<=0:
            self.ouch=0
        if self.ouch>40:
            self.cooldown=0
            self.action=4
            self.oAction=4
            self.vx=0
            self.vy=0
            self.ouch=0

        if self.oAction!=self.action and self.oAction!=5: #cooldown timer resets whenever a new action is performed
            if self.action!=0:
                self.cooldown=0
                pList[self.n].hitten=False
        self.oAction = self.action

        if self.health<=0 and self.airborne==False:
            self.action=5
            self.vx=0
            self.vy=0
            if self.cooldown==self.char[5][2]:
                self.lose=True


class PlayerDisplay(object):
    def __init__(self,x,y,n):
        self.x=x
        self.y=y
        self.n=n
        self.health=100

    def healthBar(self,n,health,player1,player2):
        self.health=health
        if self.n==1:
            draw.rect(screen,BLACK,(150,40,400,50))
            rect=Rect(self.x,self.y,self.health*-2,50)
            rect.normalize()
            draw.rect(screen,LIME,rect)
        if self.n==2:
            draw.rect(screen,BLACK,(650,40,400,50))
            draw.rect(screen,LIME,(self.x,self.y,self.health*2,50))
        screen.blit(ui,(127,22))
        if player1.action==11 or player1.action==12 or player2.action==11 or player2.action==12 or player1.action==14 or player2.action==14:
            screen.blit(skull,(550,17))

    def stunBar(self,ouch,player1,player2):
        self.ouch=ouch
        if self.n==1:
            draw.rect(screen,BLACK,(850,110,200,25))
            rect=Rect(self.x,self.y,self.ouch*-5,25)
            rect.normalize()
            draw.rect(screen,YELLOW,rect)
            for i in range(player2.points):
                screen.blit(playerIcons[0],(self.x+30*i+5,self.y-75))
        if self.n==2:
            draw.rect(screen,BLACK,(150,110,200,25))
            draw.rect(screen,YELLOW,(self.x,self.y,self.ouch*5,25))
            for i in range(player1.points):
                screen.blit(playerIcons[0],(self.x-30*i-75,self.y-75))

    # draw.circle(screen, WHITE, (round(player1.px+player1.width / 2), round(player1.py)), 5)
    # draw.circle(screen, WHITE, (round(player2.px+ player2.width / 2), round(player2.py)), 5)
    #

def drawScreen(mode,player1,player2,playerSprites,projectileSprites,cameraRect):
    'drawScreen(n) - Displays everything need on screen, depending on type of game'
    playerSprites.clear(screen,autumnBG)
    projectileSprites.clear(screen,autumnBG)
    screen.blit(autumnBG,(0,0))
    screen.blit(autumnBG2,(0,0))
    screen.blit(autumnGR,groundRect)
    screen.blit(autumnGR2,(0,525))
    #draw.rect(screen,(90,39,41),(groundRect))
    #draw.rect(screen,BLACK,(0,575,1200,125))
    # draw.rect(screen,GREEN,player1.hurtbox,1)
    # draw.rect(screen,RED,player2.hurtbox,1)
    # draw.rect(screen,BLUE,player2.rect,1)
    # draw.circle(screen, YELLOW, (round(avgpx), round(player1.py - 120)), 5)
    # draw.rect(screen,WHITE,Rect(player2.px,player2.py+30,230,320))
    # draw.circle(screen, WHITE, (round(player1.px), round(player1.py)), 5)
    # draw.circle(screen, WHITE, (round(player2.px), round(player2.py)), 5)
    playerSprites.draw(screen)
    projectileSprites.draw(screen)


    copy=screen.subsurface(cameraRect).copy()
    copy=transform.smoothscale(copy,(width,height))
    screen.blit(copy,(0,0))
    # draw.rect(screen,WHITE,cameraRect,1)

    health1.healthBar(1,player1.health,player1,player2)
    health2.healthBar(2,player2.health,player1,player2)
    ouch1.stunBar(player1.ouch,player1,player2)
    ouch2.stunBar(player2.ouch,player1,player2)

class Projectile(sprite.Sprite):
    def __init__(self, n, pType, px, py, vx, vy, direction):
        sprite.Sprite.__init__(self)
        self.image=pType            #
        self.pType=pType
        self.rect=Rect(px-27,py-11,55,22)
        self.n=n                    #player number (1,2)
        self.px=px                  #projectile pos x
        self.py=py                  #projectile pos y
        self.vx=vx                  #projectile velocity x
        self.vy=vy                  #projectile velocity y
        self.direction=direction    #projectile direction (rTrue,lFalse)

    def update(self,pList,projectileSprites):
        if self.direction:
            self.px+=self.vx
            self.rect=Rect(self.px+27+18,self.py-11+90,55,22)
        else:
            self.image=transform.flip(self.pType, True, False)
            self.px-=self.vx
            self.rect=Rect(self.px,self.py-11+90,55,22)
        if self.px+27<0 or self.px-27>1200:
            self.remove(projectileSprites)
            pList[self.n].projectileCount-=1
            pList[self.n].pHitten=False


RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)

CREAM=(245,242,208)
LIME=(76,187,23)

titleBG = image.load('backgrounds/titleBG.png').convert()
autumnBG=image.load('backgrounds/autumnBG.png').convert()
cssBG=image.load('backgrounds/cssBG.png').convert()
autumnBG2=image.load('backgrounds/autumnBG2.png').convert()
autumnGR=image.load('backgrounds/autumnGR.png').convert()
autumnGR2=image.load('backgrounds/autumnGR2.png').convert()

beefalo=image.load('icons/beefaloIcon.png').convert_alpha()
ui=image.load('backgrounds/ui.png').convert_alpha()
skull=image.load('icons/skull.png').convert_alpha()
playerIcons=loadSprites('icons/characterIcon/')


wilsonPortrait = image.load('portrait/wilson.png').convert_alpha()
wendyPortrait = image.load('portrait/wendy.png').convert_alpha()
woodiePortrait = image.load('portrait/woodie.png').convert_alpha()
willowPortrait = image.load('portrait/willow.png').convert_alpha()

blowdart=image.load('wilson/leftAttack/blowdart.png').convert_alpha()

music=mixer.music.load("music/Don't Starve Together - Main Theme2.wav")

menuClick=mixer.Sound('music/menuClick.wav')
charList=['WILSON','WENDY','WOODIE','WILLOW','DEERCLOPS','MOOSEGOOSE','DRAGONFLY','BEARGER']
groundRect=Rect(0,550,1200,200)

health1=PlayerDisplay(550,40,1)
health2=PlayerDisplay(650,40,2)
ouch1=PlayerDisplay(150,110,2)
ouch2=PlayerDisplay(1050,110,1)

myClock=time.Clock()
dt=myClock.tick(60)

running=True
def game(mode,one,two):
    myClock = time.Clock()
    myClock.tick(60)
    global keys, avgpx, evt
    playerSprites = sprite.Group()

    player1=one
    player2=two

    playerSprites.add(player1)
    playerSprites.add(player2)

    add1=0
    add2=0

    leftpx=240
    cameraRect = Rect(leftpx, 150, 720, 420)

    projectileSprites = sprite.Group()
    screen.blit(autumnBG,(0,0))
    running=True
    while running:
        for evt in event.get():
            if evt.type==KEYDOWN:
                if evt.key==K_ESCAPE:

            if evt.type==QUIT:
                quit()

        keys=key.get_pressed()

        if player1.lose or player2.lose:
            if player1.lose:
                add2=player2.points+1
            if player2.lose:
                add1=player1.points+1
            playerSprites.empty()
            projectileSprites.empty()

            if mode=='multi':
                player1=Player(1,wilson,wilsonHitbox,0,100,150,50,[False,False,False,False,False,False,False],400,400,0,0,True,False,0,200) #normally 200
                player2=Player(2,wilson,wilsonHitbox,0,100,150,50,[False,False,False,False,False,False,False],700,400,0,0,False,False,0,200)
            if mode=='single':
                player1=Player(1,wilson,wilsonHitbox,0,100,150,50,[False,False,False,False,False,False,False],300,400,0,0,True,False,0,200)
                player2=Boss(2,deerclops,deerclopsHitbox,4,250,350,30,[False,False,False,False,False,False,False],550,400,0,0,False,False,0,200)   #pvb

            playerSprites.add(player1)
            playerSprites.add(player2)
            player1.points=add1
            player2.points=add2
            if add1==2 or add2==2:
                VICTORY(mode,player1,player2)


        pList=['',player1,player2]



        for i in range(1,3,1):
            pList[i].takeInput(i,pList)
            pList[i].checkHit(pList[i].image,pList,playerSprites)
            pList[i].findVelocity(pList[i].speed)
            pList[i].findAction(projectileSprites,pList)
            cameraRect,leftpx=pList[i].updatePos(mode,pList,cameraRect,leftpx)

        avgpx=((pList[1].px+pList[1].width/2)+(pList[2].px+pList[2].width/2))/2
        projectileSprites.update(pList,projectileSprites)
        playerSprites.update(pList)

        if player1.lose==False and player2.lose==False:
            avgpx=(player1.px+player2.px)/2
            drawScreen(mode,player1,player2,playerSprites,projectileSprites,cameraRect)

        myClock.tick(60)
        display.flip()

#
TITLEMENU()
# CSS('multi')
# game('single',Player(1,wilson,wilsonHitbox,0,100,150,50,[False,False,False,False,False,False,False],300,400,0,0,True,False,0,200),
#      Boss(2,deerclops,deerclopsHitbox,4,250,350,30,[False,False,False,False,False,False,False],550,400,0,0,False,False,0,200))   #pvb
# game('multi',Player(1,wilson,wilsonHitbox,0,100,150,50,[False,False,False,False,False,False,False],400,400,0,0,True,False,0,200),
#      Player(2,wilson,wilsonHitbox,0,100,150,50,[False,False,False,False,False,False,False],700,400,0,0,False,False,0,200))        #pvp
# VICTORY(wilson,wilson)
quit()