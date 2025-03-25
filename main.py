from microbit import *
import MakerBit

Makerbit.connect()  # Initialize the MakerBit motor driver

while True:
    if button_a.is_pressed():
        makerbit.run_motor(MakerbitMotor.A, makerbitMotorDirection.FORWARD, 100)  # Run Motor A at full speed

makerbit.set_motor_rotation(MakerBitMotor.A, MakerBitMotorRotation.FORWARD)