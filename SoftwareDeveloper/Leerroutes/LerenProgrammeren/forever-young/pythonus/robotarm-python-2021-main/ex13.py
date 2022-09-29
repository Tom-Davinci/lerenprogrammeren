from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
teller = 1
while teller < 9:
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "":
        robotArm.wait()
    for i in range(0, teller):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(0, teller):
        robotArm.moveLeft()
    teller += 1
robotArm.wait()