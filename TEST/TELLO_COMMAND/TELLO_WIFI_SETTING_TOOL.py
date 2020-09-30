# File Name  : TELLO_WIFI_SETTING_TOOL.py
# LastUpdate : 2020/09/18

import socket
import tkinter as tk
import threading
import sys
import re

SSID = 'WLX313_DRONE'
pw = 'wlx313drone'

# UDPソケット生成
#local_ip = socket.gethostbyname(socket.gethostname()) #ローカルIP自動取得取得
local_ip = '192.168.10.2'  #手動ローカルIP設定
local_port = 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((local_ip, local_port))
tello_address = ('192.168.10.1', 8889) #TelloEDUのアドレス設定

# Tello EDUにSDKコマンドを送る関数
def send_command(msg):
    print(msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)

#切断ボタン
def btnEnd():
    print("---end---")
    sys.exit()

#WiFi設定ボタン
def btnWiFi():
    global ssid
    global pw
    send_command('ap WLX313_DRONE wlx313drone')

def btnCommand():
    send_command('command')

#GUI設定
root = tk.Tk()
root.title(u'TELLO_WIFI_SETTING_TOOL')
root.geometry('300x100')

fm_select3 = tk.LabelFrame(root,width=300,height=300,text="操作ボタン")
fm_select3.pack(ipadx=10,ipady=10,padx=10,pady=10)

#操作ボタン
btnEnd = tk.Button(fm_select3, text='切断',height=1,width=10,command=btnEnd)
btnWiFi = tk.Button(fm_select3, text='WiFi設定',height=1,width=10,command=btnWiFi)
btnCommand = tk.Button(fm_select3, text='SDKコマンド',height=1,width=10,command=btnCommand)

btnEnd.grid(row=0, column=0,padx=2,pady=2)
btnWiFi.grid(row=0,column=1,padx=2,pady=2)
btnCommand.grid(row=0,column=2,padx=2,pady=2)

#コマンド受信スレッド
def recv():
    global CMD
    while True:
        try:
            data, server = sock.recvfrom(1518)
            CMD = data.decode(encoding="utf-8")
            print(CMD)
        except Exception:
            break

recvThread = threading.Thread(target=recv)
recvThread.setDaemon(True)
recvThread.start()


#CSV書き出し処理スレッド
def tello():
    global tello_status
    global lobal_ip
    local_port = 8890
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
    sock.bind((local_ip, local_port))
    print('tello_state')
    while True:
        try:
            response, ip = sock.recvfrom(1518)
            res = response.decode(encoding = "utf-8")
            res2 = re.sub('[a-z:\n\r]', '', res)
            res3 = res2.split(';')
            tello_status = res3
            print(res3)

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

def main(): # メイン関数
    while True:
        try:
            # コマンド入力待ち
            msg = input('')

            # 「end」が入力されたら接続を終了
            if 'end' in msg:
                print('--- END ---')
                sock.close()
                break

            # Tello EDUにコマンドを送る
            send_command(msg)

        #例外発生時
        except Exception as ex:
            print(ex)
            sock.close()

if __name__ == '__main__':
    main()

root.mainloop()
