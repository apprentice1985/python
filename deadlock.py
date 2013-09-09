#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Deadlock - Chapter 21 - deadlock.py
import threading
import time

a = 5
alock = threading.Lock()
b = 5
block = threading.Lock()
def thread1calc():
    print "Thread1 acquiring lock a\n"
    alock.acquire()
    time.sleep(5)
    
    print "Thread1 acquiring lock b\n"
    block.acquire()
    time.sleep(5)
    
    a += 5
    b += 5
    print "Thread1 releasing both locks\n"
    block.release()
    alock.release()
def thread2calc():
    print "Thread2 acquiring lock b\n"
    block.acquire()
    time.sleep(5)
    
    print "Thread2 acquiring lock a\n"
    alock.acquire()
    time.sleep(5)
    
    a += 10 
    b += 10
    
    print "Thread2 releasing both locks\n"
    block.release()
    alock.release()

t = threading.Thread(target = thread1calc)
t.setDaemon(True)
t.start()

t = threading.Thread(target = thread2calc)
t.setDaemon(True)
t.start()

while 1:
    #Sleep forever
    time.sleep(300)