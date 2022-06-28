# нашел на просторах интернета и решил реализовать
# задача: выбрать одно число от 1 до 3. выбрать два числа от 4 до 7. одно число от 8 до 9.
# и два числа от 11 до 15. записать выбранные числа и произвольном порядке.
# первое число - номер дельта. второе число - сумма двух первых чисел
# далее добавляем сумму двух первых чисел к последующим


import random

list_of_numbers = [0, 0, 0, 0, 0, 0]
final_list = []


def gen():
    list_of_numbers[0] = random.randint(1, 3)
    list_of_numbers[1] = random.randint(4, 5)
    list_of_numbers[2] = random.randint(6, 7)
    list_of_numbers[3] = random.randint(8, 10)
    list_of_numbers[4] = random.randint(11, 13)
    list_of_numbers[5] = random.randint(14, 15)
    random.shuffle(list_of_numbers)
    # print(f'list of number {list_of_numbers}')
    final_list.clear()
    final_list.append(list_of_numbers[0])
    x2 = list_of_numbers[0]+list_of_numbers[1]
    final_list.append(x2)
    for i in range(len(list_of_numbers)-2):
        x3 = x2 + list_of_numbers[1+i]
        final_list.append(x3)
    print(f'final list {final_list}')
    return list_of_numbers, final_list


for i in range(3):
    gen()
