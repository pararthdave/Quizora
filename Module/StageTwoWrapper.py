from stage2 import StageTwo
class Stage2Wrapper:
    def stage2Wrap(self):
        stg2=StageTwo()
        flag=stg2.lostWoods()
        if flag<5:
            stg2.pitfall()
            stg2.outofwoods()
