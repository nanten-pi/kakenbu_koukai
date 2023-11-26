import RPi.GPIO as GPIO
import sys
import time
duty1 = 80
duty2 = 70
duty3 = 60
#ねえこれなんて読むと思う? 周波数だってさ!
Frequencys = 50
#pinset
GPIO.setmode(GPIO.BCM)
motor1DIR = 6
motor2DIR = 5
motor3DIR = 26
motor4DIR = 27
motor1PWM = 4
motor2PWM = 18
motor3PWM = 13
motor4PWM = 12
#GPIOset
GPIO.setup(motor1DIR,GPIO.OUT)
GPIO.setup(motor2DIR,GPIO.OUT)
GPIO.setup(motor3DIR,GPIO.OUT)
GPIO.setup(motor4DIR,GPIO.OUT)
GPIO.setup(motor1PWM,GPIO.OUT)
GPIO.setup(motor2PWM,GPIO.OUT)
GPIO.setup(motor3PWM,GPIO.OUT)
GPIO.setup(motor4PWM,GPIO.OUT)
#PWMset
p1 = GPIO.PWM(motor1PWM,Frequencys)
p2 = GPIO.PWM(motor2PWM,Frequencys)
p3 = GPIO.PWM(motor3PWM,Frequencys)
p4 = GPIO.PWM(motor4PWM,Frequencys)
#PWMready?
#The argument Duty (翻訳様々)
p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
#1 縦移動正面右モータ
#2 縦移動正面右モータ
#3 押出モータ
#4 押出モータ
#5 縦移動正面左モータ
#6 縦移動正面左モータ
#7 並行移動モータ
#8 平行移動モータ
try:
    while True:
        #sysでキーの読み込み
        c = sys.stdin.read(1)
        if c == '1':
            p1.ChangeDutyCycle(duty)
            GPIO.output(motor1DIR,GPIO.HIGH)
            time.sleep(10)
            p1.ChangeDutyCycle(0)
        elif c == '2':
            p1.ChangeDutyCycle(duty)
            GPIO.output(motor1DIR,GPIO.LOW)
            time.sleep(10)
            p1.ChangeDutyCycle(0)
        elif c == '3':
            GPIO.output(motor2DIR,GPIO.HIGH)
            p2.ChangeDutyCycle(duty)
            time.sleep(10)
            p2.ChangeDutyCycle(0)
        elif c == '4':
            p2.ChangeDutyCycle(duty)
            GPIO.output(motor2DIR,GPIO.LOW)
            time.sleep(10)
            p2.ChangeDutyCycle(0)
        elif c == '5':
            GPIO.output(motor3DIR,GPIO.HIGH)
            p3.ChangeDutyCycle(duty)
            time.sleep(10)
            p3.ChangeDutyCycle(0)

        elif c == '6':
            p3.ChangeDutyCycle(duty)
            GPIO.output(motor3DIR,GPIO.LOW)
            time.sleep(10)
            p3.ChangeDutyCycle(0)
        elif c == '7':
            GPIO.output(motor4DIR,GPIO.HIGH)
            p4.ChangeDutyCycle(duty)
            time.sleep(10)
            p4.ChangeDutyCycle(0)
        elif c == '8':
            p4.ChangeDutyCycle(duty)
            GPIO.output(motor4DIR,GPIO.LOW)
            time.sleep(10)
            p4.ChangeDutyCycle(0)
        elif c =='x':#high high
            GPIO.output(motor1DIR,GPIO.HIGH)
            GPIO.output(motor3DIR,GPIO.HIGH)
            p1.ChangeDutyCycle(duty)
            p3.ChangeDutyCycle(duty)
            time.sleep(10)
            p1.ChangeDutyCycle(0)
            p3.ChangeDutyCycle(0)

        elif c=='y':#low LOW
            GPIO.output(motor1DIR,GPIO.LOW)
            GPIO.output(motor3DIR,GPIO.LOW)
            p3.ChangeDutyCycle(duty)
            p1.ChangeDutyCycle(duty)
            time.sleep(10)
            p1.ChangeDutyCycle(0)
            p3.ChangeDutyCycle(0)
        elif c=='z':
            p4.ChangeDutyCycle(duty)
            GPIO.output(motor4DIR,GPIO.LOW)
            time.sleep(10)
            p4.ChangeDutyCycle(0)
        elif c=='e':
            p4.ChangeDutyCycle(duty)
            GPIO.output(motor4DIR,GPIO.HIGH)
            time.sleep(10)
            p4.ChangeDutyCycle(0)
        #「t」キーが押されたら止まる
        elif c == 't':
            #0のときとまる
            #dutyで動く(信号送信)
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
            p3.ChangeDutyCycle(0)
            p4.ChangeDutyCycle(0)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
