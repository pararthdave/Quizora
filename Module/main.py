from stage1 import StageOne
from wizardconv import Wizard
choice=input("Welcome to Quizora! an epic fantasy quiz game. Enter your choice (a/b/c/d) \n a. Play \n b. Help\n")   #intro
stg1flag=0  #flag that marks completetion of first stage
stg1 = StageOne()
wz=Wizard()    #class instance
if choice.lower().strip()=='a':
    choice = stg1.insideHut()   #scene inside the hut
    if choice.lower().strip()=='a':
        choice=stg1.outsideHut()   #scene outside the hut
        if choice.lower().strip()=='a':
            choice=stg1.wizardConversation()  
            if choice.lower().strip()=='a':  #conversation with the wizard Zoro
                wz.wizardconversationpass()
            else:
                stg1.mockWizard()   #making fun of wizard
        else: 
            stg1.gameOver()
    else:
        choice=stg1.exploreHut()   #exploring hut
        if choice.lower().strip()=='a':
            choice=stg1.wizardConversation()    #conversation with the wizard Zoro
            if choice.lower().strip()=='a':  #conversation with the wizard Zoro
                wz.wizardconversationpass()
            else:
                stg1.mockWizard()   #making fun of wizard
else:
    print("Help")
