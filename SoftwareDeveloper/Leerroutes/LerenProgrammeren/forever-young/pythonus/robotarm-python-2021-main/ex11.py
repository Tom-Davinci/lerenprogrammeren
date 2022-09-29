from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
for i in range(0, 9):
    robotArm.moveRight()
for i in range(0, 11):
    robotArm.grab()
    kleur = robotArm.scan()
    robotArm.moveLeft()
    if kleur == "white":
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
robotArm.wait()