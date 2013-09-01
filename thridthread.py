#!/usr/bin/env python
#-*- coding: utf-8 -*-
import threading, time
def doWaiting():
    print 'start waiting:', time.strftime('%H:%M:%S')
    time.sleep(100)
    print 'stop waiting:', time.strftime('%H:%M:%S')
thread1 = threading.Thread(target = doWaiting)
thread1.setDaemon(True)
thread1.start()
time.sleep(10) #Ensure thread1 has started
print '1 Current time:', time.strftime('%H:%M:%S')
print 'start join'
print '2 Current time:', time.strftime('%H:%M:%S')
print '1 thread1 is alive or not:', thread1.isAlive()
#thread1.join() #Blocked until thread1 finished
print '2 thread1 is alive or not:', thread1.isAlive()
print 'end join'