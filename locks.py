#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Threading with locks - Chapter 21 -locks.py
import threading, time
#Initialize a simple variable
b = 50
#And a lock object
l = threading.Lock()
