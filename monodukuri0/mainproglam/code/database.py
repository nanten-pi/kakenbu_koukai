import sqlite3
#基本的に実行禁止!!!!!!!
#SQL例文
# データ更新
#cur.execute('UPDATE items SET count = 1 WHERE id = "3"')
# データ削除
#cur.execute('DELETE FROM items WHERE id = "2"')
#setup
dbname = ('main.db')#データベース名.db拡張子で設定
conn = sqlite3.connect(dbname, isolation_level=None)#データベースを作成、自動コミット機能ON
cursor = conn.cursor() #カーソルオブジェクトを作成
sql = """CREATE TABLE IF NOT EXISTS main(id, name, count)"""

cursor.execute(sql)#executeコマンドでSQL文を実行

sql = """INSERT INTO main VALUES(?,?,?)"""

data = [
   (1, "カップ麺", 0),
   (2, "カップ麺", 0),
   (3, "カップ麺", 0),
   (4, "カップ麺", 0),
   (5, "カップ麺", 0),
   (6, "カップ麺", 0),
   (7, "カップ麺", 0),
   (8, "カップ麺", 0),
   (9, "カップ麺", 0),
   (10, "カップ麺", 0),
   (11, "カップ麺", 0),
   (12, "カップ麺", 0),
   (13, "カップ麺", 0),
   (14, "カップ麺", 0),
   (15, "カップ麺", 0),
   (16, "カップ麺", 0),
   (17, "カップ麺", 0),
   (18, "カップ麺", 0)
]
cursor.executemany(sql, data)#複数のデータを追加したい場合はexecutemanyメソッドを使う
conn.commit()#データベースにコミット(Excelでいう上書き保存。自動コミット設定なので不要だが一応・・
cursor.close()
conn.close()
