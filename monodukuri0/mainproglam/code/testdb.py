import sqlite3

dbname = ('test.db')#データベース名.db拡張子で設定
conn = sqlite3.connect(dbname, isolation_level=None)#データベースを作成、自動コミット機能ON
cursor = conn.cursor() #カーソルオブジェクトを作成

"""
・create table テーブル名（作成したいデータカラム）というSQL文でテーブルを宣言
　　※SQL命令は大文字でも小文字でもいい
・今回はtestテーブルに「id,name,date」カラム(列名称)を定義する※今回dateは生年月日という列
・「if not exists」はエラー防止の部分。すでに同じテーブルが作成されてるとエラーになる為
・カラム型は指定しなくても特には問題ない
　　※NULL, INTEGER(整数), REAL(浮動小数点), TEXT(文字列), BLOB(バイナリ)の5種類
"""
#データベース中のテーブル名を取得するSQL関数
sql = """INSERT INTO test VALUES(?,?,?)"""

data = [
   (1, "Taro", 19800810),
   (2, "Bob", 19921015),
   (3, "Masa", 20050505),
   (4, "Jiro", 19910510),
   (5, "Satoshi", 19880117)
]


#sql = """DROP if exists TABLE test1"""
sql = """DROP TABLE if exists test1""" #2021/9/19修正

#命令を実行
conn.execute(sql)
conn.commit()#コミットする
conn.close()
