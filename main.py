'''
Jaden Hong
ICS3U-02

Do Fight Together - FSE
A Street Fighter inspired fighting game, with a Don't Starve theme.
Matches are a best 2 out of 3, and both single player and multiplayer are supported.
'''

#basic setup, importing, initializing
from pygame import *
from random import *
font.init()
mixer.init()
width,height=1200,700
screen=display.set_mode((width,height))
screenRect=Rect(0,0,width,height)

def TITLEMENU(menu):
	'TITLEMENU(menu) - function to display the titlescreen and main menu'
	t=0 #accumulating variable for t in frames
	titleE=screenFX(None) #creating a screenFX object
	wordList = ['',                                             #a list of words that are not interactable with
	            MyText('Do Fight', 150, CREAM, 0, 100, 100,1),
	            MyText('Together', 150, CREAM, 0, 90, 250,1),
	            MyText('created by Jaden Hong', 25, CREAM, 255, 1050, 650,1)]
	interList=['',                                              #a list of words that can be interacted with
	           MyText('press ENTER to continue', 50, WHITE, 0, 100, 500,1),
	           MyText('Do Fight', 75, CREAM, 0, 100, 200-25,1),
	           MyText('Do Fight Together', 75, CREAM, 0, 100, 325-25,1),
	           MyText('Controls', 75, CREAM, 0, 100, 450-25,1),
	           MyText('Credits', 75, CREAM, 0, 100, 575-25,1)]
	titleScreen=ScreenDisplay(1,menu,'select',2,wordList,interList)          #creating a ScreenDisplay object
	myClock=time.Clock()
	myClock.tick(60) #setting to 60 fps
	running=True
	mixer.music.set_volume(1) #starting music
	mixer.music.play(-1)
	while running:
		for evt in event.get():
			if evt.type==KEYDOWN:
				if titleScreen.menu=='title':
					titleScreen.choose(evt,1,3) #.choose enables the navigation of the interList words
				if titleScreen.menu=='main menu':
					titleScreen.choose(evt,2,5)
				if evt.key==K_RETURN:
					titleScreen.selected=True
					if not titleScreen.sound:
						menuClick.play()
						titleScreen.sound=True
				if evt.type == K_ESCAPE:
					TITLEMENU('title')
			if evt.type==QUIT:
				quit()
		## drawing window
		screen.blit(titleBG,(0,0))
		titleScreen.navigate('single',[0,0,0])
		titleE.dynamic(t,0)     #allows for a dynamic zooming in effect
		titleScreen.drawScreenDisplay('null',[])
		t+=1
		display.flip()

#menu functions
def CSS(mode,rematch,pListSel):
	'CSS(mode,rematch,pListSel - takes parameters then displays the character select and stage select screens depending on modes'
	mixer.music.load("music/Don't Starve OST - Don't Starve Theme.mp3")
	mixer.music.set_volume(0.5)
	wordList = ['',
	            MyText('ENTER to confirm', 50, WHITE, 0, 100, 500,1),
	            MyText('Choose your Fighter', 50, CREAM, 255, 100, 100,1),
	            MyText('Player 1 - Choosing (m)', 35, CREAM, 255, 610, 400,1),
	            MyText('Player 2 - Choosing (c)', 35, CREAM, 255, 910, 400,1),
	            MyText('ENTER to confirm', 50, WHITE, 0, 100, 500,1),
	            MyText('Player 1 - Ready (n)', 35, CREAM, 255, 610, 400,1),
	            MyText('Player 2 - Ready (x)', 35, CREAM, 255, 910, 400,1),
	            MyText('Choose your Fighter', 50, CREAM, 255, 100, 100,1),
	            MyText('Choose the Season',75,CREAM,255,100,100,1),
	            MyText('ENTER to confirm', 50, WHITE, 0, 100, 200,1)]
	interList=[MyText('Summer',75,CREAM,0,150,550,1),
	           MyText('Autumn', 75, CREAM, 0,410, 550,1),
	           MyText('Winter',75,BLACK,0,700,550,1),
	           MyText('Spring',75,CREAM,0,970,550,1),]
	cssScreen=ScreenDisplay(1,'character','select',0,wordList,interList)

	myClock=time.Clock()
	myClock.tick(60)
	exe=False #initial value
	running=True
	playerPortrait=[wilsonPortrait,wendyPortrait,woodiePortrait,randomPortrait] #loading images
	charList=[[wilson,wilsonHitbox,0,100,150,50],                   #list of all possible character data
	          [wendy,wendyHitbox,1,100,150,50],
	          [woodie,woodieHitbox,2,100,150,50],
	          [],
	          [deerclops,deerclopsHitbox,4,250,350,30],
	          [moosegoose,moosegooseHitbox,5,250,350,30],
	          [dragonfly,dragonflyHitbox,6,250,350,30],
	          [bearger,beargerHitbox,7,260,350,30]]
	mixer.music.play(-1)
	while running:
		for evt in event.get():
			if evt.type==KEYDOWN:
				if cssScreen.menu=='character':
					cssScreen.choose(evt,0,3)
				if cssScreen.menu=='stage':
					cssScreen.choose(evt,0,3)
				if evt.key==K_RETURN:
					cssScreen.selected=True
					if cssScreen.menu=='stage':
						exe=True
				if evt.key==K_ESCAPE:
					if cssScreen.menu=='character':
						mixer.music.stop()
						mixer.music.load("music/Don't Starve Together - Main Theme2.wav")
						TITLEMENU('main menu')
					if cssScreen.menu=='stage':
						CSS(mode,False,pListSel)
			if evt.type==QUIT:
				quit()
		if exe or rematch: #starts the game if both characters and stage are selected, or rematch as a parameter was True (saves game settings from match before)
			if cssScreen.selection==3:
				cssScreen.selection=randint(0,2)
			if cssScreen.selection2==3:
				cssScreen.selection2=randint(0,2)

			one = cssScreen.selection
			two = cssScreen.selection2
			stage = cssScreen.stageSel + 2         #fixing stage numbers
			if stage > 3:
				stage -= 4
			if rematch:
				one=pListSel[1]
				stage=pListSel[0]
				if mode=='multi':
					two=pListSel[2]
				else:
					two=pListSel[0]
				rematch=False
			if mode == 'multi':         #feeding the game function the necessary parameters
				game(mode, Player(1, charList[one][0], charList[one][1], charList[one][2], charList[one][3],
				                  charList[one][4], charList[one][5], [False, False, False, False, False, False, False],
				                  400, 700, 0, 0, True, False, 0, 200),
				     Player(2, charList[two][0], charList[two][1], charList[two][2], charList[two][3],
				            charList[two][4], charList[two][5], [False, False, False, False, False, False, False],
				            700, 700, 0, 0, True, False, 0, 200), [stage, one, two],
				     charList, stage)
			else:
				two=stage+4 #bosses correspond to the season chosen
				game(mode, Player(1, charList[one][0], charList[one][1], charList[one][2], charList[one][3],
				                  charList[one][4], charList[one][5], [False, False, False, False, False, False, False],
				                  400, 700, 0, 0, True, False, 0, 200),
				     Boss(2, charList[two][0], charList[two][1], charList[two][2], charList[two][3],
				          charList[two][4], charList[two][5], [False, False, False, False, False, False, False],
				          700, 400, 0, 0, False, False, 0, 200), [stage, one, two],
				     charList, stage)  # pvb

		cssScreen.navigate(mode,pListSel)
		screen.blit(cssBG,(0,0))
		cssScreen.drawScreenDisplay(mode,playerPortrait)
		display.flip()

def VICTORY(mode,char1,char2,pListSel):
	'VICTORY(mode,char1,char2,pListSel) - takes parameters and displays the correct victory screen'
	myClock=time.Clock()
	myClock.tick(60)
	running=True
	t=0
	victoryE = screenFX(None)
	charQuotes=[['Your existence is an affront to the laws of science, Wilson!',    #2d list of quotes ( 1st index is player who won, 2nd index is player who lost)
	             'Murderer!',
	             "Murder! Bring me an axe and we'll get in the swing of things!",
	             '',
	             'This was really gross!',
	             "I don't know exactly what that thing was.",
	             "That was one fly dragon!",
	             "What a bear of a badger."],                #wilson quotes
	            ["You've gone mad, scientist.",
	             "Have we not seen enough death, Wendy?",
	             "I'll send you someplace much nicer than this, Woodie.",
	             '',
	             "Death incarnate!",
	             "It was an abomination.",
	             "It was burning on the inside",
	             "It smelt like death."], #wendy quotes
	            ['Enemy of the Forest!',
	             "Hereeee's Woodie!",
	             "Hey, c'mere Woodie! I've gotta AXE you question!",
	             '',
	             "That was a big moose!",
	             "Whatever it was, it was definitely Canadian!",
	             "He would've burn down all the trees before I chopped them",
	             "That was a big bear!"]] #woodie quotes
	if mode=='multi':
		if char1.points==2:
			word1=MyText(charQuotes[char1.charType][char2.charType],40,CREAM,255,100,600,1)
			word2=MyText(nameList[char1.charType]+' WINS!',100,WHITE,255,75,75,1)
		else:
			word1=MyText(charQuotes[char2.charType][char1.charType],40,CREAM,255,100,600,1)
			word2=MyText(nameList[char2.charType]+' WINS!',100,WHITE,255,75,75,1)
	else:
		if char1.points==2:
			word1=MyText(charQuotes[char1.charType][char2.charType],40,CREAM,255,100,500,1)
			word2=MyText(nameList[char1.charType]+' WINS!',100,WHITE,255,100,100,1)
		else:
			word1=MyText(('Day '+str(randint(0,100))+' Everyone is dead'),40,CREAM,255,100,550,1)
			word2=MyText(nameList[char2.charType]+' WINS!',100,WHITE,255,100,100,1)
	wordList = ['',
	            word1,
	            word2]
	interList=[MyText('Rematch', 75, CREAM, 0, 600, 300, 1),
	           MyText('Continue', 75, CREAM, 0, 600, 400, 1),
	           MyText('Quit', 75, CREAM, 0, 600, 500, 1)]
	victoryScreen=ScreenDisplay(1,'victory','select',0,wordList,interList)
	while running:
		for evt in event.get():
			if evt.type==KEYDOWN:
				if victoryScreen.menu=='victory':
					victoryScreen.choose(evt,0,2)
				if evt.key==K_RETURN:
					victoryScreen.selected=True
			if evt.type==QUIT:
				quit()
		screen.blit(victoryBG,(0,0))
		victoryE.dynamic(t,0)
		victoryScreen.navigate(mode,pListSel)
		victoryScreen.drawScreenDisplay(mode,[])
		display.flip()
		t+=1

def PAUSE(mode):
	'PAUSE(mode) - pauses the game and gives player 1 the option to resume, check controls, or end game'
	myClock = time.Clock()
	copy=screen.subsurface((0,0,1200,700)).copy()
	myClock.tick(60)
	running = True
	wordList = [MyText('Paused',75,CREAM,255,540,175,1)]
	interList = [MyText('Resume', 50, CREAM, 255, 540, 275, 1),
	             MyText('Controls',50,CREAM, 255, 540, 350, 1),
	             MyText('End Game',50,CREAM, 255, 540, 425, 1)]
	pauseScreen = ScreenDisplay(1, 'pause', 'select', 0, wordList, interList)
	while running:
		for evt in event.get():
			if evt.type == KEYDOWN:
				if pauseScreen.menu == 'pause':
					pauseScreen.choose(evt, 0, 2)
				if evt.key == K_RETURN:
					pauseScreen.selected = True
			if evt.type == QUIT:
				quit()
		screen.blit(copy, (0, 0))
		screen.blit(pauseBG, (400, 100))
		running=pauseScreen.navigate(mode, [0,0,0])
		pauseScreen.drawScreenDisplay(mode, None)
		display.flip()

def CONTROLS(mode):
	'CONTROLS(mode) - displays the control menu, showing controls, attacks, and tips'
	myClock = time.Clock()
	myClock.tick(60)
	running = True
	wordList = [MyText('Controls', 75, CREAM, 255, 100, 75, 1)]
	interList = [MyText('Movement', 50, CREAM, 255, 100, 175, 1),
	             MyText('Attacks', 50, CREAM, 255, 100, 250, 1),
	             MyText('More Information', 50, CREAM, 255, 100, 325, 1)]
	controlScreen = ScreenDisplay(1, 'control', 'select', 0, wordList, interList)
	while running:
		for evt in event.get():
			if evt.type == KEYDOWN:
				if controlScreen.menu == 'control':
					controlScreen.choose(evt,0,2)
				if evt.key == K_RETURN or evt.key==K_ESCAPE:
					controlScreen.selected = True
			if evt.type == QUIT:
				quit()

		screen.blit(optionsBG, (0,0))
		if controlScreen.selection==0:
			screen.blit(movement,(300,100))
		elif controlScreen.selection==1:
			screen.blit(attacks,(300,100))
		controlScreen.drawScreenDisplay(mode, None)
		running = controlScreen.navigate(mode, [0, 0, 0])
		display.flip()

def CREDITS():
	'CREDITS() - displays the credits (if you stay for long enough then a bug i encountered before gets put to use'
	cScreen=screenFX(None)
	mixer.music.load('music/ragtime.wav')
	mixer.music.play(-1)
	tp=0    #inital variables
	cooldown=0
	myClock = time.Clock()
	myClock.tick(60)
	running = True
	#creates the initial koalefants for the credits
	kCount=25
	particles=[]
	for i in range(kCount):
		x=randint(0,1200)
		y=randint(0,700)
		speed=randint(-3,3)
		while speed==0:
			speed=randint(-3,3)
		left=randint(0,1)
		up=randint(0,1)
		type=randint(0,2)
		particles.append([x,y,speed,left,up,type])
	wordList = [MyText("Do Fight Together", 75, WHITE, 255, 75, 150, 1),
	            MyText("Made by: Jaden Hong",35,WHITE, 255, 75, 300, 0),
	            MyText("All game assets from: Klei Entertainment",35,WHITE, 255, 75, 400, 0),
	            MyText("For ICS3U-02 (June 5th 2020)",35,WHITE, 255, 75, 500, 0),
	            MyText("Special thanks to:",35,WHITE,255,75,600,0),
	            MyText("Samir, Yuxi, Ashad, Ali, Jaden, Matthew",25,WHITE,255,75,650,0)]
	while running:
		for evt in event.get():
			if evt.type==KEYDOWN:
				running=False
			if evt.type==QUIT:
				quit()
		draw.rect(screen,BLACK,(0,0,1200,700))
		#particle system for the koalefants (partially random movements in the x, y direction, and spawns them in randint ranges on the edges)
		for i in range(kCount):
			x=randint(0,1200)
			if tp%2==0:
				particles[i][1]+=particles[i][2]
				particles[i][0]+=particles[i][2]
			sRect=Rect(-200,-200,1600,1100)
			if not sRect.collidepoint(particles[i][0],particles[i][1]):
				wallFrom=randint(0,1)
				if wallFrom==1:
					particles[i][0]=x
					particles[i][1]=0
				else:
					particles[i][0]=randint(0,700)
					particles[i][1]=0
				particles[i][2] = randint(-3, 3)
				while particles[i][2] == 0:
					particles[i][2] = randint(-3, 3)
				particles[i][3]=randint(0,1)
				particles[i][4]=randint(0,1)
				particles[i][5] = randint(0, 2)
			pic=transform.smoothscale(creditPics[particles[i][5]], (abs(particles[i][2])*50+100,abs(particles[i][2])*50+100))
			#different states of particles (random direction both up and down, left and right)
			if particles[i][3]==1:
				if particles[i][4]==1:
					screen.blit(transform.flip(pic,True,False),(particles[i][0],particles[i][1]))
				else:
					screen.blit(transform.flip(pic,True,True), (particles[i][0], particles[i][1]))
			else:
				if particles[i][4]==1:
					screen.blit(pic,(particles[i][0],particles[i][1]))
				else:
					screen.blit(transform.flip(pic,False,True), (particles[i][0], particles[i][1]))
		s=Surface((100,700)) ##creating a black translucent surface
		s.set_alpha(128)
		s.fill((0,0,0))
		screen.blit(s,(500,0))
		draw.rect(screen,BLACK,(0,0,500,700))
		if tp%60==0:
			cooldown=0
		screen.blit(cheer[cooldown//30],(500,450))
		##scrolling down (moving 1 every other frame to all the words in word list
		for i in range(len(wordList)):
			wordList[i].basic()
			if tp%2==0:
				wordList[i].locy-=1
		#special effect
		if tp>=1000:
			cScreen.dynamic(tp,1)
			if tp==2000: #preventing from letting program crash (if you dont do this, memory becomes full and you will see a very glitchy rainbow effect
				running=False
		display.flip()
		tp+=1
		cooldown+=1
		if not running:
			mixer.music.stop()
			mixer.music.load("music/Don't Starve Together - Main Theme2.wav")
			# mixer.music.play()

#defining misc functions
def wordPic(txt,size,col,alpha,type):
	'wordPic(text,size,colour,alpha,type) - takes parameters and creates an image of text'
	global Font
	if type==1:
		Font=font.Font('fonts/belisa_plumilla.ttf',size)
	else:
		Font=font.SysFont('Arial',size)
	fontPic=Font.render(str(txt), True, col)
	alphaFont=Surface(fontPic.get_size(),SRCALPHA)
	alphaFont.fill((255,255,255,alpha))
	fontPic.blit(alphaFont,(0,0),special_flags=BLEND_RGBA_MULT)
	return fontPic

#movement functions
def friction(vx,airborne):
	'friction(vx,airborne) - slows down speed of a character untill it reaches 0'
	if airborne:
		s=0.5
	else:
		s=3.5
	if vx>s:
		vx-=s
	elif vx<-s:
		vx+=s
	else:
		vx=0
	return vx
def findHitbox(n,pList):
	'findHitbox(n,pList) - updates the general hurtbox of a player'
	pList[n].hurtbox=Rect(pList[n].px+20,pList[n].py+5,60,145)
	if pList[n].charType<4:
		pList[n].hurtbox=Rect(pList[n].px+20,pList[n].py+20,60,130)
	else:
		pList[n].hurtbox=Rect(pList[n].px+10,pList[n].py+30,230,320)

#classes
class ScreenDisplay(object):
	'a class which is used for the different menu types'
	def __init__(self,n,menu,effect,selection,wordList,interList):
		self.n=n
		self.menu=menu
		self.effect=effect
		self.selection=selection #selection player 1 and default
		self.selection2=0        #selection for player 2
		self.wordList = wordList    #word list
		self.interList = interList  #interactable word list

		self.sound=False
		self.stageSel=0
		self.selected=False
		self.change=False
		self.confirm=False
		self.confirm2=False
		self.musicStop = True

	def choose(self,evt,lB,uB):
		'choose(self,evt,lowerBound,upperBound) - allows for navigation of interactable words'
		if self.menu!='stage' and not (self.confirm and self.confirm2 and self.menu=='character') and not (self.menu=='victory' and self.selected) and not (self.menu=='pause' and self.selected):
			if evt.key==K_LEFT or evt.key==K_UP:
				self.selection-=1
				if self.selection<lB:
					self.selection=uB
			if evt.key==K_RIGHT or evt.key==K_DOWN:
				self.selection+=1
				if self.selection>uB:
					self.selection=lB
			if evt.key == K_a or evt.key==K_w:
				self.selection2 -= 1
				if self.selection2 < lB:
					self.selection2 = uB
			if evt.key == K_d or evt.key==K_s:
				self.selection2 += 1
				if self.selection2 > uB:
					self.selection2 = lB
		else:
			if evt.key==K_LEFT or evt.key==K_UP:
				self.stageSel-=1
				if self.stageSel<lB:
					self.stageSel=uB
			if evt.key==K_RIGHT or evt.key==K_DOWN:
				self.stageSel+=1
				if self.stageSel>uB:
					self.stageSel=lB

		if evt.key==K_m:
			self.confirm=True
		if evt.key==K_n:
			self.confirm=False
		if evt.key == K_c:
			self.confirm2 = True
		if evt.key == K_x:
			self.confirm2 = False

	def drawScreenDisplay(self,mode,imageList):
		'drawScreenDisplay(self,mode,imageList) - draws the window for the ScreenDisplay object'
		menuParam=[['title',1,4,1,2,False],        #2d list of menu's and their corresponding upper bounds, lower bounds, and other params that choosing behaviour
		           ['t title',1,4,1,2,False],
		           ['main menu',3,4,2,6,True],
		           ['character',2,5,0,0,False],
		           ['stage',9,11,0,4,False],
		           ['pause',0,1,0,3,True],
		           ['victory',1,3,0,3,True],
		           ['control',0,1,0,3,False]]
		if self.menu=='character':
			screen.blit(imageList[self.selection],(600,100))
			if mode=='multi':
				screen.blit(imageList[self.selection2],(900,100))
		if self.menu=='stage':
			screen.blit(stageBG,(0,0))
		indent=False        #determines whether or not a little beefalo icon will indent the word selected
		for i in range(8):
			if self.menu==menuParam[i][0]:
				x1,x2=menuParam[i][1],menuParam[i][2]
				y1,y2=menuParam[i][3],menuParam[i][4]
				indent=menuParam[i][5]
				break
			else:
				x1,x2,y1,y2=0,0,0,0 #temp variables for use in blitting the words later on
		if self.menu=='character':
			if self.confirm and self.confirm2:
				x1,x2=5,8
			if mode=='single':
				x1,x2=2,4
			if self.confirm and mode=='single':
				x1,x2=5,7
		for i in range(x1,x2):
			self.wordList[i].basic()
			if self.selected:
				self.wordList[i].fadeAway()
				if self.wordList[i].alpha==0:       #fades out the option selected until it's transparent where it will then continue
					self.change=True
			else:
				self.wordList[i].fadeIn()
		for i in range(y1,y2):
			if self.menu!='stage':
				self.interList[i].chosen(i,self.selection,indent)
			else:
				self.interList[i].chosen(i,self.stageSel,indent)
			if self.selected:
				self.interList[i].fadeAway()
				if self.interList[i].alpha==0:
					self.change=True
			else:
				self.interList[i].fadeIn()

	def navigate(self,mode,pListSel):
		'navigate(self,mode,playerListSelection) - function to determine what menu to progress to (is called whenever game is ready to progress, also returning the value of "running"'
		if self.selected and self.change:
			self.sound=False
			self.change=False
			if self.menu=='title':
				self.menu='t title'
			elif self.menu=='t title':
				if self.interList[1].alpha==0:
					self.menu='main menu'
					self.selection=2
			elif self.menu=='main menu':
				if self.selection==2: #single
					mixer.music.stop()
					self.selection=1
					CSS('single',False,pListSel)
				if self.selection==3:
					mixer.music.stop()
					self.selection=1
					CSS('multi',False,pListSel)
				if self.selection==4:
					CONTROLS(mode)
				if self.selection==5:
					CREDITS()

			elif self.menu=='character':
				if mode=='multi':
					if self.confirm and self.confirm2:
						self.menu = 'stage'
				else:
					if self.confirm:
						self.menu = 'stage'
			elif self.menu=='victory':
				if self.selection==0:
					CSS(mode,True,pListSel)
				elif self.selection==1:
					TITLEMENU('main menu')
				elif self.selection==2:
					TITLEMENU('title')
			elif self.menu=='pause':
				if self.selection==0:
					return False
				if self.selection==1:
					CONTROLS(mode)
					self.selected=False
				if self.selection==2:
					mixer.music.stop()
					mixer.music.load("music/Don't Starve Together - Main Theme2.wav")
					TITLEMENU('title')
			elif self.menu=='control':
				return False
			if not self.menu=='t title':
				self.selected=False
		return True

def loadSprites(path):
	'loadSprites(path)- takes file path and returns list of each sprite in folder'
	picList=[]
	for i in range(50):
		try:
			picList.append(image.load(path+str(i)+'.png').convert_alpha()) #loads each image if possible (file name will be 0.png, then 1.png, until not valid)
		except:
			return picList
'''
The idea for using this format to show animations was taught to me by Samir Bhuyian

For each player and boss there are two 2d lists corresponding to them.
The first mega-list contains the sprites that are to be displayed on screen.
The second mega-list contains only the hitbox sprites (masks) for use in finding collision for attacks.
The list in reality looks like : [[[a,b,c,...],NUM,NUM]],[[a,b,c,...],NUM,NUM]],[[a,b,c,...],NUM,NUM]],...]  

The first index is related to the action took (index 3 is walking).
In each index is a list which would look like [[a,b,c,...], NUMBER, NUMBER]
The first item is a list of sprites, which is returned from the loadSprites function. 
The second item is the number of frames it will take before the next image in the sprite list will be displayed.
The third item is the total number of frames the animation will play before ending
The hitbox list has two extra parameters for detailing damage and hitstun dealt by attacks.
'''
wilson=[[loadSprites('wilson/idle/'),15,59],            #-1,0
        [loadSprites('wilson/crouch/'),10,19],          #1
        [loadSprites('wilson/guard/'),8,47],            #2
        [loadSprites('wilson/walk/'),8,63],             #3
        [loadSprites('wilson/jump/'),15,44],            #4
        [loadSprites('wilson/nAttack/'),7,27],          #5
        [loadSprites('wilson/upAttack/'),5,19],         #6
        [loadSprites('wilson/downAttack/'),3,20],       #7
        [loadSprites('wilson/leftAttack/'),10,49],      #8
        [loadSprites('wilson/rightAttack/'),5,39],      #9
        [loadSprites('wilson/airAttack/'),6,41],        #10
        [loadSprites('wilson/hurt/'),10,29],            #11
        [loadSprites('wilson/hurtair/'),10,19],         #12
        [loadSprites('wilson/collapse/'),7,69],         #13
        [loadSprites('wilson/death/'),20,139]]          #15
wilsonHitbox=[[0,0,0,0],                                                      #-1,0
              [0,0,0,0],                                                      #1
              [0,0,0,0],                                                      #2
              [0,0,0,0],                                                      #3
              [0,0,0,0],                           #inc,tot,damage,hitstun    #4
              [loadSprites('wilson/nAttack/hitbox/'),7,27,15,10],             #5
              [loadSprites('wilson/upAttack/hitbox/'),5,19,12,6],             #6
              [loadSprites('wilson/downAttack/hitbox/'),3,20,10,10],          #7
              [loadSprites('wilson/leftAttack/hitbox/'),10,49,15,15],         #8
              [loadSprites('wilson/rightAttack/hitbox/'),5,39,15,100],        #9
              [loadSprites('wilson/airAttack/hitbox/'),6,41,15,14],           #10
              [0,0,0,0],            #12                                       #11
              [0,0,0,0],           #13                                        #12
              [0,0,0,0],    #14                                               #13
              [0,0,0,0]]          #15                                         #14
wendy=[[loadSprites('wendy/idle/'),15,59],              #-1,0
       [loadSprites('wendy/crouch/'),10,19],            #1
       [loadSprites('wendy/guard/'),8,47],              #2
       [loadSprites('wendy/walk/'),8,63],               #3
       [loadSprites('wendy/jump/'),15,44],              #4
       [loadSprites('wendy/nAttack/'),7,27],            #5
       [loadSprites('wendy/upAttack/'),5,34],           #6
       [loadSprites('wendy/downAttack/'),3,20],         #7
       [loadSprites('wendy/leftAttack/'),10,49],        #8
       [loadSprites('wendy/rightAttack/'),7,41],        #9
       [loadSprites('wendy/airAttack/'),8,39],          #10
       [loadSprites('wendy/hurt/'),10,29],              #11
       [loadSprites('wendy/hurtair/'),10,29],           #12
       [loadSprites('wendy/collapse/'),7,69],           #13
       [loadSprites('wendy/death/'),20,139]]            #14
wendyHitbox=[[0,0,0,0],                                                       #-1,0
             [0,0,0,0],                                                       #1
             [0,0,0,0],                                                       #2
             [0,0,0,0],                                                       #3
             [0,0,0,0],                          #inc,tot,damage,hitstun      #4
             [loadSprites('wendy/nAttack/hitbox/'),7,27,13,10],               #5
             [loadSprites('wendy/upAttack/hitbox/'),5,34,10,6],               #6
             [loadSprites('wendy/downAttack/hitbox/'),3,20,12,10],            #7
             [loadSprites('wendy/leftAttack/hitbox/'),10,49,25,25],           #8
             [loadSprites('wendy/rightAttack/hitbox/'),7,41,12,17],           #9
             [loadSprites('wendy/airAttack/hitbox/'),8,39,13,14],             #10
             [0,0,0,0],                                                       #11
             [0,0,0,0],                                                       #12
             [0,0,0,0],                                                       #13
             [0,0,0,0]]                                                       #14
woodie=[[loadSprites('woodie/idle/'),15,59],            #-1,0
        [loadSprites('woodie/crouch/'),10,19],          #1
        [loadSprites('woodie/guard/'),8,47],            #2
        [loadSprites('woodie/walk/'),8,63],             #3
        [loadSprites('woodie/jump/'),16,45],            #4
        [loadSprites('woodie/nAttack/'),7,27],          #5
        [loadSprites('woodie/upAttack/'),6,35],         #6
        [loadSprites('woodie/downAttack/'),3,20],       #7
        [loadSprites('woodie/leftAttack/'),10,49],      #8
        [loadSprites('woodie/rightAttack/'),4,23],      #9
        [loadSprites('woodie/airAttack/'),6,41],        #10
        [loadSprites('woodie/hurt/'),10,29],            #11
        [loadSprites('woodie/hurtair/'),10,19],         #12
        [loadSprites('woodie/collapse/'),7,69],         #13
        [loadSprites('woodie/death/'),20,139]]          #14
woodieHitbox=[[0,0,0,0],                                                      #-1,0
              [0,0,0,0],                                                      #1
              [0,0,0,0],                                                      #2
              [0,0,0,0],                                                      #3
              [0,0,0,0],                           #inc,tot,damage,hitstun    #4
              [loadSprites('woodie/nAttack/hitbox/'),7,27,13,13],             #5
              [loadSprites('woodie/upAttack/hitbox/'),6,35,15,15],            #6
              [loadSprites('woodie/downAttack/hitbox/'),3,20,12,10],          #7
              [loadSprites('woodie/leftAttack/hitbox/'),10,49,25,25],         #8
              [loadSprites('woodie/rightAttack/hitbox/'),4,23,7,10],          #9
              [loadSprites('woodie/airAttack/hitbox/'),6,41,15,14],           #10
              [0,0,0,0],                                                      #11
              [0,0,0,0],                                                      #12
              [0,0,0,0],                                                      #13
              [0,0,0,0]]                                                      #14

deerclops=[[loadSprites('deerclops/idle/'),20,79],              #0      x
           [loadSprites('deerclops/walk/'),7,41],              #1       x
           [loadSprites('deerclops/iceAttack/'),15,104],         #2
           [loadSprites('deerclops/slashAttack/'),20,79],       #3
           [loadSprites('deerclops/hurt/'),5,19],              #4       x
           [loadSprites('deerclops/death/'),14,139],]            #5
deerclopsHitbox=[[0,0,0,0],
                 [0,0,0,0],
                 [loadSprites('deerclops/iceAttack/hitbox/'),15,104,100,25],
                 [loadSprites('deerclops/slashAttack/hitbox/'),34,25],
                 [0,0,0,0],
                 [0,0,0,0]]
moosegoose=[[loadSprites('moosegoose/idle/'),20,79],              #0      x
            [loadSprites('moosegoose/walk/'),7,41],              #1       x
            [loadSprites('moosegoose/attack/'),12,95],         #2
            [loadSprites('deerclops/slashAttack/'),20,79],       #3
            [loadSprites('moosegoose/hurt/'),20,39],              #4       x
            [loadSprites('moosegoose/death/'),14,125],]            #5
moosegooseHitbox=[[0,0,0,0],
                  [0,0,0,0],
                  [loadSprites('moosegoose/attack/hitbox/'),12,95,50,25],
                  [loadSprites('deerclops/slashAttack/hitbox/'),34,25],
                  [0,0,0,0],
                  [0,0,0,0]]
dragonfly=[[loadSprites('dragonfly/idle/'),20,79],              #0      x
           [loadSprites('dragonfly/walk/'),7,27],              #1       x
           [loadSprites('dragonfly/attack/'),15,119],         #2
           [loadSprites('deerclops/slashAttack/'),20,79],       #3
           [loadSprites('dragonfly/hurt/'),7,20],              #4       x
           [loadSprites('dragonfly/death/'),14,139],]            #5
dragonflyHitbox=[[0,0,0,0],
                 [0,0,0,0],
                 [loadSprites('dragonfly/attack//hitbox/'),15,119,67,25],
                 [loadSprites('deerclops/slashAttack/hitbox/'),34,25],
                 [0,0,0,0],
                 [0,0,0,0]]
bearger=[[loadSprites('bearger/idle/'),20,79],              #0      x
         [loadSprites('bearger/walk/'),6,47],              #1       x
         [loadSprites('bearger/attack/'),15,89],         #2
         [loadSprites('deerclops/slashAttack/'),20,79],       #3
         [loadSprites('bearger/hurt/'),6,17],              #4       x
         [loadSprites('bearger/death/'),14,139],]            #5
beargerHitbox=[[0,0,0,0],
               [0,0,0,0],
               [loadSprites('bearger/attack/hitbox/'),15,89,67,0],
               [loadSprites('deerclops/slashAttack/hitbox/'),34,25],
               [0,0,0,0],
               [0,0,0,0]]

#classes
class Player(sprite.Sprite):
	'class for the controllable player characters. inherits from the pygame.sprite.Sprite class.'
	def __init__(self,n,char,charhit,charType,width,height,speed,inputs,px,py,vx,vy,direction,airborne,action,health):
		sprite.Sprite.__init__(self)

		self.n=n                    #player number (1,2)
		self.inputs=inputs          #player inputs [up,down,left,right,jump,attack,shield]
		self.char=char              #player animation sprite mega list
		self.charhit=charhit        #players hitbox sprite mega list
		self.charType=charType      #integer value of all players types (0 - Wilson, 1 -Wendy, 2 - Woodie, 3 - (random), 4 - Deerclops, 5 - Moosegoose, 6 - Dragonfly, 7 - Bearger)
		self.width=width            #player width
		self.height=height          #player height
		self.px=px                  #player pos x
		self.speed=speed            #players speed
		self.push=False             #boolean used to determine the camera rect object

		if n==1:
			self.oPlayer=2          #other player's number
		else:
			self.oPlayer=1

		self.py=py                  #player pos y
		self.vx=vx                  #player velocity x
		self.vy=vy                  #player velocity y
		self.direction=direction    #player direction (rTrue,lFalse)
		self.airborne=airborne      #player airborne check (True False)
		self.inAction=False         #if player is taking an action
		self.action=action          #player action taken
		self.oAction=action         #one frame ago's aciton
		self.hurtbox=Rect(self.px+20,self.py+5,width,height) #taking player hurtbox
		self.cooldown=0             #animation timer cooldown
		self.ani=char[action][2]    #what frame limit player has per animation

		self.health=health          #player health
		self.hitstun=0              #if player is unable to take action
		self.hitten=False           #
		self.pHitten=False          #
		self.superArmor=False       #allows bosses to become invulnerable to damage

		self.ouch=0                 #stunmeter
		self.lose=False             #boolean whether player wins or loses
		self.points=0               #amount of games won
		self.projectileCount=0      #num of projectiles from player
		self.proj=0                 #projectile to be added

		#sprite class attributes
		self.image=char[action][0][self.cooldown//char[action][1]],(px-8,py)

		self.rect=Rect(px,py,width,height)

	def update(self,pList):
		'update(self,playerList) - updates the player to match the correct sprite'
		self.ani=self.char[self.action][2]  #frame limit for animations
		self.cooldown+=1                       #increasing the frame count for the cycles
		##since not all sprites will be centered, and if so, the start location might need to be different
		##both the x and y locations need to be adjusted for each animation.
		##adjustlistU is added to the rect to raise or lower the position y, adjustListR and adjustListU move the position x left or right
		if self.charType==0:
			adjustListL=[0,0,0,0,0,-22,-22,-28,0,-50,0,0,0,-10,-87] #wilson adjust list
			adjustListR=[0,0,0,0,0,0,-8,0,0,0,0,0,0,-90,0]
			adjustListU=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		elif self.charType==1:
			adjustListL = [0, 0, 0, -20, 0, -30, -38, -45, -10, -70, -30, 0, 0, -22, -105] #wendy adjust list
			adjustListR = [0, 0, 0, -25, 0, -3, 0, -5, -5, -2, 0, 0, 0, -76, 0]
			adjustListU = [0, 0, 0, 0, 0, 4, -17, 2, 8, 12, 0, 0, 0, -10, 8]
		elif self.charType==2:
			adjustListL = [0, 0, 0, -10, 0, -30, -70, -20, -30, -50, -15, 0, 0, -22, -100] #woodie adjust list
			adjustListR = [0, 0, 0, 10, 5, 5, -50, 9, -3, -40, 4, 0, 0, -96, 10]
			adjustListU = [0, 0, 0, 0, 0, -8, -13, 15, 0, 0, 0, 0, 0, 0, 8]
		elif self.charType==4:
			adjustListL=[0,0,-250,0,0,0] #deerclops adjust list
			adjustListR=[0,0,-100,0,0,0]
			adjustListU=[0,-5,-50,0,-60,0]
		elif self.charType==5:
			adjustListL=[-150,-110,-170,0,-130,-130] #moosegoose adjust list
			adjustListR=[-100,-90,-30,0,-120,-430]
			adjustListU=[-90 ,-133,-133,0,-150,-163]
		elif self.charType==6:
			adjustListL=[-70,-70,-200,0,-60,-60] #dragonfly adjust list
			adjustListR=[-80,-80,-90,0,-70,-25]
			adjustListU=[0 ,0,-65,0,10,-30]
		elif self.charType==7:
			adjustListL=[-45,-150,-100,0,-50,-60] #bearger adjust list
			adjustListR=[-50,-120,-100,0,-30,-185]
			adjustListU=[0,-80,-65,0,-10,-50]

		if self.cooldown>self.ani:      #reseting the cooldown timer to 0 once animation is done
			self.cooldown=0
			self.inAction=False
		if self.px+self.width/2<=avgpx: #determining if a player should be facing the left or right, aswell as updating values if needing to be changed
			self.rect=Rect(self.px+adjustListR[self.action],self.py+adjustListU[self.action],self.width,self.height)
			self.image=self.char[self.action][0][self.cooldown//self.char[self.action][1]]
			self.direction=True
		else:
			self.rect=Rect(self.px+adjustListL[self.action],self.py+adjustListU[self.action],self.width,self.height)
			self.image=transform.flip(self.char[self.action][0][self.cooldown//self.char[self.action][1]],True,False)
			self.direction=False

	def checkHit(self,image,pList,playerSprites):
		"checkHit(self,image,playerList,playerSprites) - method for finding collisions between the players hitbox and the other player's hurtbox"
		attackd=False #for bosses det. whether they attacked or not
		if pList[self.n].charType>3:
			if self.anger>self.limit:
				self.superArmor=True
			else:
				self.superArmor=False
		##checks to see if other player is available to get hit by attack
		if pList[self.oPlayer].action!=14 and pList[self.oPlayer].superArmor==False:
			if self.charhit[self.action][2]>0:
				#temporarily changes the character's sprite to the hitbox sprite
				if self.direction:
					self.image=self.charhit[self.action][0][self.cooldown//self.charhit[self.action][1]]
				else:
					self.image=transform.flip(self.charhit[self.action][0][self.cooldown//self.charhit[self.action][1]],True,False)
				playerSprites.clear(screen,autumnBG)
				playerSprites.draw(screen)
				if sprite.collide_mask(pList[self.n],pList[self.oPlayer]) is not None and pList[self.oPlayer].action<13: #checks if there are collisions between
					if not pList[self.n].hitten:                                                                         # hitbox and enemy hurtbox
						if pList[self.oPlayer]!=11 or pList[self.oPlayer]!=12:
							if pList[self.oPlayer].hitstun==0:
								pList[self.oPlayer].hitstun=self.charhit[self.action][4]
								if pList[self.oPlayer].inputs[2] and pList[self.n].charType<4:          #mechanic where if the player holds back,
									pList[self.oPlayer].health-=self.charhit[self.action][3]/5          #they will receive less damage than usual
								else:
									pList[self.oPlayer].health-=self.charhit[self.action][3]
								pList[self.oPlayer].ouch+=self.charhit[self.action][4]
							pList[self.n].hitten=True
							if pList[self.oPlayer].charType>3:          #boss mechanic, if self.anger reaches a threshold, the boss will ignore the player's attack
								pList[self.oPlayer].anger+=1
							pList[self.oPlayer].findSound('ouch')           #plays the sound effect of getting hurt
				attackd=True
		## checking for projectile collision (same mechanics as regular collision)
		if self.projectileCount>0 and pList[self.oPlayer].superArmor==False:
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
					pList[self.oPlayer].findSound('ouch')
				attackd=True
		##giving super armor to bosses
		if attackd and self.cooldown==self.char[self.action][2]:
			if self.superArmor:
				self.superArmor=False
				self.anger=0
		self.image=image #resetting the player's image to how it looked prior to this function

	def takeInput(self,n,pList):
		'takeInput(n,n,playerList) - method which takes all inputs of a player'
		p1InputList=[keys[K_UP],keys[K_DOWN],keys[K_LEFT],keys[K_RIGHT],keys[K_n],keys[K_m],keys[K_COMMA],keys[K_PERIOD]] #lists of all inputs of player 1 and 2
		p2InputList=[keys[K_w],keys[K_s],keys[K_a],keys[K_d],keys[K_x],keys[K_c],keys[K_v],keys[K_b]]
		pInputList=['',p1InputList,p2InputList]
		if self.health>0 and self.action!=13:
			for i in range(7):
				if pInputList[n][i]:
					self.inputs[i]=True
				else:
					self.inputs[i]=False
			#special cases for input manipulation
			if self.inputs[2] and self.inputs[3]:
				self.inputs[2],self.inputs[3]=False,False
			if self.action==11 or self.action==12 or self.inputs[1]:
				self.inputs[4]=False

	def findSound(self,status):
		'findSound(self,status) - finds the correct sound effect to accompany a player depending on given parameters'
		r = -1
		if status=='ouch':
			if self.health > 0:
				if self.charType < 4:
					r=randint(0,2)
				else:
					r=1
			else:
				if self.oAction!=14:
					r=3
		elif status=='idle':
			if self.action==2:
				r=2
		else:
			if self.charType>3:
				if self.cooldown==60 and self.inAction:
					r=0
		if not r==-1:
			charFX[self.charType][r].set_volume(0.35)
			charFX[self.charType][r].play()

	def findAction(self,projectileSprites,pList):
		'findAction(self,projectileSprites,playerList) - finds the players action depending on their status and inputs'
		if self.action!=13: #player can not input when they are collapsed
			if not self.direction:           #switching rightmost player inputs for left and right
				if self.action!=14:
					if self.inputs[2] or self.inputs[3]:
						temp=self.inputs[3]
						temp2=self.inputs[2]
						self.inputs[3]=temp2
						self.inputs[2]=temp
			if not self.inAction:           #letting the player act if their previous action is finished (applies to attacks)
				if self.action!=14:
					if not self.airborne:   #matching inputs to movement
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
					self.action=4    #player jumps
				#matching player inputs to attacks
				elif self.inputs[5] and self.action!=13:
					self.hitten=False
					self.inAction=True
					if self.airborne:
						self.action=10        #aerial attack
					elif self.action==0 and self.inputs[0]:
						self.action=6         #up attack
					elif self.action==1:
						self.action=7         #down attack
					elif self.action==2:
						self.action=8         #projectile attack
						if self.projectileCount<1:
							#summoning projectiles
							charMod=[250,100,150]
							if self.direction:
								modi = charMod[self.charType]*-1
							else:
								modi = charMod[self.charType]
							if self.charType==0:
								self.proj = Projectile(self.n, blowdart, self.px+modi, self.py, 7, 0, self.direction)
							if self.charType==1:
								self.proj = Projectile(self.n, ghosts[randint(0,2)], self.px+modi, self.py, 3, 0, self.direction)
							if self.charType==2:
								self.proj = Projectile(self.n, wood, self.px+modi, self.py, 5, 0, self.direction)
							projectileSprites.add(self.proj)
							self.projectileCount += 1
					elif self.action==3:
						self.action=9   #right attack
					else:
						self.action=5   #neutral attack
		else:
			if self.cooldown==69:
				self.action=0   #player collapse animation gets up after 69 frames

		#check hitstun animation
		if self.hitstun>0 and self.action!=5 and self.action!=13:
			self.vx=0
			self.vy=0
			if self.airborne:   #setting action to hurt
				self.action=12
			else:
				self.action=11
			self.hitstun-=1
		##handling whether the player collapses after taking too much damage in a short period of time
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

		if self.oAction!=self.action and (self.oAction!=14 or not(self.oAction==5 and self.charType>3)):#cooldown timer resets whenever a new action is performed
			if self.action!=0 or self.oAction!=13:
				self.cooldown=0
				pList[self.n].hitten=False
		self.oAction = self.action
		if self.health<=0 and self.airborne==False:   #setting player action to dead
			self.findSound('ouch')
			self.action=14
			self.vx=0
			self.vy=0
			if self.cooldown==self.char[14][2]:
				self.lose=True

	def findVelocity(self,charSpeed):
		'findVelocity(self,characterSpeed) - takes environment conditions then adjusts the velocity of the player'
		i=1
		if self.inputs[2]: #section applies velocity left=-1, right=+1
			i=-1
		if self.inputs[3]:
			i=1
		if self.action!=13 and (self.inputs[2] or self.inputs[3]): #finding the velocity of the player if they walk forward or backwards
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
		if self.inputs[2] and self.inputs[3] or self.inputs[1]: #left and right input or crouch sets velocity to 0
			if not self.airborne:
				self.vx=0
		self.vx=friction(self.vx,self.airborne) #adds friction
		if self.inputs[4] and self.airborne==False and self.inputs[1]==False and self.action<4: #adding instantaneous velocity when player jumps
			self.vy=275
			self.airborne=True
			if self.inAction:
				self.vy=0
				self.airborne=False
		if self.airborne: #subjecting player to gravity
			self.vy-=12
			if self.inputs[1]: #fast falling when player presses down
				if self.vy>-15:
					self.vy=-25
				self.vy-=10
		if self.inAction:       #setting players velocity to 0 if taking action
			if not self.airborne:
				self.vx=0
				self.vy=0

	def updatePos(self,mode,pList,cameraRect,leftpx):
		'updatePos(self,mode,playerList,cameraRect,leftpx) - updates movesment of character'
		opx=self.px #temporary value
		self.px+=round(self.vx/dt)      #changing the characters x and y positions divided by the ratio of milleseconds it takes to do one frame
		self.py-=round(self.vy/dt)
		if abs(pList[1].px-pList[2].px)>720-pList[self.oPlayer].width: #not allowing the player to move if they move past the bounds of the camera
			self.px=opx
			self.vx=0
		if self.push and abs(pList[1].px-pList[2].px)<=720-self.width: #updating the position of the camera whenever the character is allowed ot push the wall
			cameraRect, leftpx = updateCamera(pList[1], pList[2], leftpx)
		self.push=False
		pList[self.oPlayer].oPush=False
		if self.px <= leftpx or self.px>=leftpx+720-self.width:         #determining if the player is pushing the wall
			if cameraRect.collidepoint(self.px-self.width,self.py)==False or cameraRect.collidepoint(self.px+self.width,self.py)==False:
				self.push=True

		#colliding with outer walls (dimensions of the entire arena
		if self.px>1200-self.width:
			self.vx=0
			self.px=1200-self.width
		if self.px<0:
			self.vx=0
			self.px=0
		findHitbox(self.n,pList)
		if self.hurtbox.colliderect(groundRect) or (self.inputs[4] and self.airborne==False and self.inAction==False): #resetting frame count when player collides/leaves ground
			if not (self.charType>3 and self.action==5):
				self.airborne=False
				if self.action<13:
					self.cooldown=0
				self.inAction=False
		elif self.py==550-self.height:
			self.airborne=False
		else:
			self.airborne=True
		if not self.airborne:   #setting player  to above ground
			self.vy=0
			self.py=550-self.height
			findHitbox(self.n,pList)
		if self.hurtbox.colliderect(pList[self.oPlayer].hurtbox) and self.hitstun<=0 and self.charType<4: #moving characters away from each other if they collide
			if self.direction:
				self.vx-=7.5
			else:
				self.vx+=7.5
			self.vx=friction(self.vx,self.airborne)
		findHitbox(self.n,pList)
		return cameraRect, leftpx #cameraRect and leftpx is equal to what this function returns

class Boss(Player):
	'class for the bosses, inheriting from the player class. functions almost the same as the player except their input is from cpu, and actions are changed'
	def __init__(self,n,char,charhit,charType,width,height,speed,inputs,px,py,vx,vy,direction,airborne,action,health):
		Player.__init__(self,n,char,charhit,charType,width,height,speed,inputs,px,py,vx,vy,direction,airborne,action,health)
		limitlist=[2,1,2,2] #the amount of hits a boss will take before getting super armor
		self.inRange=False
		# self.py=py
		self.hurtbox=Rect(self.px+10,self.py+30,230,320) #taking boss hitbox
		self.anger=0    #initial value
		self.limit=limitlist[self.charType-4]

	def takeInput(self,n,pList):
		'takeInput(n) - method which takes all inputs of a boss'
		avgpx=(pList[1].px+pList[2].px)/2 #location between player and boss

		#walking towards player
		self.inputs[3],self.inputs[2]=False,False #left and right
		if not pList[1].hurtbox.colliderect(pList[2].hurtbox) and pList[self.oPlayer].action<14:  #walking towards the player if the boss is not in walking range
			if self.px<=avgpx:
				self.inputs[3]=True
			else:
				self.inputs[2]=True
			self.inRange=False
		else:
			self.inRange=True
		##handles sound effects
		if self.inAction:
			self.findSound('attack')
		else:
			self.findSound('idle')

		##giving bosses the ability to attack
		self.inputs[5] = False
		if self.inRange: #boss in range for attack
			if pList[self.oPlayer].health>0 and pList[self.oPlayer].action<14:
				self.inputs[5]=True

	def findAction(self,projectileSprites,pList):
		'findAction(self,projectileSprites,playerList) - finds the action of the boss'
		if self.action!=5: #not dead
			if not self.direction:           #switching rightmost player inputs for left and right
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
				if self.inputs[5]: #and self.action!=13:
					self.hitten=False
					self.inAction=True
					self.action=2
		else:
			if self.cooldown==69 and self.action!=5: #boss returning to neutral state
				self.action=0

		if self.hitstun>0 and self.health>0:
			self.vx=0
			self.vy=0
			self.hitstun-=10
			self.action=4
			self.inAction=True
		self.ouch=0

		if self.oAction!=self.action : #cooldown timer resets whenever a new action is performed
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

class Projectile(sprite.Sprite):
	'class for projectiles'
	def __init__(self, n, pType, px, py, vx, vy, direction):
		sprite.Sprite.__init__(self)
		self.image=pType            #sprite.Sprite atribute
		self.pType=pType            #original projectile image
		self.rect=Rect(px-27,py-11,55,22)
		self.n=n                    #player number (1,2)
		self.px=px                  #projectile pos x
		self.py=py                  #projectile pos y
		self.vx=vx                  #projectile velocity x
		self.vy=vy                  #projectile velocity y
		self.direction=direction    #projectile direction (rTrue,lFalse)
		self.vis=False              #projectile visibility

	def update(self,pList,projectileSprites,leftpx):
		'update(self,playerList,projectileSprites,leftpx) - updates the position, direction, existance, and image of the projectile'
		#updating image
		if not self.vis:
			self.image = emptyImage
		else:
			if self.direction:
				self.image = self.pType
			else:
				self.image=transform.flip(self.pType, True, False)
		# updating the sprite based off of direction
		if self.direction:
			self.px+=self.vx
			self.rect=Rect(self.px+27,self.py-11+90,55,22)
		else:
			self.px-=self.vx
			self.rect=Rect(self.px-27,self.py-11+90,55,22)
		if ((self.px+30<leftpx or self.px-30>leftpx+720) and pList[self.n].action!=8) or (pList[self.n].action>10 and self.vis==False): #removing projectile under conditions
			self.remove(projectileSprites)
			pList[self.n].projectileCount-=1
			pList[self.n].pHitten=False
		if pList[self.n].cooldown==39 and pList[self.n].action==8:  #finding visibility
			self.vis=True
		else:
			if not self.vis:
				self.vis=False

class PlayerDisplay(object):
	'class for display in game'
	def __init__(self,x,y,n):
		self.x=x        #pos x
		self.y=y        #pos y
		self.n=n        #player number

	def healthBar(self, health):
		'healthBar(self,health) - creates the health bar for each player'
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

	def stunBar(self,ouch,player1,player2):
		'stunBar(self,ouch,player1,player2) - takes parameters and creates a bar which represents the stun meter of a player'
		self.ouch=ouch
		if self.n==1:
			draw.rect(screen,BLACK,(850,110,200,25))
			rect=Rect(self.x,self.y,self.ouch*-5,25)
			rect.normalize()
			draw.rect(screen,YELLOW,rect)
			for i in range(player2.points):
				screen.blit(playerIcons[player2.charType],(self.x+30*i+5,self.y-75))
		if self.n==2:
			draw.rect(screen,BLACK,(150,110,200,25))
			draw.rect(screen,YELLOW,(self.x,self.y,self.ouch*5,25))
			for i in range(player1.points):
				screen.blit(playerIcons[player1.charType],(self.x-30*i-75,self.y-75))

	def ticking(self,tp):
		'ticking(self,time passed) - creates the clock timer'
		tp=5400-tp      #5400 is number of frames left (1 min 30 seconds)
		tSeconds=tp//60
		tmSeconds=round((tp%60)*5/3)
		##formating the clock using string methods and math
		if tSeconds>=60:
			factor=tSeconds//60
			tSeconds=(tp-3600*factor)//60
		tMSeconds=tp//3600
		tmstr='{:0>2d}'.format(tmSeconds)
		tSstr='{:0>2d}'.format(tSeconds)
		tMSstr='{:0>1d}'.format(tMSeconds)
		tString=tMSstr+':'+tSstr+':'+tmstr
		t=MyText(tString,50,WHITE,255,self.x-15,self.y-35,0)
		t.basic()   #blitting text

#visual functions
def drawScreen(player1,player2,playerSprites,projectileSprites,cameraRect,BG,FG,stage,FX,tp):
	'drawScreen(p1,p2,playerSprites,projectileSprites,cameraRect,background,foreground,stageeffects,time passed) - Displays all game elements on screen'
	playerSprites.clear(screen,BG)      #sprite methods
	projectileSprites.clear(screen,BG)
	screen.blit(BG,(0,150))
	#draw.rect(screen,(90,39,41),(groundRect))
	#draw.rect(screen,BLACK,(0,575,1200,125))
	# draw.rect(screen,GREEN,player1.hurtbox,1)
	# draw.rect(screen, BLUE, player1.rect, 1)
	# draw.rect(screen,RED,player2.hurtbox,1)
	# draw.rect(screen,BLUE,player2.rect,1)
	# draw.circle(screen, YELLOW, (round(avgpx), round(player1.py - 120)), 5)
	# draw.rect(screen,WHITE,Rect(player2.px,player2.py+30,230,320))
	# draw.circle(screen, WHITE, (round(player1.px), round(player1.py)), 5)
	# draw.circle(screen, WHITE, (round(player2.px), round(player2.py)), 5)
	# draw.rect(screen,WHITE,cameraRect,1)
	# draw.circle(screen, WHITE, (round(player1.px+player1.width / 2), round(player1.py)), 5)
	# draw.circle(screen, WHITE, (round(player2.px+ player2.width / 2), round(player2.py)), 5)
	#background particle objects
	#background particle objects
	if stage == 3:                      #applying weather effects to screen
		FX.leaves(cameraRect,True)
	if stage == 0:
		FX.snow(cameraRect,True)
	if stage == 1:
		FX.rain(cameraRect,True)
	playerSprites.draw(screen)
	projectileSprites.draw(screen)
	#foreground particle objects
	if stage == 3:
		FX.leaves(cameraRect,False)
	if stage == 0:
		FX.snow(cameraRect,False)
	if stage == 1:
		FX.rain(cameraRect,False)
	screen.blit(FG, (0, 150))

	#zooming in the screen so that you see the right amount
	copy=screen.subsurface(cameraRect).copy()
	copy=transform.smoothscale(copy,(width,height))
	screen.blit(copy,(0,0))
	#blitting other game elements
	health1.healthBar(player1.health)
	health2.healthBar(player2.health)
	ouch1.stunBar(player1.ouch,player1,player2)
	ouch2.stunBar(player2.ouch,player1,player2)
	timer.ticking(tp)

def updateCamera(player1, player2, leftpx):
	'updateCamera(player1,player2,leftpx) - updates the camera rect object based on player interaction'
	pList=[0,player1,player2]
	if player1.push:
		i=1
	elif player2.push:
		i=2
	if pList[i].px <= leftpx:
		leftpx = pList[i].px
	elif pList[i].px >= leftpx + 720 - pList[i].width:      #left px represents the leftmost point of the camera rect
		leftpx = pList[i].px - 720 + pList[i].width
	#reseting bounds
	if leftpx<0:
		leftpx=0
	elif leftpx>480:
		leftpx=480

	cameraRect=Rect(leftpx,150,720,420)
	return cameraRect,leftpx

class screenFX(object):
	'class for effects that can be applied to the screen, both in game and in title'
	def __init__(self,stage):
		self.stage=stage
		self.val=1
		self.bounds=0
		self.particles=[]

	def construct(self,stage):
		'contruct(self,stage) - constructs the particles that will be used depending on the season/stage'
		seasonP=[[250,0,2],
		         [250,4,2],
		         [0,0,0],
		         [15,7,4]]
		for i in range(seasonP[stage][0]):
			#giving attributes to each individual particle, like pos x, pos y, speed, direction(l or r) and type if applicable
			x=randint(0,1200)
			y=randint(0,700)
			speed=randint(1,seasonP[stage][2])
			direction=randint(0,1)
			pType=randint(0,seasonP[stage][1])
			self.particles.append([x,y,speed,direction,pType])

	def dynamic(self, t, mode):
		'dynamic(self, time passed, mode) - is a visual method which produces a pulsating effect which can liven up backgrounds'
		if t%3==0:  #executing every 3 frames
			self.bounds+=self.val
			if self.bounds>50 or self.bounds<=0:
				if mode==0:
					self.val*=-1
		if mode==0:         #captures a part of the screen to be copied
			capture = Rect(self.bounds,self.bounds,1200-self.bounds*2,700-self.bounds*2)
		else:
			capture = Rect(self.bounds*12/7,self.bounds,1200-self.bounds*24/7,700-self.bounds)
		##blits the capture to the screen
		copy = screen.subsurface(capture).copy()
		copy = transform.smoothscale(copy, (width, height))
		screen.blit(copy, (0, 0))

	def rain(self,cRect,BG):
		'rain(self,cameraRect,layer) - applies the rain effect'
		for i in range(len(self.particles)):
			##updates and refreshes rain particles
			x=randint(0,1200)
			self.particles[i][1]+=self.particles[i][2]+7
			if (self.particles[i][2]==1 and BG) or (self.particles[i][2]==2 and BG==False): ##gives depth to the layers, making foreground and background layers
				disp=True
			else:
				disp=False
			if self.particles[i][1]>700:
				self.particles[i][0]=x
				self.particles[i][1]=0
				self.particles[i][2]=randint(1,2)
			#drawing only the projectiles on screen
			if cRect.collidepoint(self.particles[i][0]-50,self.particles[i][1]) or cRect.collidepoint(self.particles[i][0]+50,self.particles[i][1]):
				if disp:
					r=rainCol[self.particles[i][4]][0]      #taking from a list of rain colours
					g=rainCol[self.particles[i][4]][1]
					b=rainCol[self.particles[i][4]][2]
					draw.line(screen,(r,g,b),(self.particles[i][0],self.particles[i][1]),(self.particles[i][0],self.particles[i][1]+self.particles[i][2]*15),self.particles[i][2])
					draw.circle(screen,(r,g,b),(self.particles[i][0]+self.particles[i][2]//2,self.particles[i][1]+self.particles[i][2]*7),self.particles[i][2])

	def snow(self,cRect,BG):
		'snow(self,cameraRect,layer) - applies the snow effect'
		##same idea as rain, except a few tweaks due to the different behaviours
		col=randint(230,255)
		for i in range(len(self.particles)):
			x=randint(0,1200)
			self.particles[i][1]+=self.particles[i][2]
			if self.particles[i][2]<=1:
				if BG:
					disp=True
				else:
					disp=False
			else:
				if BG:
					disp=False
				else:
					disp=True
			if self.particles[i][1]>700:
				self.particles[i][0]=x
				self.particles[i][1]=0
				self.particles[i][2]=randint(1,2)
			#drawing only the projectiles on screen
			if cRect.collidepoint(self.particles[i][0]-50,self.particles[i][1]) or cRect.collidepoint(self.particles[i][0]+50,self.particles[i][1]):
				if disp:
					draw.circle(screen,(col,col,col),(self.particles[i][0],self.particles[i][1]),self.particles[i][2])

	def leaves(self,cRect,BG):
		'leaves(self,cameraRect,layer) - applies the falling leaves effect'
		##same idea as snow and rain, except this time there will be falling images
		for i in range(len(self.particles)):
			#updating
			x=randint(0,1200)
			self.particles[i][1]+=self.particles[i][2]
			if (self.particles[i][2]<=2 and BG) or (self.particles[i][2]>2 and BG==False):
				disp=True
			else:
				disp=False
			#refreshing
			if self.particles[i][1]>700:
				self.particles[i][0]=x
				self.particles[i][1]=0
				self.particles[i][2]=randint(1,4)
				self.particles[i][3]=randint(0,1)
				self.particles[i][4]=randint(0,7)
			copy = transform.smoothscale(leaves[self.particles[i][4]],(self.particles[i][2]*10+20,self.particles[i][2]*10+20))
			if cRect.collidepoint(self.particles[i][0]-50,self.particles[i][1]) or cRect.collidepoint(self.particles[i][0]+50,self.particles[i][1]):
				if disp:
					if self.particles[i][3]==1:
						screen.blit(copy,(self.particles[i][0],self.particles[i][1]))
					else:
						screen.blit(transform.flip(copy,True,False),(self.particles[i][0],self.particles[i][1]))

class MyText(object):
	'class for making customizing text with different functionalities'
	def __init__(self,txt,size,col,alpha,locx,locy,font):
		self.txt=txt        #text
		self.size=size      #size
		self.col=col        #colour
		self.alpha=alpha    #alpha value
		self.mulVal=1       #multiplication value
		self.locx=locx      #x
		self.locy=locy      #y
		self.dlocy=0        #delta location y, distance from center
		self.speed=1/8      #default speed value
		self.font=font      #font

	def chosen(self,optionSel,menuNum,indent):
		'chosen(self,optionSelection,menuNumber,indent) - makes the selected word floating'
		if optionSel==menuNum:
			self.dlocy+=self.mulVal*self.speed
			if abs(self.dlocy)>10:
				self.mulVal*=-1
			if indent:      ##indents the word with a beefalo icon
				screen.blit(wordPic(self.txt, self.size, self.col, self.alpha,self.font), (self.locx + 50, self.locy+self.dlocy))
				screen.blit(beefalo,(self.locx,self.locy+self.size/5.5))
			else:
				screen.blit(wordPic(self.txt, self.size, self.col, self.alpha,self.font), (self.locx, self.locy+self.dlocy))
		else:               ## displays word as normal
			screen.blit(wordPic(self.txt, self.size, self.col, self.alpha,self.font), (self.locx, self.locy))
	def basic(self):
		'basic(self) - the most basic type of text'
		screen.blit(wordPic(self.txt, self.size, self.col, self.alpha,self.font), (self.locx, self.locy))
	def fadeAway(self):
		'fadeAway(self) - fades the text to transparency'
		if self.alpha-1>=0:
			self.alpha-=3
	def fadeIn(self):
		'fadeIn(self) - fades the text in to full opacity'
		if self.alpha+1<=255:
			self.alpha+=3

##inital values
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)

CREAM=(245,242,208)
LIME=(76,187,23)

##loading images
titleBG = image.load('backgrounds/titleBG.png').convert()
cssBG=image.load('backgrounds/cssBG.png').convert()
victoryBG=image.load('backgrounds/victoryBG.png').convert()
stageBG=image.load('backgrounds/seasons.png').convert()
pauseBG=image.load('backgrounds/pause.png').convert_alpha()
optionsBG=image.load('backgrounds/optionsBG.png').convert()
attacks=image.load('backgrounds/attacks.png').convert_alpha()
movement=image.load('backgrounds/movement.png').convert_alpha()

autumnBG=image.load('backgrounds/new/autumnBG.png').convert()
autumnFG=image.load('backgrounds/new/autumnFG.png').convert_alpha()
winterBG=image.load('backgrounds/new/winterBG.png').convert()
winterFG=image.load('backgrounds/new/winterFG.png').convert_alpha()
springBG=image.load('backgrounds/new/springBG.png').convert()
springFG=image.load('backgrounds/new/springFG.png').convert_alpha()
summerBG=image.load('backgrounds/new/summerBG.png').convert()
summerFG=image.load('backgrounds/new/summerFG.png').convert_alpha()

leaves=loadSprites('particles/leaves/')

emptyImage=image.load('particles/none.png').convert_alpha()
blowdart=image.load('wilson/leftAttack/blowdart.png').convert_alpha()
ghosts=loadSprites('wendy/leftAttack/projectile/')
wood=image.load('woodie/leftAttack/wood.png').convert_alpha()



beefalo=image.load('icons/beefaloIcon.png').convert_alpha()
creditPics=loadSprites('extras/pics/')
cheer=loadSprites('extras/')
ui=image.load('backgrounds/ui.png').convert_alpha()
playerIcons=loadSprites('icons/characterIcon/')

wilsonPortrait = image.load('portrait/wilson.png').convert_alpha()
wendyPortrait = image.load('portrait/wendy.png').convert_alpha()
woodiePortrait = image.load('portrait/woodie.png').convert_alpha()
randomPortrait = image.load('portrait/random.png').convert_alpha()

#loading sounds and music
mixer.music.load("music/Don't Starve Together - Main Theme2.wav")
menuClick=mixer.Sound('music/FX/menuClick.wav')
#lists
charFX=[[mixer.Sound('music/FX/wilson/0.wav'),  ##2d list of sound effects for each character
         mixer.Sound('music/FX/wilson/1.wav'),
         mixer.Sound('music/FX/wilson/2.wav'),
         mixer.Sound('music/FX/wilson/3.wav')],
        [mixer.Sound('music/FX/wendy/0.wav'),
         mixer.Sound('music/FX/wendy/1.wav'),
         mixer.Sound('music/FX/wendy/2.wav'),
         mixer.Sound('music/FX/wendy/3.wav')],
        [mixer.Sound('music/FX/woodie/0.wav'),
         mixer.Sound('music/FX/woodie/1.wav'),
         mixer.Sound('music/FX/woodie/2.wav'),
         mixer.Sound('music/FX/woodie/3.wav')],
        [],
        [mixer.Sound('music/FX/deerclops/attack.wav'), #deerclops
         mixer.Sound('music/FX/deerclops/hurt.wav'),
         mixer.Sound('music/FX/deerclops/idle.wav'),
         mixer.Sound('music/FX/deerclops/death.wav')],
        [mixer.Sound('music/FX/moosegoose/attack.wav'), #moosegoose
         mixer.Sound('music/FX/moosegoose/hurt.wav'),
         mixer.Sound('music/FX/moosegoose/idle.wav'),
         mixer.Sound('music/FX/moosegoose/death.wav')],
        [mixer.Sound('music/FX/dragonfly/attack.wav'), #dragonfly
         mixer.Sound('music/FX/dragonfly/hurt.wav'),
         mixer.Sound('music/FX/dragonfly/idle.wav'),
         mixer.Sound('music/FX/dragonfly/death.wav')],
        [mixer.Sound('music/FX/bearger/attack.wav'), #bearger
         mixer.Sound('music/FX/bearger/hurt.wav'),
         mixer.Sound('music/FX/bearger/idle.wav'),
         mixer.Sound('music/FX/bearger/death.wav')]]

rainCol=[(74,101,131),  #list of rgb values for rain colour
         (108,128,148),
         (78,104,129),
         (105,122,140),
         (60,83,105)]
seasonList=[[winterBG,winterFG], #list of seasons and their backgrounds
            [springBG,springFG],
            [summerBG,summerFG],
            [autumnBG,autumnFG]]
nameList=['WILSON','WENDY','WOODIE','','DEERCLOPS','MOOSEGOOSE','DRAGONFLY','BEARGER']

###creating class objects
groundRect=Rect(0,550,1200,200)
health1=PlayerDisplay(550,40,1)
health2=PlayerDisplay(650,40,2)
ouch1=PlayerDisplay(150,110,2)
ouch2=PlayerDisplay(1050,110,1)
timer=PlayerDisplay(550,150,1)
###setting time
myClock=time.Clock()
dt=myClock.tick(60)
#mouse.set_visible(False)
running=True
def game(mode,p1,p2,pListSel,charList,stage):
	'game(player1,player2,playerListSelection,characterList,stage choice) - given parameters creates the actual game to play'
	seasonBG,groundBG=seasonList[stage][0],seasonList[stage][1] #finds the correct background and foreground
	myClock = time.Clock()
	myClock.tick(60)
	global keys, avgpx, evt
	playerSprites = sprite.Group() #holds different sprites and can have methods applied to all of its sprites within
	projectileSprites = sprite.Group()
	tp=0
	musicList=[['winterPVP','winterPVE'],
	           ['springPVP','springPVE'],
	           ['summerPVP','summerPVE'],
	           ['autumnPVP','autumnPVE']]
	if mode=='single':
		m=1
	else:
		m=0
	mixer.music.load('music/'+musicList[stage][m]+'.wav')   #plays the correct music for stage and mode
	mixer.music.set_volume(0.25)
	mixer.music.play()
	##creating initial variables
	player1=p1
	player2=p2
	one = pListSel[1]
	two = pListSel[2]
	playerSprites.add(player1)
	playerSprites.add(player2)
	add1=0
	add2=0
	FX=screenFX(stage) #adding screen effects
	FX.construct(stage)
	leftpx=240
	cameraRect = Rect(leftpx, 150, 720, 420)
	running=True
	##basic game loop
	while running:
		for evt in event.get():
			if evt.type==KEYDOWN:
				if evt.key==K_ESCAPE: #opens pause menu
					mixer.music.pause()
					PAUSE(mode)
					mixer.music.unpause()
			if evt.type==QUIT:
				quit()
		keys=key.get_pressed()

		###reseting the characters position, health, and statuses
		if player1.lose or player2.lose or tp>=5400:
			mixer.music.play(0,0)
			if player1.lose:
				add2=player2.points+1
			if player2.lose:
				add1=player1.points+1
			playerSprites.empty()
			projectileSprites.empty()
			##setting values back to default ones
			if mode=='multi':
				player1=Player(1, charList[one][0], charList[one][1], charList[one][2], charList[one][3],
				               charList[one][4], charList[one][5], [False, False, False, False, False, False, False],
				               400, 700, 0, 0, True, False, 0, 200)
				player2=Player(2, charList[two][0], charList[two][1], charList[two][2], charList[two][3],
				               charList[two][4], charList[two][5], [False, False, False, False, False, False, False],
				               700, 700, 0, 0, False, False, 0, 200)
			if mode=='single':
				player1 = Player(1, charList[one][0], charList[one][1], charList[one][2], charList[one][3],
				                 charList[one][4], charList[one][5], [False, False, False, False, False, False, False],
				                 400, 700, 0, 0, True, False, 0, 200)
				player2 = Boss(2,charList[two][0], charList[two][1], charList[two][2], charList[two][3],
				               charList[two][4], charList[two][5], [False, False, False, False, False, False, False],
				               700, 700, 0, 0, True, False, 0, 200)   #pvb
			tp=0
			playerSprites.add(player1)
			playerSprites.add(player2)
			player1.points=add1
			player2.points=add2     ##re-adding the points to the victor

			if add1==2 or add2==2:  ##game is over, heading to victory screen
				mixer.music.stop()
				mixer.music.load("music/Don't Starve Together - Main Theme2.wav")
				VICTORY(mode,player1,player2,pListSel)
			leftpx=240
			cameraRect = Rect(leftpx, 150, 720, 420)
		pList=['',player1,player2]          ###PLIST is used for many functions as a way to access both player 1 and 2's data

		##performing all individual player method for both players
		for i in range(1,3,1):
			pList[i].takeInput(i,pList)
			pList[i].checkHit(pList[i].image,pList,playerSprites)
			pList[i].findVelocity(pList[i].speed)
			pList[i].findAction(projectileSprites,pList)
			cameraRect,leftpx=pList[i].updatePos(mode,pList,cameraRect,leftpx)
		avgpx=((pList[1].px+pList[1].width/2)+(pList[2].px+pList[2].width/2))/2 ##position between both players
		projectileSprites.update(pList,projectileSprites,leftpx)        #updating all items in both sprite groups
		playerSprites.update(pList)
		# if player1.lose==False and player2.lose==False:         ##drawing the screen as long as
		# 	print('asdfasdfadsfasdfasd')
		avgpx=(player1.px+player2.px)/2
		drawScreen(player1,player2,playerSprites,projectileSprites,cameraRect,seasonBG,groundBG,stage,FX,tp)
		myClock.tick(60)
		display.flip()
		tp+=1
# TITLEMENU('title')
# CREDITS()
# CSS('single',False,[2,0,2])
# game('single',Player(1,wilson,wilsonHitbox,0,100,150,50,[False,False,False,False,False,False,False],300,400,0,0,True,False,0,200),
#      Boss(2,dragonfly,dragonflyHitbox,6,250,350,30,[False,False,False,False,False,False,False],550,400,0,0,False,False,0,200),[2,0,6],   #pvb
#              [[wilson,wilsonHitbox,0,100,150,50],
#               [wendy,wendyHitbox,1,100,150,50],
#               [woodie,woodieHitbox,2,100,150,50],
#               [],
#               [deerclops,deerclopsHitbox,4,250,350,30],
#               [moosegoose,moosegooseHitbox,5,250,430,30],
#               [dragonfly,dragonflyHitbox,6,250,350,30],
#               [bearger,beargerHitbox,7,260,350,30]],2)
game('multi',Player(1,wilson,wilsonHitbox,0,100,150,50,[False,False,False,False,False,False,False],400,400,0,0,True,False,0,200),
     Player(2,woodie,woodieHitbox,2,100,150,50,[False,False,False,False,False,False,False],700,400,0,0,False,False,0,200),[0,0,2],
     [[wilson,wilsonHitbox,0,100,150,50],
      [wendy,wendyHitbox,1,100,150,55],
      [woodie,woodieHitbox,2,100,150,45],
      [],
      [deerclops,deerclopsHitbox,4,250,350,30],
      [moosegoose,moosegooseHitbox,4,250,350,30],
      [dragonfly,dragonflyHitbox,4,250,350,30],
      [bearger,beargerHitbox,4,250,350,30]],2)        #pvp
# VICTORY('multi',wilson,wendy)
quit()