import libhousy
#You can define helper functions here, make sure to but them *above* the main function
def launch(robot):
    robot.beltZ1.Set(-0.8)
    robot.beltZ2.Set(-0.8)
    robot.beltZ3.Set(1)
    robot.upperTension.Extend()
    robot.lowerTension.Retract()




def main(robot: libhousy.robot):
#Here is where your recurring code will go
    if robot.controller.getButton(robot.controller.Button.rBumper):
        robot.shootWheel.Set(1)

    else:
        robot.shootWheel.Set(0)

    if (robot.controller.getAxis(robot.controller.Axis.rTrigger) > 0.8 and robot.controller.getButton(robot.controller.Button.rBumper)):
        launch(robot)

    else:
        robot.beltZ1.Set(0)
        robot.beltZ2.Set(0)
        robot.beltZ3.Set(0)
       
    
