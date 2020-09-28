"""
Rachael Howard
82772985
Sources: Mostly just random Google searches for the different usages of pop, remove, insert, and append. Also stackoverflow
for how to print elements from a list on different lines because I didn't want to use horizontal lists (I think they're confusing
in the context of this game) and was drawing a blank.
https://stackoverflow.com/questions/13443588/how-can-i-format-a-list-to-print-each-element-on-a-separate-line-in-python
"""

#Imports random library for use with the shuffle_bricks function
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
    """Sets up the main and discard piles. The discard pile remains empty, while the main pile is filled with numbers from 1-60 using the append command. Parameters: None"""
    main_pile = []
    discard = []
    #Fills the main_pile list by iterating through the number 1-60 and appending them to the list.
    for number in range(1,61):
        main_pile.append(number)
    #Returns the full main pile and an empty discard pile
    return (main_pile, discard)


def shuffle_bricks(bricks):
    """Shuffles a list of bricks using the random.shuffle function. Parameters: bricks (list)"""
    random.shuffle(bricks)

def check_bricks(main_pile, discard):
    """Check if there are any cards left in the main pile of bricks. If there are not, it shuffles the discard pile and
then adds the entirety of the discard pile to the main pile. The top (first) brick of the main pile is then removed and added
to the discard pile. Parameters: main_pile, discard"""
    #Check to make sure length of main pile is 0 (i.e. the pile is empty)
    if len(main_pile) == 0:
        #Shuffle the discard pile
        shuffle_bricks(discard)
        #Since this is a list, we can use the in-built extend function to add all elements of the discard pile to the main pile.
        main_pile.extend(discard)
        #Clear discard pile
        discard = []
        #Isolate the first element of the main pile.
        main_pile_first_element = main_pile[0]
        #Append this element to the discard pile, thus starting our discard pile.
        discard.append(main_pile_first_element)
        #Remove the previously chosen element from the main pile.
        main_pile.remove(main_pile[0])
    #If there are cards left in the main pile, leave everything as is.
    else:
        main_pile = main_pile
        discard = discard
    #Return the new main_pile and discard pile
    return main_pile, discard


def check_tower_blaster(tower):
    """Uses the inbuilt sort function to determine if the bricks in the specified tower are in ascending order. This
means that the tower is stable. The boolean values of True and False are returned. Parameters: tower."""
    #if the tower is not sorted, then it is unstable and therefore returns a boolean value of false.
    if tower != sorted(tower):
        return False
    else:
        return True


def get_top_brick(brick_pile):
    """Remove and return the top (first) brick from any given pile of bricks. Parameters: brick_pile"""
    #Ensure that the top_brick is the first brick from the given pile and is returned as an integer. The pop function also removes the brick from the pile.
    top_brick = int(brick_pile.pop(0))
    return top_brick


def deal_initial_bricks(main_pile):
    """Starting with blank towers, add 10 bricks to each tower from the main pile, taking turns with the computer getting the
first brick. The bricks are placed one on top of another. Parameters: main_pile"""
    #Initialize blank towers.
    computer_tower = []
    human_tower = []
    #While the towers have less than 10 elements, iterate through the loop, adding the next brick at the top of the main pile to each tower
    while len(computer_tower) < 10 and len(human_tower) < 10:
        #The computer tower is always added to first
        computer_tower.insert(0,get_top_brick(main_pile))
        human_tower.insert(0,get_top_brick(main_pile))
    #The two towers are returned as a tuple
    return (human_tower, computer_tower)


def add_brick_to_discard(brick, discard):
    """Add the given brick to the top (first element) of the discard pile. Parameters: brick, discard"""
    discard.insert(0,brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    """Find the given brick to be replaced in the given tower, and then replace it with the new brick. Parameters: new_brick, brick_to_be_replaced, tower, discard """
    if brick_to_be_replaced in tower:
        brick_position = tower.index(brick_to_be_replaced)
        tower.insert(brick_position, new_brick)
        add_brick_to_discard(brick_to_be_replaced, discard)
        tower.pop(tower.index((brick_to_be_replaced)))
        return True
    else:
        return False

def computer_play(tower, main_pile, discard):
    """This is a completely brute force strategy that breaks the tower into pieces and only allows bricks that meet the guidelines.
    The default is the discard pile (because that's how I play), but it chooses from the main pile if there are any issues.
    Parameters: tower, main_pile, discard"""
    #Instructor/TA note: Please do not judge my logical/programming skills by this. I spent 4 hours tracking down a bug that turned out to be in my my find_and_replace function.

    #Default to discard pile
    brick = get_top_brick(discard)
    #Name of the pile for use in game dialogue
    pile_choice = "discard pile"
    #Brute force all the way. I split the 60 possible cards into slices, and then assigned those slices to an index value. If anything happens and the brick doesn't fit those criteria (I was getting periodic errors and I am tired), it defaults to the main pile and runs something similar.
    if tower[0] > brick and  brick < 6:
        find_and_replace(brick, tower[0], tower, discard)
    elif  brick <= tower[1] and brick < 12 and brick >=6:
        find_and_replace(brick, tower[1], tower, discard)
    elif brick <= tower[2] and brick < 18 and brick >=12:
        find_and_replace(brick, tower[2], tower, discard)
    elif brick <= tower[3] and brick < 24 and brick >=18:
        find_and_replace(brick, tower[3], tower, discard)
    elif brick <= tower[4] and brick < 30 and brick >=24:
        find_and_replace(brick, tower[4], tower, discard)
    elif brick >= tower[5] and brick < 36 and brick >=30:
        find_and_replace(brick, tower[5], tower, discard)
    elif brick >= tower[6] and brick < 42 and brick >=36:
        find_and_replace(brick, tower[6], tower, discard)
    elif  brick >= tower[7] and brick < 48 and brick >=42:
        find_and_replace(brick, tower[7], tower, discard)
    elif brick >= tower[8] and brick < 54 and brick >=48:
        find_and_replace(brick, tower[8], tower, discard)
    elif brick >= tower[9] and brick < 61 and brick >=54:
        find_and_replace(brick, tower[9], tower, discard)
    #Same same, but different
    else:
        brick = get_top_brick(main_pile)
        pile_choice = "main pile"
        if brick >= 55:
            find_and_replace(brick, tower[9], tower, discard)
        elif brick >=49 and brick <55:
            find_and_replace(brick, tower[8], tower, discard)
        elif brick >=43 and brick < 49:
            find_and_replace(brick, tower[7], tower, discard)
        elif brick >= 35 and brick <43:
            find_and_replace(brick, tower[6], tower, discard)
        elif brick >=29 and brick <35:
            find_and_replace(brick, tower[5], tower, discard)
        elif brick >=23 and brick < 29:
            find_and_replace(brick, tower[4], tower, discard)
        elif brick >= 15 and brick <23:
            find_and_replace(brick, tower[3], tower, discard)
        elif brick >= 10 and brick < 15:
            find_and_replace(brick, tower[2], tower, discard)
        elif brick >= 5 and brick <10:
            find_and_replace(brick, tower[1], tower, discard)
        elif brick < 5:
            find_and_replace(brick, tower[0], tower, discard)

    return tower, pile_choice, brick



def print_tower(tower):
    """Print the tower in a vertical form so that it is more tower-like. Parameters: tower"""
    #Create the vertical tower by iterating over the list and printing each element on a new line, and tabbed over for visual clarity.
    for i in range(10):
        print("\t\t" + str(tower[i]))
    #Return a blank space for visual clarity
    return ""


def choose_pile(main_pile, discard):
    """Determines which pile the human player would like to choose from. Also offers a help function to clarify the rules. Parameters: main_pile, discard"""
    while True:
        #Using a try/except block in case the user enters gibberish.
        try:
            pile_choice = input("Type 'D' to take the discard brick, 'M' to take the mystery brick, or 'H' for help.\n")
            #Any string starting with D or d will mean the user has chosen the discard brick
            if  pile_choice[0] == 'D' or  pile_choice[0] == 'd':
                #The top brick from the discard pile is chosen
                discard_pile_brick = get_top_brick(discard)
                #The pile picked is declared as the string "discard pile" to be used in the message to the player
                pile_picked_from = "discard pile"
                #Return the individual value of the brick as well as what pile it was chosen from (discard)
                return discard_pile_brick, pile_picked_from

            #Any string starting with M or m will mean the user has chosen the mystery brick
            if  pile_choice[0] == 'M' or  pile_choice[0] == 'm':
                #The top brick from the main pile is chosen
                main_pile_brick = get_top_brick(main_pile)
                # The pile picked is declared as the string "main pile" to be used in the message to the player
                pile_picked_from = "main pile"
                # Return the individual value of the brick as well as what pile it was chosen from (main)
                return main_pile_brick, pile_picked_from

            #Allows the player to ask for help if they need a reminder on the rules.
            if pile_choice[0] == 'H' or pile_choice[0] == 'H':
                print("You have 2 options: You can choose the visible brick from the discard pile ('D') or you can choose\na mystery brick from the main pile. If you choose the brick from the discard pile\nyou must use it. However, if you choose the brick from the mystery pile, you have the choice to NOT use it. \n\n")

        #If the player enters in nonsense, this block is triggered. They are told to enter a correct value, and the function is restarted until they enter in something correct.
        except:
            print("Please enter 'D', 'M', or 'H'.")
            continue


def ask_yes_or_no(prompt):
  """Asks the player if they would like to perform an action again. Parameters: prompt"""
  while True:
    action_again = input(prompt)
    #This function only considers the first letter in the string. So, "Ysdfsdf" returns True and "Nsdfsdl" returns False.
    if action_again[0] == "y" or action_again[0]== "Y":
       return True
    elif action_again[0] == "n" or action_again[0]== "N":
       return False
    #If the player enters something that does not start with one of the above letters, they will be prompted to try again.
    else:
       print("Please enter Y or N to continue\n")


def which_brick_to_replace(tower):
    """Asks the user to specify which brick, based on the brick value, that they would like to remove from their tower and replace
with the newly chosen brick. Parameters: tower"""
    #Set the value of the brick to None until something is chosen.
    brick_to_replace = None
    #Keep asking this question until the player enters a valid number
    while True:
        brick_to_replace = input("What brick would you like to replace?\n")
        #Try/except block in case the player enters a brick value that is not an integer
        try:
            #The brick value must be an integer
            brick_to_replace = int(brick_to_replace)
        except:
            #If an integer isn't entered, the player will be asked to try again
            print("Please enter a correct number.")
            continue
        #If the integer is between 1 and 60 and exists in the player tower, then it is returned as the value brick_to_replace
        if 0 < int(brick_to_replace) <= 60:
            for bricks in tower:
                if brick_to_replace == bricks:
                    return brick_to_replace


def main():
    """Where the magic happens, including all functionality. Parameters: None """
    #Initialize the main pile, discard pile, and both players' towers as empty lists
    main_pile = []
    discard = []
    human_tower = []
    computer_tower = []

    #Print the game instructions and starting graphics
    print(print_instructions())
    #Unpack the tuple returned from the setup_bricks() function into the main_pile and discard lists
    main_pile, discard = setup_bricks()
    #Shuffle the main_pile
    shuffle_bricks(main_pile)

    #The human and computer towers are formed using the deal_initial_bricks function
    human_tower,computer_tower = deal_initial_bricks(main_pile)

    #The top brick of the main pile is turned over to begin the discard pile
    discard.append(int(get_top_brick(main_pile)))

    #Print the computer tower and your tower at the beginning of the game. This is done using the vertical format fro the print_tower function, but I was having a hard time getting it to do multiple towers
    print("Computer Tower \t Your Tower")
    #This works exactly the same way as the print_towers function, but returns two towers with headings
    for i in range(10):
        print("\t" + str(computer_tower[i]) + "\t\t\t\t" + str(human_tower[i]))
    #Spacers to keep things visually clean
    print("\n")
    print("/ "*25)

    #The loop runs (and the game continues to play) until someone wins (i.e. check_tower_blaster returns a value of True). The value of check_tower_blaster is checked after each player's turn.
    while check_tower_blaster(computer_tower)== False and check_tower_blaster(human_tower) == False:
        #Let the player know that it is the computer's turn
        print("\nCOMPUTER'S TURN")
        #Check the bricks to ensure that the main pile is not empty. Return the new piles from the check_bricks function if it is
        main_pile, discard = check_bricks(main_pile, discard)
        #The new computer_tower, the pile from which they chose, and the brick they chose are unpacked from the computer_play return tuple
        computer_tower, pile_choice, brick = computer_play(computer_tower, main_pile, discard)
        #Let the player know which brick the computer chose, and from what pile
        print("The computer picked", brick, "from the", pile_choice)
        #Check to see if the computer's tower is stable. If it is, the game is over and the message and winning tower is returned
        if check_tower_blaster(computer_tower) == True:
            print("The computer has won the game with a tower of:")
            print(print_tower(computer_tower))
            break

        #Spacers to keep things visually clean
        print()
        print("/ " * 25 +"\n")

        #Alerts the player that is their turn and shows them their tower using the print_tower function
        print("YOUR TURN")
        print("Computer Tower \t Your Tower")
        for i in range(10):
            print("\t" + str(computer_tower[i]) + "\t\t\t\t" + str(human_tower[i]))
        #print("This is your current tower:")
        #print(print_tower(human_tower))

        #Check the bricks to ensure that the main pile is not empty. Return the new piles from the check_bricks function if it is
        main_pile, discard = check_bricks(main_pile, discard)

        #I was running into issues getting errors, and this seems to have fixed it even though it essentially does the same thing as the check_bricks function above. I don't know. It's Sunday and I'm tired. Whatever works at this point.
        #if len(discard) <= 0:
            #discard.append(main_pile[0])
            #main_pile.pop(0)

        #Lets the user know the value of the top (visible) brick of the discard pile
        print("The top card on the discard pile is", discard[0], "\n")

        #Unpack the return from the choose_pile function so the values can be used in the player message
        user_brick, pile_choice = choose_pile(main_pile, discard)

        #Tell the player what brick they picked and from what pile
        print("You picked", user_brick, "from the", pile_choice)

        #If the player picked the mystery brick from the main pile, give them the choice as to whether or not they want to use it using the ask_yes_or_no function.
        if pile_choice == "main pile":
            use_brick = ask_yes_or_no("Do you want to use this brick? Y/N: \n")

            #If the player chooses to use the brick
            if use_brick:
                #Identify the exact brick they want to replace in their tower will be determined with the which_brick_to_replace function
                brick_to_replace = which_brick_to_replace(human_tower)
                #It will then be replaced using the find_and_replace function
                find_and_replace(user_brick, brick_to_replace, human_tower, discard)
                #The new tower is printed using the print_tower function
                print("Your new tower is:")
                print(print_tower(human_tower))

            #If the player decides not to use the brick
            else:
                #Print the tower using the print_tower function
                print("Your turn is over. Your tower is still")
                print(print_tower(human_tower))
                #Add the brick they don't want to the discard pile using the add_brick_to_discard function
                add_brick_to_discard(user_brick, discard)

        #If they choose to use the brick from the discard pile
        else:
            # Identify the exact brick they want to replace in their tower will be determined with the which_brick_to_replace function
            brick_to_replace = which_brick_to_replace(human_tower)
            # It will then be replaced using the find_and_replace function
            find_and_replace(user_brick, brick_to_replace, human_tower, discard)
            #Tell the player their move
            print("You replaced:", brick_to_replace, "with:", user_brick)
            print("Your new tower is:")
            #Print the tower using the print_tower function
            print(print_tower(human_tower))

        #Spacers to keep things visually clean
        print()
        print("/ " * 25)
        #Check to see if the human_tower is stable using the check_tower_blaster function. If it is stable (i.e. the values are in order), then the game is over

        if check_tower_blaster(human_tower) == True:
            #Tell the player they won and print the winning tower
            print("You have won the game with a tower of:")
            print(print_tower(human_tower))

    #When someone has one the game (computer or player), let them know the game is over.
    print("\nGame Over! Please restart to play again.")

if __name__ == '__main__':
    main()