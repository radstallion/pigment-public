from multiprocessing import Process,  Queue, Event
import serial
import serial.tools.list_ports
import win32api
from win32con import *
from console_message import *
import time

def execCmd(queue,e):
    try:
        while True:
            q = queue.get()
            if q == 48 :
                x,y = win32api.GetCursorPos()
                win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, 50, 0)
            elif q == 49:
                x,y = win32api.GetCursorPos()
                win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, -50, 0)
            if e.is_set():
                break;
    except KeyboardInterrupt:
        pass


def main():
    log(OKBLUE,"starting")
    port = ""
    skip = True
    while(skip):
        log(OKBLUE,"searching for device")
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
             if "Arduino" in p[1]:
                 log(OKBLUE,"device found")
                 port =p[0]
                 skip = False
        time.sleep(1)

    ser = serial.Serial(port)
    log(OKGREEN,"connected")
    queue = Queue()
    event = Event()
    p = Process(target=execCmd,args=(queue,event))
    p.daemon = True
    p.start()

    log(OKGREEN,"ready")
    log(WARNING,'Press Ctrl-C to quit.')

    try:
        while(1):
            if ser.inWaiting():
                read = ser.readline()
                ser.flush()
                print(read)
                queue.put(read[0])


    except KeyboardInterrupt:
        log(OKGREEN,"ending")
        event.set()
        p.join()
        log(OKGREEN,"ended")

if __name__ == '__main__':
    log(OKBLUE,"setting up")

    main()
    log(OKGREEN,"exited")
