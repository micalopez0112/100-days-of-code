print("""
    :"'._..---.._.'";
    `.             .'
    .'    ^   ^    `.
   :      a   a      :                 __....._
   :     _.-0-._     :---'""'"-....--'"        '.
    :  .'   :   `.  :                          `,`.
     `.: '--'--' :.'                             ; ;
      : `._`-'_.'                                ;.'
      `.   '"'                                   ;
       `.               '                        ;
        `.     `        :           `            ;
         .`.    ;       ;           :           ;
       .'    `-.'      ;            :          ;`.
   __.'      .'      .'              :        ;   `.
 .'      __.'      .'`--..__      _._.'      ;      ;
 `......'        .'         `'""'`.'        ;......-'
jgs    `.......-'                 `........'      """)
print("Welcome to treasure hunt island!")
print("Your mission is to find the treasure.")
print("You are at a crossroad. Where do you want to go? Type 'left' or 'right'")
choice1 = input()
if choice1 == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    choice2 = input()
    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        choice3 = input()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fall into a hole. Game Over.")