from Classes.Vector import Vector

class EnemySuper:
    def __init__(self):
        pass

    def stealthDistance(self, player):
        if self.stealthRange >= (self.pos - player.pos).length() and (self.pos - player.pos).length() > self.soundRange:
            return True
        return False

    def alertDistance(self,enemy2):
        distanceVector = self.pos.copy().subtract(enemy2.pos)
        if distanceVector.length() <= (self.radius+enemy2.radius):
            print("Overlap")
        elif distanceVector.length() < 520:
            enemy2.found = True
            self.found = True

    def inLOS(self, player):
        leftVision: Vector = self.pos.copy().subtract(self.leftgen)
        rightVision: Vector = self.pos.copy().subtract(self.rightgen)
        playerVector = self.pos - player.pos

        if self.length >= playerVector.length():
            if playerVector.angleToX() >= leftVision.angleToX() and playerVector.angleToX() <= rightVision.angleToX():
                self.found = True
                self.normalBoundary.color = "red"
        elif self.length * 2 < playerVector.length():
            self.found = False

    def updateSoundDistance(self, player):
        if self.soundRange >= (self.pos - player.pos).length():
            self.found = True

    def stop(self, player):
        if (self.radius + player.radius) + 20 >= (self.pos - player.pos).length():
            self.direction = Vector(0, 0)

    def follow(self, player):
        self.losColour = 'rgba(255,0,0,0.6)'
        playertest = player.pos.copy().subtract(self.pos)
        self.direction = playertest

    def search(self, player):
        playerVector = self.pos - player.pos
        vectorOfLeft = self.leftBoundary.pA - self.leftBoundary.pB
        Vectorleft = self.pos.copy().subtract(vectorOfLeft)
        Left = self.pos.copy().subtract(Vectorleft)

        angleLess = Left.getNormal().angle(playerVector.getNormal())
        vectorToNormal = (self.normalBoundary.pA - self.normalBoundary.pB)
        VectorNormal = self.pos.copy().subtract(vectorToNormal)
        normal = self.pos.copy().subtract(VectorNormal)

        tester = playerVector.getNormal().angle(normal.getNormal())

        if self.found:
            if round(angleLess, 2) > round(tester, 2):
                self.lineLeftGen.rotate(self.rotation)
                self.normalLine.rotate(self.rotation)
                self.lineRightGen.rotate(self.rotation)
            elif round(angleLess, 2) < round(tester, 2):
                self.lineLeftGen.rotate(-self.rotation)
                self.normalLine.rotate(-self.rotation)
                self.lineRightGen.rotate(-self.rotation)