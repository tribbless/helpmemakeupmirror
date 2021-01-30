import socket, threading
import numpy as np
import cv2
from face_shape import face_shape_detect
import os

def binder(client_socket, addr):
    print("=======================================")
    print("\n\nclient가 접속하였습니다.\n\n")
    try:
        while True:
            # 접속한 클라이언트의 주소입니다.
            print('Connected by', addr)

            length = recvall(client_socket, 16)
            stringData = recvall(client_socket, int(length))
            data = np.frombuffer(stringData, dtype='uint8')

            decimg = cv2.imdecode(data, 1)
            cv2.imwrite('SERVER.jpg', decimg)

            result = face_shape_detect.main('SERVER.jpg')
            print(result)
            # 얼굴형 결과 보내기
            # face_shape = "Oblong"
            client_socket.send(result.encode())
    except:
        print("client except")
    finally:
        print("클라이언트 접속이 끊겼습니다. : ", addr)
        client_socket.close()
        check = os.path.isfile('SERVER.jpg')
        if check == True:
            print("사진을 삭제합니다.")
            os.remove('SERVER.jpg')

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


# 접속할 서버 주소입니다. 여기에서는 루프백(loopback) 인터페이스 주소 즉 localhost를 사용합니다.
HOST = '192.168.219.101'
# 클라이언트 접속을 대기하는 포트 번호입니다.
PORT = 9999

# 소켓 객체를 생성합니다.
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 포트 사용중이라 연결할 수 없다는
# WinError 10048 에러 해결를 위해 필요합니다.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
# HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
# 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다.
# PORT는 1-65535 사이의 숫자를 사용할 수 있습니다.
server_socket.bind((HOST, PORT))

# 서버가 클라이언트의 접속을 허용하도록 합니다.
server_socket.listen()

try:
    print("        < Server Start >        \n")
    while True:
        # accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다.
        client_socket, addr = server_socket.accept()
        th = threading.Thread(target=binder, args=(client_socket, addr))
        th.start()
except:
    print("server except")
finally:
    print("서버 소켓을 닫습니다.")
    server_socket.close()
    check = os.path.isfile('SERVER.jpg')
    if check == True:
        print("사진을 삭제합니다.")
        os.remove('SERVER.jpg')


print("111")

'''
# 무한루프를 돌면서
while True:

    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다.
    data = client_socket.recv(1024)

    # 빈 문자열을 수신하면 루프를 중지합니다.
    if not data:
        break


    # 수신받은 문자열을 출력합니다.
    print('Received from', addr, data.decode())

    # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코)
    #print(type(data))
    #client_socket.sendall(data)

    face_shape = "Oblong"
    client_socket.sendall(face_shape.encode())
'''

# 소켓을 닫습니다.
client_socket.close()
server_socket.close()