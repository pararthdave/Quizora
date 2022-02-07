class StageTwo:
    def lostWoods(self):
        print("You're lost in forest and feeling immensely tired")
        print("Suddenly you see a humanoid figure arising from river, your first instinct is to runaway and hide.\nBut Alas! You're too tired to do so you just stand there and accept the fate.")
        print("You hear a soft voice as you except the destiny to fall upon you,'Hello Stranger, I'm nature spirit of this river. I offer you a small quest to take relax your ordeal.\nI'll ask you 5 questions of which, if you answered all correctly I'll guide you a safe passage out of woods.\nAnswer at least 3 correctly and I'll replenish your health.\nIn addition to that I shall grant you fire spell as well.'\nPress any button to continue")
        qflag=0
        choice=input("Question1\na.\nb.\nc.\nd.(Correct Option)\n>")
        if choice.lower().strip()=='d':
            qflag+=1
            print("Correct!")
        else:
            print("Incorrect!")
        choice=input("Question2\na.\nb.\nc.\nd.(Correct Option)\n>")
        if choice.lower().strip()=='d':
            qflag+=1
            print("Correct!")
        else:
            print("Incorrect!")
        choice=input("Question3\na.\nb.\nc.\nd.(Correct Option)\n>")
        if choice.lower().strip()=='d':
            qflag+=1
            print("Correct!")
        else:
            print("Incorrect!")
        choice=input("Question4\na.\nb.\nc.\nd.(Correct Option)\n>")
        if choice.lower().strip()=='d':
            qflag+=1
            print("Correct!")
        else:
            print("Incorrect!")
        choice=input("Question5\na.\nb.\nc.\nd.(Correct Option)\n>")
        if choice.lower().strip()=='d':
            qflag+=1
            print("Correct!")
        else:
            print("Incorrect!")
        if qflag<3:
            print("Game Over")
        elif qflag>=3 and qflag<5:
            print("Energy Replenished!")
        elif qflag==5:
            print("Stage 2 cleared! You're out of the forest and in a safe camp now.")
        return qflag
    def pitfall(self):
        print("While roaming aimlessly you suddenly feel ground vanishing beanith your feet, you find yourself in a deep pit and it's all dark here.")
        input("It seems like it's right time to use your newly learned fire spell, press any key to cast spell")
        print("A orb of fire appears in front of you illuminating the pit, in the bright light you see a vine climbing up the pit. You use it and succefully climb out of the pit. And continue towards your journey.")
    def outofwoods(self):
        print("You see a portal that leads you to the safe camp, but as you approach a guardian appears in front of you. Answer this question correctly and then only you'll be allowed to travel through my portal. Answer incorrectly and I shall perish you with a flick of finger.")
        choice=input("Question\na.\nb.(Correct Option)\nc.\nd.\n>")
        if choice.lower().strip()=='b':
            print("Very good! you may travel through portal")
            print("Stage 2 cleared succefully! You find yourself in a safe camp now.")
        else:
            print("Incorrect!!!\nThe guardian vaporized you in a single second.\nGAME OVER")
