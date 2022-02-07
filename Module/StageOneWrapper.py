from stage1 import StageOne
from wizardconv import Wizard
class StageWrapper:
    
    def stageOneWrap(self):
        stg1 = StageOne()
        clear1=0
        choice='a'
        wz=Wizard()    #class instance
        if choice.lower().strip()=='a':
            choice = stg1.insideHut()   #scene inside the hut
            if choice.lower().strip()=='a':
                choice=stg1.outsideHut()   #scene outside the hut
                if choice.lower().strip()=='a':
                    choice=stg1.wizardConversation()  
                    if choice.lower().strip()=='a':  #conversation with the wizard Zoro
                        wz.wizardconversationpass()
                        clear1+=1
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
                        clear1+=1
                    else:
                        stg1.mockWizard()   #making fun of wizard
        else:
            print("Help")
        return clear1
        
