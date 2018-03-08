try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.healthIMG import HealthIMG


class Health(HealthIMG):
    def __init__(self,first:HealthIMG,second:HealthIMG,third:HealthIMG):
        self.hearts = [first,second,third]
        self.heart1=self.heart2=self.heart3=self.heart4 = 1
        self.heartList = [self.heart1,self.heart2,self.heart3,self.heart4]
        self.last = 3

    def damageTaken(self):
        if self.last > 0:
            if self.heartList[self.last] == 1:
                self.heartList[self.last] = 2
                self.hearts[self.last-1].frameIndex = [1,0]
            elif self.heartList[self.last] == 2:
                self.heartList[self.last] = 3
                self.hearts[self.last-1].frameIndex = [2,0]
            elif self.heartList[self.last] == 3:
                self.heartList[self.last] = 4
                self.hearts[self.last-1].frameIndex = [3,0]
            elif self.heartList[self.last] == 4:
                self.hearts[self.last-1].frameIndex = [4,0]
                self.last -= 1
        else:
            print("DEAD")




