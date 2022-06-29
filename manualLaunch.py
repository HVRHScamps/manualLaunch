# inclue code to help us talk to the robot
import libhousy

def main(robot: libhousy.robot):
    # Here is where your recurring code will go
    if  robot.controller.getButton(robot.controller.Button.rBumper):
        robot.shootWheel.Set(1)
    else:
        robot.shootWheel.Set(0)

        if robot.controller.getAxis(robot.controller.Axis.rTrigger) >=.8:
            robot.beltZ1.Set(-0.8)
            robot.beltZ2.Set(-0.8)
            robot.beltZ3.Set(1)
            robot.upperTension.Extend()
            robot.lowerTension.Retract()
        else:
            robot.pickupMotor.Set(0)
            robot.pickupPneumatic.Retract()
            robot.beltZ1.Set(0)
            robot.beltZ2.Set(0)
            robot.beltZ3.Set(0)

    

    

    # After everything is done, we tell the main program to stop us

