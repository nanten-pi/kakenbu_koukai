# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import paramiko

#主関数
#終了時の確認まで取ると　素人にやさしい設計
def howclose():
    if messagebox.askokcancel("確認", "本当に閉じていいですか？"):
        root.destroy()

def connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.connect('raspberrypi.local', username='ksc', password='ksc')
    # コマンド実行
    stdin, stdout, stderr = client.exec_command('cd ../../main')

    # コマンド実行後に標準入力が必要な場合
    stdin.write('password\n')
    stdin.flush()
    # 実行結果を表示

    client.close()

def runrunro():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.connect('raspberrypi.local', username='ksc', password='ksc')
    # コマンド実行
    stdin, stdout, stderr = client.exec_command('python testconsol.py')

    # コマンド実行後に標準入力が必要な場合
    stdin.write('password\n')
    stdin.flush()
    # 実行結果を表示

    client.close()

#戻すの!(切り替え関数)
def make():
    global frame

    frame_app.destroy()

    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.pack(fill = tk.BOTH, pady=20)
    # 各種ウィジェットの作成
    finishbutton=ttk.Button(root,text="終了",width=10,command=howclose)
    finishbutton.place(x=0,y=0)

    #設定
    #正直妥協（placeオプションが使えなかった)　悔しいので次は頑張る
    opt_networkbutton = ttk.Button(frame,text="ネットワーク接続の設定",default="disable",command=changecustom)
    opt_networkbutton.pack()

    opt_networkbutton = ttk.Button(frame,text="ソフトウェアの設定",default="disable",state="disabled")
    opt_networkbutton.pack()

    #接続
    connectbutton = ttk.Button(frame,text="接続",width=50,command=change,default="active")
    #connectbutton.place(x=150,y=400)
    connectbutton.pack()
    copy_label = ttk.Label(frame, justify="center",text="© 2022 Hiroshima Prefectural Hiroshima Junior High School All Rights Reserved.")
    copy_label.pack()
def make1():
    global frame

    frame_app1.destroy()

    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.pack(fill = tk.BOTH, pady=20)
    # 各種ウィジェットの作成
    finishbutton=ttk.Button(root,text="終了",width=10,command=howclose)
    finishbutton.place(x=0,y=0)

    #設定
    #正直妥協（placeオプションが使えなかった)　悔しいので次は頑張る
    opt_networkbutton = ttk.Button(frame,text="ネットワーク接続の設定",default="disable",command=changecustom)
    opt_networkbutton.pack()

    opt_networkbutton = ttk.Button(frame,text="ソフトウェアの設定",default="disable",state="disabled")
    opt_networkbutton.pack()


    #接続
    connectbutton = ttk.Button(frame,text="接続",width=50,command=change,default="active")
    #connectbutton.place(x=150,y=400)
    connectbutton.pack()

    copy_label = ttk.Label(frame, justify="center",text="© 2022 Hiroshima Prefectural Hiroshima Junior High School All Rights Reserved.")
    copy_label.pack()
#画面二枚目
def change():
    global frame_app

    frame.destroy()

    # メインフレームの作成と設置
    frame_app = ttk.Frame(root)
    frame_app.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    button_change_frame_app = ttk.Button(frame_app, text="ウィンドウを戻す", command=make)
    button_edit=ttk.Button(frame_app, text="モータの設定を編集",state="disabled")
    button_main=ttk.Button(frame_app, text="でーたべーすをつつく!",state="disabled")
    button_consol=ttk.Button(frame_app, text="コマンドプロンプトを使用",command=runrunro)
    # 各種ウィジェットの設置
    button_consol.pack()
    button_edit.pack()
    button_main.pack()
    button_change_frame_app.pack()
#設定画面
def changecustom():
    global frame_app1
    frame.destroy()
    frame_app1 = ttk.Frame(root)
    frame_app1.pack(fill = tk.BOTH,pady=20)
    #カスタム
    ip_label = ttk.Label(frame_app1,text="IPアドレスを設定")
    ip = ttk.Entry(frame_app1,width=20)
    password_label=ttk.Label(frame_app1,text="パスワードを設定")
    password = ttk.Entry(frame_app1,width=20)
    hostname_label = ttk.Label(frame_app1,text="ホストネームをせってい")
    hostname = ttk.Entry(frame_app1,width=20)
    button_savepoint = ttk.Button(frame_app1,text="書き込み(セーブ)")
    button_change_frame_app = ttk.Button(frame_app1, text="ウィンドウを戻す", command=make1)
    ip_label.pack()
    ip.pack()
    password_label.pack()
    password.pack()
    hostname_label.pack()
    hostname.pack()
    button_savepoint.pack()
    button_change_frame_app.pack()
if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title("自動商品配置機試作一号制御ソフトウェア")
    root.geometry("800x600")

    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    finishbutton=ttk.Button(root,text="終了",width=10,command=howclose)
    finishbutton.place(x=0,y=0)

    #設定
    #正直妥協（placeオプションが使えなかった)　悔しいので次は頑張る
    opt_networkbutton = ttk.Button(frame,text="ネットワーク接続の設定",default="disable",command=changecustom)
    opt_networkbutton.pack()

    opt_networkbutton = ttk.Button(frame,text="ソフトウェアの設定",default="disable",state="disabled")
    opt_networkbutton.pack()
    #接続
    connectbutton = ttk.Button(frame,text="接続",width=50,command=lambda:[change(),connect()],default="active")
        #connectbutton.place(x=150,y=400)
    connectbutton.pack()
#ネタバグある　rootのままにしといて
    copy_label = ttk.Label(frame, justify="center",text="© 2022 Hiroshima Prefectural Hiroshima Junior High School All Rights Reserved.")
    copy_label.pack()



    root.protocol("WM_DELETE_WINDOW", howclose)
    root.mainloop()
#制作　情報研究会 17期生 Hironori Kohisa
