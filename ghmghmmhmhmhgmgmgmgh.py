field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def print_field(my_field):
    print(' _ _ _')
    for i in my_field:
        c = ""
        for b in i:
            c += '|' + b
        print(c + '|')


def make_move(my_field, move, coo):
    if my_field[(coo - 1) // 3][(coo - 1) % 3] == "_":
        my_field[(coo - 1) // 3][(coo - 1) % 3] = move
        return my_field, True
    else:
        return my_field, False
    if coo > 9:
        return my_field, False

while True:
    print('LETS PLAY!')
    print_field(field)
    move_type = ['X', 'O']
    move_ch = 0
    print('Move of: ', move_type[move_ch % 2])

    while True:
        coords = int(input('make your move: '))
        field = make_move(field, move_type[move_ch % 2], coords)[0]
        print(field[0])
        print_field(field)
        move_ch += 1
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
