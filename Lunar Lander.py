
"""
Rachael Howard
82772985
I worked alone without help.
Win: 0,0,0,0,10,10,0,10,10,10,10,20,20,0,0
Loss: 0,0,0,0,0,0,0,0,0,0,0
"""

#Define the function game(), which contains the entire game.
def game():

    #Define initial values for altitude (m), velocity (m/s), fuel remaining (liters), and fuel usage (liters/m/s)
    altitude = 100
    velocity = 0
    fuel_remaining = 100
    burn_constant = 0.15


    #Starting art.
    #ASCII Image from lgbeard at https://www.asciiart.eu/space/spaceships.
    #ASCII Font from http://patorjk.com/software/taag/#p=display&h=0&v=0&f=Big&t=Lunar%20Lander


    lunarlanderart = """
                             ____
                            /___.`--.____ .--. ____.--(
                                   .'_.- (    ) -._'.
                                 .'.'    |'..'|    '.'.
                          .-.  .' /'--.__|____|__.--'\ '.  .-.
                         (O).)-| |  \    |    |    /  | |-(.(O)
                          `-'  '-'-._'-./      \.-'_.-'-'  `-'
                             _ | |   '-.________.-'   | | _
                          .' _ | |     |   __   |     | | _ '.
                         / .' ''.|     | /    \ |     |.'' '. \ 
                         | |( )| '.    ||      ||    .' |( )| |
                         \ '._.'   '.  | \    / |  .'   '._.' /
                          '.__ ______'.|__'--'__|.'______ __.'
                         .'_.-|         |------|         |-._'.
                        //\   |         |--::--|         |  //\ \ 
                       //  \  |         |--::--|         | //  \ \ 
                      //    \ |        /|--::--|\        |//    \ \ 
                     / '._.-'/|_______/ |--::--| \_______|\`-._.'  \ 
                    / __..--'        /__|--::--|__\        `--..__  \ 
                   / /               '-.|--::--|.-'               \  \ 
                  / /                   |--::--|                   \  \ 
                 / /                    |--::--|                    \  \ 
             _.-'  `-._                 _..||.._                  _.-` '-._
            '--..__..--'               '-.____.-'                '--..__..-'
    
    
      _                                         _                            _               
     | |                                       | |                          | |              
     | |       _   _   _ __     __ _   _ __    | |        __ _   _ __     __| |   ___   _ __ 
     | |      | | | | | '_ \   / _` | | '__|   | |       / _` | | '_ \   / _` |  / _ \ | '__|
     | |____  | |_| | | | | | | (_| | | |      | |____  | (_| | | | | | | (_| | |  __/ | |   
     |______|  \__,_| |_| |_|  \__,_| |_|      |______|  \__,_| |_| |_|  \__,_|  \___| |_|   
                                                                                             
    """

    #Print starting art and welcome
    print(lunarlanderart)
    print("Welcome to Lunar Lander!")

    #Set count of seconds to 0. Each maneuver is equal to 1 second.
    count = 0

    #The following data/input loop will run until the altitude is 0 or negative
    while altitude > 0:
        print("Your current altitude is", altitude,"m")
        print("Your current velocity is", round(velocity,2),"m/s")
        print("You currently have",fuel_remaining,"liters of fuel remaining.")
        print()

        #Try/except block to prevent the program from quitting if the player enters something other than a numerical value
        try:
            #Get input from player about how much fuel they want to burn.
            print("How much fuel would you like to burn?")
            fuel_used = int(input())

            #Increase maneuver count.
            count += 1

            #If the player enters a negative number, they burn 0 fuel
            if fuel_used < 0:
                fuel_used = 0
                print("-----------------------------------------")
                fuel_remaining -= fuel_used

            #If the amount the player inputs is larger than the amount of fuel remaining, set the amount of fuel burned equal to what is remaining in the tank.
            elif fuel_used > fuel_remaining:
                fuel_used = fuel_remaining
                print("-----------------------------------------")
                fuel_remaining = 0

            elif fuel_used > 0 and fuel_used <= fuel_remaining:
                print("-----------------------------------------")
                fuel_remaining = fuel_remaining - fuel_used


            #Velocity increases by 1.6 m/s and decreases by the amount proportional (burn constant) to the fuel used
            velocity = velocity + 1.6 - (burn_constant*fuel_used)
            #Altitude decreases by velocity
            altitude -= velocity

        except:
            print("-----------------------------------------------------------")
            print("Invalid number. Please enter a number between 0 and", fuel_remaining)
            print("-----------------------------------------------------------")
            continue

    #Lander success art from https://www.asciiart.eu/space/spaceships
    landersuccessart = """
                       /                      _
                      <=                     <_K
                      |\ 
              \|/     |
               |______|
               /       \ 
              / /_\ /_\ \ 
              |   : :   |
             /|   : :   |\               _   ...
            : |  /___\  | :            _| |  ...~~~~~
            : |  [   ]  | ;           ( |U|  ...~~~~~
             \|  [   ]  |/             A|S|  ~~~~~~~~
          +-------|-|-------+          H|A|  ~~~~~~~~
         /|       |-|       |\         H|_|  |
        /\|       |-|       |/\        HIp   |
       /  +-------|-|-------+  \       wII   |
      /          /|-|\          \       II   |
     /            |-|            \      II   |
    `-'           |-|           `-'    cxI   |
                 `---'
    """
    #Lander failure art from https://www.asciiart.eu/weapons/explosives
    landerfailureart = """
                                   ________________
                              ____/ (  (    )   )  \___
                             /( (  (  )   _    ))  )   )\ 
                           ((     (   )(    )  )   (   )  )
                         ((/  ( _(   )   (   _) ) (  () )  )
                        ( (  ( (_)   ((    (   )  .((_ ) .  )_
                       ( (  )    (      (  )    )   ) . ) (   )
                      (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                      ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                     ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                      (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                     ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                      ((  (   )(    (     _    )   _) _(_ (  (_ )
                       (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                       ((__)        \|||lll|l||///          \_))
                                (   /(/ (  )  ) )\   )
                              (    ( ( ( | | ) ) )\   )
                               (   /(| / ( )) ) ) )) )
                             (     ( ((((_(|)_)))))     )
                              (      ||\(|(|)|/||     )
                            (        |(||(||)||||        )
                              (     //|/l|||)|\ \     )
                            (/ / //   /|//||||\  \ \  \ _)
    
    """

    #If altitude is less than or equal to 0m, the game is over.
    if altitude <= 0:

        #Player wins if velocity is less than 10 m/s
        if velocity < 10:
            print(landersuccessart)
            print("You've landed safely in",count,"seconds at a velocity of",round(velocity,2),"m/s.")
            print("You had",fuel_remaining,"liters of fuel remaining. Game over.")
            #Initialize play function to ask player if they want to play again
            play()

        else:
            #Player loses if velocity is greater than or equal to 10 m/s
            print(landerfailureart)
            print("You've crashed and burned after",count,"seconds at a velocity of",round(velocity,2),"m/s.")
            print("You had", fuel_remaining, "liters of fuel remaining. Game over.")
            # Initialize play function to ask player if they want to play again
            play()


#Ask again function just reruns the play function.
def askagain():
    return play()

#Play function
def play():
    #Ask player if they want to play again
    play = input("Do you want to play again? (Y/N)\n")

    #If the player choses to play, the game restarts.
    if (play == "y" or play == "Y"):
        game()

    #If the player choses not to play, the program will exit.
    elif (play == "n" or play == "N"):
        print("Okay. Restart the program if you change your mind.")

    #If the player enters anything but Y,y,N,n, the askagain function is initialized. It will continue to run until they enter a valid input.
    else:
        askagain()

#Initialize game
game()