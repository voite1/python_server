import socket
import select
import sys

def server(log_buffer=sys.stderr):
    ''' Additional assignment using select module, select.select function call '''
    
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    sock.bind(address)

    print >>log_buffer, "making a server on {0}:{1}".format(*address)
    sock.listen(5)
    
    # setting up input list for select module
    inpt = [sock]

    try:
        while True:
            print >>log_buffer, 'waiting for a connection'
            select_input, select_output, select_except = select.select(inpt, [], [])
            
            for s in select_input:
                if s == sock:
                    conn, address = sock.accept()
                    while True:
                        data = conn.recv(16)
                        print >>log_buffer, 'received "{0}"'.format(data)
                        conn.sendall(data)
                        if len(data) < 16:
                            break
                    conn.close()
                else:
                    pass
                    
    except KeyboardInterrupt:
        conn.close()
        sock.close()
        sys.exit(0)


if __name__ == '__main__':
    server()
    sys.exit(0)
