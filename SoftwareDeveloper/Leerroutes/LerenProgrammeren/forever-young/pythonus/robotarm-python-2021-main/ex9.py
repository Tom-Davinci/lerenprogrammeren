from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for i in range(0,4):
    for i in range(0, 4):
        robotArm.grab()
        for i in range(0,4):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(0,4):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()