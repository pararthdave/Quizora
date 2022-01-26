class StageOne:
    def insideHut(self):
        print("\nHello Adventurer! Good luck with your journey into this game. With wit and wisdom you may reach hieghts of Valour.\n")
        choice=input("You wake up in a and look around, the world suddenly appeared to be different and something familiar at the same time.\nYou remember sleeping late at night after playing your favourite game 'Quizora' and this particular place is similar to that. You're in a hut and you look around to find a door. What do you do next?\na.Open it and go outside \nb.Explore the hut\n")
        return choice
    def outsideHut(self):
        choice=input("\nYou see a wizard outside! He's famously known as Zoro as you remember him from game. You\na.Go and talk to him\nb.Run inside and sleep again hoping to wake up in your world.\n")
        return choice
    def wizardConversation(self):
        choice=input("The wizard smiles at you and ask you, how may I help you Adventurer?\na.Ask him how to proceed further in game\nb.Tell him you're a greater wizard as you can vanish a whole pizza in 5 minutes\n")
        return choice
    def stageOneIntro(self):
        print("The wizard said,'You must answer riddles and puzzles, fight demons and collect artifacts and spells, with the sword of thy darkness shall vanish and ligth will prevail!")
        print("There are 10 stages to test you, I shall grant you a magical sword if you answer this question of mine correctly, as I'm no good around those demonic boxes called computers")
        choice=input("Question1\na.\nb.\nc.(correct option)\nd.\n")
        return choice
    def correctAnswerStage1(self):
        print("Very well! That's a correct answer, Here is the magical sword that'll help you around with the quest")
        print("Item Obtained: MAGICAL SWORD <DAMAGE:5, RANGE:1, ATK SPD:3>")
        choice=input("Good Luck with Stage 1\nPress any key to start")
        choice=input("You're teleported in a different world now! Suddenly you spot a dwarf coming to attack you with a wooden sword. You\na.Laugh at him\nb.Get ready to parry that attack with sword.\n")
        return choice
    def dwarfAttackScene1(self):
        print("You got hurt by a wood splinter that later caused infection eventually leading you to your death. GAME OVER!")
        print("Never underestimate the problem, no matter how small and puny it seems... ")
    def dwarfAttackScene2(self):
        print("You successfully blocked the attack and prepare your sword to inflict a strike. Answer this question to kill the dwarf in a single blow.")
        choice=input("QUESTION2\na.\nb.(correct answer)\nc.\nd.\n")
        return choice
    def ogreAttackIntro(self):
        print("Congratulations you've killed your very first monster! Way to go.../nREMAINING HP:100%")
        print("You see another monster approaching, it looks like an ogre directly from fairytales. His belly is dancing rhythmetically with each step and he's carrying a huge club")
        choice=input("What do you do next?\na.Run away into the woods\nb.Fight the huge ogre\n")
        return choice
    def ogreAttackScene1(self):
        print("You ran away into forest, after running for a while you feel safe. But now you're lost!")
        print("Stage One completed successfully!!!")
    def ogreAttackScene2(self):
        print("The ogre landed his club directly on your head as you try to attack him, leaving you unconcious. You should know when to run and when to attack...\n GAME OVER!")
    def dwarfTwoStrike(self):
        print("Ohh no, the sword strike only lowered half of dwarf's HP, he attacked you again with his wodden sword lowering your HP to 60%")
        print("You killed the dwarf with your next sword strike \nREMAINING HP:60%\n")
        print("You see another monster approaching, it looks like an ogre directly from fairytales. His belly is dancing rhythmetically with each step and he's carrying a huge club")
        choice=input("What do you do next?\na.Run away into the woods\nb.Fight the huge ogre\n")
        return choice
    def incorrectAnswerStage1(self):
        print("It's an incorrect answer, the sword only serves wisdom...\nGAME OVER!")
    def mockWizard(self):
        print("You dare make fun of me mortal! I've been here since the beginning of time...\n")
        print("The wizard waves his staff and you are immediately teleported to the real world\nGAME OVER!")
    def exploreHut(self):
        print("You found nothing of interest inside the hut")
        choice=input("What do you do next?\na.Go outside\nb.Get back to sleep hoping to wake up in your world again\n")
        return choice
    def invalidChoice(self):
        print("Invalid Choice!")
    def gameOver(self):
        print("GAME OVER!")

