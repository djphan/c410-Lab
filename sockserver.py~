import socket
import sys
import thread
import curses


def makeSocket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ('Socket Created')
        return s

    except socket.error as msg:
        print ('Failed to make socket. Error code: ' + str(msg[0]) + ' , Error Message: ' + str(msg[1]))
        sys.exit();

def connectHost(s, host='www.google.com', port=80):
    try:
        remote_ip = socket.gethostbyname(host)
        print ('IP address of ' + host + ' is: ' + remote_ip)

    except socket.gaierror:
        print ('Host name could not be resolved')
        sys.exit()

    s.connect((remote_ip, port))
    print ('Socket connected to ' + host + ' on IP: ' + remote_ip)

def sendSocketMessage(s, message = 'GET / HTTP/1.1\r\n\r\n'):
    try:
        s.sendall(message.encode("UTF8"))
        print("SEND SUCCESS")

    except:
        print("SEND FAIL")
        sys.exit()

def recieveSocketMessage(s):
    reply = s.recv(4096)
    print(reply)


def bindSocket(s, host='', port=8889):
    try:
        s.bind((host, port))
        print('Socket Bind Completed')

    except socket.error as msg:
        print ( 'Bind failed. Error code: ' + str(msg[0]) + ' Message ' + str(msg[1]) )
        sys.exit()


def clientThread(conn):
    conn.send("Welcome to the server. Please type your name and hit enter.\r\n")
    while True:
        data = conn.recv(1024)
        data2 = str(data).strip()
        reply = '< Hello ' + data2 + ' >\r\n'
        

        if not data or data2 == chr(27):
            break

        conn.sendall(reply.encode("UTF-8"))

    conn.close()

if __name__ == "__main__":
    s = makeSocket()
    # connectHost(s, host, port)
    # sendSocketMessage(s)
    # recieveSocketMessage(s)
    bindSocket(s)
    s.listen(2)
    print ('Socket now listening...')

    while 1:
        conn, addr = s.accept()
        print('Connected with ' + str(addr[0]) + ':' + str(addr[1]))
        thread.start_new_thread(clientThread, (conn,))
        
        
    s.close()


    


    
