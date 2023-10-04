import pygame;
import sys;
import os;
import globals;
import words;
false = False;
true = True;

projectdirectory = os.getcwd();

def newinputmap(key):
    if key[pygame.K_ESCAPE]:
        pygame.quit();
    elif key[pygame.K_RETURN]:
        lives -= 1;
        currentimage = hangmanstates[7 - lives]
    elif key[pygame.K_a]:
        return 'a'
    elif key[pygame.K_b]:
        return 'b'
    elif key[pygame.K_c]:
        return 'c'
    elif key[pygame.K_d]:
        return 'd'
    elif key[pygame.K_e]:
        return 'e'
    elif key[pygame.K_f]:
        return 'f'
    elif key[pygame.K_g]:
        return 'g'
    elif key[pygame.K_h]:
        return 'h'
    elif key[pygame.K_i]:
        return 'i'
    elif key[pygame.K_j]:
        return 'j'
    elif key[pygame.K_k]:
        return 'k'
    elif key[pygame.K_l]:
        return 'l'
    elif key[pygame.K_m]:
        return 'm'
    elif key[pygame.K_n]:
        return 'n'
    elif key[pygame.K_o]:
        return 'o'
    elif key[pygame.K_p]:
        return 'p'
    elif key[pygame.K_q]:
        return 'q'
    elif key[pygame.K_r]:
        return 'r'
    elif key[pygame.K_s]:
        return 's'
    elif key[pygame.K_t]:
        return 't'
    elif key[pygame.K_u]:
        return 'u'
    elif key[pygame.K_v]:
        return 'v'
    elif key[pygame.K_w]:
        return 'w'
    elif key[pygame.K_x]:
        return 'x'
    elif key[pygame.K_y]:
        return 'y'
    elif key[pygame.K_z]:
        return 'z'
    elif key[pygame.K_1]:
        return '1'
    elif key[pygame.K_2]:
        return '2'
    elif key[pygame.K_3]:
        return '3'
    elif key[pygame.K_4]:
        return '4'
    elif key[pygame.K_5]:
        return '5'
    elif key[pygame.K_6]:
        return '6'
    elif key[pygame.K_7]:
        return '7'
    elif key[pygame.K_8]:
        return '8'
    elif key[pygame.K_9]:
        return '9'
    elif key[pygame.K_0]:
        return '0'
    else:
        return None
def newgameloop(word, category):
    # print('newgameloop')
    pygame.init();
    clock = pygame.time.Clock();
    screenwidth = 800;
    screenheight = 600;
    screen = pygame.display.set_mode((screenwidth, screenheight))
    hangmanstates = [
        pygame.image.load(projectdirectory + '/images/hangman0.png'), #7 guesses left
        pygame.image.load(projectdirectory + '/images/hangman1.png'), #6
        pygame.image.load(projectdirectory + '/images/hangman2.png'), #5
        pygame.image.load(projectdirectory + '/images/hangman3.png'), #4
        pygame.image.load(projectdirectory + '/images/hangman4.png'), #3
        pygame.image.load(projectdirectory + '/images/hangman5.png'), #2
        pygame.image.load(projectdirectory + '/images/hangman6.png'), #1
        pygame.image.load(projectdirectory + '/images/hangman7.png'), #gameover
    ];
    # globals.hangmanstates = hangmanstates;
    guessesleft = len(hangmanstates) - 1
    currentimage = hangmanstates[len(hangmanstates) - 1 - guessesleft];
    running = true;
    guessedright = []
    guessedwrong = []
    cooldown = 500
    timelastpressed = 0
    timenow = timelastpressed;
    gameresult = None;

    if ' ' in word:
        guessedright.append(' ');

    initialdraw(currentimage, word, category, guessesleft, screen);
    pygame.display.update();

    timegamelaststarted = 0;
    timegameended = 0;
    while running:
        clock.tick(10)
        timenow = pygame.time.get_ticks();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
        key = pygame.key.get_pressed();

        if gameresult == None: # if the game is not over
            letter = None;
            if timenow - timelastpressed > cooldown:
                letter = newinputmap(key);


            if letter == None:
                # print('letter is none')
                continue;
            else:
                timelastpressed = timenow;
            if letter in word:
                guessedright.append(letter);
            else:
                guessedwrong.append(letter)
                guessesleft -= 1;
                currentimage = hangmanstates[len(hangmanstates) - 1 - guessesleft];
            gameresult = checkifdone(guessesleft, guessedright, word);
            drawstuffonscreen(currentimage, word, category, guessesleft, guessedright, guessedwrong, screen);
            pygame.display.update();
            timegamelaststarted = timenow;
        else:
            gameended = true;
            if timenow - timegamelaststarted < 1000:
                if gameended:

                    gameended = false;

                    fonttype = "Times New Roman";
                    fontsize = 100;
                    font = pygame.font.SysFont(fonttype, fontsize);
                    stringg = 0;
                    if gameresult == true:
                        stringg = font.render('you WON!', 1, (0, 0, 0))
                    else:
                        stringg = font.render('you lost!', 1, (0, 0, 0))
                    screen.blit(stringg, (10, 400))
                    pygame.display.update();
                    gameended = false;
            else:
                timegameended = timenow;
                break;
    drew = false;
    while timenow - timegameended < 3000:
        key = pygame.key.get_pressed();
        timenow = pygame.time.get_ticks();
        if not drew: #makes sure to not draw this every frame
            screen.fill((180, 180, 180));
            fonttype = "Times New Roman";
            fontsize = 25;
            font = pygame.font.SysFont(fonttype, fontsize);
            stringg = 0;

            stringg = font.render('Press escape to exit. Otherwise, the next round will start in 3 seconds', 1, (0, 0, 0))
            screen.blit(stringg, (30,30));
            drew = true;
            pygame.display.update();

        if key[pygame.K_ESCAPE]:
            globals.restart = false;
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
def initialdraw(image, word, category, guessesleft, screen):
    screen.fill((180, 180, 180));
    screen.blit(image, (0, 0));
    blanks = "";
    for letter in word:
        if letter == ' ':
            blanks = blanks + ' ';
        else:
            blanks = blanks + '_';
        blanks = blanks + ' ';
    fonttype = "Times New Roman";
    fontsize = 30;
    font = pygame.font.SysFont(fonttype, fontsize);
    livesimg = font.render('guesses left: ' + str(guessesleft), 1, (0, 0, 0));
    guessedimg = font.render('guessed: ', 1, (0, 0, 0));
    categoryimg = font.render('Genre: ' + category, 1, (0, 0, 0));
    screen.blit(livesimg, (64, 3));
    screen.blit(guessedimg, (300, 400))
    screen.blit(categoryimg, (300, 0))

    blankrendered = font.render(blanks,1,(0,0,0))
    screen.blit(blankrendered, (140, 300));

def checkifdone(guessesleft, guessedright, word):
    if guessesleft == 0:
        return false;
    else:
        for letter in word:
            if letter in guessedright:
                continue;
            else:
                return None;
        return true;

def drawstuffonscreen(image, word, category, guessesleft, guessedright, guessedwrong, screen):
    screen.fill((180, 180, 180));
    screen.blit(image, (0, 0));
    blanks = "";
    for letter in word:
        if letter in guessedright:
            blanks = blanks + letter;
        else:
            blanks = blanks + '_';
        blanks = blanks + ' ';
    strguessedwrong = ''
    for letter in guessedwrong:
        strguessedwrong = strguessedwrong + letter + ','
    fonttype = "Times New Roman";
    fontsize = 30;
    font = pygame.font.SysFont(fonttype, fontsize);
    livesimg = font.render('guesses left: ' + str(guessesleft), 1, (0, 0, 0));
    guessedimg = font.render('guessed: ' + strguessedwrong, 1, (0, 0, 0));
    categoryimg = font.render('Genre: ' + category, 1, (0, 0, 0));
    screen.blit(livesimg, (64, 3));
    screen.blit(guessedimg, (300, 400));
    screen.blit(categoryimg, (300, 0));
    blankrendered = font.render(blanks, 1, (0, 0, 0));
    screen.blit(blankrendered, (140, 300));

if __name__ == '__main__':
    while globals.restart:
        word = words.getword();
        category = words.getcategory(word);
        newgameloop(word = word, category = category);