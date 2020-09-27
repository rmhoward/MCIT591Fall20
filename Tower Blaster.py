import random

def print_instructions():
  """Returns the instructions for the game. Parameters: None.
     Art taken from https://ascii.co.uk/art/towers and http://patorjk.com/software/taag/#p=display&f=Big&t=Tower%20Blaster"""
  return ("""
  _______                       ____  _           _            
 |__   __|                     |  _ \| |         | |           
    | | _____      _____ _ __  | |_) | | __ _ ___| |_ ___ _ __ 
    | |/ _ \ \ /\ / / _ \ '__| |  _ <| |/ _` / __| __/ _ \ '__|
    | | (_) \ V  V /  __/ |    | |_) | | (_| \__ \ ||  __/ |   
    |_|\___/ \_/\_/ \___|_|    |____/|_|\__,_|___/\__\___|_|  
    \n 
Instructions: Stabilize your tower by putting the blocks in numerical order with the highest number at the bottom
and the lowest number on the top.  You will always have two blocks to choose from: The one at the top of the discard 
pile and a mystery block.  Choose wisely! The first player to stabilize their tower wins.
                 
                                |>>>
                                |
                            _  _|_  _
                           |;|_|;|_|;|
                           \ .    .  /
                            \ :  .  /
                             ||:   |
                             ||:.  |
                             ||:  .|
                             ||:   |       
                             ||: , |            
                             ||:   |
                             ||: . |
                             ||_   |
  """)

def setup_bricks():
    main_pile = []
    discard = []
    for number in range(1,61):
        main_pile.append(number)
    return (main_pile,discard)


def shuffle_bricks(bricks):
    random.shuffle(bricks)
    return bricks


def check_bricks(main_pile, discard):
    if len(main_pile) == 0:
        discard = shuffle_bricks(discard)
        main_pile = main_pile.extend(discard)
        main_pile_first_element = main_pile[0]
        discard.append(main_pile_first_element)
        main_pile.pop[0]
    return main_pile, discard


def check_tower_blaster(tower):
    if tower != sorted(tower):
        return False
    else:
        return True


def get_top_brick(brick_pile):
    top_brick = brick_pile[0]
    del brick_pile[0]
    return top_brick


def deal_initial_bricks(main_pile):
    computer_tower = []
    human_tower = []
    while len(human_tower) < 10:
        computer_tower.append(main_pile[0])
        main_pile.remove(main_pile[0])
        human_tower.append(main_pile[0])
        main_pile.remove(main_pile[0])
    return (human_tower, computer_tower)


def add_brick_to_discard(brick, discard):
    discard.insert(0,brick)
    return discard

def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    if brick_to_be_replaced in tower:
        brick_position = tower.index(brick_to_be_replaced)
        tower.remove(tower[brick_position])
        tower.insert(brick_position, new_brick)
        add_brick_to_discard(brick_to_be_replaced,discard)
        return True
    else:
        return False


def computer_play(tower, main_pile, discard):
    list = [0,1]
    choice = random.choice(list)
    if choice == 0:
        brick = get_top_brick(main_pile)
        pile_choice = "main pile"

        if brick in range(1, 16):
            for i in range(0, 2):
                if tower[i] > brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break

        elif brick in range(16, 31):
            for i in range(2, 5):
                if tower[i] > brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break

        elif brick in range(31, 46):
            for i in range(5, 7):
                if tower[i] > brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break
        else:
            for i in range(7, 10):
                if tower[i] > brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break
    else:
        brick = get_top_brick(discard)
        pile_choice = "discard pile"
        if brick in range(1, 16):
            for i in range(0, 2):
                if tower[i] > brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break

        elif brick in range(16, 31):
            for i in range(2, 5):
                if tower[i] > brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break

        elif brick in range(31, 46):
            for i in range(5, 7):
                if tower[i] > brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break
        else:
            for i in range(7, 10):
                if tower[i] > brick:
                    find_and_replace(brick, tower[i], tower, discard)
                    break
    return tower, pile_choice


def print_tower(tower):
    for i in range(10):
        print("\t\t" + str(tower[i]))
    return ""

def choose_pile(main_pile, discard):
    while True:
        pile_choice = input("Type 'D' to take the discard brick, 'M' to take the mystery brick, or 'H' for help.\n")

        if  pile_choice[0] == 'D' or  pile_choice[0] == 'd':
            discard_pile_brick = get_top_brick(discard)
            which_pile_picked = "discard"
            return discard_pile_brick, which_pile_picked

        if  pile_choice[0] == 'M' or  pile_choice[0] == 'm':
            main_pile_brick = get_top_brick(main_pile)
            which_pile_picked = "main_pile"
            return main_pile_brick, which_pile_picked

        if pile_choice[0] == 'H' or pile_choice[0] == 'H':
            print("You can decide to use the known mystery brick")




def ask_yes_or_no(prompt):
  """Asks the player if they would like to perform an action again. Parameters: prompt"""
  while True:
    action_again = input(prompt)
    #This function only considers the first letter in the string. So, "Ysdfsdf" returns True and "Nsdfsdl" returns False.
    if action_again[0] == "y" or action_again[0]== "Y":
       return True
    elif action_again[0] == "n" or action_again[0]== "N":
       return False
    else:
       print("Please enter Y or N to continue\n")

def which_brick_to_replace(tower):
    brick_to_replace = None
    while True:
        brick_to_replace = input("What brick would you like to replace?\n")
        try:
            brick_to_replace = int(brick_to_replace)
        except ValueError as error:
            print("Please enter a correct number.")
            continue
        if 0 < int(brick_to_replace) <= 60:
            for bricks in tower:
                if brick_to_replace == bricks:
                    return brick_to_replace


def main():
    main_pile = []
    discard = []
    human_tower = []
    computer_tower = []
    brick_pile = []

    print(print_instructions())
    main_pile,discard = setup_bricks()
    main_pile = shuffle_bricks(main_pile)

    #The human and computer towers are created
    human_tower,computer_tower = deal_initial_bricks(main_pile)

    #The top brick of the main pile is turned over to begin the discard pile
    discard.append(int(get_top_brick(main_pile)))


    #Print the computer tower and your tower at the beginning of the game in a vertical structure
    print("Computer Tower \t Your Tower")
    for i in range(10):
        print("\t" + str(computer_tower[i]) + "\t\t\t\t" + str(human_tower[i]))
    print("/ "*25)

    while check_tower_blaster(computer_tower)== False and check_tower_blaster(human_tower) == False:
        print("COMPUTER'S TURN")
        computer_tower, pile_choice = computer_play(computer_tower, main_pile,discard)
        print("The computer replaced a brick with one from the", pile_choice)
        if check_tower_blaster(computer_tower) == True:
            print("The computer has won the game with a tower of:")
            print(print_tower(computer_tower))
            break

        print()
        print("/ " * 25 +"\n")

        print("YOUR TURN")
        print("This is your current tower:")
        print(print_tower(human_tower))
        main_pile, discard = check_bricks(main_pile, discard)
        print("The top card on the discard pile is", get_top_brick(discard), "\n")
        user_brick, pile_choice = choose_pile(main_pile, discard)
        print("You picked", user_brick, "from the", pile_choice)
        if pile_choice != "discard":
            use_brick = ask_yes_or_no("Do you want to use this brick? Y/N: \n")
            if use_brick:
                brick_to_replace = which_brick_to_replace(human_tower)
                find_and_replace(user_brick, brick_to_replace, human_tower, discard)
                print("Your new tower is:")
                print(print_tower(human_tower))
            else:
                print("Your turn is over. Your tower is still")
                print(print_tower(human_tower))
                add_brick_to_discard(user_brick, discard)
        else:
            brick_to_replace = which_brick_to_replace(human_tower)
            find_and_replace(user_brick, brick_to_replace, human_tower, discard)
            print("You replaced:", brick_to_replace, "with:", user_brick)
            print("Your new tower is:")
            print(print_tower(human_tower))
        print()
        print("/ " * 25)
        if check_tower_blaster(human_tower) == True:
            print("You have won the game with a tower of:")
            print(print_tower(human_tower))

    print("\nGame Over")

main()