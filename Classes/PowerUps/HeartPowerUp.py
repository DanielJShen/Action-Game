from Classes.PowerUps.PowerUp import PowerUp
from Classes.Utilities.Vector import Vector

class HeartPowerUp(PowerUp):
    def __init__(self):
        self.speedBonus = 5

    def Apply(self,previous, noHearts,health,healthOB,healthList,heart1,HealthIMG,canvas,offset): #Changes the speed within projectile
        if health.heartList[health.last] > 1:
            health.heartList[health.last] = 1
            health.hearts[health.last - 1].frameIndex = [0, 0]
        elif health.last < noHearts:
            health.last += 1
            health.heartList[health.last] = 1
            health.hearts[health.last - 1].frameIndex = [0, 0]
        else:
            noHearts += 1
            healthList.append(HealthIMG(Vector(previous, 50), heart1))
            previous += 50
            health.hearts.append(healthList[noHearts - 1])
            health.heartList.append(1)
            health.last += 1
        return noHearts
        health.draw(noHearts, canvas, offset, healthOB)