import socket
import time


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print(s.recv(1024))
    for data in ['Michael', 'Tracy', 'Sarah']:
        # 发送数据:
        s.send(data.encode('utf-8'))
        print (s.recv(1024))
    s.send('exit'.encode('utf-8'))
    s.close()