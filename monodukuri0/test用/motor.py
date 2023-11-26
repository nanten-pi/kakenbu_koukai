import RPi.GPIO as gpio
#pinset
gpio.setmode(gpio.BCM)
PWM_MAX = 100
leftMotor_DIR_pin = 22
gpio.setup(leftMotor_DIR_pin, gpio.OUT)
rightMotor_DIR_pin = 23
gpio.setup(rightMotor_DIR_pin, gpio.OUT)

gpio.output(leftMotor_DIR_pin, gpio.LOW)
gpio.output(rightMotor_DIR_pin, gpio.LOW)
leftMotor_PWM_pin = 17
rightMotor_PWM_pin = 18
gpio.setup(rightMotor_PWM_pin, gpio.OUT)
gpio.setup(leftMotor_PWM_pin, gpio.OUT)
#PWMSET
leftMotorPWM = gpio.PWM(leftMotor_PWM_pin,20)
rightMotorPWM = gpio.PWM(rightMotor_PWM_pin,20)
#PWM
leftMotorPWM.start(0)
leftMotorPWM.ChangeDutyCycle(0)
rightMotorPWM.start(0)
rightMotorPWM.ChangeDutyCycle(0)
leftMotorPower = 0
rightMotorPower = 0
def getMotorPowers():
    return (leftMotorPower,rightMotorPower)
def setMotorLeft(power):
    if power < 0:
        gpio.output(leftMotor_DIR_pin, gpio.LOW)
        pwm = -int(PWM_MAX * power)  
