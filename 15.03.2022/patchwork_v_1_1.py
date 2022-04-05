import pygame
import sys
import numpy as np
import os

# from all_tiles import ALL_TILES

from collections import Counter

from random import choice



ALL_TILES = {
    'tile_1': {
        'size': np.array([[False,True,False], [True,True,True], [False,True,False]]),
        'price': 5,
        'time': 4
    },
    'tile_2': {
        'size': np.array([[True,True,False], [False,True,True]]),
        'price': 3,
        'time': 2
    },
    'tile_3': {
        'size': np.array([[False,True,True], [True,True,True], [True,False,False]]),
        'price': 8,
        'time': 6
    },
    'tile_4': {
        'size': np.array([[True,True,True,True], [False,False,True,True]]),
        'price': 10,
        'time': 5
    },
    'tile_5': {
        'size': np.array([[True,True,True], [False,True,False], [True,True,True]]),
        'price': 2,
        'time': 3
    },
    'tile_6': {
        'size': np.array([[False,False,True,False,False], [True,True,True,True,True], [False,False,True,False,False]]),
        'price': True,
        'time': 4
    },
    'tile_7': {
        'size': np.array([[False,True,True], [False,True,False], [False,True,False], [True,True,False]]),
        'price': True,
        'time': 2
    },
    'tile_8': {
        'size': np.array([[True,True], [True,False]]),
        'price': 3,
        'time': True
    },
    'tile_9': {
        'size': np.array([[True,True,True,True]]),
        'price': 3,
        'time': 3
    },
    'tile_TrueFalse': {
        'size': np.array([[True,True,True], [True,False,True]]),
        'price': True,
        'time': 2
    },
    'tile_True': {
        'size': np.array([[True,True,True,True], [False,False,True,False]]),
        'price': 3,
        'time': 4
    },
    'tile_True2': {
        'size': np.array([[True,True], [True,True]]),
        'price': 6,
        'time': 5
    }

}


# os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

WIDTH, HEIGHT = 800, 700
# size = (1920, 1080)

infoObject = pygame.display.Info()
# print(infoObject)
# pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

size = (infoObject.current_w, infoObject.current_h)

# screen = pygame.display.set_mode(size)
# screen = pygame.display.set_mode(size, pygame.RESIZABLE)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
# screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
# pygame.FULLSCREEN
pygame.display.set_caption("Game")
width = height = 40
margin = 10
red = (255, 0, 0)
white = (255, 255, 255)
pink = (255, 162, 147)
grey = (205, 205, 205)
green = (0, 125, 0)
WHITE = (255, 255, 255)

center_const = 50

start_x1 = size[0]/2 - center_const - 9*width - (9+1)*margin
start_y1 = 125

start_x2 = size[0]/2 + center_const
start_y2 = start_y1

# полЯ
mas = [[False]*9 for i in range(9)]

# для первого
field_1 = mas  # видимое
field_imaginary_1 = mas  # мнимое поле, для выделения куда ставиться тайл

# для второго
field_2 = mas  # видимое
field_imaginary_2 = mas  # мнимое поле, для выделения куда ставиться тайл


pygame.draw.line(screen, WHITE, [size[0]/2, 0], [size[0]/2, size[1]])
pygame.draw.line(screen, WHITE, [size[0]/2-50, 0], [size[0]/2-50, size[1]])
pygame.draw.line(screen, WHITE, [size[0]/2+50, 0], [size[0]/2+50, size[1]])



score_1 = 0
score_2 = 0



class Tile:
    def __init__(self, price, time, shape):
        self.price = price
        self.time = time
        self.shape = shape

    def get_all_configuration(self):
        mas = []
        for i in range(0, 4):
            mas.append(np.rot90(self.shape, k=i, axes=(0, 1)))

        f = np.flip(self.shape, axis=1)

        for i in range(0, 4):
            mas.append(np.rot90(f, k=i, axes=(0, 1)))

        return mas
    # numpy.rot90(self.shape, k = 1, axes = (0, 1))
    def get_tile_length_and_width(self):
        return self.shape.shape()



piece = ALL_TILES['tile_4']['size']
price = ALL_TILES['tile_4']['price']



all_configuration = Tile(1, 4, piece).get_all_configuration()

# отрисовка поля для первого игрока
for row in range(9):
    for col in range(9):
        if field_1[row][col] == True:
            color = red
        else:
            color = grey
        x = start_x1 + col * width + margin * (col + 1)
        y = start_y1 + row * height + margin * (row + 1)
        pygame.draw.rect(screen, color, (x, y, width, height))

# отрисовка поля для второго
for row in range(9):
    for col in range(9):
        if field_2[row][col] == True:
            color = red
        else:
            color = grey
        x = start_x2 + col * width + margin * (col + 1)
        y = start_y2 + row * height + margin * (row + 1)
        pygame.draw.rect(screen, color, (x, y, width, height))


pygame.display.update()
# pygame.display.flip()

# последняя клетка первого игрока
colum_1 = -1 # это нужно для первой проверки на изменение координат КЛЕТКИ
string_1 = -1

# последняя клетка второго игрока
colum_2 = -1 # это нужно для первой проверки на изменение координат КЛЕТКИ
string_2 = -1

person = 1

number_configuration = 0



human1 = {
    "person": 1,
    "field": field_1,
    "start_x": start_x1,
    "start_y": start_y1,
    "field_imaginary": field_imaginary_1,
    "colum": colum_1,
    "string": string_1
}


human2 = {
    "person": 2,
    "field": field_2,
    "start_x": start_x2,
    "start_y": start_y2,
    "field_imaginary": field_imaginary_2,
    "colum": colum_2,
    "string": string_2
}

def player_actions(human):
    print("запуск новой функции")

    global person

    global piece

    global number_configuration
    global all_configuration


    start_x = human["start_x"]
    start_y = human["start_y"]

    field = human["field"]
    field_imaginary = human["field_imaginary"]

    colum = human["colum"]
    string = human["string"]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEMOTION:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            # print(f'x={x_mouse}, y={y_mouse}')
            # print(f'colum!!!!!={colum}, row!!!!!!!={string}')

            # проверка на изменение координат КЛЕТКИ
            if ((x_mouse - start_x) // (margin + width)) == colum and ((y_mouse - start_y) // (margin + height)) == string:
                return
            colum = int( (x_mouse - start_x) // (margin + width) )   # ряд
            string = int((y_mouse - start_y) // (margin + height) )  # строка

            if colum < 0 or string < 0:
                print('переведите курсор на своё поле')
                return

            print(f'colum={colum}, row={string}')

            # # внутреннее обновление последней клетки
            # if person == 1:
            #   colum_1 = colum
            #   string_1 = string
            # else:
            #   colum_2 = colum
            #   string_2 = string

            # FIELD[row][colum] = True
            zero_array = np.zeros((9, 9), bool)

            # l_, w_ = 0, 0
            # w_, l_ = np.shape(piece_local)
            # print("string =" + str(string))
            # print("colum =" + str(colum))

            # print(w_, l_)
            # zero_array[string:string + l_, colum:colum + w_] = piece_local

            try:
                l_, w_ = 0, 0

                l_, w_ = np.shape(piece)
                # print(l_, w_)

                zero_array[string:string + l_, colum:colum + w_] = piece

            except BaseException as exception:
                return

            summa = np.invert(zero_array & field)
            if False in summa:
                print('ошибка')
            else:
                # field = np.logical_or(zero_array, field)
                field_imaginary = zero_array
            # FIELD[row:row + 3, colum:colum + 3] = piece
            # print(FIELD1)
            # print(f'colum={colum}, row={string}')

            # отрисовка действительного
            for row in range(9):
                for col in range(9):
                    if field[row][col] == True:
                        color = red
                    else:
                        color = grey
                    x = start_x + col * width + margin * (col + 1)
                    y = start_y + row * height + margin * (row + 1)
                    pygame.draw.rect(screen, color, (x, y, width, height))
            pygame.display.update()

            # отрисовка мнимого
            for row in range(9):
                for col in range(9):
                    if field_imaginary[row][col] == True:
                        x = start_x + col * width + margin * (col + 1)
                        y = start_y + row * height + margin * (row + 1)
                        color = pink
                        pygame.draw.rect(screen, color, (x, y, width, height))

            pygame.display.update()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            # print(f'x={x_mouse}, y={y_mouse}')

            if person == 1:
                if x_mouse<start_x or x_mouse>size[0]/2-center_const or y_mouse<start_y or y_mouse>start_y+9*width+10*margin:
                    print("игрок 1 - курсор не на вашем поле")
                    return
            elif person == 2:
                if x_mouse>start_x+9*width+10*margin or x_mouse<size[0]/2+center_const or y_mouse<start_y or y_mouse>start_y+9*width+10*margin:
                    print("игрок 2 - курсор не на вашем поле")
                    return


            colum = int( (x_mouse - start_x) // (margin + width) )  # ряд
            row = int( (y_mouse - start_y) // (margin + height) )  # строка

            zero_array = np.zeros((9, 9), bool)

            try:
                l_, w_ = 0, 0

                l_, w_ = np.shape(piece)
                # print(l_, w_)

                zero_array[string:string + l_, colum:colum + w_] = piece

            except BaseException as exception:
                return

            # l_, w_ = np.shape(piece_local)
            # zero_array[row:row + l_, colum:colum + w_] = piece_local

            summa = np.invert(zero_array & field)
            if False in summa:
                print('ошибка')
                return
            else:
                field = np.logical_or(zero_array, field)

            # print(f'colum={colum}, row={row}')

            for row in range(9):
                for col in range(9):
                    if field[row][col] == True:
                        color = red
                    else:
                        color = grey
                    x = start_x + col * width + margin * (col + 1)
                    y = start_y + row * height + margin * (row + 1)
                    pygame.draw.rect(screen, color, (x, y, width, height))
            pygame.display.update()


            # внутренне обновление поля
            human["field"] = field
            human["field_imaginary"] = field_imaginary


            # ход передаётся другому игроку
            print("передача хода")
            name_random_tile = choice(list(ALL_TILES.keys())) 
            piece = ALL_TILES[name_random_tile]['size']
            # price = ALL_TILES[name_random_tile]['price']
            # time = ALL_TILES[name_random_tile]['time']

            score_1 = np.isclose(field_1, True).sum()
            score_2 = np.isclose(field_2, True).sum()

            print(score_1)
            print(score_2)

            if person == 1:
                person = 2
                return
            else:
                person = 1
                return


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit(0)

            elif event.key == pygame.K_RIGHT:
                if number_configuration == 0:
                    all_configuration = Tile(1, 4, piece).get_all_configuration()
                number_configuration += 1
                piece = all_configuration[number_configuration%8]
                print(piece)

                print("поворот")

                zero_array = np.zeros((9, 9), bool)

                # l_, w_ = 0, 0
                # w_, l_ = np.shape(piece_local)
                # print("string =" + str(string))
                # print("colum =" + str(colum))

                # print(w_, l_)
                # zero_array[string:string + l_, colum:colum + w_] = piece_local

                try:
                    l_, w_ = 0, 0

                    l_, w_ = np.shape(piece)
                    # print(l_, w_)

                    zero_array[string:string + l_, colum:colum + w_] = piece

                except BaseException as exception:
                    return

                summa = np.invert(zero_array & field)
                if False in summa:
                    print('ошибка')
                else:
                    # field = np.logical_or(zero_array, field)
                    field_imaginary = zero_array
                # FIELD[row:row + 3, colum:colum + 3] = piece
                # print(FIELD1)
                # print(f'colum={colum}, row={string}')

                # отрисовка действительного
                for row in range(9):
                    for col in range(9):
                        if field[row][col] == True:
                            color = red
                        else:
                            color = grey
                        x = start_x + col * width + margin * (col + 1)
                        y = start_y + row * height + margin * (row + 1)
                        pygame.draw.rect(screen, color, (x, y, width, height))
                pygame.display.update()

                # отрисовка мнимого
                for row in range(9):
                    for col in range(9):
                        if field_imaginary[row][col] == True:
                            x = start_x + col * width + margin * (col + 1)
                            y = start_y + row * height + margin * (row + 1)
                            color = pink
                            pygame.draw.rect(screen, color, (x, y, width, height))

                pygame.display.update()


        # внутреннее обновление последней клетки
        
        human["colum"] = colum
        human["string"] = string


while True:
    if person == 1:
        player_actions(human1)
    else:
        player_actions(human2)

