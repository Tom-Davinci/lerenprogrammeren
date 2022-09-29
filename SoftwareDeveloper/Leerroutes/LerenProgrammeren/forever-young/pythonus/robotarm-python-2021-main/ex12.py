from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
teller = 9
while teller < 10:
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "red":
        for i in range(0, teller):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(0, teller):
            robotArm.moveLeft()
        robotArm.moveRight()
    else:
        robotArm.drop()
        robotArm.moveRight()
    teller -= 1
robotArm.wait()