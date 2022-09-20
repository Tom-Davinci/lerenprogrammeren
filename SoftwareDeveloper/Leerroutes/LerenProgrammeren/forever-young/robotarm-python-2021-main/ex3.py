from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
for i in range(0, 4):
    robotArm.grab()
    for x in range(0, 9):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(0, 9):
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()