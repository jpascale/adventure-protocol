import socket, select, string, sys
 
def prompt() :
    sys.stdout.write('You> ')
    sys.stdout.flush()
 
#main function
if __name__ == "__main__":
     
    host = 'localhost'
    port = 5000
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host.'
    prompt()
     
    while True:
        socket_list = [sys.stdin, s]
         
        # Incoming message from server or from sdtin?
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                
                if data:
                	sys.stdout.write(data)
                	prompt()
                else:
                	print '\nDisconnected from remote server'
             
            #message entered in stdin
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()
                