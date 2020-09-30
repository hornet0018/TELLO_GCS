# File Name  : TELLO_UTILITY.py
# LastUpdate : 2020/09/24

import socket
import json
import time
import csv
import tkinter as tk
import threading
import sys
import re
import datetime

event = threading.Event()

event_flag = False
stop_flag1=True
stop_flag2=True
stop_flag3=True
stop_flag4=True
stop_flag5=True
stop_flag6=True
stop_flag7=True

# UDPソケット生成
#local_ip = socket.gethostbyname(socket.gethostname()) #ローカルIP自動取得取得WSLをインストールしていると取得できない
local_ip = '192.168.10.2'  #手動ローカルIP設定
local_port = 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((local_ip, local_port))
tello_address = ('192.168.10.1', 8889) #TelloEDUのアドレス設定

# Tello EDUに手動コマンドを送る関数
def send_command(msg):
    print(msg)
    msg = msg.encode(encoding="utf-8")
    event_flag = False
    event.clear()
    sock.sendto(msg, tello_address)

#切断ボタンコマンド
def btnEnd():
    print("---end---")
    sys.exit()

#スタートコマンド
def btnCommand():
    send_command('command')
    #send_command('mon')   #ミッションパッド認識有効化

#下向きカメラスタートコマンド
def btnMdirection():
    send_command('mdirection 0')

#離陸ボタンコマンド
def btnTakeoff():
    send_command('takeoff')

#着陸ボタンコマンド
def btnLand():
    send_command('land')

#ミッション1開始ボタン
def btnMission1():
    global stop_flag1
    if stop_flag1:
        print("mission1 start!!") 
        stop_flag1 = False
        mission1Thread = threading.Thread(target=mission1)
        mission1Thread.setDaemon(True)
        mission1Thread.start()
    else:
        print("misson1 already starting")


#ミッション1停止ボタン
def btnMission1end():
    global stop_flag1
    print("mission1 stop!!")
    stop_flag1 = True
 
#ミッション1  
def mission1(): #90度右回転を4回後、着陸します
    global stop_flag1  
    send_command('cw 90')
    event.wait() #イベントが発生するまで待機する
    send_command('cw 90')
    event.wait() #イベントが発生するまで待機する
    send_command('cw 90')
    event.wait() #イベントが発生するまで待機する
    send_command('cw 90')
    event.wait() #イベントが発生するまで待機する
    send_command('land') 
    event.wait()
    print('misson1 compleat!!')
    stop_flag1 = True
    #if stop_flag1:  #終了処理
    #        break    

#ミッション2開始ボタン
def btnMission2():
    global stop_flag2
    if stop_flag2:
        print("mission2 start!!") 
        stop_flag2 = False
        mission2Thread = threading.Thread(target=mission2)
        mission2Thread.setDaemon(True)
        mission2Thread.start()
    else:
        print("misson2 already starting")

#ミッション2停止ボタン
def btnMission2end():
    global stop_flag2
    print("mission2 stop!!")
    stop_flag2 = True

#ミッション2
def mission2():        #相対位置制御
    global stop_flag2
    while True:
        send_command('forward 30')
        event.wait()
        send_command('back 30')
        event.wait()
        if stop_flag2:  #終了処理
            print('misson2 compleat!!')
            stop_flag2 = True
            break

#ミッション3開始ボタン
def btnMission3():
    global stop_flag3
    if stop_flag3:
        print("mission3 start!!") 
        stop_flag3 = False
        mission3Thread = threading.Thread(target=mission3)
        mission3Thread.setDaemon(True)
        mission3Thread.start()
    else:
        print("misson3 already starting")
     

#ミッション3停止ボタン
def btnMission3end():
    global stop_flag3
    print("mission3 stop!!")
    stop_flag3 = True

#ミッション3
def mission3():   #絶対位置制御サンプル
    global stop_flag3
    while True:
        send_command('go 0 25 100 50 m1')
        event.wait()
        send_command('go 0 -25 100 50 m1')
        event.wait()
        if stop_flag3:  #終了処理
            print('misson3 compleat!!')
            stop_flag3 = True
            break    

#ミッション4開始ボタン
def btnMission4():
    global stop_flag4
    if stop_flag4:
        print("mission4 start!!") 
        stop_flag4 = False
        mission4Thread = threading.Thread(target=mission4)
        mission4Thread.setDaemon(True)
        mission4Thread.start()
    else:
        print("misson4 already starting")


#ミッション4停止ボタン
def btnMission4end():
    global stop_flag4
    print("mission4 stop!!")
    stop_flag4 = True

#ミッション4
def mission4():
    global stop_flag4
    while True:
        time.sleep(1)
        if stop_flag4:  #終了処理
            print('misson4 compleat!!')
            stop_flag4 = True
            break

#ミッション5開始ボタン
def btnMission5():
    global stop_flag5
    if stop_flag5:
        print("mission5 start!!") 
        stop_flag5 = False
        mission5Thread = threading.Thread(target=mission5)
        mission5Thread.setDaemon(True)
        mission5Thread.start()
    else:
        print("misson5 already starting")

#ミッション5停止ボタン
def btnMission5end():
    global stop_flag5
    print("mission5 stop!!")
    stop_flag5 = True

#ミッション5
def mission5():
    while True:
        time.sleep(1)
        if stop_flag5:  #終了処理
            print('misson5 compleat!!')
            break

#ミッション6開始ボタン
def btnMission6():
    global stop_flag6
    if stop_flag6:
        print("mission6 start!!") 
        stop_flag6 = False
        mission6Thread = threading.Thread(target=mission6)
        mission6Thread.setDaemon(True)
        mission6Thread.start()
    else:
        print("misson6 already starting")

#ミッション6停止ボタン
def btnMission6end():
    global stop_flag6
    print("mission6 stop!!")
    stop_flag6 = True

#ミッション6
def mission6():
    while True:
    
        time.sleep(1)
        if stop_flag6:  #終了処理
            print('misson6 compleat!!')
            break

#ミッション7開始ボタン
def btnMission7():
    global stop_flag7
    if stop_flag7:
        print("mission7 start!!") 
        stop_flag7 = False
        mission7Thread = threading.Thread(target=mission7)
        mission7Thread.setDaemon(True)
        mission7Thread.start()
    else:
        print("misson7 already starting")
    

#ミッション7停止ボタン
def btnMission7end():
    global stop_flag7
    print("mission7 stop!!")
    stop_flag7 = True

#ミッション7
def mission7():
    while True:
       
        time.sleep(1)
        if stop_flag7:  #終了処理
            print('misson7 compleat!!')
            break

#ストップコマンド
def btnStop():
    send_command('stop')

#緊急停止コマンド
def btnEStop():
    send_command('emergency')

#上昇コマンド
def btnUp():
    send_command('up 20')

#降下コマンド
def btnDown():
    send_command('down 20')

#右移動コマンド
def btnRight():
    send_command('right 20')

#左移動コマンド
def btnLeft():
    send_command('left 20')

#前進コマンド
def btnForward():
    send_command('forward 20')

#後進コマンド
def btnBack():
    send_command('back 20')

#ホームコマンド
def btnM1home():
    send_command('go 0 0 50 50 m1')

#GUI設定
root = tk.Tk()
root.title(u'Tello Utility v1.0')
root.geometry('700x550')
fm_select = tk.LabelFrame(root,width=300,height=300,text="TelloEDU")
fm_select.pack(ipadx=10,ipady=10,padx=10,pady=10)
fm_select2 = tk.LabelFrame(root,width=300,height=300,text="SGP30")
fm_select2.pack(ipadx=10,ipady=10,padx=10,pady=10)
fm_select3 = tk.LabelFrame(root,width=300,height=300,text="操作ボタン")
fm_select3.pack(ipadx=10,ipady=10,padx=10,pady=10)
fm_select4 = tk.LabelFrame(root,width=100,height=100,text="緊急停止")
fm_select4.pack(ipadx=10,ipady=10,padx=10,pady=10)
fm_select5 = tk.LabelFrame(root,width=100,height=100,text="コマンド実行結果")
fm_select5.pack(ipadx=10,ipady=10,padx=10,pady=10)


## padx , pady ：外側の横、縦の隙間
lblBattery=tk.Label(fm_select,text=u'Battery: --')
lblHeight=tk.Label(fm_select,text=u'Height: --')
lblRoll=tk.Label(fm_select,text=u'Roll: --')
lblPitch=tk.Label(fm_select,text=u'Pitch: --')
lblYaw=tk.Label(fm_select,text=u'Yaw: --')
lblTemph=tk.Label(fm_select,text=u'Temph: --')
lblPad=tk.Label(fm_select,text=u'MissonPad ID: --')
lblX=tk.Label(fm_select,text=u'X: --')
lblY=tk.Label(fm_select,text=u'Y: --')
lblZ=tk.Label(fm_select,text=u'Z: --')

## ラベルを配置
lblBattery.grid(row=0, column=0,padx=2,pady=2)
lblHeight.grid(row=0, column=1,padx=2,pady=2)
lblRoll.grid(row=0, column=2,padx=2,pady=2)
lblPitch.grid(row=0, column=3,padx=2,pady=2)
lblYaw.grid(row=0, column=4,padx=2,pady=2)
lblTemph.grid(row=0, column=5,padx=2,pady=2)
lblPad.grid(row=1, column=0,padx=2,pady=2)
lblX.grid(row=1, column=1,padx=2,pady=2)
lblY.grid(row=1, column=2,padx=2,pady=2)
lblZ.grid(row=1, column=3,padx=2,pady=2)

#センサーの情報
lbltvoc=tk.Label(fm_select2,text=u'TVOC: --',)
lblco2=tk.Label(fm_select2,text=u'CO2eq: --')
lblethanol=tk.Label(fm_select2,text=u'Raw Ethanol: --')
lblh2=tk.Label(fm_select2,text=u'Raw H2: --')
lblbat=tk.Label(fm_select2,text=u'Battery : --')

lbltvoc.grid(row=0, column=0,padx=2,pady=2)
lblco2.grid(row=0, column=1,padx=2,pady=2)
lblethanol.grid(row=0, column=2,padx=2,pady=2)
lblh2.grid(row=0, column=3,padx=2,pady=2)
lblbat.grid(row=0, column=4,padx=2,pady=2)

#操作ボタン
btnEnd = tk.Button(fm_select3, text='切断',height=1,width=10,command=btnEnd)
btnTakeoff = tk.Button(fm_select3, text='離陸',height=1,width=10,command=btnTakeoff)
btnLand = tk.Button(fm_select3, text='着陸',height=1,width=10,command=btnLand)
btnMission1 = tk.Button(fm_select3, text='ミッション1開始',height=1,width=10,command=btnMission1)
btnMission2 = tk.Button(fm_select3, text='ミッション2開始',height=1,width=10,command=btnMission2)
btnMission3 = tk.Button(fm_select3, text='ミッション3開始',height=1,width=10,command=btnMission3)
btnMission4 = tk.Button(fm_select3, text='ミッション4開始',height=1,width=10,command=btnMission4)
btnMission5 = tk.Button(fm_select3, text='ミッション5開始',height=1,width=10,command=btnMission5)
btnMission6 = tk.Button(fm_select3, text='ミッション6開始',height=1,width=10,command=btnMission6)
btnMission7 = tk.Button(fm_select3, text='ミッション7開始',height=1,width=10,command=btnMission7)
btnMission1end = tk.Button(fm_select3, text='ミッション1停止',height=1,width=10,command=btnMission1end)
btnMission2end = tk.Button(fm_select3, text='ミッション2停止',height=1,width=10,command=btnMission2end)
btnMission3end = tk.Button(fm_select3, text='ミッション3停止',height=1,width=10,command=btnMission3end)
btnMission4end = tk.Button(fm_select3, text='ミッション4停止',height=1,width=10,command=btnMission4end)
btnMission5end = tk.Button(fm_select3, text='ミッション5停止',height=1,width=10,command=btnMission5end)
btnMission6end = tk.Button(fm_select3, text='ミッション6停止',height=1,width=10,command=btnMission6end)
btnMission7end = tk.Button(fm_select3, text='ミッション7停止',height=1,width=10,command=btnMission7end)
btnCommand = tk.Button(fm_select3, text='SDKコマンド',height=1,width=10,command=btnCommand)
btnStop = tk.Button(fm_select3,text='ストップ',height=1,width=10,command=btnStop)
btnM1home = tk.Button(fm_select3,text='M1ホーム',height=1,width=10,command=btnM1home)
btnUp = tk.Button(fm_select3, text='上昇',height=1,width=10,command=btnUp)
btnDown = tk.Button(fm_select3, text='降下',height=1,width=10,command=btnDown)
btnRight = tk.Button(fm_select3, text='右移動',height=1,width=10,command=btnRight)
btnLeft = tk.Button(fm_select3, text='左移動',height=1,width=10,command=btnLeft)
btnForward = tk.Button(fm_select3, text='前進',height=1,width=10,command=btnForward)
btnBack = tk.Button(fm_select3, text='後進',height=1,width=10,command=btnBack)
btnMdirection = tk.Button(fm_select3, text='ミッションパッド',height=1,width=10,command=btnMdirection)

btnEnd.grid(row=0, column=0,padx=2,pady=2)
btnTakeoff.grid(row=0,column=1,padx=2,pady=2)
btnLand.grid(row=0,column=2,padx=2,pady=2)
btnMdirection.grid(row=0, column=3,padx=2,pady=2)
btnCommand.grid(row=0,column=4,padx=2,pady=2)
btnStop.grid(row=0,column=5,padx=2,pady=2)
btnM1home.grid(row=0,column=6,padx=2,pady=2)
btnUp.grid(row=1, column=0,padx=2,pady=2)
btnDown.grid(row=1, column=1,padx=2,pady=2)
btnLeft.grid(row=1, column=2,padx=2,pady=2)
btnRight.grid(row=1, column=3,padx=2,pady=2)
btnForward.grid(row=1, column=4,padx=2,pady=2)
btnBack.grid(row=1, column=5,padx=2,pady=2)
btnMission1.grid(row=3,column=0,padx=2,pady=2)
btnMission2.grid(row=3,column=1,padx=2,pady=2)
btnMission3.grid(row=3,column=2,padx=2,pady=2)
btnMission4.grid(row=3,column=3,padx=2,pady=2)
btnMission5.grid(row=3,column=4,padx=2,pady=2)
btnMission6.grid(row=3,column=5,padx=2,pady=2)
btnMission7.grid(row=3,column=6,padx=2,pady=2)
btnMission1end.grid(row=4,column=0,padx=2,pady=2)
btnMission2end.grid(row=4,column=1,padx=2,pady=2)
btnMission3end.grid(row=4,column=2,padx=2,pady=2)
btnMission4end.grid(row=4,column=3,padx=2,pady=2)
btnMission5end.grid(row=4,column=4,padx=2,pady=2)
btnMission6end.grid(row=4,column=5,padx=2,pady=2)
btnMission7end.grid(row=4,column=6,padx=2,pady=2)

#緊急停止
btnEStop = tk.Button(fm_select4,text='緊急停止',bg='#FF4500',height=1,width=10,command=btnEStop)

btnEStop.grid(row=0,column=0,padx=2,pady=2)

#実行結果
lblcmd=tk.Label(fm_select5,text=u' --')

lblcmd.grid(row=0,column=0,padx=2,pady=2)


#CSV書き出し処理スレッド
def tello():
    global tello_status
    global lobal_ip
    local_port = 8890
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
    sock.bind((local_ip, local_port))
    path = './data/'
    date_fmt = '%Y-%m-%d_%H%M%S'
    file_name = '%sstatus-%s.csv' % (path, datetime.datetime.now().strftime(date_fmt))
    csvhead = ["pitch", "roll", "yaw", "vgx", "vgy", "vgz", "templ", "temph", "tof",
               "h", "bat", "baro", "time", "agx", "agy", "agz",]
    print('tello_state')
    while True:
        try:
            response, ip = sock.recvfrom(1518)
            res = response.decode(encoding = "utf-8")
            res2 = re.sub('[a-z:\n\r]', '', res)
            res3 = res2.split(';')
            tello_status = res3
            print("start")
            print(res)
            
            #GUI表示用
            lblBattery['text'] = "Battery: "+str('{:3}'.format(int(tello_status[11])))+" %"
            lblHeight['text'] = "ToF : "+str('{:3}'.format(int(tello_status[9])))+" cm"
            lblRoll['text'] = "Roll: "+str('{:5}'.format(int(tello_status[2])))+" °"
            lblPitch['text'] = "Pitch: "+str('{:5}'.format(int(tello_status[1])))+" °"
            lblYaw['text'] = "Yaw: "+str('{:5}'.format(int(tello_status[3])))+" °"
            lblTemph['text'] = "Temph: "+str('{:5}'.format(int(tello_status[8])))+" ℃"
            
        
            try:
                with open(file_name, 'x',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(csvhead)
                    writer.writerow(tello_status)
            except FileExistsError:
                with open(file_name, 'a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(tello_status)
            time.sleep(0.01)
        except socket.error:
            print('\nTello Status Exit . . .\n')
            sock.close()
            break
        except KeyboardInterrupt:
            print('\nTello Status Exit . . .\n')
            sock.close()
            break

telloThread = threading.Thread(target=tello)
telloThread.setDaemon(True)
telloThread.start()

#返答コマンド取得スレッド
def recv():
    global CMD
    while True:
        try:
            data, server = sock.recvfrom(1518)
            CMD = data.decode(encoding="utf-8")
            print(CMD)
            lblcmd['text'] = CMD
            event.set()    #イベント発生
            event_flag = True
        except Exception:
            break
recvThread = threading.Thread(target=recv)
recvThread.setDaemon(True)
recvThread.start()

root.mainloop()

