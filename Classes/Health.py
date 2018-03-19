try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.healthIMG import HealthIMG


class Health(HealthIMG):
    def __init__(self,healthList,noHearts):
        self.hearts:list = healthList
        self.heartList = []
        for i in range(0,self.hearts.__len__()+1):
            self.heart = 1
            self.heartList.append(self.heart)
        self.lastHeart = noHearts
        self.last = noHearts
        print(self.last , "test")

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



