"""
You are in a lunar module, some distance above the Moon's surface. Gravity is pulling you toward the Moon at an
ever-increasing rate of speed. You have a limited amount of fuel to use, and each time you burn fuel,
you reduce your speed by a certain amount. If you burn the right amount of fuel at the right time, you can land
safely (that is, when you reach the Moon's surface, you are not going too fast).
"""

#Define initial values for altitude (m), velocity (m/s), fuel remaining (kg), and fuel usage (kg/m/s)

altitude = 7000
velocity = 1000
fuel_remaining = 500
fuel_burn = 30
burn_constant = 2.5


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

#Print starting art
print(lunarlanderart)

#Ask player if they want to start the game
print("Welcome to Lunar Lander. Would you like to play? (Y/N)")
play = input()

#Set count of seconds to 0. Each maneuver is equal to 1 second.
count = 0

#If the player does want to play, the following data/input loop will run until the altitude is 0 or negative
if play == "Y":
    while altitude > 0:
        print("Your current altitude is", altitude)
        print("Your current velocity is", velocity)
        print("You currently have",fuel_remaining,"kg of fuel remaining.")
        print()

        #try/except block to prevent the program from quitting if the player enters something other than a numerical value
        try:
            #Get input from player about how much fuel they want to burn.
            print("How much fuel would you like to burn?")
            fuel_burn = int(input())

            #Increase maneuver count. Used as a high score
            count += 1

            #If the amount the player inputs is larger than the amount of fuel remaining, set the amount of fuel burned equal to what is remaining in the tank.
            if fuel_burn > fuel_remaining:
                fuel_burn = fuel_remaining
            print("-----------------------------------------")
            fuel_remaining -= fuel_burn

            #Velocity and altitude calculations
            velocity = velocity + 1.6 - (burn_constant*fuel_burn)
            altitude -= velocity

        except:
            print("-----------------------------------------------------------")
            print("Invalid number. Please enter a number betwee 0 and", fuel_remaining)
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

#If altitude is less than or equal to 0m
if altitude <= 0:

    #Player wins if velocity is less than or equal to 5m/s
    if velocity <=5:
        print(landersuccessart)
        print("You've landed safely in",count,"seconds! Game over.")

    else:
        #Player loses if velocity is greater than 5m/s
        print(landerfailureart)
        print("You've crashed and burned after",count,"second. Better luck next time!")

#If the player choses not to play, the program will exit.
if play == "N":
    print("Okay. Restart the program if you change your mind.")