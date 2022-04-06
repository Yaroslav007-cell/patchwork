import pygame
import sys
import numpy as np
import os

# from all_tiles import ALL_TILES

from collections import Counter

from random import choice

all_price = 0

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
print(infoObject)
# pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

# w = 1920, h = 1080 
size = (infoObject.current_w, infoObject.current_h)
# print("w = " + str(infoObject.current_w))
# print("h = " + str(infoObject.current_h))
    


# screen = pygame.display.set_mode(size)
# screen = pygame.display.set_mode(size, pygame.RESIZABLE)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
# screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
# pygame.FULLSCREEN
pygame.display.set_caption("Game")

side = int( 40/1980 * infoObject.current_w )  # сторона квадратика
side_enlarged = int( 50/1980 * infoObject.current_w )
margin = int( 1/4 * side )
margin_enlarged = int( 1/4 * side_enlarged )

# print(side)
# print(side_enlarged)
# print(side)
# print(margin)

# field_size = 9*side + 10*margin
field_size = 9*side + (9+1)*margin
field_size_enlarged = 9*side_enlarged + (9+1)*margin_enlarged

# print(field_size)

# field_size_1 = 9*round(side) + 10*round(margin)

# print(9*round(side) + 10*round(margin))

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 125, 0)
WHITE = (255, 255, 255)
pink = (255, 162, 147)
grey = (205, 205, 205)
grey = grey_dark = (136, 136, 136)
grey_bright = (185, 185, 185)

colors_tile = {
    "red": (255, 0, 0),
    "green": (45, 150, 49),
    "fiol": (83, 61, 161),
    "blue": (35, 35, 250),
    "pink": (201, 22, 88),
    "orange": (201, 114, 22),
    "yellow": (193, 232, 19),
    "turquoise": (58, 204, 207)
}


center_const = int( 50/1980*size[0] )
center_const = 50


middle_x = int( size[0]/2 )
middle_y = int( size[1]/2 )


start_middle_x1 = int( middle_x - 0.45 * middle_x )
start_middle_y1 = int( 0.4 * size[1] )

start_middle_x2 = int( middle_x + 0.45 * middle_x )
start_middle_y2 = int( 0.4 * size[1] )



start_x1 = int( start_middle_x1 - field_size/2 )
start_y1 = int( start_middle_y1 - field_size/2 )
start_x1_enlaged = int( start_middle_x1 - field_size_enlarged/2 )
start_y1_enlaged = int( start_middle_y1 - field_size_enlarged/2 )

start_x2 = int( start_middle_x2 - field_size/2 )
start_y2 = int( start_middle_y2 - field_size/2 )
start_x2_enlaged = int( start_middle_x2 - field_size_enlarged/2 )
start_y2_enlaged = int( start_middle_y2 - field_size_enlarged/2 )



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

# Colors:
random_color_tile = choice(list(colors_tile.keys()))
random_color = colors_tile[random_color_tile]


# color_sq_a = random_color   # квадратик главного (более яркий)
# color_sq_b = red            # квадратик
# color_fi_a = grey_bright    # поле главного (более яркое)
# color_fi_b = grey           # поле
# # background_color = black
# # imaginary_color = pink

colors_scheme = {
    "Random color" : {
        "color_sq_a" : random_color,
        "color_sq_b" : red,
        "color_fi_a" : grey_bright,
        "color_fi_b" : grey,
        "background_color" : black,
        "imaginary_color" : pink
    },
    "Dark theme" : {
        "color_sq_a" : (49, 155, 141),
        "color_sq_b" : (34, 70, 70),
        "color_fi_a" : (144, 144, 144),
        "color_fi_b" : (107, 107, 107),
        "background_color" : black,
        "imaginary_color" : (155, 209, 211)
    }
}

name_color_scheme = "Dark theme"

color_sq_a = colors_scheme[name_color_scheme]["color_sq_a"]
color_sq_b = colors_scheme[name_color_scheme]["color_sq_b"]
color_fi_a = colors_scheme[name_color_scheme]["color_fi_a"]
color_fi_b = colors_scheme[name_color_scheme]["color_fi_b"]

imaginary_color = colors_scheme[name_color_scheme]["imaginary_color"]


# version: big or small
# def draw_dey(field, version):
def draw_dey(field, start_x, start_y, color_square=red, color_field=grey, side=side, margin=margin):
    # pygame.draw.rect(screen, colors_tile["blue"], (start_x, start_y, field_size, field_size))
    # side = dimensions["side"]
    # margin = dimensions["margin"]
    for row in range(9):
        for col in range(9):
            if field[row][col] == True:
                color = color_square
            else:
                color = color_field
            x = start_x + col * side + margin * (col + 1)
            y = start_y + row * side + margin * (row + 1)
            pygame.draw.rect(screen, color, (x, y, side, side))
    pygame.display.update()

def draw_mnim(field_imaginary, start_x, start_y, side=side, margin=margin, imaginary_color=pink):
    # side = dimensions["side"]
    # margin = dimensions["margin"]
    for row in range(9):
        for col in range(9):
            if field_imaginary[row][col] == True:
                x = start_x + col * side + margin * (col + 1)
                y = start_y + row * side + margin * (row + 1)
                color = imaginary_color
                pygame.draw.rect(screen, color, (x, y, side, side))
    pygame.display.update()


# отрисовка поля для первого игрока
draw_dey(field_1, start_x1_enlaged, start_y1_enlaged, color_square=color_sq_a, color_field=color_fi_a, side=side_enlarged, margin=margin_enlarged)

# отрисовка поля для второго
draw_dey(field_2, start_x2, start_y2, color_square=color_sq_b, color_field=color_fi_b)

pygame.display.update()
# pygame.display.flip()


# последняя клетка первого и второго игрока
colum_1, string_1, colum_2, string_2 = -1, -1, -1, -1
# это нужно для первой проверки на изменение координат КЛЕТКИ

person = 1

number_configuration = 0


human1 = {
    "person": 1,
    "field": field_1,
    "start_x": start_x1,
    "start_y": start_y1,
    "start_x_enlaged": start_x1_enlaged,
    "start_y_enlaged": start_y1_enlaged,
    "field_imaginary": field_imaginary_1,
    "colum": colum_1,
    "string": string_1
}

human2 = {
    "person": 2,
    "field": field_2,
    "start_x": start_x2,
    "start_y": start_y2,
    "start_x_enlaged": start_x2_enlaged,
    "start_y_enlaged": start_y2_enlaged,
    "field_imaginary": field_imaginary_2,
    "colum": colum_2,
    "string": string_2
}



def player_actions(human):
    # print("запуск новой функции")

    global person

    global piece

    global random_color

    global number_configuration
    global all_configuration

    if person==1:
        start_x = start_x1_enlaged
        start_y = start_y1_enlaged

    else:
        start_x = start_x2_enlaged
        start_y = start_y2_enlaged


    # if person==1:
    #     start_x_enlaged = start_x1_enlaged
    #     start_y_enlaged = start_y1_enlaged
    #     start_x = start_x2
    #     start_y = start_y2
    # else:
    #     start_x_enlaged = start_x2_enlaged
    #     start_y_enlaged = start_y2_enlaged
    #     start_x = start_x1
    #     start_y = start_y1
    # start_x = human["start_x"]
    # start_y = human["start_y"]
    # start_x_enlaged = human[]

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
            if ((x_mouse - start_x) // (margin_enlarged + side_enlarged)) == colum and ((y_mouse - start_y) // (margin_enlarged + side_enlarged)) == string:
                # return
                continue
            colum = int( (x_mouse - start_x) // (margin_enlarged + side_enlarged) )   # ряд
            string = int((y_mouse - start_y) // (margin_enlarged + side_enlarged) )  # строка

            if colum < 0 or string < 0:
                # print('переведите курсор на своё поле')
                # return
                continue


            # print(f'colum={colum}, row={string}')

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
                # return
                continue

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
            draw_dey(field, start_x, start_y,  color_field=color_fi_a, color_square=color_sq_a, side=side_enlarged, margin=margin_enlarged)

            # отрисовка мнимого
            draw_mnim(field_imaginary, start_x, start_y, side=side_enlarged, margin=margin_enlarged, imaginary_color=imaginary_color)


        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            # print(f'x={x_mouse}, y={y_mouse}')

            if person == 1:
                if x_mouse<start_x or x_mouse>size[0]/2-center_const or y_mouse<start_y or y_mouse>start_y+9*side_enlarged+10*margin_enlarged:
                    print("игрок 1 - курсор не на вашем поле")
                    # return
                    continue

            elif person == 2:
                if x_mouse>start_x+9*side_enlarged+10*margin_enlarged or x_mouse<size[0]/2+center_const or y_mouse<start_y or y_mouse>start_y+9*side_enlarged+10*margin_enlarged:
                    print("игрок 2 - курсор не на вашем поле")
                    # return
                    continue

            colum = int( (x_mouse - start_x) // (margin_enlarged + side_enlarged) )  # ряд
            row = int( (y_mouse - start_y) // (margin_enlarged + side_enlarged) )  # строка

            zero_array = np.zeros((9, 9), bool)

            try:
                l_, w_ = 0, 0

                l_, w_ = np.shape(piece)
                # print(l_, w_)

                zero_array[string:string + l_, colum:colum + w_] = piece

            except BaseException as exception:
                # return
                continue

            # l_, w_ = np.shape(piece_local)
            # zero_array[row:row + l_, colum:colum + w_] = piece_local

            summa = np.invert(zero_array & field)
            if False in summa:
                print('ошибка')
                # return
                continue

            else:
                field = np.logical_or(zero_array, field)

            # print(f'colum={colum}, row={row}')

            # отрисовка только действительного
            draw_dey(field, start_x, start_y, color_square=color_sq_a, color_field=color_fi_a, side=side_enlarged, margin=margin_enlarged)


            # внутренне обновление поля
            human["field"] = field
            human["field_imaginary"] = field_imaginary


            # ход передаётся другому игроку
            print("передача хода")
            name_random_tile = choice(list(ALL_TILES.keys())) 
            piece = ALL_TILES[name_random_tile]['size']
            all_configuration = Tile(1, 4, piece).get_all_configuration()
            # price = ALL_TILES[name_random_tile]['price']
            # time = ALL_TILES[name_random_tile]['time']
            # all_price _+= price

            score_1 = np.isclose(field_1, True).sum()
            score_2 = np.isclose(field_2, True).sum()

            print("score_1 = " + str(score_1))
            print("score_2 = " + str(score_2))

            # razmer_polya = 9*side_enlarged+(9+1)*margin_enlarged
            if person == 1:
                person = 2
                # для первого
                pygame.draw.rect(screen, black, (start_x, start_y, field_size_enlarged, field_size_enlarged))
                draw_dey(human1["field"], start_x1, start_y1, color_field=color_fi_b, color_square=color_sq_b)
                # для второго
                pygame.draw.rect(screen, black, (start_x2, start_y2, field_size, field_size))
                draw_dey(human2["field"], start_x2_enlaged, start_y2_enlaged, color_field=color_fi_a, color_square=color_sq_a, side=side_enlarged, margin=margin_enlarged)

            else:
                person = 1
                # для второго
                pygame.draw.rect(screen, black, (start_x, start_y, field_size_enlarged, field_size_enlarged))
                draw_dey(human2["field"], start_x2, start_y2, color_field=color_fi_b, color_square=color_sq_b)
                # для первого
                pygame.draw.rect(screen, black, (start_x1, start_y1, field_size, field_size))
                draw_dey(human1["field"], start_x1_enlaged, start_y1_enlaged, color_field=color_fi_a, color_square=color_sq_a, side=side_enlarged, margin=margin_enlarged)


            random_color_tile = choice(list(colors_tile.keys()))
            random_color = colors_tile[random_color_tile]

            # return
            continue




        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit(0)

            elif event.key == pygame.K_RIGHT:
                if number_configuration == 0:
                    all_configuration = Tile(1, 4, piece).get_all_configuration()
                number_configuration += 1
                piece = all_configuration[number_configuration%8]
                # print(piece)

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
                    # return
                    continue

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
                draw_dey(field, start_x, start_y, color_field=color_fi_a, color_square=color_sq_a, margin=margin_enlarged, side=side_enlarged)

                # отрисовка мнимого
                draw_mnim(field_imaginary, start_x, start_y, imaginary_color=imaginary_color, margin=margin_enlarged, side=side_enlarged)


        # внутреннее обновление последней клетки
        human["colum"] = colum
        human["string"] = string


while True:
    if person == 1:
        player_actions(human1)
        # print("остановка функции")
    else:
        player_actions(human2)
        # print("остановка функции")

