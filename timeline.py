import random
import copy


# Создаем ветку времени
timeline = [0]*30
buttons = [random.randint(1, 28) for _ in range(5)]
for idx_of_button in buttons:
    timeline[idx_of_button] = 1

first_place = 0
second_place = 0
number_of_buttons_at_the_beginning = 10


players_buttons = [max(first_place, second_place)]+[number_of_buttons_at_the_beginning]*2

class TimeLine:
    def __init__(self, player, price, time, first_place, second_place):
        self.player = player
        self.price = price
        self.time = time
        self.first_place = first_place
        self.second_place = second_place

    def move(self):
        if self.player == 1:
            self.first_place += self.time
            if self.second_place < self.first_place:
                self.player = 2
        if self.player == 2:
            self.second_place += self.time
            if self.second_place > self.first_place:
                self.player = 1

    def spent_buttons_for_tile(self):
        players_buttons[self.player] -= price
        players_buttons[self.player] += time
        if players_buttons[self.player] < 0:
            print(f"player {len(players_buttons)-self.player} wins")

    def get_score_of_player(self):
        return players_buttons[self.player]

    def end_the_game(self):
        if self.first_place > len(timeline) or self.second_place > len(timeline):
            return False
        return True


while is_it_end:
    if player == 1:
        T = TimeLine(player, price, time, first_place, second_place)


