import socket
import cv2
import numpy

def client_main(image_path):

    # 서버의 주소입니다. hostname 또는 ip address를 사용할 수 있습니다.
    HOST = '192.168.219.108'
    # 서버에서 지정해 놓은 포트 번호입니다.
    PORT = 9999


    # 소켓 객체를 생성합니다.
    # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # 지정한 HOST와 PORT를 사용하여 서버에 접속합니다.
    client_socket.connect((HOST, PORT))

    # 사진 전송
    frame = cv2.imread(image_path)

    #capture = cv2.VideoCapture(0)
    #ret, frame = capture.read()

    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()

    client_socket.send(str(len(stringData)).ljust(16).encode())
    client_socket.send(stringData)
    # 메시지를 전송합니다.
    #client_socket.sendall('안녕'.encode())

    # 메시지를 수신합니다.
    face_shape = client_socket.recv(1024)
    print('Received', repr(face_shape.decode()))
    face_shape = face_shape.decode()
    # 소켓을 닫습니다.
    client_socket.close()

    return face_shape
