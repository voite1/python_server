import socket
import sys

def list_services(start=1000, end=3000):
    ''' Provide a list of ports for a specified range
    usage: list_services(start, end) '''
    
    # check for input boundaries
    if (start < 1 or end > 65535):
        print "Socket range should fall between 1 and 65535"
        sys.exit(0)
    
    # Print services
    for i in range(start,end+1):
        try:
            service = socket.getservbyport(i)
            print "Port:", i, ", Service:", service
        except Exception:
            # If service running
            pass
    
    # Sending success signal
    sys.exit(0)

if __name__ == "__main__":
    list_services()
    
    
