import socket
import threading
import time


def tcp_link(sock, address):
    print('Accept new connection from %s:%s...' % address)
    sock.send(b"Welcome!")
    '''
    # 接收客户端发来的字节数据
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    # 解码字节数据,这时得到的就是原图像文件的字节流
    img_bytes = base64.b64decode(data.decode('utf-8'))
    '''
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % address)


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 9999))
    s.listen(100)
    print('Waiting for connection.')
    # 无限循环为每个客户端请求开启一个线程来处理
    while True:
        # 接受一个新连接:
        sock, address = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcp_link, args=(sock, address))
        t.start()