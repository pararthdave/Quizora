choice=input("Welcome to Quizora! an epic fantasy quiz game. Enter your choice (a/b/c/d) \n a. Play \n b. Help\n")
stg1flag=0
if choice.lower().strip()=='a': #main game menu
    print("\nHello Adventurer! Good luck with your journey into this game. With wit and wisdom you may reach hieghts of Valour.\n")
    choice=input("You wake up in a and look around, the world suddenly appeared to be different and something familiar at the same time.\nYou remember sleeping late at night after playing your favourite game 'Quizora' and this particular place is similar to that. You're in a hut and you look around to find a door. What do you do next?\na.Open it and go outside \nb.Explore the hut\n")
    if choice.lower().strip()=='a':
        choice=input("\nYou see a wizard outside! He's famously known as Zoro as you remember him from game. You\na.Go and talk to him\nb.Run inside and sleep again hoping to wake up in your world.\n")
        if choice.lower().strip()=='a':
            choice=input("The wizard smiles at you and ask you, how may I help you Adventurer?\na.Ask him how to proceed further in game\nb.Tell him you're a greater wizard as you can vanish a whole pizza in 5 minutes\n")
            if choice.lower().strip()=='a':
                print("The wizard said,'You must answer riddles and puzzles, fight demons and collect artifacts and spells, with the sword of thy darkness shall vanish and ligth will prevail!")
                print("There are 10 stages to test you, I shall grant you a magical sword if you answer this question of mine correctly, as I'm no good around those demonic boxes called computers")
                choice=input("Question1\na.\nb.\nc.(correct option)\nd.")
                if choice.lower().strip()=='c':
                    print("Very well! That's a correct answer, Here is the magical sword that'll help you around with the quest")
                    print("Item Obtained: MAGICAL SWORD <DAMAGE:5, RANGE:1, ATK SPD:3>")
                    choice=input("Good Luck with Stage 1\nPress any key to start")
                    choice=input("You're teleported in a different world now! Suddenly you spot a dwarf coming to attack you with a wooden sword. You\na.Laugh at him\nb.Get ready to parry that attack with sword.\n")
                    if choice.lower().strip()=='a':
                        print("You got hurt by a wood splinter that later caused infection eventually leading you to your death. GAME OVER!")
                        print("Never underestimate the problem, no matter how small and puny it seems...x ")
                    elif choice.lower().strip()=='b':
                        print("You successfully blocked the attack and prepare your sword to inflict a strike. Answer this question to kill the dwarf in a single blow.")
                        choice=input("QUESTION2\na.\nb.(correct answer)\nc.\nd.\n")
                        if choice.lower().strip()=='b':
                            print("Congratulations you've killed your very first monster! Way to go.../nREMAINING HP:100%")
                            print("You see another monster approaching, it looks like an ogre directly from fairytales. His belly is dancing rhythmetically with each step and he's carrying a huge club")
                            choice=input("What do you do next?\na.Run away into the woods\nb.Fight the huge ogre\n")
                            if choice.lower().strip()=='a':
                                print("You ran away into forest, after running for a while you feel safe. But now you're lost!")
                                print("Stage One completed successfully!!!")
                            else: 
                                print("The ogre landed his club directly on your head as you try to attack him, leaving you unconcious. You should know when to run and when to attack...\n GAME OVER!")
                        else:
                            print("Ohh no, the sword strike only lowered half of dwarf's HP, he attacked you again with his wodden sword lowering your HP to 60%")
                            choice=input("You killed the dwarf with your next sword strike \nREMAINING HP:60%\n")
                            print("You see another monster approaching, it looks like an ogre directly from fairytales. His belly is dancing rhythmetically with each step and he's carrying a huge club")
                            choice=input("What do you do next?\na.Run away into the woods\nb.Fight the huge ogre\n")
                            if choice.lower().strip()=='a':
                                print("You ran away into forest, after running for a while you feel safe. But now you're lost!")
                                print("Stage One completed successfully!!!")
                                stg1flag=1
                            else: 
                                print("The ogre landed his club directly on your head as you try to attack him, leaving you unconcious. You should know when to run and when to attack...\n GAME OVER!")
                    else:
                        print("Invalid Choice!")
                else:
                    print("It's an incorrect answer, the sword only serves wisdom...")
            else:
               print("You dare make fun of me mortal! I've been here since the beginning of time...\n")
               print("The wizard waves his staff and you are immediately teleported to the real world\nGAME OVER!")     
        else:
            print("GAME OVER!")
    elif choice.lower().strip()=='b':
        print("You found nothing of interest inside the hut")
        choice=input("What do you do next?\na.Go outside\nb.Get back to sleep hoping to wake up in your world again\n")
        if choice.lower().strip()=='a':
            choice=input("\nYou see a wizard outside! He's famously known as Zoro as you remember him from game. You\na.Go and talk to him\nb.Run inside and sleep again hoping to wake up in your world.\n")
            if choice.lower().strip()=='a':
                choice=input("The wizard smiles at you and ask you, how may I help you Adventurer?\na.Ask him how to proceed further in game\nb.Tell him you're a greater wizard as you can vanish a whole pizza in 5 minutes\n")
            if choice.lower().strip()=='a':
                print("The wizard said,'You must answer riddles and puzzles, fight demons and collect artifacts and spells, with the sword of thy darkness shall vanish and ligth will prevail!")
                print("There are 10 stages to test you, I shall grant you a magical sword if you answer this question of mine correctly, as I'm no good around those demonic boxes called computers")
                choice=input("Question1\na.\nb.\nc.(correct option)\nd.")
                if choice.lower().strip()=='c':
                    print("Very well! That's a correct answer, Here is the magical sword that'll help you around with the quest")
                    print("Item Obtained: MAGICAL SWORD <DAMAGE:5, RANGE:1, ATK SPD:3>")
                    choice=input("Good Luck with Stage 1\nPress any key to start")
                    choice=input("You're teleported in a different world now! Suddenly you spot a dwarf coming to attack you with a wooden sword. You\na.Laugh at him\nb.Get ready to parry that attack with sword.\n")
                    if choice.lower().strip()=='a':
                        print("You got hurt by a wood splinter that later caused infection eventually leading you to your death. GAME OVER!")
                        print("Never underestimate the problem, no matter how small and puny it seems...x ")
                    elif choice.lower().strip()=='b':
                        print("You successfully blocked the attack and prepare your sword to inflict a strike. Answer this question to kill the dwarf in a single blow.")
                        choice=input("QUESTION2\na.\nb.(correct answer)\nc.\nd.\n")
                        if choice.lower().strip()=='b':
                            print("Congratulations you've killed your very first monster! Way to go.../nREMAINING HP:100%")
                            print("You see another monster approaching, it looks like an ogre directly from fairytales. His belly is dancing rhythmetically with each step and he's carrying a huge club")
                            choice=input("What do you do next?\na.Run away into the woods\nb.Fight the huge ogre\n")
                            if choice.lower().strip()=='a':
                                print("You ran away into forest, after running for a while you feel safe. But now you're lost!")
                                print("Stage One completed successfully!!!")
                            else: 
                                print("The ogre landed his club directly on your head as you try to attack him, leaving you unconcious. You should know when to run and when to attack...\n GAME OVER!")
                        else:
                            print("Ohh no, the sword strike only lowered half of dwarf's HP, he attacked you again with his wodden sword lowering your HP to 60%")
                            choice=input("You killed the dwarf with your next sword strike \nREMAINING HP:60%\n")
                            print("You see another monster approaching, it looks like an ogre directly from fairytales. His belly is dancing rhythmetically with each step and he's carrying a huge club")
                            choice=input("What do you do next?\na.Run away into the woods\nb.Fight the huge ogre\n")
                            if choice.lower().strip()=='a':
                                print("You ran away into forest, after running for a while you feel safe. But now you're lost!")
                                print("Stage One completed successfully!!!")
                                stg1flag=1
                            else: 
                                print("The ogre landed his club directly on your head as you try to attack him, leaving you unconcious. You should know when to run and when to attack...\n GAME OVER!")
                    else:
                        print("Invalid Choice!")
                else:
                    print("It's an incorrect answer, the sword only serves wisdom...")
            else:
               print("You dare make fun of me mortal! I've been here since the beginning of time...\n")
               print("The wizard waves his staff and you are immediately teleported to the real world\nGAME OVER!")     
        else:
            print("GAME OVER!")
    else:
        print("Invalid Choice!")
elif choice.lower().strip()=='b': #main game menu
    print("Welcome to the help section!\n")
else:
    print("Invalid Choice!")
if stg1flag==1:
    print("Congratulations on completeing first stage!!!")
else:
    print("Try again and win this, may the devs be with you...")