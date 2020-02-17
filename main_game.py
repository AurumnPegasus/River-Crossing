import pygame
import os
import time

pygame.init()
clock = pygame.time.Clock()
done = False
blue = (0, 0, 200)
brown = (100, 40, 0)
screen = pygame.display.set_mode((1080, 760))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


x_player = 500
y_player = 730
x_change_player = 0
y_change_player = 0
level_player_one = 1
level_player_two = 1
total_score_one = 0
total_score_two = 0
time_one = 0
time_two = 0
enemy_one_x = 0
enemy_one_y = 650
enemy_five_x = 0
enemy_five_y = 40
enemy_two_x = 0
enemy_two_y = 530
enemy_four_x = 0
enemy_four_y = 230
enemy_two_x_b = 980
enemy_two_y_b = 450
enemy_four_x_b = 980
enemy_four_y_b = 150
enemy_three_x = 0
enemy_three_y = 340
first_time_ship_one = True
first_time_ship_two = True
first_time_ship_two_b = True
first_time_ship_three = True
change_enemy_one = 1
change_enemy_two = 1.5
change_enemy_two_b = 1.5
change_enemy_three = 2
score_player_one = 0
max_player_one = 760
threshold_player_one = 760
playerone = True
exit_kar = False
for_score = [False, False, False, False, False, False, False, False, False,
             False, False, False, False, False]
pillar_position = [(200, 700), (370, 590), (650, 590), (500, 390),
                   (220, 390), (900, 280), (400, 280), (750, 90), (400, 90), (550, 0)]


class Enemies():

    def __init__(self, image_local, level, x_start, y_start):
        self.image_local = image_local
        self.level = level
        self.x_start = x_start
        self.y_start = y_start

    def initialise(self):
        screen.blit(self.image_local, (self.x_start, self.y_start))


class Player():

    def __init__(self, x, y, image_local):
        self.x = x
        self.y = y
        self.image_local = image_local

    def initialise(self):
        screen.blit(self.image_local, (self.x, self.y))


def keep_score_one(y):
    if y < globals()['max_player_one'] and y < globals()[
            'threshold_player_one']:
        globals()['max_player_one'] = y
        if y >= 730:
            for_score[0] = True
            globals()['threshold_player_one'] = 730
            return 5
        elif y > 620 and y < globals()['threshold_player_one'] - 100 and for_score[0]:
            for_score[1] = True
            globals()['threshold_player_one'] = 620
            return 10
        elif y > 570 and y < globals()['threshold_player_one'] - 40 and for_score[1]:
            for_score[2] = True
            globals()['threshold_player_one'] = 570
            return 10
        elif y > 520 and y < globals()['threshold_player_one'] - 30 and for_score[2]:
            for_score[3] = True
            globals()['threshold_player_one'] = 520
            return 10
        elif y > 420 and y < globals()['threshold_player_one'] - 80 and for_score[3]:
            for_score[4] = True
            globals()['threshold_player_one'] = 420
            return 10
        elif y > 380 and y < globals()['threshold_player_one'] - 30 and for_score[4]:
            for_score[5] = True
            globals()['threshold_player_one'] = 380
            return 10
        elif y > 320 and y < globals()['threshold_player_one'] - 50 and for_score[5]:
            for_score[6] = True
            globals()['threshold_player_one'] = 320
            return 10
        elif y > 280 and y < globals()['threshold_player_one'] - 30 and for_score[6]:
            for_score[7] = True
            globals()['threshold_player_one'] = 280
            return 10
        elif y > 230 and y < globals()['threshold_player_one'] - 40 and for_score[7]:
            for_score[8] = True
            globals()['threshold_player_one'] = 230
            return 10
        elif y > 130 and y < globals()['threshold_player_one'] - 90 and for_score[8]:
            for_score[9] = True
            globals()['threshold_player_one'] = 130
            return 10
        elif y > 70 and y < globals()['threshold_player_one'] - 50 and for_score[9]:
            for_score[10] = True
            globals()['threshold_player_one'] = 70
            return 10
        elif y > 30 and y < globals()['threshold_player_one'] - 30 and for_score[10]:
            for_score[11] = True
            globals()['threshold_player_one'] = 30
            return 10
        elif y < 10:
            globals()['threshold_player_one'] = 0
            return 5
    return 0


def keep_score_two(y):
    if y > globals()['max_player_one'] and y > globals()[
            'threshold_player_one']:
        globals()['max_player_one'] = y
        if y < 10:
            for_score[0] = True
            globals()['threshold_player_one'] = 10
            return 5
        elif y < 90 and globals()['threshold_player_one'] + 70 < y and for_score[0]:
            for_score[1] = True
            globals()['threshold_player_one'] = 90
            return 10
        elif y < 130 and globals()['threshold_player_one'] + 30 < y and for_score[1]:
            for_score[2] = True
            globals()['threshold_player_one'] = 130
            return 10
        elif y < 230 and globals()['threshold_player_one'] + 90 < y and for_score[2]:
            for_score[3] = True
            globals()['threshold_player_one'] = 230
            return 10
        elif y < 290 and globals()['threshold_player_one'] + 50 < y and for_score[3]:
            for_score[4] = True
            globals()['threshold_player_one'] = 290
            return 10
        elif y < 330 and globals()['threshold_player_one'] + 30 < y and for_score[4]:
            for_score[5] = True
            globals()['threshold_player_one'] = 330
            return 10
        elif y < 380 and globals()['threshold_player_one'] + 40 < y and for_score[5]:
            for_score[6] = True
            globals()['threshold_player_one'] = 380
            return 10
        elif y < 440 and globals()['threshold_player_one'] + 50 < y and for_score[6]:
            for_score[7] = True
            globals()['threshold_player_one'] = 440
            return 10
        elif y < 520 and globals()['threshold_player_one'] + 70 < y and for_score[7]:
            for_score[8] = True
            globals()['threshold_player_one'] = 520
            return 10
        elif y < 570 and globals()['threshold_player_one'] + 30 < y and for_score[8]:
            for_score[9] = True
            globals()['threshold_player_one'] = 570
            return 10
        elif y < 620 and globals()['threshold_player_one'] + 40 < y and for_score[9]:
            for_score[10] = True
            globals()['threshold_player_one'] = 620
            return 10
        elif y < 730 and globals()['threshold_player_one'] + 100 < y and for_score[10]:
            for_score[11] = True
            globals()['threshold_player_one'] = 730
            return 10
        elif y > 740 and for_score[11]:
            globals()['threshold_player_one'] = 0
            return 5
    return 0


def make_land():
    pygame.draw.rect(screen, brown, pygame.Rect(0, 0, 1080, 40))
    pygame.draw.rect(screen, brown, pygame.Rect(0, 605, 1080, 40))
    pygame.draw.rect(screen, brown, pygame.Rect(0, 405, 1080, 40))
    pygame.draw.rect(screen, brown, pygame.Rect(0, 305, 1080, 40))
    pygame.draw.rect(screen, brown, pygame.Rect(0, 105, 1080, 40))
    pygame.draw.rect(screen, brown, pygame.Rect(0, 720, 1080, 40))


_image_library = {}


def get_image(path):
    global _image_library
    image = pygame.image.load(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


while not exit_kar:
    if level_player_one == 5 or level_player_two == 5:
        exit_kar = True
        print(str(level_player_one) + "  " + str(level_player_two))
        continue
    if playerone:
        done = False
        for_score = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False]
        start_ticks = pygame.time.get_ticks()
        seconds_player_one = 0
        score_player_one = 0
        globals()['max_player_one'] = 760
        globals()['threshold_player_one'] = 760
        globals()['score_player_one'] = 0
        x_player = 500
        y_player = 730
        x_change_player = 0
        y_change_player = 0
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    exit_kar = True
                    playerone = True
                    globals()['level_player_one'] += 1
                    globals()['total_score_one'] += score_player_one
                    globals()['time_one'] += seconds_player_one
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change_player = -3
                    elif event.key == pygame.K_RIGHT:
                        x_change_player = 3
                    elif event.key == pygame.K_UP:
                        y_change_player = -3
                    elif event.key == pygame.K_DOWN:
                        y_change_player = 3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change_player = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        y_change_player = 0

            if x_player + x_change_player > 1030 or x_player + x_change_player < 0:
                pass
            else:
                x_player += x_change_player
            if y_player + y_change_player > 730 or y_player + y_change_player < 0:
                pass
            else:
                y_player += y_change_player
            spiderman_image = pygame.transform.scale(
                get_image('spiderman.png'), (50, 30))
            ship_image = pygame.transform.scale(
                get_image('ship.png'), (100, 70))
            pillar_image = pygame.transform.scale(
                get_image('pillar.png'), (50, 50))
            kraken_image = pygame.transform.scale(
                get_image('kraken.png'), (100, 70))
            sea_image = pygame.transform.scale(
                get_image('sea-monster.png'), (100, 70))
            screen.fill(blue)
            make_land()
            player_one = Player(x_player, y_player, spiderman_image)
            player_one.initialise()
            globals()['score_player_one'] += keep_score_one(y_player)
            textsurface = myfont.render(
                'Score is ' + str(globals()['score_player_one']), False, (255, 255, 255))
            screen.blit(textsurface, (0, 0))
            seconds_player_one = (pygame.time.get_ticks() - start_ticks) / 1000
            textsurface = myfont.render('Time ' + str(seconds_player_one),
                                        False, (255, 255, 255))
            screen.blit(textsurface, (930, 0))
            if score_player_one == 120:
                playerone = False
                done = True
                globals()['total_score_one'] += score_player_one
                globals()['time_one'] += seconds_player_one
                globals()['level_player_one'] += 1
                continue

            if first_time_ship_one:
                change_enemy_one = 1 * globals()['level_player_one']
            else:
                change_enemy_one = -1 * globals()['level_player_one']
            if enemy_one_x + change_enemy_one > 980:
                first_time_ship_one = False
            if enemy_one_x + change_enemy_one < 0:
                first_time_ship_one = True

            if first_time_ship_two:
                change_enemy_two = 1.5 * globals()['level_player_one']
            else:
                change_enemy_two = -1.5 * globals()['level_player_one']
            if enemy_two_x + change_enemy_two > 980:
                first_time_ship_two = False
            if enemy_two_x + change_enemy_two < 0:
                first_time_ship_two = True

            if first_time_ship_two_b:
                change_enemy_two_b = 1.5 * globals()['level_player_one']
            else:
                change_enemy_two_b = -1.5 * globals()['level_player_one']
            if enemy_two_x_b + change_enemy_two_b > 980:
                first_time_ship_two_b = False
            if enemy_two_x_b + change_enemy_two_b < 0:
                first_time_ship_two_b = True

            if first_time_ship_three:
                change_enemy_three = 2 * globals()['level_player_one']
            else:
                change_enemy_three = -2 * globals()['level_player_one']
            if enemy_three_x + change_enemy_three > 980:
                first_time_ship_three = False
            if enemy_three_x + change_enemy_three < 0:
                first_time_ship_three = True

            enemy_three_x += change_enemy_three
            enemy_two_x_b += change_enemy_two_b
            enemy_two_x += change_enemy_two
            enemy_one_x += change_enemy_one
            enemy_one = Enemies(ship_image, globals()['level_player_one'],
                                enemy_one_x, enemy_one_y)
            enemy_one.initialise()
            enemy_two = Enemies(kraken_image, globals()['level_player_one'],
                                enemy_two_x, enemy_two_y)
            enemy_two.initialise()
            enemy_two_b = Enemies(ship_image, globals()['level_player_one'],
                                  enemy_two_x_b, enemy_two_y_b)
            enemy_two_b.initialise()
            enemy_three = Enemies(sea_image, globals()['level_player_one'],
                                  enemy_three_x, enemy_three_y)
            enemy_three.initialise()
            enemy_four = Enemies(ship_image, globals()['level_player_one'],
                                 enemy_two_x, enemy_four_y)
            enemy_four.initialise()
            enemy_four_b = Enemies(kraken_image, globals()['level_player_one'],
                                   enemy_two_x_b, enemy_four_y_b)
            enemy_four_b.initialise()
            enemy_five = Enemies(ship_image, globals()['level_player_one'],
                                 enemy_one_x, enemy_five_y)
            enemy_five.initialise()
            pillar = []
            for i in pillar_position:
                pillar.append(
                    Enemies(
                        pillar_image,
                        globals()['level_player_one'],
                        i[0],
                        i[1]))
            for i in range(len(pillar_position)):
                pillar[i].initialise()

            if x_player < enemy_one_x + 100 and x_player > enemy_one_x - 35:
                if y_player < enemy_one_y + 70 and y_player > enemy_one_y - 30:
                    done = True
            if x_player < enemy_two_x + 100 and x_player > enemy_two_x - 35:
                if y_player < enemy_two_y + 70 and y_player > enemy_two_y - 30:
                    done = True
            if x_player < enemy_two_x_b + 100 and x_player > enemy_two_x_b - 45:
                if y_player < enemy_two_y_b + 70 and y_player > enemy_two_y_b - 30:
                    done = True
            if x_player < enemy_three_x + 100 and x_player > enemy_three_x - 35:
                if y_player < enemy_three_y + 70 and y_player > enemy_three_y - 30:
                    done = True
            if x_player < enemy_two_x + 100 and x_player > enemy_two_x - 35:
                if y_player < enemy_four_y + 70 and y_player > enemy_four_y - 30:
                    done = True
            if x_player < enemy_two_x_b + 100 and x_player > enemy_two_x_b - 35:
                if y_player < enemy_four_y_b + 70 and y_player > enemy_four_y_b - 30:
                    done = True
            if x_player < enemy_one_x + 100 and x_player > enemy_one_x - 35:
                if y_player < enemy_five_y + 70 and y_player > enemy_five_y - 30:
                    done = True

            for i in pillar_position:
                if x_player < i[0] + 40 and x_player > i[0] - 40:
                    if y_player < i[1] + 50 and y_player > i[1] - 20:
                        done = True
                        break

            pygame.display.flip()
            clock.tick(60)

        done = False
        while not done and level_player_two < 5:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    done = True
                    playerone = False
                    globals()['total_score_one'] += score_player_one
                    globals()['time_one'] += seconds_player_one
                if event.type == pygame.QUIT:
                    done = True
                    exit_kar = True
                    playerone = True
                    globals()['total_score_one'] += score_player_one
                    globals()['time_one'] += seconds_player_one
            screen.fill((0, 0, 0))
            textsurface = myfont.render(
                'Press any key to continue Deadpool', False, (255, 0, 0))
            screen.blit(textsurface, (500, 300))
            score = myfont.render('Score is ' + str(globals()['score_player_one']),
                                  False, (255, 0, 0))
            screen.blit(score, (300, 500))
            time_taken = myfont.render('Time ' + str(seconds_player_one),
                                       False, (255, 0, 0))
            screen.blit(time_taken, (700, 500))
            pygame.display.flip()
            clock.tick(60)
    else:
        done = False
        for_score = [False, False, False, False, False, False, False, False,
                     False, False, False, False, False, False]
        start_ticks = pygame.time.get_ticks()
        x_player = 500
        y_player = 0
        seconds_player_one = 0
        score_player_one = 0
        x_change_player = 0
        y_change_player = 0
        globals()['score_player_one'] = 0
        globals()['max_player_one'] = 0
        globals()['threshold_player_one'] = 0
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    exit_kar = True
                    playerone = True
                    globals()['level_player_two'] += 1
                    globals()['total_score_two'] += score_player_one
                    globals()['time_two'] += seconds_player_one
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x_change_player = -3
                    elif event.key == pygame.K_d:
                        x_change_player = 3
                    elif event.key == pygame.K_w:
                        y_change_player = -3
                    elif event.key == pygame.K_s:
                        y_change_player = 3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        x_change_player = 0
                    if event.key == pygame.K_s or event.key == pygame.K_w:
                        y_change_player = 0

            if x_player + x_change_player > 1030 or x_player + x_change_player < 0:
                pass
            else:
                x_player += x_change_player
            if y_player + y_change_player > 730 or y_player + y_change_player < 0:
                pass
            else:
                y_player += y_change_player
            spiderman_image = pygame.transform.scale(
                get_image('deadpool.png'), (50, 30))
            ship_image = pygame.transform.scale(
                get_image('ship.png'), (100, 70))
            pillar_image = pygame.transform.scale(
                get_image('pillar.png'), (50, 50))
            kraken_image = pygame.transform.scale(
                get_image('kraken.png'), (100, 70))
            sea_image = pygame.transform.scale(
                get_image('sea-monster.png'), (100, 70))
            screen.fill(blue)
            make_land()
            player_one = Player(x_player, y_player, spiderman_image)
            player_one.initialise()
            score_player_one += keep_score_two(y_player)
            if score_player_one == 115:
                score_player_one = 120
            textsurface = myfont.render('Score is ' + str(score_player_one),
                                        False, (255, 255, 255))
            screen.blit(textsurface, (0, 730))
            seconds_player_one = (pygame.time.get_ticks() - start_ticks) / 1000
            textsurface = myfont.render(
                'Time ' + str(seconds_player_one), False, (255, 255, 255))
            screen.blit(textsurface, (930, 730))
            if score_player_one == 120:
                playerone = False
                done = True
                globals()['total_score_two'] += score_player_one
                globals()['time_two'] += seconds_player_one
                globals()['level_player_two'] += 1
                continue

            if first_time_ship_one:
                change_enemy_one = 1 * globals()['level_player_two']
            else:
                change_enemy_one = -1 * globals()['level_player_two']
            if enemy_one_x + change_enemy_one > 980:
                first_time_ship_one = False
            if enemy_one_x + change_enemy_one < 0:
                first_time_ship_one = True

            if first_time_ship_two:
                change_enemy_two = 1.5 * globals()['level_player_two']
            else:
                change_enemy_two = -1.5 * globals()['level_player_two']
            if enemy_two_x + change_enemy_two > 980:
                first_time_ship_two = False
            if enemy_two_x + change_enemy_two < 0:
                first_time_ship_two = True

            if first_time_ship_two_b:
                change_enemy_two_b = 1.5 * globals()['level_player_two']
            else:
                change_enemy_two_b = -1.5 * globals()['level_player_two']
            if enemy_two_x_b + change_enemy_two_b > 980:
                first_time_ship_two_b = False
            if enemy_two_x_b + change_enemy_two_b < 0:
                first_time_ship_two_b = True

            if first_time_ship_three:
                change_enemy_three = 2 * globals()['level_player_two']
            else:
                change_enemy_three = -2 * globals()['level_player_two']
            if enemy_three_x + change_enemy_three > 980:
                first_time_ship_three = False
            if enemy_three_x + change_enemy_three < 0:
                first_time_ship_three = True

            enemy_three_x += change_enemy_three
            enemy_two_x_b += change_enemy_two_b
            enemy_two_x += change_enemy_two
            enemy_one_x += change_enemy_one
            enemy_one = Enemies(ship_image, globals()['level_player_two'],
                                enemy_one_x, enemy_one_y)
            enemy_one.initialise()
            enemy_two = Enemies(kraken_image, globals()['level_player_two'],
                                enemy_two_x, enemy_two_y)
            enemy_two.initialise()
            enemy_two_b = Enemies(ship_image, globals()['level_player_two'],
                                  enemy_two_x_b, enemy_two_y_b)
            enemy_two_b.initialise()
            enemy_three = Enemies(sea_image, globals()['level_player_two'],
                                  enemy_three_x, enemy_three_y)
            enemy_three.initialise()
            enemy_four = Enemies(ship_image, globals()['level_player_two'],
                                 enemy_two_x, enemy_four_y)
            enemy_four.initialise()
            enemy_four_b = Enemies(kraken_image, globals()['level_player_two'],
                                   enemy_two_x_b, enemy_four_y_b)
            enemy_four_b.initialise()
            enemy_five = Enemies(ship_image, globals()['level_player_two'],
                                 enemy_one_x, enemy_five_y)
            enemy_five.initialise()
            pillar = []
            for i in pillar_position:
                pillar.append(
                    Enemies(
                        pillar_image,
                        globals()['level_player_two'],
                        i[0],
                        i[1]))
            for i in range(len(pillar_position)):
                pillar[i].initialise()

            if x_player < enemy_one_x + 100 and x_player > enemy_one_x - 35:
                if y_player < enemy_one_y + 70 and y_player > enemy_one_y - 30:
                    done = True
            if x_player < enemy_two_x + 100 and x_player > enemy_two_x - 35:
                if y_player < enemy_two_y + 70 and y_player > enemy_two_y - 30:
                    done = True
            if x_player < enemy_two_x_b + 100 and x_player > enemy_two_x_b - 45:
                if y_player < enemy_two_y_b + 70 and y_player > enemy_two_y_b - 30:
                    done = True
            if x_player < enemy_three_x + 100 and x_player > enemy_three_x - 35:
                if y_player < enemy_three_y + 70 and y_player > enemy_three_y - 30:
                    done = True
            if x_player < enemy_two_x + 100 and x_player > enemy_two_x - 35:
                if y_player < enemy_four_y + 70 and y_player > enemy_four_y - 30:
                    done = True
            if x_player < enemy_two_x_b + 100 and x_player > enemy_two_x_b - 35:
                if y_player < enemy_four_y_b + 70 and y_player > enemy_four_y_b - 30:
                    done = True
            if x_player < enemy_one_x + 100 and x_player > enemy_one_x - 35:
                if y_player < enemy_five_y + 70 and y_player > enemy_five_y - 30:
                    done = True

            for i in pillar_position:
                if x_player < i[0] + 40 and x_player > i[0] - 40:
                    if y_player < i[1] + 50 and y_player > i[1] - 20:
                        done = True
                        break

            pygame.display.flip()
            clock.tick(60)

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    done = True
                    playerone = True
                    globals()['total_score_two'] += score_player_one
                    globals()['time_two'] += seconds_player_one
                if event.type == pygame.QUIT:
                    done = True
                    exit_kar = True
                    playerone = True
                    globals()['total_score_two'] += score_player_one
                    globals()['time_two'] += seconds_player_one
            screen.fill((0, 0, 0))
            textsurface = myfont.render('Press any key to continue Spiderman',
                                        False, (255, 0, 0))
            screen.blit(textsurface, (500, 300))
            score = myfont.render('Score is ' + str(score_player_one),
                                  False, (255, 0, 0))
            screen.blit(score, (300, 500))
            time_taken = myfont.render('Time ' + str(seconds_player_one),
                                       False, (255, 0, 0))
            screen.blit(time_taken, (700, 500))
            pygame.display.flip()
            clock.tick(60)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            exit_kar = True
            exit(0)
    screen.fill((0, 0, 0))
    if total_score_one > total_score_two:
        textsurface = myfont.render('SPIDERMAN WINS',
                                    False, (255, 0, 0))
        screen.blit(textsurface, (500, 50))
    elif total_score_two > total_score_one:
        textsurface = myfont.render('DEADPOOL WINS',
                                    False, (255, 0, 0))
        screen.blit(textsurface, (500, 50))
    else:
        if time_one > time_two:
            textsurface = myfont.render('SPIDERMAN WINS',
                                        False, (255, 0, 0))
            screen.blit(textsurface, (500, 50))
        elif time_two > time_one:
            textsurface = myfont.render('DEADPOOL WINS',
                                        False, (255, 0, 0))
            screen.blit(textsurface, (500, 50))
    textsurface = myfont.render('Final Score Deadpool',
                                False, (255, 0, 0))
    screen.blit(textsurface, (500, 400))
    score = myfont.render('Score is ' + str(globals()['total_score_two']),
                          False, (255, 0, 0))
    screen.blit(score, (300, 500))
    time_taken = myfont.render('Time ' + str(globals()['time_two']),
                               False, (255, 0, 0))
    screen.blit(time_taken, (700, 500))
    textsurface = myfont.render('Final Score Spiderman',
                                False, (255, 0, 0))
    screen.blit(textsurface, (500, 100))
    score = myfont.render('Score is ' + str(globals()['total_score_one']),
                          False, (255, 0, 0))
    screen.blit(score, (300, 200))
    time_taken = myfont.render('Time ' + str(globals()['time_one']),
                               False, (255, 0, 0))
    screen.blit(time_taken, (700, 200))
    pygame.display.flip()
    clock.tick(60)
