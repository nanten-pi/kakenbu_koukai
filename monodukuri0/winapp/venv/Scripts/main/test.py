#自力でデザインするのは普通に無理なんよ
#https://page.sourceforge.net/
#手を抜きます.
from tkinter import *
from tkinter import ttk
#アスタリスクでインポートすればもじゅーるめいいらないの!?!?!?!??!?初耳gaku
root = Tk()
root.title('自動商品配置機試作一号制御ソフトウェア')

# Frame as Widget Container
frame1 = ttk.Frame(
    root,
    padding=10)
frame1.grid()

# Label 1
icon = PhotoImage(file='flow2.png')

label1 = ttk.Label(
    frame1,
    image=icon)
label1.grid(row=0, column=0)



# ボタン
button1 = ttk.Button(
    frame1,
    text='終了',
    command=lambda: root.quit())
button1.place(x=200,y=100)

root.mainloop()
#© 2022 Hironori Kohisa,Sena Hiyama
