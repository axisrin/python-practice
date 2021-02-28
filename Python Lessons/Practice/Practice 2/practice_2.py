

def f21():

    set1 = {'gn':4,'pony':5,'php':6}
    set2 = {'gn':1,'pony':2,'php':3}
    sec_set = {'2000':0,'1997':set2,'1969':set1}
    # sec_set1 = {'svg':set1,'roff':6}
    # sec_set2 = {'svg':set3,'roff':set2}
    third_set = {'1978':sec_set,'1987':7,'1980':8}
    apex_set = {'1972':third_set,'1969':9}

    cords1 = [1969, 'php', 'abap', 1969, 1978]
    cords2 = [1969, 'php', 'io', 1972, 1978]

    def third_index_step(x):
        coord = str(x[3])
        if type(apex_set[coord]) is dict:
            return fourth_index_step(x, apex_set[coord])
        else:
            return apex_set[coord]

    def fourth_index_step(x, tree):
        coord = str(x[4])
        if type(tree[coord]) is dict:
            return zero_index_step(x, tree[coord])
        else:
            return tree[coord]

    def zero_index_step(x, tree):
        coord = str(x[0])
        if type(tree[coord]) is dict:
            return first_index_step(x, tree[coord])
        else:
            return tree[coord]

    def first_index_step(x, tree):
        coord = str(x[1])
        return tree[coord]

    def go_tree(x):
        return third_index_step(x)

    # return go_tree(cords1)
    go_tree(cords1)
    go_tree(cords2)

    print(f'f({cords1}) = {go_tree(cords1)}')
    print(f'f({cords2}) = {go_tree(cords2)}')

# print(f'f(n) = {f21()}')


f21()
# stroke = str(cords[0])

# set1[stroke]

# print(find_cord(cords))

# def third_index_step(x):
#     coord = str(x[3])
#     if type(apex_set[coord]) is dict:
#         return fourth_index_step(x, apex_set[coord])
#     else:
#         return apex_set[coord]
#
# def fourth_index_step(x, tree):
#     coord = str(x[4])
#     if type(tree[coord]) is dict:
#         return zero_index_step(x, tree[coord])
#     else:
#         return tree[coord]
#
# def zero_index_step(x, tree):
#     coord = str(x[0])
#     if type(tree[coord]) is dict:
#         return first_index_step(x, tree[coord])
#     else:
#         return tree[coord]
#
# def first_index_step(x, tree):
#     coord = str(x[1])
#     return tree[coord]
#
# def go_tree(x):
#     return third_index_step(x)

# go_tree(cords1)
# go_tree(cords2)

# print(f'f({cords1}) = {go_tree(cords1)}')
# print(f'f({cords2}) = {go_tree(cords2)}')

# 1.2

def f22(x):
    # num = bin(x)
    # num_str = str(num)
    # f_peace = num_str[2:5]
    # e_peace = num_str[6:7]
    # d_peace = num_str[8:15]
    # c_peace = num_str[16:20]
    # b_peace = num_str[21:22]
    # a_peace = num_str[23:34]
    #
    # new_num_str =  d_peace + a_peace + b_peace + f_peace + c_peace + e_peace
    # new_num = new_num_str

    a = (x & 0x00000FFF) << 12
    b = (x & 0x00003000) >> 2
    c = (x & 0x0007C000) >> 12
    d = (x & 0x07F80000) << 5
    e = (x & 0x18000000) >> 27
    f = (x & 0xE0000000) >> 22

    return hex(d+a+b+f+c+e)


print(f'f({hex(0xf0611342)}) = {f22(0xf0611342)}')
print(f'f({hex(0xdc2c1325)}) = {f22(0xdc2c1325)}')

# 1.3

persones1 = [

    ['+79785106993', '', 0.7, '21‐06‐04', '', 'Кокозман И.З.', 'Кокозман И.З.'],
    ['+78255267029', '', 0.2, '17‐12‐01', '', 'Цосберг Р.И.', 'Цосберг Р.И.'],
    ['+76665611851', '', 0.3, '24‐10‐00', '', 'Догомберг Ю.Б.', 'Догомберг Ю.Б.'],
    ['+76665611851', '', 0.3, '24‐10‐00', '', 'Догомберг Ю.Б.', 'Догомберг Ю.Б.'],

]

persones2 = [

    ['+79747571829', '', 0.0, '17‐09‐03', '', 'Наченко И.В.', 'Наченко И.В.'],
    ['+70433000396', '', 0.4, '09‐12‐03', '', 'Гутяк М.З.', 'Гутяк М.З.'],
    ['+70176904775', '', 0.8, '07‐11‐03', '', 'Балазберг С.Р.', 'Балазберг С.Р.'],
    ['+76463568478', '', 0.1, '23‐09‐03', '', 'Зинилян В.Д.', 'Зинилян В.Д.'],
    ['+76463568478', '', 0.1, '23‐09‐03', '', 'Зинилян В.Д.', 'Зинилян В.Д.'],

]

def f23(x):

    #  Создаём массив без повторов
    y = []
    for i in x:
        if i not in y:
            y.append(i)

    # y_missed_columns = []
    # for i in range(len(y)):
    #     for j in y[i]:
    #         if bool(j) is False:
    #             y.pop(i)

    # Преобразование второго столбца
    for column in y:
        if column[1] == '':
            del column[1]

    # Преобразование четвёртого столбца
    for column in y:
        if column[3] == '':
            del column[3]

    # Удаление дубликатов
    for column in y:
        if column[3] is column [4]:
            del column[4]

    # for y in x:
    #     print(y)

    # for i in range(len(x)):
    #     if (x[1] == x[i-1]):
    #         x.pop(i)

    # Преобразование тел. номеров
    for column in y:
        old_column = column[0]
        tel_column = old_column[5:]
        column[0] = tel_column[0:3]+"-"+tel_column[3:5]+"-"+tel_column[5:7]

    # Преобразование коэфицентов
    for column in y:
        column[1] = '{:.0%}'.format(column[1])


    # Преобразование Даты
    for column in y:
        column[2] = column[2][6:8] + "-" +column[2][3:5] + "-" + column[2][0:2]

    # Преобразование Инициалов
    for column in y:
        column[3] = column[3][:(column[3].find('.') + 1)]
        column[3] = column[3][(column[3].find(' ') + 1):] + ' ' + column[3][:(column[3].find(' '))]

    y_new_table = []

    column_nums = 0

    # Транспанирование таблицы
    for column_total in y[0]:
        y_new_strokes = []
        for column in y:
            y_new_strokes.append(column[column_nums])
        y_new_table.append(y_new_strokes)
        column_nums += 1


    print(y_new_table)
    return y_new_table

f23(persones1)
f23(persones2)
