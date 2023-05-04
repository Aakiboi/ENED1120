#!/usr/bin/env pybricks-micropython

""" def subTask1a():
    laps = 4
    dist = 900
    for i in range(laps):
        driving(dist)
        print(robot.distance())
        wait(5)
        driving(-dist)
        print(robot.distance())
        wait(5)



def brakeRobot(lm, rm):
    lm.brake()
    rm.brake()


def subTask1b():
    laps = int(input("Enter number of laps: "))
    dist = float(input("Enter distance (m): ")) * 1000
    j = 180
    for i in range(laps):
        driving(dist)
        turnRobot(j)
        print(robot.distance())
        wait(5)
        driving(dist)
        print(robot.distance())
        turnRobot(-180)
        j -= 1 """

# Function for all tests and Subtaks

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.1
right_motor = Motor(Port.A)
medium_motor = Motor(Port.C)
obsens = UltrasonicSensor(Port.S2)
colorsens = ColorSensor(Port.S4)
left_motor = Motor(Port.D)
gy = GyroSensor(Port.S1)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=155)
robot.settings(straight_speed=700, turn_rate=150) 

""" laps = int(input("Enter number of laps: "))
dist = float(input("Enter distance (m): ")) * 1000  """



""" Function that gets the scanned list of the barcode and matches with existing list.
    Returns the barcode type
"""
def barcodeCheck(barcodeList):
    barcodeDict = {1:[0, 1, 1, 1], 
                   2:[0, 1, 0, 1], 
                   3:[0, 0, 1, 1], 
                   4:[0, 1, 1, 0]}

    keys = list(barcodeDict.keys())
    values = list(barcodeDict.values())
    barcodeList.reverse()

    if barcodeList in values:
        return keys[values.index(barcodeList)]
    else:
        return "Wrong Box"

# Function to drop the box
def drop():
    medium_motor.run_angle(1000, 1325, then=Stop.HOLD, wait=True)
    medium_motor.stop()
    medium_motor.brake()

# Function to lift the box
def lift():
    medium_motor.run_angle(-1000, 1600, then=Stop.HOLD, wait=True)

# Function that uses the gyro sensor to course correct and 
# drive in a straight line
def driving(distance):
    gy.reset_angle(0)
    if distance > 0:
        while robot.distance() <= distance:
            correction = (0 - gy.angle()) * 1
            robot.drive(150, correction)
        robot.stop()
    else:
        while robot.distance() >= distance:
            correction = (0 - gy.angle()) * 1
            robot.drive(-150, correction)
        robot.stop()
        left_motor.brake()
        right_motor.brake()
    robot.reset()
    gy.reset_angle(0)

# Function that stops the robot
def obstacle(distance):
    while robot.distance() < distance:
        print(robot.distance())
        print(str(obsens.distance()))
        if obsens.distance() > 70:
            right_motor.run(300)
            left_motor.run(280)
        else:
            robot.stop()
            robot.reset()
            left_motor.brake()
            right_motor.brake()
            break
         
""" def drivingnow(distance):
    distance = 69 + (distance * 25.4)
    while robot.distance() < distance:
        print(robot.distance())
        print(str(obsens.distance()))
        right_motor.run(315)
        left_motor.run(280)
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    robot.reset()

          """

def gyroprint():
    gy.reset_angle(0)
    while True:
        print(str(gy.angle()))

def obsensprint():
    while True:
        print(str(obsens.distance()))

""" Part of the barcode function that gets the light value reading and
    returns black or white to be appended to a list
"""
def whiteorblack(lightVal):
    if lightVal < 30:
        return 0
    else:
        return 1
    
# Robot moves slowly
def slowMove(givenspeed, givendistance):
    robot.reset()
    rmconst, lmconst = givenspeed, givenspeed
    speed = givenspeed
    while robot.distance() <= givendistance:
        print("distance:", str(robot.distance()))
        print("reflection value:", str(colorsens.reflection()))
        if gy.angle() > 0:
            rmconst = speed * 1.1
            lmconst =  speed * 0.9
        elif gy.angle() < 0:
            rmconst = speed * 0.9
            lmconst = speed * 1.1
        else:
            rmconst = speed
            lmconst = speed
        print((lmconst,rmconst))
        left_motor.run(lmconst)
        right_motor.run(rmconst)
    
    robot.stop()
    left_motor.brake()
    right_motor.brake()

# Robot reverses slowly 
def slowReverseMove(givenspeed, givendistance):
    robot.reset()
    rmconst, lmconst = givenspeed, givenspeed
    speed = givenspeed
    while robot.distance() >= givendistance:
        print("distance:", str(robot.distance()))
        print("reflection value:", str(colorsens.reflection()))
        if gy.angle() > 0:
            rmconst = speed * 1.1
            lmconst =  speed * 0.9
        elif gy.angle() < 0:
            rmconst = speed * 0.9
            lmconst = speed * 1.1
        else:
            rmconst = speed
            lmconst = speed
        print((lmconst,rmconst))
        left_motor.run(lmconst)
        right_motor.run(rmconst)

    robot.stop()
    left_motor.brake()
    right_motor.brake()


"""def finalsub3diff():

    slowMove(50, 55)
    barlist = []

    readspeed = 50
    readist = 13
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    wait(3000)
    barlist.append(whiteorblack(colorsens.reflection()))
    slowMove(readspeed, readist)
    print(colorsens.reflection())
    barlist.append(whiteorblack(colorsens.reflection()))
    robot.stop()
    wait(3000)
    slowMove(readspeed, readist)
    print(colorsens.reflection())
    barlist.append(whiteorblack(colorsens.reflection()))
    robot.stop()
    wait(3000)
    slowMove(readspeed, readist)
    print(colorsens.reflection())
    barlist.append(whiteorblack(colorsens.reflection()))
    robot.stop()
    wait(3000)

    print(barlist)
    print(barcodeCheck(barlist))
"""

# Function to encapsulate all functions to perform final demo subtask 3
# Moves from Home A to stop at box to scan the barcode and return the right barcode type
def finalsub3():
    slowMove(50, 55)
    barlist = []

    readspeed = 50
    readist = 13
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    wait(3000)
    """ Color Sensor reads barcode and appends to list based on light value
        After appending all barcodes, the function- BarcodeCheck, checks the appended list and 
        returns the correct barcode type.
    """
    barlist.append(whiteorblack(colorsens.reflection()))
    slowMove(readspeed, readist)
    print(colorsens.reflection())
    barlist.append(whiteorblack(colorsens.reflection()))
    robot.stop()
    wait(3000)
    slowMove(readspeed, readist)
    print(colorsens.reflection())
    barlist.append(whiteorblack(colorsens.reflection()))
    robot.stop()
    wait(3000)
    slowMove(readspeed, readist)
    print(colorsens.reflection())
    barlist.append(whiteorblack(colorsens.reflection()))
    robot.stop()
    wait(3000)

    print(barlist)
    print(barcodeCheck(barlist))

def straight(distance):
    distance = distance * 25.4
    lmconst = 170
    rmconst = 170
    speed = 170
    robot.reset()
    gy.reset_angle(0)
    while robot.distance() <= distance:
        if gy.angle() > 0:
            rmconst = speed * 1.1
            lmconst =  speed * 0.9
        elif gy.angle() < 0:
            rmconst = speed * 0.9
            lmconst = speed * 1.1
        else:
            rmconst = speed
            lmconst = speed
        print((lmconst,rmconst))
        left_motor.run(lmconst)
        right_motor.run(rmconst)

    robot.stop()
    left_motor.brake()
    right_motor.brake()
    gy.reset_angle(0)


# Function to turn the robot 90 degrees clockwise
def turning():
    angle = 86.6 # degrees
    speed = 100
    while gy.angle() < angle:
        print(gy.angle())
        right_motor.run(speed=( -1*speed))
        left_motor.run(speed=speed)
        wait(10)  

    right_motor.brake()
    left_motor.brake()
    gy.reset_angle(0)

# Function to turn the robot 180 degrees clockwise
def turning180():
    angle = 176.5 # degrees
    speed = 100
    while gy.angle() < angle:
        print(gy.angle())
        right_motor.run(speed=(-1*speed))
        left_motor.run(speed=speed)
        wait(10)  

    right_motor.brake()
    left_motor.brake()
    gy.reset_angle(0)

# Function to turn the robot 90 degrees counter clockwise
def turningleft():
    gy.reset_angle(0)
    angle = 87.3 # degrees
    speed = 100
    while gy.angle() > -angle:
        print(gy.angle())
        right_motor.run(speed=speed)
        left_motor.run(speed=(-1*speed))
        wait(10)  

    right_motor.brake()
    left_motor.brake()
    gy.reset_angle(0)

# Function to encapsulate all functions to perform final demo subtask 1
# Moves from Home A to Home B after stopping for 5 seconds at given box
def finalsub1(boxnum):
    area = {7: 3, 8:8.6, 9:15, 10:21, 11:27, 12:33}
    straight(36)
    wait(3000)
    turning()
    wait(3000)
    straight(6+area[boxnum])
    wait(5000)
    straight(103-(6+area[boxnum]))
    wait(3000)
    turning()
    wait(3000)
    straight(35.6)
    wait(3000)
    turning180() 

# Function to encapsulate all functions to perform final demo subtask 2
# Moves from Home B to Home A
def finalsub2():
    straight(13)
    wait(3000)
    turningleft()
    wait(3000)
    straight(103)
    wait(3000)
    turningleft()
    straight(11)
    
def colortest():
    while True:
        print("color:", str(colorsens.color()))
        print("reflection value:", colorsens.reflection())
        
    
def test1():
    area = {7: 3, 8:7.3, 9:12, 10:17, 11:39, 12:45}
    choice = 8
    straight(36.8)
    wait(3000)
    turning()
    wait(3000)
    straight(6+area[9])
    wait(5000)


""" Function that detects when the handle of the robot 
    is under the box and then stops for final demo
    subtask 4
"""
def sensorbox(obsens):
    robot.reset() 
    while True:
        print(obsens.distance())
        if obsens.distance() > 75:
            left_motor.run(50)
            right_motor.run(48)
        else:
            break
    
    robot.stop()
    left_motor.brake()
    right_motor.brake()


# Function to encapsulate all functions to perform final demo subtask 4
def finalsub4():
    
    slowMove(106, 70) # straight
    wait(2000)
    turning()
    wait(2000)
    slowReverseMove(-100, -70) # reverse
    wait(2000)
    turning() # turn right
    wait(2000)
    slowMove(90, 140) # straight
    wait(2000) 
    turningleft() # turning left
    wait(2000)
    drop()
    wait(2000)
    sensorbox(obsens) # senses box
    wait(2000)
    lift()
    wait(2000)
    turningleft()
    slowMove(105, 60)
