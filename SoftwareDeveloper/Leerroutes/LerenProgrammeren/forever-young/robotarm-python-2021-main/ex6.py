from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
for i in range(0, 7):
    robotArm.moveRight()
for i in range(0, 8):
    robotArm.grab()
    for x in range(0, 1):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(0, 2):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()