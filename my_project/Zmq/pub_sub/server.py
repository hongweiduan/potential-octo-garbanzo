# !/usr/bin/python
# -*- coding:utf-8 -*-

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5000")

while 1:
    msg = raw_input('input your data:')
    socket.send(msg)


