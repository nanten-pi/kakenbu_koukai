import sys
import motor
import time
import sqlite3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dbname = 'main.db'
conn = sqlite3.connect(dbname)
cursor = conn.cursor()
#1 正面左下スイッチ 並列つなぎで繋ぐ
#2　正面右上スイッチ　並列繋ぎで繋ぐ
#3 左スイッチ
#4 右スイッチ
sensor1 = 16
sensor2 = 17
sensor3 = 22
sensor4 = 23
GPIO.setup(sensor1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sql1 = """UPDATE Fruit SET count = 1 WHERE id = 1 """
sql2 = """UPDATE Fruit SET count = 1 WHERE id = 2 """
sql3 = """UPDATE Fruit SET count = 1 WHERE id = 3 """
sql4 = """UPDATE Fruit SET count = 1 WHERE id = 4 """
sql5 = """UPDATE Fruit SET count = 1 WHERE id = 5 """
sql6 = """UPDATE Fruit SET count = 1 WHERE id = 6 """
sql7 = """UPDATE Fruit SET count = 1 WHERE id = 7 """
sql8 = """UPDATE Fruit SET count = 1 WHERE id = 8 """
sql9 = """UPDATE Fruit SET count = 1 WHERE id = 9 """
sql10 = """UPDATE Fruit SET count = 1 WHERE id = 10 """
sql11 = """UPDATE Fruit SET count = 1 WHERE id = 11 """
sql12 = """UPDATE Fruit SET count = 1 WHERE id = 12 """
sql13 = """UPDATE Fruit SET count = 1 WHERE id = 13 """
sql14 = """UPDATE Fruit SET count = 1 WHERE id = 14 """
sql15 = """UPDATE Fruit SET count = 1 WHERE id = 15 """
sql16 = """UPDATE Fruit SET count = 1 WHERE id = 16 """
sql17 = """UPDATE Fruit SET count = 1 WHERE id = 17 """
sql18 = """UPDATE Fruit SET count = 1 WHERE id = 18 """
while True:
    sw_status1 = GPIO.input(sensor1)
    sw_status2 = GPIO.input(sensor2)
    sw_status3 = GPIO.input(sensor3)
    sw_status4 = GPIO.input(sensor4)
    sql = """SELECT id FROM main WHERE count < 1"""
    cursor.execute(sql)
    result=cursor.fetchone()#データを1行抽出
    result1=''.join(map(str, result))
    #もしかしたら
    result2=int(result1)
    if result is None :#ループ離脱条件(データを抽出しきって空になったら)
        break #breakでループ離脱
    elif sw_status1 == 0:
        motor.updownstop
    elif sw_status2 == 0:
        motor.updownstop
    elif sw_status3 == 0:
        motor.rightleftstop
    elif sw_status4 == 0:
        motor.rightleftstop
    elif result1 == '1':
        motor.type1
        cursor.execute(sql1)
    elif result1 == '2':
        motor.type2
        cursor.execute(sql2)
    elif result1 == '3':
        motor.type3
        cursor.execute(sql3)
    elif result1 == '4':
        motor.type4
        cursor.execute(sql4)
    elif result1 == '5':
        motor.type5
        cursor.execute(sql5)
    elif result1 == '6':
        motor.type6
        cursor.execute(sql6)
    elif result1 == '7':
        motor.type7
        cursor.execute(sql7)
    elif result1 == '8':
        motor.type8
        cursor.execute(sql8)
    elif result1 == '9':
        motor.type9
        cursor.execute(sql9)
    elif result1 == '10':
        motor.type10
        cursor.execute(sql10)
    elif result1 == '11':
        motor.type11
        cursor.execute(sql11)
    elif result1 == '12':
        motor.type12
        cursor.execute(sql12)
    elif result1 == '13':
        motor.type13
        cursor.execute(sql13)
    elif result1 == '14':
        motor.type14
        cursor.execute(sql14)
    elif result1 == '15':
        motor.type14
        cursor.execute(sql15)
    elif result1 == '16':
        motor.type15
        cursor.execute(sql16)
    elif result1 == '17':
        motor.type17
        cursor.execute(sql17)
    elif result1 == '18':
        motor.type18
        cursor.execute(sql18)
cursor.close()
conn.close()
