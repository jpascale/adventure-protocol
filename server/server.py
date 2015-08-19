import socket
import select

DEBUG = True

def send_data_all (sck, message):
    '''Sends message to everyone excepting the master socket and the sender one'''
    for socket in CONNECTION_LIST:
        if socket != master_socket and socket != sck :
            try:
                send_data(socket, message)
            except:
                # broken connection
                socket.close()
                CONNECTION_LIST.remove(socket)

def send_data(sck, data):
    try:
        sck.send(data)
    except:
        sck.close()
        CONNECTION_LIST.remove(sck)

def protocol(socketindex, rdata):
    key = rdata[0]

    if key == '#':
        rdata = rdata[1:]
        if DEBUG:
            print "DEBUG: \'#\' received.\n"
        send_data_all(socketindex, rdata)

if __name__ == "__main__":
    
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 5000
    
    #Create TCP socket
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    master_socket.bind(("0.0.0.0", PORT))
    master_socket.listen(10)
 
    CONNECTION_LIST.append(master_socket)
 
    print "Server started on port " + str(PORT)
 
    while True:
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            #Incoming connection
            if sock == master_socket:
                sockfd, addr = master_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "(%s, %s) connected" % addr
                 
                send_data_all(sockfd, "[%s:%s] connected\n" % addr)
             
            #Inconming message
            else:
                # Data recieved from client
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        protocol(sock, data)
                        #send_data_all(sock, "\r" + str(sock.getpeername()) + '> ' + data)                
                 
                except:
                    send_data_all(sock, "Client (%s, %s) is offline." % addr)
                    print "Client (%s, %s) is offline." % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
     
    master_socket.close()