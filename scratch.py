# TOWER BLASTER #
def shuffle(bricks):
    """This function simply serves to shuffle the 'bricks' list in a random order.
     It doesn't return any object. It uses the random module for suffling the
     deck of bricks.
  """
    import random
    random.shuffle(bricks)

    ##------------------------------------------------------------------------------------------------------------------------------------------------


def check_bricks(main_pile, discard):
    """ Function to add discard pile values to the main pile, if the main pile goes
      empty.
  """
    if len(main_pile) == 0:
        shuffle(discard)
        main_pile.extend(discard)
        discard = []
        x = main_pile.pop(0)
        discard.append(x)

    ##------------------------------------------------------------------------------------------------------------------------------------------------


def check_tower_blaster(tower):
    """ The function 'check_tower_blaster' looks up whether the tower is sorted (in
      ascending order) or not and returns a boolean value accordingly.
      If tower is sorted -> True
      If tower is not sorted -> False
  """
    if tower == sorted(tower):
        return True
    else:
        return False

    ##------------------------------------------------------------------------------------------------------------------------------------------------


def get_top_brick(brick_pile):
    """ This function returns the top brick in any of the piles, be it user's, computer's
      or the discard pile and returns an interger. It basically fetches the first element
      in any list.
  """
    top_element = brick_pile.pop(0)
    return int(top_element)

    ##------------------------------------------------------------------------------------------------------------------------------------------------


def deal_initial_bricks(main_pile):
    """ deal_initial_bricks is an initializing function that takes the values in the main pile and distributes
      it equally between the user and the computer wherein the computer is 'always' dealt the
      first brick in the pile.
  """
    user_pile = []
    computer_pile = []
    ## Shuffling the main_pile to ensure random assignment
    shuffle(main_pile)
    for i in range(20):
        if i % 2 == 0:
            computer_pile.insert(0, get_top_brick(main_pile))
            shuffle(main_pile)
        else:
            user_pile.insert(0, get_top_brick(main_pile))
            shuffle(main_pile)
    return (user_pile, computer_pile)

    ##------------------------------------------------------------------------------------------------------------------------------------------------


def add_brick_to_discard(brick, discard):
    """ This function adds the user chosen brick to the discard pile if they choose not to add
      it to their main pile. It doesn't return any value.
  """
    discard.insert(0, brick)

    ##------------------------------------------------------------------------------------------------------------------------------------------------


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    """ Function 'find_and_replace' finds the presence of a brick in the tower and replaces if with
      a new brick whereas the brick to be replaced is added on top of the discard pile.
      If brick is successfully substituted, it returns True.
      If brick is not found in the tower pile, it returns False.
  """
    if brick_to_be_replaced in tower:
        pos = tower.index(brick_to_be_replaced)
        add_brick_to_discard(tower[pos], discard)
        tower[pos] = new_brick
        return True
    else:
        return False


##------------------------------------------------------------------------------------------------------------------------------------------------
"""Global Variable Declaration"""
turn = 0


##------------------------------------------------------------------------------------------------------------------------------------------------

def computer_play(tower, main_pile, discard):
    """ The function responsible for the move made by the computer (that is the programmer's
      turn to change the tower is handled by this function.
  """
    ## The global variable 'turn' allows the computer to pick a number from the main pile if
    ## the number is divisible by 4.
    global turn
    if turn % 5 == 0:
        brick = get_top_brick(main_pile)
        ## The number from the main pile gets discarded if 'turn' is divisble by 4.
        if turn % 4 == 0:
            add_brick_to_discard(brick, discard)
            turn += 1
        else:
            turn += 1
            ## If the number is between 1-30, the tower will be parsed from top to bottom.
            ## If a number is found > than the brick, it will be replaced by the brick.
            if brick in range(1, 31):
                ## For the bricks in range 1-15
                if brick in range(1, 16):
                    for i in range(0, 10):
                        if tower[i] > brick:
                            find_and_replace(brick, tower[i], tower, discard)
                            break
                else:
                    for i in range(9, -1, -1):
                        if tower[i] < brick:
                            find_and_replace(brick, tower[i], tower, discard)
                            break
            ## If the number is between 31-60, the tower will be parsed in reverse order.
            ## If a number is found < than the brick, it will be replaced by the brick.
            else:
                if brick in range(31, 46):
                    for i in range(0, 10):
                        if tower[i] > brick:
                            find_and_replace(brick, tower[i], tower, discard)
                            break
                else:
                    for i in range(9, -1, -1):
                        if tower[i] < brick:
                            find_and_replace(brick, tower[i], tower, discard)
                            break

    else:
        ## Code to be executed if the brick is selected from the discard pile
        turn += 1
        brick = get_top_brick(discard)
        if brick in range(1, 31):
            for i in range(0, 10):
                if tower[i] > brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break
        else:
            for i in range(9, -1, -1):
                if tower[i] < brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break
    return tower


##------------------------------------------------------------------------------------------------------------------------------------------------

def replace_bricks_in_tower(number, user_pile, discard):
    """ Custom Function to check whether the brick user wishes to replace exists in the tower
      and returns the modified list.
  """
    brick_to_replace = input("Enter the brick you wish to replace in the tower- ")
    ## To check whether the value for brick to be replaced is an integer or not
    check_list = [str(i) for i in range(1, 61)]
    while brick_to_replace not in check_list:
        brick_to_replace = input("!!Wrong Value Entered. Try to make a valid input - ")
    ## If the user enter a brick not in the tower
    brick_to_replace = int(brick_to_replace)
    while not (find_and_replace(number, brick_to_replace, user_pile, discard)):
        print("Brick Not Found in the Tower")
        brick_to_replace = int(input("Enter the brick you wish to replace - "))
        continue
    return user_pile


##------------------------------------------------------------------------------------------------------------------------------------------------

def check_user_choice(choice, tower, main_pile, discard):
    """ 'check_user_choice' validates whether the choice entered by user is within specified bounds
       and then proceeds to modify the user tower accordingly. In case of incorrect choices, it
       asks the user to enter a correct choice till they don't make a valid input.
  """
    while choice != "Y" and choice != "y" and choice != "N" and choice != "n":
        choice = input("!! Invalid Option !! Enter a valid choice [Y/N] ")

    if choice == "N" or choice == "n":
        num = get_top_brick(discard)
        tower = replace_bricks_in_tower(num, tower, discard)

    elif choice == "Y" or choice == "y":
        num = get_top_brick(main_pile)
        c = input("Do you wish to use " + str(num) + ". [Enter Y or N] - ")
        while c != "Y" and c != "y" and c != "N" and c != "n":
            c = input("!! Invalid Option !! Enter a valid choice [Y/N] ")

        if c == "N" or c == "n":
            ## If the user chooses not to use the brick from the main pile
            add_brick_to_discard(num, discard)

            ## It considers the user willingly gives up their turn
        elif c == "Y" or c == "y":
            tower = replace_bricks_in_tower(num, tower, discard)

    return tower

    ##------------------------------------------------------------------------------------------------------------------------------------------------


def main():
    print("-------------------------- !!Let's Begin the Game!! -------------------------- \n")


computer_tower = []
user_tower = []
main_pile = [i for i in range(1, 61)]
discard = []

## Initializing the User and Computer's Towers
user_tower, computer_tower = deal_initial_bricks(main_pile)

## Initializing the discard pile
discard.append(get_top_brick(main_pile))

print("---------------------- You are going to play as Player 2 ---------------------")
print("Player 1: Tower \t Player 2: Tower")
for i in range(10):
    print("\t" + str(computer_tower[i]) + "\t\t\t" + str(user_tower[i]))

## Following code deals with the game's moves
while True:
    check_bricks(main_pile, discard)
    computer_tower = computer_play(computer_tower, main_pile, discard)
    if check_tower_blaster(computer_tower) == True:
        print("SORRY, YOU LOST. :( BETTER LUCK NEXT TIME ")
        break
    else:
        discard_pile_num = discard[0]
        print("The number available- " + str(discard_pile_num))
        print("Do you wish to use this number or use the main pile otherwise.")
        user_choice = input("Enter Y for the main pile and N to continue with the current number -  ")
        user_tower = check_user_choice(user_choice, user_tower, main_pile, discard)

        if check_tower_blaster(user_tower) == True:
            print("Player 2: Tower")
            for i in range(10):
                print("\t", user_tower[i])
            print("CONGRATULATIONS !! :) YOU WON!!")
            break
            ## Displaying the user's tower after modifications
    print("Player 2: Tower")
    for i in range(10):
        print("\t", user_tower[i])

##-----------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()