import copy
import random
DEBUG=False
# Consider using the modules imported above.

class Hat:
    def __init__(self,**allcolor):
        self.contents=[]
        for key,value in allcolor.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self,draws):
        result=[]
        if len(self.contents)<draws:
            for i in range(len(self.contents)):
                result.append(self.contents[i])
            self.contents.clear()
            return result
        else:
            for i in range(draws):
                rand = random.randint(0,len(self.contents)-1)
                result.append(self.contents[rand])
                self.contents.pop(rand)
            return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success=0
    testcases=[]
    expectedballs=[]
    for i in range(num_experiments):
        testcases.append(copy.deepcopy(hat))
    for i in range(num_experiments):
        expectedballs.append(copy.deepcopy(expected_balls))
    if DEBUG:
        for i in range(len(hat.contents)):
            print(hat.contents[i])
        print(expected_balls)
        print(num_balls_drawn)
        print(num_experiments)
    for i in range(num_experiments):
        result=testcases[i].draw(num_balls_drawn)
        for j in result:
            if (j in expectedballs[i]) and (expectedballs[i][j]!=0):
                expectedballs[i][j]=expectedballs[i][j]-1
        if all(x == 0 for x in expectedballs[i].values()):
            success=success+1
        

    return success/num_experiments
