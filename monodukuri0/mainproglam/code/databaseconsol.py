import sqlite3
dbname='main.db'
# 1.データベースに接続
conn = sqlite3.connect(dbname)

# 2.sqliteを操作するカーソルオブジェクトを作成
cursor = conn.cursor()
#SELECTはからむのこと FROMはてーぶるのこと WHEREは特定のカラムを検索したいときに
sql1 = """UPDATE main SET count = 1 WHERE id = 1 """
sql2 = """UPDATE main SET count = 1 WHERE id = 2 """
sql3 = """UPDATE main SET count = 1 WHERE id = 3 """
sql4 = """UPDATE main SET count = 1 WHERE id = 4 """
sql5 = """UPDATE main SET count = 1 WHERE id = 5 """
while True:
    sql = """SELECT id FROM main WHERE count = 0 """
    cursor.execute(sql)
    result=cursor.fetchone()#データを1行抽出
    #頭にくるやつが選択されるからそれを順番に実行していって、それに合わせてDB更新すればいいだけなのに　なぜか更新できん
    result1=''.join(map(str, result))
    if result is None :#ループ離脱条件(データを抽出しきって空になったら)
        break #breakでループ離脱
    #多分elifが実行されてない
    elif result1 == '1':

        cursor.execute(sql1)
    elif result1 == '2':

        cursor.execute(sql2)
    elif result1 == '3':

        cursor.execute(sql3)
    elif result1 == '4':

        cursor.execute(sql4)
    elif result1 == '5':

        cursor.execute(sql5)
    print(result1)
    #そもそもこの構造（printの）間違ってる説
cursor.close()
conn.close()
