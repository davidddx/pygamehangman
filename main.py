import pygame;
import sys;
import os;
import globals;
import words;
false = False;
true = True;

projectdirectory = os.getcwd();
def inputmap(key):
    word = globals.word
    if key[pygame.K_ESCAPE]:
        pygame.quit();
    elif key[pygame.K_RETURN]:
        lives -= 1;
        currentimage = hangmanstates[7 - lives]
    elif key[pygame.K_a]:
        checkletter('a', word);
    elif key[pygame.K_b]:
        checkletter('b', word);
    elif key[pygame.K_c]:
        checkletter('c', word);
    elif key[pygame.K_d]:
        checkletter('d', word);
    elif key[pygame.K_e]:
        checkletter('e', word);
    elif key[pygame.K_f]:
        checkletter('f', word);
    elif key[pygame.K_g]:
        checkletter('g', word);
    elif key[pygame.K_h]:
        checkletter('h', word);
    elif key[pygame.K_i]:
        checkletter('i', word);
    elif key[pygame.K_j]:
        checkletter('j', word);
    elif key[pygame.K_k]:
        checkletter('k', word);
    elif key[pygame.K_l]:
        checkletter('l', word);
    elif key[pygame.K_m]:
        checkletter('m', word);
    elif key[pygame.K_n]:
        checkletter('n', word);
    elif key[pygame.K_o]:
        checkletter('o', word);
    elif key[pygame.K_p]:
        checkletter('p', word);
    elif key[pygame.K_q]:
        checkletter('q', word);
    elif key[pygame.K_r]:
        checkletter('r', word);
    elif key[pygame.K_s]:
        checkletter('s', word);
    elif key[pygame.K_t]:
        checkletter('t', word);
    elif key[pygame.K_u]:
        checkletter('u', word);
    elif key[pygame.K_v]:
        checkletter('v', word);
    elif key[pygame.K_w]:
        checkletter('w', word);
    elif key[pygame.K_x]:
        checkletter('x', word);
    elif key[pygame.K_y]:
        checkletter('y', word);
    elif key[pygame.K_z]:
        checkletter('z', word);
    elif key[pygame.K_1]:
        checkletter('1', word);
    elif key[pygame.K_2]:
        checkletter('2', word);
    elif key[pygame.K_3]:
        checkletter('3', word);
    elif key[pygame.K_4]:
        checkletter('4', word);
    elif key[pygame.K_5]:
        checkletter('5', word);
    elif key[pygame.K_6]:
        checkletter('6', word);
    elif key[pygame.K_7]:
        checkletter('7', word);
    elif key[pygame.K_8]:
        checkletter('8', word);
    elif key[pygame.K_9]:
        checkletter('9', word);
    elif key[pygame.K_0]:
        checkletter('0', word);

def guessalreadycontains(guessedletter):
    guess = globals.guess;
    for letter in globals.guess:
        if guessedletter == letter:
            return true;

    return false;

def checkletter(guessedletter, word):
    newguess = '';
    # print("word: ", word)
    containsletter = false;
    index = 0;
    for aletter in word:
        if guessedletter == aletter:
            containsletter = true;
            newguess = newguess + aletter;
        elif guessalreadycontains(aletter):
            newguess = newguess + aletter;
        else: newguess = newguess + '_';
        newguess = newguess + ' ';
        index+= 1;
    if not containsletter:
        globals.lives -= 1;
        globals.guessed.append(guessedletter)
        # print(guessedletter);
    # print(globals.category)
    # print(newguess)
    globals.guess = newguess;
    print("guessed contains letter ", guessedletter, "?: ")

    globals.timelastpressed = pygame.time.get_ticks();

def checkwin():
    guess = globals.guess;
    word = globals.word;
    index = 0;
    for letter in word:
        if letter == guess[2 * index]:
            index+=1;
            continue;
        else:
            return false;
    return true;

def loserscreen():
    print("you lose");
    timenow = pygame.time.get_ticks();
    timelost = timenow;
    stayfor = 3000;
    fonttype = "Times New Roman";
    fontsize = 100;
    font = pygame.font.SysFont(fonttype, fontsize);
    youlose = font.render('you lost!',1,(0,0,0))
    globals.screen.blit(youlose, (10,400))
    pygame.display.update();
    while true:
        if timenow - timelost > 1000:
            break;
        timenow = pygame.time.get_ticks();
    timenow = pygame.time.get_ticks();
    fontsize = 30;
    font = pygame.font.SysFont(fonttype, fontsize);
    timebreak = timenow;
    globals.screen.fill((180, 180, 180));
    playagain = font.render('if you to play, wait 3 seconds. otherwise press esc', 1, (0, 0, 0))
    globals.screen.blit(playagain, (10, 400))
    pygame.display.update();
    clock = pygame.time.Clock();
    x = 1;
    while true:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
        clock.tick(30)
        x = 3 * x
        timenow = pygame.time.get_ticks();

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            sys.exit();
        if timenow - timebreak >= stayfor:
            startgame();
            break;
    return None;

def winnerscreen():
    print("you win");
    timenow = pygame.time.get_ticks();
    timelost = timenow;
    stayfor = 5000;
    fonttype = "Times New Roman";
    fontsize = 100;
    font = pygame.font.SysFont(fonttype, fontsize);
    youlose = font.render('you won!',1,(0,0,0))
    globals.screen.blit(youlose, (10,400))
    pygame.display.update();
    while true:
        if timenow - timelost > 1000:
            break;
        timenow = pygame.time.get_ticks();
    timenow = pygame.time.get_ticks();
    fontsize = 30;
    font = pygame.font.SysFont(fonttype, fontsize);
    timebreak = timenow;
    globals.screen.fill((180, 180, 180));
    playagain = font.render('if you want to play, wait 3 seconds. otherwise, press esc', 1, (0, 0, 0))
    globals.screen.blit(playagain, (10, 400))
    pygame.display.update();
    clock = pygame.time.Clock();
    x = 1;
    while true:
        clock.tick(30)
        timenow = pygame.time.get_ticks();

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            sys.exit();
        if timenow - timebreak >= stayfor:
            startgame();
            break;
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
    return None;

def startgame():
    globals.lives = len(globals.hangmanstates) - 1;
    globals.word = words.getword();
    globals.guess = words.generateguessString(globals.word);
    globals.category = words.getcategory(globals.word);
    globals.guessed = [];

def gameloop():
    pygame.init();
    clock = pygame.time.Clock();
    screenwidth = 800;
    screenheight = 600;
    globals.screen = pygame.display.set_mode((screenwidth, screenheight))
    screen = pygame.display.set_mode((screenwidth, screenheight));
    running = True;
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
    globals.hangmanstates = hangmanstates;
    globals.lives = len(hangmanstates) - 1;
    lives = globals.lives;
    globals.word = words.getword();
    globals.guess = words.generateguessString(globals.word);
    globals.category = words.getcategory(globals.word);

    currentimage = hangmanstates[len(hangmanstates) - 1 - lives];

    cooldown = 500 #milliseconds
    while running:
        clock.tick(30)
        screen.fill((180,180,180));
        key = pygame.key.get_pressed();
        currentimage = hangmanstates[len(hangmanstates) - 1 - globals.lives];
        screen.blit(currentimage, (0, 0))


        ##Displays Lives##
        fonttype = "Times New Roman";
        fontsize = 30;
        font = pygame.font.SysFont(fonttype, fontsize);

        guessedstring = "";
        for aletter in globals.guessed:
            guessedstring = guessedstring + aletter + ',' ;

        livesimg = font.render('guesses left: ' + str(globals.lives), 1, (0, 0, 0));
        guessimg = font.render(globals.guess, 1, (0,0,0));
        guessedimg = font.render('guessed: ' + guessedstring, 1, (0,0,0));
        categoryimg = font.render('Genre: ' + globals.category, 1, (0,0,0));
        screen.blit(livesimg, (64, 3));
        screen.blit(guessimg, (screenwidth/2, screenheight/2));
        screen.blit(guessedimg, (300,400))
        screen.blit(categoryimg, (300, 0))
        globals.timenow = pygame.time.get_ticks();
        if globals.timenow - globals.timelastpressed >= cooldown:
            inputmap(key);

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
        if checkwin() == true:
            winnerscreen();
        if (globals.lives == 0):
            loserscreen();
        pygame.display.update();

if __name__ == '__main__':

    gameloop();
