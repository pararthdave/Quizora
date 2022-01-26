from stage1 import StageOne
choice=input("Welcome to Quizora! an epic fantasy quiz game. Enter your choice (a/b/c/d) \n a. Play \n b. Help\n")   #intro
stg1flag=0  #flag that marks completetion of first stage
stg1 = StageOne()    #class instance
if choice.lower().strip()=='a':
    choice = stg1.insideHut()   #scene inside the hut
    if choice.lower().strip()=='a':
        choice=stg1.outsideHut()   #scene outside the hut
        if choice.lower().strip()=='a':
            choice=stg1.wizardConversation()    #conversation with the wizard Zoro
            if choice.lower().strip()=='a':
                choice=stg1.stageOneIntro()   #Introduction to stage 1
                if choice.lower().strip()=='c':
                    choice=stg1.correctAnswerStage1()   #Correct Answer 1 Scene
                    if choice.lower().strip()=='a':
                        stg1.dwarfAttackScene1()    #Dwarf attack
                    elif choice.lower().strip()=='b':
                        choice=stg1.dwarfAttackScene2()   #Second alternative dwarf attack
                        if choice.lower().strip()=='b':
                            choice=stg1.ogreAttackIntro()   #ogre attack
                            if choice.lower().strip()=='a':
                                stg1.ogreAttackScene1()    #choice 1 ogre attack
                            else:
                                stg1.ogreAttackScene2()  #choice 2 ogre attack
                        else:
                            choice=stg1.dwarfTwoStrike()  #incorrect answer scene dwarf attack
                            if choice.lower().strip()=='a':
                                stg1.ogreAttackScene1()    #choice 1 ogre attack
                            else:
                                stg1.ogreAttackScene2()
                    else:
                        stg1.invalidChoice()   
                else: 
                    stg1.incorrectAnswerStage1()     #incorrect answer question from wizard
            else:
                stg1.mockWizard()   #making fun of wizard
        else: 
            stg1.gameOver()
    else:
        choice=stg1.exploreHut()   #exploring hut
        if choice.lower().strip()=='a':
            choice=stg1.wizardConversation()    #conversation with the wizard Zoro
            if choice.lower().strip()=='a':
                choice=stg1.stageOneIntro()   #Introduction to stage 1
                if choice.lower().strip()=='c':
                    choice=stg1.correctAnswerStage1()   #Correct Answer 1 Scene
                    if choice.lower().strip()=='a':
                        stg1.dwarfAttackScene1()    #Dwarf attack
                    elif choice.lower().strip()=='b':
                        choice=stg1.dwarfAttackScene2()   #Second alternative dwarf attack
                        if choice.lower().strip()=='b':
                            choice=stg1.ogreAttackIntro()   #ogre attack
                            if choice.lower().strip()=='a':
                                stg1.ogreAttackScene1()    #choice 1 ogre attack
                            else:
                                stg1.ogreAttackScene2()  #choice 2 ogre attack
                        else:
                            choice=stg1.dwarfTwoStrike()  #incorrect answer scene dwarf attack
                            if choice.lower().strip()=='a':
                                stg1.ogreAttackScene1()    #choice 1 ogre attack
                            else:
                                stg1.ogreAttackScene2()
                    else:
                        stg1.invalidChoice()   
                else: 
                    stg1.incorrectAnswerStage1()     #incorrect answer question from wizard
            else:
                stg1.mockWizard()   #making fun of wizard
        else: 
            stg1.gameOver()
else:
    print("Help")
