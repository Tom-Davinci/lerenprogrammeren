from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for i in range(0, 3):
    robotArm.grab()
    for x in range(0, 1):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(0, 1):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()