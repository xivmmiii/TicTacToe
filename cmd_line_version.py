from random import choice


def pos_validation(player):
    if player == 'user':
        position = int(input('Enter position : '))
        while position not in range(1, 10) or position in entered_pos:
            print('Enter valid position')
            position = int(input('Enter position : '))

    else:
        left_pos = [x for x in list(pos_values.keys()) if x not in entered_pos]
        if len(left_pos) == 0:
            return
        position = choice(left_pos)

    entered_pos.append(position)
    return position


def update_game(position, value):
    global game
    pos_values[position] = value
    game = f'''
               |           |
         {pos_values[1]}     |     {pos_values[2]}     |     {pos_values[3]}
               |           |
    -----------------------------------
               |           |
         {pos_values[4]}     |     {pos_values[5]}     |     {pos_values[6]}
               |           |
    -----------------------------------
               |           |
         {pos_values[7]}     |     {pos_values[8]}     |     {pos_values[9]}
               |           |
    '''


pos_values = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',

}

game = f'''
           |           |
     {pos_values[1]}     |     {pos_values[2]}     |     {pos_values[3]}
           |           |
-----------------------------------
           |           |
     {pos_values[4]}     |     {pos_values[5]}     |     {pos_values[6]}
           |           |
-----------------------------------
           |           |
     {pos_values[7]}     |     {pos_values[8]}     |     {pos_values[9]}
           |           |
'''

winning_combinations = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {1, 4, 7},
    {2, 5, 8},
    {3, 6, 9},
    {1, 5, 9},
    {3, 5, 7}
]

print(f"Tic Tac Toe\n{game}\n\nYou are assigned 'x'\nEnter position number 1-9 to assign 'x' to the position\n")

entered_pos = []
user_combinations = []
comp_combinations = []

game_over = False
while not game_over:
    user_position = pos_validation('user')
    user_combinations.append(user_position)
    update_game(user_position, 'x')
    for item in winning_combinations:
        if item.issubset(user_combinations):
            print('You won')
            game_over = True
            break
    print(f'You : {game}')
    comp_position = pos_validation('comp')
    comp_combinations.append(comp_position)
    update_game(comp_position, 'o')
    if not game_over:
        print(f'Computer : {game}')
        for item in winning_combinations:
            if item.issubset(comp_combinations):
                print('You lost')
                game_over = True
                break

        if len(user_combinations) + len(comp_combinations) == 9:
            print('Draw')
            game_over = True
