class Robot():
    class Robot1():
        def __init__(self):
            pass
    def __init__(self):
        self.robotRot = 0
        self.targetRot = 0
        self.rotSpeed = 1
    
    def RotateToTarget(self, target):
        self.targetRot = target

        deltaRot = self.targetRot - self.robotRot
        if(deltaRot > 0):
            if(deltaRot < 180):
                pass
                #L
            else:
                pass
                #R
        else:
            if(deltaRot < -180):
                pass
                #L
            else:
                pass
                #R
