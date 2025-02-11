# monty hall, more idiomatic

doors = ['goat', 'goat', 'car']
show_doors = ['1', '2', '3']

def doors_input():
    print(f'[{show_doors[0]}] [{show_doors[1]}] [{show_doors[2]}]\n')
    return input('Pick a door 1, 2, or 3?')
    
def quiz():
    print("Pick a door to win a car!")

    door_val = int(doors_input()) - 1

    # use a list comprehension iterator to select the 2 doors the player didn't enter, leaving a list in other_doors
    other_doors = [i for i in range(3) if i != door_val]
    # using next() to iterate the i value, select the fisrt one that is a goat to show the player
    show_doors[next(i for i in other_doors if doors[i] == 'goat')] = 'goat'
            
    print(f'[{show_doors[0]}] [{show_doors[1]}] [{show_doors[2]}]')
    
    print('Would you like to pick a different door?')
    new_door = input('y or n?: ')

    if new_door.lower() == 'y':
        door_val = int(input('New Choice: ')) - 1
            
    show_doors[door_val] = doors[door_val]
    print(f'[{show_doors[0]}] [{show_doors[1]}] [{show_doors[2]}]')

    if doors[door_val] == 'car':
        print('Winner!')
    else:
        print('Bad luck, thanks for playing!')
        
quiz()
