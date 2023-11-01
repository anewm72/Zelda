#Control shift and F reindents everything!!
import pygame
import time
import random
global begin

run = 0
begin = 0
talk = 0
pygame.init()
width = 640
height = 480
x = 550
y = 420
w = 30
h = 30
mon_x = random.randint(100, 115)
mon_y = random.randint(100, 115)
mon_2x = random.randint(100, 115)
mon_2y = random.randint(100, 115)
mon_w = 20
mon_h = 20
charx = width-w
chary = height // 2 - h // 2

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 204, 51)
ojo = (255, 153, 51)
blue = (85, 85, 255)
purple = (102, 51, 255)
peacock = (51, 161, 201)
yellow = (204, 255, 51)
olive = (192, 255, 62)
deep_pink = (255, 20, 147)
green = (51, 204, 51)
gree = (204, 255, 51)
red_orange = (255, 102, 51)
monster_colours = [yellow, ojo, red_orange]

#Need to work on my classes

class tutorial():
    print("Welcome to The Legend of Zelda! (reprised by Abby).")
    print("Go ahead and press 's' to begin!")
    def started():
        print("Awesome! Now try and move around a little, using WASD, the usual.")
        print("You can also click space to open your inventory (it's a bit empty now, but it'll get bigger).")
    def glitch():
        print("Uh oh, look who's here...it's a glitch trying to invade the game!  Watch out for these...at the moment they won't look to attack you, but don't go running into them!")
    def end():
        print("Well, there's your first quest! I suppose you should make haste and get on with the game...but in the meantime, good luck!")
    

class Character():
    def __init__(self, name, hit_taken):
        self.name = name
        self.max_hit_points = 10
        self.hit_taken = current_hit_points

    def hit(self):
        self.current_hit_points = self.max_hit_points + self.hit_taken
        

class inventory():
    item_list = []
    items = item_list

    def __init__(self):
        item_list = []
        items = item_list

    def view_items():
        return

    def add_item(self, item):
        self.items[item.name] = item
             

class quests():
    def set_star(done):
        quest = pygame.image.load("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/C821B49B-D237-4407-9490-B7D5616A90D4.png")
        quest_small = pygame.transform.scale(quest, (50, 50))
        screen.blit(quest_small, (100, 200))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            quest_point = quest_small.get_rect()
            quest_point.center = (75, 180)
            if quest.get_rect().collidepoint(mouse_pos):
                quests.no1(done)
   
    def no1(done):
        if done == 0:
            print("Hello visitor to these great lands! This is your first quest, and to get you started I suppose we should go easy on you.")
            print("Let's see...go to that hut!")
            done = done + 1
            tutorial.end()
        else:
            return

def room_1(begin):
    begin = begin + 1
    screen.fill(green)
    log = pygame.image.load("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/FAA8C151-9782-429A-AC0D-C34DE6AEE1D0.png")
    log_small = pygame.transform.scale(log, (50, 50))
    screen.blit(log_small, (200,250))
    hut = pygame.image.load("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/1C4583AE-7D2D-42A0-B74D-4A06D2DDFDA4.png")
    hut_small = pygame.transform.scale(hut, (100, 100))
    screen.blit(hut_small, (10, 0))
    link = pygame.image.load("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/3B186224-18AA-4878-889A-561E91271AAD.png")
    link_small = pygame.transform.scale(link, (w,h))
    screen.blit(link_small, (x,y))
    pause = pygame.image.load("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/7B1B8D8D-85F6-4B1B-BE67-FCAAFE8AA142.png")
    global pause_small
    pause_small = pygame.transform.scale(pause, (80, 70))
    screen.blit(pause_small, (110, 412))
    quitting = pygame.image.load("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/8C9A65F0-A5BA-4622-9514-AE7D06675120.png")
    global quitting_small
    quitting_small = pygame.transform.scale(quitting, (80, 50))
    screen.blit(quitting_small, (180, 422))
    wall_1 = pygame.draw.rect(screen, blue, (0, 40, 20, height-20), 0)
    wall_2 = pygame.draw.rect(screen, blue, (100, 0, width, 20), 0)
    wall_3 = pygame.draw.rect(screen, blue, (width-20, 0, 20, height), 0)
    wall_4 = pygame.draw.rect(screen, blue, (0, height - 20, width-20, 20), 0)
    points = [(150, 160), (180, 120), (185, 140), (190, 140), (185, 160)]
    if begin == 1:
        tutorial.started()
    if begin == 200:
        tutorial.glitch()
        global done
        done = 0
    if begin > 1000:
        if begin < 2000:
            quests.set_star(done)
                    
def room_2(begin):
    screen.fill(peacock)
    link = pygame.image.load("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/3B186224-18AA-4878-889A-561E91271AAD.png")
    link_small = pygame.transform.scale(link, (w,h))
    screen.blit(link_small, (x,y))
    
                
intro_sound = pygame.mixer.Sound('//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/131659__bertrof__game-sound-intro-to-game.wav')
pygame.mixer.Sound.play(intro_sound)
pygame.mixer.music.stop()
screen = pygame.display.set_mode((width, height))
start = True
running = False
back = True
while (start):
    run = run + 1
    if run == 1:
        tutorial()
    main_menu = pygame.image.load("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/Zelda Main Menu.jpg")
    main_menu_large = pygame.transform.scale(main_menu, (850, 550))
    screen.blit(main_menu_large, (-100,-50))
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        start = False
        running = True
        room1 = True
    else:
        start = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

if running == True:
    pygame.mixer.music.load('//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/489035__michael-db__game-music-01.wav')
    pygame.mixer.music.play(-1)

while (running):
    if begin <= 10:
        if str(begin)[-1] == '0':
            mon_x = random.randint(20, 620)
            if mon_x <= x + 20:
                    mon_x = 10
            mon_y = random.randint(20, 460)
            if mon_y >= y - 20:
                  if mon_y <= y+ 20:
                     mon_y = 10
    else:
        if str(begin)[-1] == '0':
            if str(begin)[-2] == '0':
                mon_x = random.randint(20, 620)
                if mon_x <= x + 20:
                        mon_x = 10
                mon_y = random.randint(20, 460)
                if mon_y >= y - 20:
                      if mon_y <= y+ 20:
                         mon_y = 10
                          
    begin = begin + 1
    if back == True:
        room_1(begin)
    else:
        room_2(begin)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if x < 20:
            x = x
        elif x > 0:
            x -= 4
            mon_x = mon_x
            mon_y = mon_y
                
    if keys[pygame.K_w]:
        if y < 20:
            y = y
        elif y > 0:
            y -= 4
            mon_x = mon_x
            
    if keys[pygame.K_d]:
        if x == 640-50:
            x = x
        elif x < width-w:
            x += 4
            
    if keys[pygame.K_s]:
        if y == 460-h:
            y = y
        elif y < height-h:
            y += 4

    if keys[pygame.K_SPACE]:
        print(inventory.items)
                
    #Collision code
    if x + w > mon_x and x < mon_x + mon_w:
        if y + h >= mon_y and y < mon_y + mon_h:
            if x - mon_x > 10:
                running = True
            else:
                screen.fill(red)
                time.sleep(1)
                if run < 200:
                    pygame.mixer.music.stop()
                    end_sound = pygame.mixer.Sound("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/382310__myfox14__game-over-arcade.wav")
                    pygame.mixer.Sound.play(end_sound)
                    time.sleep(2)
                    print("Why'd you just join the game and run into that thing! Ah well, try again later!")
                    running = False
                elif run < 1000:
                    pygame.mixer.music.stop()
                    end_sound = pygame.mixer.Sound("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/382310__myfox14__game-over-arcade.wav")
                    pygame.mixer.Sound.play(end_sound)
                    time.sleep(2)
                    print("I told you not to go running into them! Well, you lost the game, try again soon!")
                    running = False
                else:
                    pygame.mixer.music.stop()
                    end_sound = pygame.mixer.Sound("//FILE/UserFolders$/Students/Intake2020/NewmanA20/Downloads/382310__myfox14__game-over-arcade.wav")
                    pygame.mixer.Sound.play(end_sound)
                    time.sleep(2)
                    print("Uh oh, you died...better luck next time?")
                    running = False
                
    if x > 40 and x < 60:
        if y > 50 and y < 70:
            back = False
            print("Now teleporting...")
            
                
    #Monsters now back to squares because collisions work considerably better with them        
    pygame.draw.rect(screen, random.choice(monster_colours),(mon_x, mon_y, mon_w, mon_h),0)
    #Need to add this after a random amount of time
    #pygame.draw.rect(screen, random.choice(monster_colours),(mon_2x, mon_2y, mon_w, mon_h),0)   
    pygame.display.flip()
    time.sleep(0.005)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            pausing = pause_small.get_rect()
            pausing.center = (130, 432)
            quitting = quitting_small.get_rect()
            quitting.center = (190, 433)
            if pausing.collidepoint(mouse_pos):
                print("Paused")
            elif quitting.collidepoint(mouse_pos):
                print("Are you sure you wish to quit? (click another point on the screen if not)")
                time.sleep(2)
                mouse_pos = pygame.mouse.get_pos()
                if quitting.collidepoint(mouse_pos):
                    running = False
                else:
                    running = True
# quit pygame
pygame.quit()
