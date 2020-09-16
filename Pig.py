#Import necessary packages.
import random
import time

def print_instructions():
  """Returns the instructions for the game. Parameters: None."""
  return ("Welcome to Pig!\nRoll the dice as many times as you wish on each turn, and each roll will be added to your score. \nBUT if you roll a 6, your score for that round is 0. \nThe first player to get a score that is equal to or higher than 50 wins!")

def is_game_over(computer_score, human_score):
  "Determines if the game is over. The game ends when the first player reaches 50 AND there is no tie. Parameters: computer_score, human_score"
  if (computer_score >= 50 or human_score >= 50) and (computer_score != human_score):
    return True
  else:
    return False

def roll():
  """Rolls a fair 6-sided die and returns the result. Parameters: None. """
  return random.randint(1, 6)

def ask_yes_or_no(prompt):
  """Asks the player if they would like to perform an action again. Parameters: prompt"""
  while True:
    action_again = input(prompt)
    #This function only considers the first letter in the string. So, "Ysdfsdf" returns True and "Fsdfsdl" returns False.
    if action_again[0] == "y" or action_again[0]== "Y":
       return True
    elif action_again[0] == "n" or action_again[0]== "N":
       return False
    else:
       print("Please enter Y or N to continue")

def show_current_status(computer_score, human_score):
  """Shows the current score of each player and which player is ahead (or if there is a tie). Parameters: computer_score, human_score"""
  print("The computer's score is",computer_score,".")
  print("Your score is",human_score,".")
  if computer_score > human_score:
    print("The computer is",computer_score-human_score,"points ahead of you.")
  elif computer_score < human_score:
    print("You are",human_score-computer_score,"points ahead of the computer.")
  else:
    print("You are tied.")

def show_final_results(computer_score, human_score):
  """Tells which player won the game, and by how many points. Parameters: computer_score, human_score"""
  if computer_score > human_score:
    return "You lost by "+ str(computer_score - human_score) + " points."
  elif human_score > computer_score:
    return "You won by "+ str(human_score - computer_score) + " points."

def computer_move(computer_score, human_score):
  """The computer rolls a random number of times and displays the result of each roll. Parameters: computer_score, human_score """
  #The total number of points for this round
  comp_roll_total = 0
  #Determines the number of times the computer will roll using the roll() function. This is not optimal, but it does make the game decently difficult do to the random nature of the rolls.
  number_of_turns = roll()
  #Sets number of turns taken in this round to 0
  turn_count = 0
  #While the turn count is less than or equal to the random number of times the computer will roll, the computer rolls.
  while turn_count <= number_of_turns:
    print("It is the computer's turn")
    #roll_value is taken from the function roll()
    roll_value = roll()
    #A roll that is not a 6 assigns the value to the total (comp_roll_total)
    if roll_value != 6:
      comp_roll_total += roll_value
      print("The computer rolls a", roll_value)
      print("The computer's total roll from this turn equals", comp_roll_total, ".")
      print("-------------------------------------------------------------")
      #Set round total equal to the variable computer_score
      computer_score = comp_roll_total
      #Increase the turn count
      turn_count += 1
    #A roll of 6 sets the total score of the round to 0 and immediately ends the computer's turn.
    elif roll_value == 6:
      #Set computer_score = 0. This is equivalent to setting the round_score to 0.
      computer_score = 0
      turn_count = 0
      print("The computer rolled a six! The total score for this round is", computer_score, ".")
      print("-------------------------------------------------------------")
      break
  #The total score for the round is returned as the variable computer_score
  return computer_score

def human_move(computer_score, human_score):
  """The player must roll at least once. The first roll is done automatically. After that,
  the user will be asked if they want to roll again repeatedly until they choose to end their
  turn.
  ▪ If the user chooses to roll again, and DOES NOT roll a 6, this function
  adds the roll to the total of the rolls made during this move.
  ▪ If the user chooses to roll again, and DOES roll a 6, the function returns 0.
  ▪ If the user chooses not to roll again, the function returns the total of the
  rolls made during this move. Parameters: computer_move, human_move"""
  #The total number of points for this round
  hum_roll_total = 0
  # Sets number of turns taken in this round to 0
  turn_count = 0
  #Automatically rolls the first roll for the player.
  print("You must roll at least once. Let me do that for you.")
  # roll_value is taken from the function roll()
  roll_value = roll()
  #The following if/else statment follows the parameters laid out in the docstring.
  if roll_value != 6:
    hum_roll_total += roll_value
    turn_count += 1
    print("You rolled a", roll_value)
    print("Your total roll from this turn equals", hum_roll_total, ". You rolled", turn_count, "times.")
    print("-------------------------------------------------------------")
    human_score = hum_roll_total
  else:
    human_score = 0
    print("You rolled a six! Your turn is over")
    turn_count = turn_count + 1
    print("Your total roll from this turn equals", human_score, ". You rolled", turn_count, "times.")
    print("-------------------------------------------------------------")
    #Exit the entire function if the automatic first roll is a 6
    return 0

  #Once the first roll has been made, the user is repeatedly asked if they want to roll again until their turn ends.
  while turn_count >=1 and ask_yes_or_no("Do you want to roll again? (Y/N)\n")==True:
    # roll_value is taken from the function roll()
    roll_value = roll()
    # The following if/else statment follows the parameters laid out in the docstring.
    if roll_value != 6:
      hum_roll_total += roll_value
      turn_count += 1
      print("You rolled a", roll_value)
      print("Your total roll from this turn equals", hum_roll_total, ". You rolled",turn_count,"times.")
      print("-------------------------------------------------------------")
      human_score = hum_roll_total
    else:
      human_score = 0
      print("You rolled a six! Your turn is over")
      turn_count = turn_count + 1
      print("Your total roll from this turn equals", human_score, ". You rolled",turn_count,"times.")
      print("-------------------------------------------------------------")
      break
  # The total score for the round is returned as the variable human_score
  return human_score

def main():
  """Executes the program. Parameters: None."""
  print(print_instructions())
  #Set initial values for computer_score and human_score to 0.
  computer_score = 0
  human_score = 0
  #Used to pause the script for 1 second to make things more readable
  time.sleep(1)
  #Ask the user if they want to play. A "N" or "n" ends the program. Otherwise, the following while loop will run
  if ask_yes_or_no("Would you like to play? (Y/N)\n") == True:
    #As long as the is_game_over function is not flagged to False...
    while is_game_over(computer_score, human_score) == False:
      #Increment the computer_score from main() by the score from the computer_move function
      computer_score += computer_move(computer_score,human_score)
      #Print statements are to help the user better see the difference between the computer_move, human_move, and show_current_status output
      print("/////////////////////////////////////////////////////////////")
      show_current_status(computer_score, human_score)
      #Check whether or not the game is over. Even if the computer is ahead, the human player will have one more turn to finish the loop.
      is_game_over(computer_score, human_score)
      print("/////////////////////////////////////////////////////////////")
      time.sleep(1)
      #Alert the human player that it is their turn
      print("It is your turn")
      human_score += human_move(computer_score, human_score)
      time.sleep(1)
      show_current_status(computer_score, human_score)
      print("/////////////////////////////////////////////////////////////")
      time.sleep(1)
      #Check again whether the game is over. Probably redundant.
      is_game_over(computer_score, human_score)
  #Print the final results.
  print("Game Over!!")
  print(show_final_results(computer_score, human_score))

if __name__ == ‘__main__’:
  main()