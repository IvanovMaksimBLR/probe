#цель: отработка навыков работы с классами
#семья собирает на новую квартру
#немного топорный вариант)
#требуются доработки в:
#указать кто на какую работу ходит
#кто каким спортом занимается
# доработать выгул питомца
#
#

from random import randint

from termcolor import cprint


class Family:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.train = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сыт на  {}, физическая форма на {} '.format(
            self.name, self.fullness, self.train)

    def shopping(self):
        if self.house.food <= 20:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 100
            self.house.food += 100
            # self.fullness -= 2


    # приготовили еды из продуктов
    def cooking(self):
        if self.house.dish <= 50:
            cprint('{} приготовил вкуснейшей еды'.format(self.name), color='yellow')
            self.house.dish += 100
            self.house.food -= 100
            # self.fullness -= 5

    # поели готовой еды
    def eat(self):
        if self.house.dish >= 20:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
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
        self.house.dish -= 5
        self.train -= 10

    # уборка квартиры
    def cleaning(self):
        cprint('{} убрал в квартире'.format(self.name), color='blue')
        self.house.clean += 100
        # self.fullness -= 5

    # выгуливать питомца. (доработать логику)
    def walking(self):
        cprint('{} выгулял чихуяшку'.format(self.name), color='green')
        self.fullness -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    # переработать логику действий.
    def act(self):
        if self.train <= 10:
            cprint('{} пора заняться собой...'.format(self.name), color='red')
            return

        if self.fullness < 10:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.train <= 100:
            self.training()
        elif self.house.dish <= 10:
            self.cooking()
        elif self.house.clean <= 0:
            self.cleaning()



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

#решить проблему "накопления" дней + накопления денег
# счетчик циклов?
day = 1
while rent_house.money <= 1500000:

    print('==============начался новый день №', day, '===================')
    day += 1
    for citisen in residents:
        citisen.act()
        citisen.work()
        citisen.eat()
        citisen.walking()  #придумать как выгуливать по очереди или когда нужно
    print('--- в конце дня ---')
    for citisen in residents:
        print(citisen)
    print(rent_house)

years = round(day / 365, 2)
cprint('Собрали на квартиру! понадобилось {} лет'.format(years), color='cyan')
cprint('ура! своя квартира!!!', color='cyan')
