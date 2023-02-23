import threading
import socket #the library for networking
from queue import Queue
target = input('Enter the targeted ip address: ')
queue = Queue() # queue object
open_ports = [] # a list to store the open ports the program founds
ImportantPorts = {21:'ftp' '     vsftpd 2.3.4',22:'ssh' '     OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)',23:'telnet' '     Linux telnetd',25:'smtp' '     Postfix smtpd',53:'domain' '     ISC BIND 9.4.2',80:'http' '     Apache httpd 2.2.8 ((Ubuntu) DAV/2)',111:'rpcbind' '     2 (RPC #100000)',139:'netbois-ssn' '     Samba smbd 3.X - 4.X (workgroup: WORKGROUP)',445:'netbios-ssn' '     Samba smbd 3.X - 4.X (workgroup: WORKGROUP)',512:'exec' '     netkit-rsh rexecd',513:'login' ,514:'shell',1099: 'java-rmi' '     GNU Classpath grmiregistry',1524:'bindshell' '     Metasploitable root shell',2049:'nfs' '     2-4 (RPC #100003)',2121:'ccproxy-ftp' '     ProFTPD 1.3.1',3306:'mysql' '     MySQL 5.0.51a-3ubuntu5',5432:'postgresql' '     PostgreSQL DB 8.3.0 - 8.3.7',5900:'vnc' '     VNC (protocol 3.3)',6000:'X11' '     (access denied)',6667:'irc' '     UnrealIRCd',8009:'ajp13' '     Apache Jserv (Protocol v1.3)',8180: 'http' '     Apache Tomcat/Coyote JSP engine 1.1'}

def portScan(port, target):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True # this means the scan was successful any no errors occured
    except:
        return False

# scanning using one thread is insufficient and slow, so i will use multi-threading and queues to effictivly scan multiple ports at a time

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker(): # the method that the threads will use
    while not queue.empty(): # as long as the queue is not empty
        port = queue.get() # the thread will take the next element & it will be removed
        if portScan(port, target):
            if port not in ImportantPorts:
                print("{}/tcp   open    unknown".format(port))
                open_ports.append(port) # to list the open ports
            else:
                print("{}/tcp   open    {}".format(port, ImportantPorts[port]))
                open_ports.append(port) # to list the open ports
        else:
            continue
            #print("Port {} is closed!".format(port)) if i were to print the closed ports, the result will be choatic and to prevent that i'll print the open ones only
            
port_list = range(1,10000)

fill_queue(port_list=port_list)

thread_list = []
def run():
     # my own computer
    for t in range(500):
        thread = threading.Thread(target=worker) # i pointed the target function to the worker function instead of calling it
        thread_list.append(thread)

    for thread in thread_list:
        thread.start() # here the programs start launching the 500 threads

    for thread in thread_list:
        thread.join() # it doesn't join the thread until it finishes it work (it's like an indication of stopping)

    print("Open ports are: ", open_ports) # this won't print until all threads finished their work