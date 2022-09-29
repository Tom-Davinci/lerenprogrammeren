from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
teller = 9
while teller > 0:
    robotArm.grab()
    for i in range(0, teller):
        robotArm.moveRight()
    teller -= 1
    robotArm.drop()
    for i in range(0, teller):
        robotArm.moveLeft()
    teller -= 1
robotArm.wait()