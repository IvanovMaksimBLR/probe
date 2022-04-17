# задачи: создать класс семья(Jon, Kat), создать класс домашний питомец (Cihua)
# откладывать зп в конце
# месяца на покупку квартиры( цикл дней должен закнчится когда будет собранна нужнная сумма)


from random import randint

from termcolor import cprint


class Family:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.train = 0
        self.house = None

    def __str__(self):
        return 'Я - {}, сыт на  {}, физическая форма на '.format(
            self.name, self.fullness, self.train)

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    # приготовили еды из продуктов
    def cooking(self):
        if self.house.dish <= 10:
            cprint('{} приготовил вкуснейшей еды'.format(self.name), color='yellow')
            self.house.dish += 50
            self.house.food -= 50

    # поели готовой еды
    def eat(self):
        if self.house.dish >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.dish -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    # придумать как распредлить тренировки в зависимости от того кто тренируется

    def training(self):
        cprint('{} сходил на тренировку'.format(self.name), color='blue')
        self.train += 50
        self.fullness -= 10

    # каждый ходит на конкретно свою работу(разработчик, айчар)
    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 250
        self.fullness -= 10

    # уборка квартиры
    def cleaning(self):
        cprint('{} убрал в квартире'.format(self.name), color='blue')
        self.house.clean += 10

    # выгуливать питомца. (доработать логику)
    def walking(self):
        cprint('{} выгулял чихуяшку'.format(self.name), color='green')
        self.fullness -= 3

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    # переработать логику действия.
    def act(self):
        if self.fullness <= 0:
            cprint('{} охренел...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
#        elif self.house.money < 50:
#           self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()



class House:

    def __init__(self):
        self.food = 100
        self.money = 100
        self.clean = 100
        self.dish = 100

    def __str__(self):
        return 'В доме осталось продуктов {}, сумма денег {}, чистота квартиры {}, готовой еды {}'.format(
            self.food, self.money, self.clean, self.dish, self.dish)


residents = [
    Family(name='Joe'),
    Family(name='Kat'),
]

# изменить цель. тут должен быть заезд на съеммную квартиру.
rent_house = House()
for citisen in residents:
    citisen.go_to_the_house(house=rent_house)
# в этом блоке изменить цель. while количество денег на новую квартиру. прервать цикл. указать сколько понадобилось
# дней.
#решить проблему "накопления" дней + накопления денег
cash = House.self.money()
while cash < 41000:
    print('================ день {} ==================')
    for citisen in residents:
        citisen.act()
        citisen.work()
    print('------------ в конце дня -------------')
    for citisen in residents:
        print(citisen)
    print(rent_house)
