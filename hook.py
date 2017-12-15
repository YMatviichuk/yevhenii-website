#!/usr/bin/python
import socket
import sys
import os

if __name__ == "__main__":
    with daemon.DaemonContext():
        run()

def run():
    if (len(sys.argv) != 2 or not sys.argv[1].isdigit()):
        print 'Usage: hook <port>',
        exit()

    p = int(sys.argv[1])
    l = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', p))
    s.listen(1)
    while 1:
        (c, a) = s.accept()
        l.append(c)
        os.system("git pull")
        os.system("hugo -D")


