# Задание: при покупных ценах в $ производить перерасчет розничных цен на продукты в случае роста курса $.
# Перерасчет цен произвоидить в случае когда рентабельность, установвленная в размере 15% снижается до 0.
# Исходыне данные : курс- 2р за 1$, рентабельность( торговая нацценка) -15%, НДС -10%
#

d_1 = 2    #курс у.е на момент покупки товара
d_2 = 2  #курс у.е. на данный момент. (!!!! далее нужно будет найти способ запарсить его)
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

# в цикле прогоняем список товаров по закупочной цене и умножаем на курс у.е+ндс+рентабельность
for goods in goods.items():
    goods_2.update({goods[0]:
                        {'purchase': goods[1] * d_1,
                         'nds': goods[1]*d_1 * nds,
                         'profibility': goods[1]*d_1 * prfibility,
                         'total price': goods[1]*d_1 + (goods[1]*d_1 * prfibility) + (goods[1]*d_1 * nds)}
                    })
    goods_3.update({goods[0]:
                        {'purchase': goods[1] * d_2,
                         'nds': goods[1]*d_2 * nds,
                         'profibility': goods[1]*d_2 * prfibility,
                         'total price': goods[1]*d_2 + (goods[1]*d_1 * prfibility) + (goods[1]*d_1 * nds)}
                    })
print(goods_2)
print(goods_3)

# !!!как подступиться без ключа?!
price1 = goods_2['nuts']['total price']
pur1 = goods_3['nuts']['purchase']
nds1 = goods_2['nuts']['nds']
print(price1, pur1, nds1)

x = price1 - nds1 - pur1

print(x)

if x >= 0:
    for goods_2 in goods_2.items():
        print('Товар:', goods_2[0], 'Имеет цену:', goods_2[1]['total price'])

else:
    for goods_3 in goods_3.items():
        print('Товар:', goods_3[0], 'Имеет цену:', goods_3[1]['total price'])

#проверка
# rise = 0
# while x >= 0:
#     d_2 += 0.10
#     rise += 1
#     print(rise)
