from Classes.Vector import Vector

class View:
    
    def __init__(self):
        pass
    
    def moveScreen(self,offset,playerPos,width,height):
        charPosMinOffset = playerPos + offset
        center = Vector(width/2, height/2)
        maxDisplacement = height * (4 / 5) - center.y
        minDisplacement = height * (11 / 20) - center.y
        #Right
        if charPosMinOffset.x > center.x+maxDisplacement:
            offset.subtract(Vector(abs(center.x+maxDisplacement - charPosMinOffset.x), 0))
        elif charPosMinOffset.x > center.x+minDisplacement:
            offset.subtract(Vector(abs((center.x+minDisplacement) - charPosMinOffset.x)/50, 0))
        #Left
        if charPosMinOffset.x < center.x-maxDisplacement:
            offset.add(Vector(abs((center.x-maxDisplacement) - charPosMinOffset.x), 0))
        elif charPosMinOffset.x < center.x-minDisplacement:
            offset.add(Vector(abs((center.x-minDisplacement) - charPosMinOffset.x)/50, 0))

        #Down
        if charPosMinOffset.y > center.y+maxDisplacement:
            offset.subtract(Vector(0, abs(charPosMinOffset.y - (center.y+maxDisplacement))))
        if charPosMinOffset.y > center.y+minDisplacement:
            offset.subtract(Vector(0, abs(charPosMinOffset.y - (center.y+minDisplacement))/50))

        #Up
        if charPosMinOffset.y < center.y-maxDisplacement:
            offset.add(Vector(0, abs(charPosMinOffset.y - (center.y-maxDisplacement))))
        if charPosMinOffset.y < center.y-minDisplacement:
            offset.add(Vector(0, abs(charPosMinOffset.y - (center.y-minDisplacement))/50))