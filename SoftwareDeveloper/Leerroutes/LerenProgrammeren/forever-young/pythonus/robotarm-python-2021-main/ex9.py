from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
teller = 1
for i in range(0,4):
    for i in range(0, teller):
        robotArm.grab()
        for i in range(0,4): robotArm.moveRight()
        robotArm.drop()
        for i in range(0,4): robotArm.moveLeft()
    robotArm.moveRight()
    teller += 1
robotArm.wait()