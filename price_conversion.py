# скрипт для расчета рентабельности.
#
#
#
#

d_1 = 2    #курс у.е на момент покупки товара
d_2 = 2    #курс у.е. на данный маомент. ( далее нужно будет найти способ запарсить его)
nds = 0.10 #ставка ндс 10%
prfibility = 0.15 # % заложенной рентабельности
# список товаров по закупочной цене в у.е
goods = {
    'nuts': 1.5,
    'tomatos': 1,
    'banan': 2
}

# создаем два словаря для записи цен после конвертации
goods_2 = {}   #цена в нац валюте ( у.е * на курс на момент ПОКУПКИ+ ндс + % заложенной рентабельности)
goods_3 = {}   #цена в нац валюте ( у.е * на курс в ДАННЫЙ момент+ ндс + % заложенной рентабельности)

# в цикле прогоняем список товаров по закупочной цене и умножаем на курс у.е
for goods in goods.items():
    goods_2.update({goods[0]:
                        {'purchase': goods[1] * d_1,
                         'nds': goods[1]*d_1 * nds,
                         'profibility': goods[1]*d_1 * prfibility,
                         'total price': goods[1]*d_1 * (10 * prfibility) * (10 * nds)}
                    })
    goods_3.update({goods[0]:
                        {'purchase': goods[1] * d_2,
                         'nds': goods[1]*d_2 * nds,
                         'profibility': goods[1]*d_2 * prfibility,
                         'total price': goods[1]*d_2 * (10 * prfibility) * (10 * nds)}
                    })
print(goods_2)
print(goods_3)

x = goods_2['nuts']['total price'] - goods_3['nuts']['profibility'] - goods_2['nuts']['purchase']- goods_2['nuts']['nds']
#решить как подступиться без имени
print(x)

if x >= 0:
    for goods_2 in goods_2.items():
        print('товар-', goods_2[0], 'имеет цену', goods_2['price'])
    else:
        print('товар-', goods_3[0], 'имеет цену', goods_3['price'])