from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 3
for i in range(0, 6):
    robotArm.moveRight()
    for i in range(0, 6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()
robotArm.wait()