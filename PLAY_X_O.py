def print_field(my_field):
    print(' _ _ _')
    for i in my_field:
        c = ""
        for b in i:
            c += '|' + b
        print(c + '|')


def make_move(my_field, move_type, coords):
    coords[0] = coords[0]-1
    coords[1] = coords[1]-1
    if coords[0] > 2 or coords[1] > 2:
        status = False
        print(status)
        print_field(my_field)
        status = False
        return status
    if coords[0] <= 2 and coords[1] <= 2:
        if my_field[coords[0]][coords[1]] != 'O' and my_field[coords[0]][coords[1]] != 'X':
            my_field[coords[0]][coords[1]] = move_type
            status = True
            print(status)
            print_field(field)
            return status
        if my_field[coords[0]][coords[1]] == 'O' or my_field[coords[0]][coords[1]] == 'X':
            status = False
            print(status)
            print_field(field)
            coords = []
            return status


while True:
    print('Начинаем игру')
    field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    person = 1
    X_or_O = 'X'
    print_field(field)

    while True:
        if field[0].count('X') == 3 or field[1].count('X') == 3 or field[2].count('X') == 3:
            print('Крестики выиграли!')
            break
        elif field[0].count('O') == 3 or field[1].count('O') == 3 or field[2].count('O') == 3:
            print('Нолики выиграли!')
            break
        elif field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X':
            print('Крестики выиграли!')
            break
        elif field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O':
            print('Нолики выиграли!')
            break
        elif field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O':
            print('Нолики выиграли!')
            break
        elif field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X':
            print('Крестики выиграли!')
            break
        elif field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X':
            print('Крестики выиграли!')
            break
        elif field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O':
            print('Крестики выиграли!')
            break
        elif '_' not in field[0] and '_' not in field[1] and '_' not in field[2]:
            print('Ничья!')
            break
        else:
            if person == 1:
                X_OR_O = 'X'
            if person == 2:
                X_OR_O = 'O'
            print('Ходит человек №', person)
            coords_column = int(input('Введите рядок'))
            coords_rou = int(input('Введите столбик'))
            coords_to_def = []
            coords_to_def.append(coords_column)
            coords_to_def.append(coords_rou)
            if person == 1:
                person = person + 1
            elif person == 2:
                person -= 1
            debug = make_move(field, X_OR_O, coords_to_def)
            if debug == False:
                if person == 1:
                    person += 1
                elif person == 2:
                    person -= 1
