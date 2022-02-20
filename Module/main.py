from re import A
from pyrsistent import b
from StageOneWrapper import StageWrapper
from StageTwoWrapper import Stage2Wrapper
choice=input("Welcome to Quizora! an epic fantasy quiz game. Enter your choice (a/b/c/d) \n a. Play \n b. Help\n>") 
print(choice)
stg1w=StageWrapper()
clr=stg1w.stageOneWrap()
if clr!=0:
    stg2w=Stage2Wrapper()
    stg2w.stage2Wrap()