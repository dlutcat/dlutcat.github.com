#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import time
import threading
import Queue

def server(port, N):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    q = Queue.Queue()
    for x in range(N):
        t = threading.Thread(target=thread_worker, args=(q, ))
        t.daemon = True
        t.start()
    print 'Ready and waiting with %d threads on port %d' % (N, port)
    while True:
        cli, addr = s.accept()
        q.put(cli)

def thread_worker(q):
    sock = q.get()
    handle_request(sock, time.sleep)

def handle_request(s, sleep):
    try:
        s.recv(1024)
        sleep(0.1)
        s.send('''http/1.0 200 OK
                  Hello World! ''')
        s.shutdown(socket.SHUT_WR)
        print '.',
    except Exception, ex:
        print ex
    finally:
        sys.stdout.flush()
        s.close()

if __name__ == '__main__':
    server(4444, 5)
