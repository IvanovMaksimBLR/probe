# на курсах дали задание нарисовать блок схему похода в магазин. И я решил в очередной раз попрактиковаться в ООП)
class Shop:
    def __init__(self):
        self.milk = 3
        self.bread = 2
        self.tea = 0
    def __str__(self):
        return 'В магазине осталось молока: {} ,хлеба {},чая {} упаковку '.format(
            self.milk, self.bread, self.tea)

class Man:
    def __init__(self):
        # self.name = 'joe'
        self.milk = 0
        self.bread = 0
        self.tea = 0
        self.shop = None

    def __str__(self):
        return 'Я взял -молока {} пакет,хлеба {} буханку,чая {} упаковку '.format(
            self.milk, self.bread, self.tea)
    def bmilk(self):

            if self.shop.milk >= 1:
                print('Сходил в магазин за молоком')
                self.milk += 1
                self.shop.milk -= 1
            else:
                print('молока нет')


    def bbread(self):

        if self.shop.bread >= 1:
            print('Сходил в магазин за хлебом')
            self.bread += 1
            self.shop.bread -= 1
        else:
            print('нет хлеба')


    def btea(self):

        if self.shop.tea >= 1:
            print('Сходил в магазин за чаем')
            self.tea += 1
            self.shop.tea -= 1
        else:
            print('нет чая')



    def shopping(self):
        if self.milk <= 0:
            self.bmilk()
        if self.bread <= 0:
            self.bbread()
        if self.tea <= 0:
            self.btea()
    def go_shopping(self, shop):
        self.shop = shop
joe = Man()
monetka = Shop()
joe.go_shopping(shop=monetka)
joe.shopping()
print(joe)
print(monetka)