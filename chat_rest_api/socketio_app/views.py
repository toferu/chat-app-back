from django.shortcuts import render

# Create your views here.

# set async_mode to 'threading', 'eventlet', 'gevent' or 'gevent_uwsgi' to
# force a mode else, the best mode is selected automatically from what's
# installed
async_mode = 'eventlet'

import os

# from django.http import HttpResponse
import socketio
import json
# basedir = os.path.dirname(os.path.realpath(__file__))
# sio = socketio.Server(async_mode=async_mode)
# sio = socketio.Server(logger= True, cors_allowed_origins="*")

# thread = None



# sio.on('send_message', lambda a, b :
#     sio.emit('my_response', {'data': b}))



def index(request):
    
    return 


# def index(request):
#     global thread
#     if thread is None:
#         thread = sio.start_background_task(background_thread)
#     return HttpResponse(open(os.path.join(basedir, 'static/index.html')))


# def background_thread():
#     """Example of how to send server generated events to clients."""
#     count = 0
#     while True:
#         sio.sleep(10)
#         count += 1
#         sio.emit('my_event', {'data': 'Server generated event'},
#                  namespace='/test')


# @sio.event
# def my_event(sid, message):
#     sio.emit('my_response', {'message': 'data'}, room=sid)


# @sio.event
# def my_broadcast_event(sid, message):
#     sio.emit('my_response', {'data': message['data']})


# @sio.event
# def join(sid, message):
#     sio.enter_room(sid, message['room'])
#     sio.emit('my_response', {'data': 'Entered room: ' + message['room']},
#              room=sid)


# @sio.event
# def leave(sid, message):
#     sio.leave_room(sid, message['room'])
#     sio.emit('my_response', {'data': 'Left room: ' + message['room']},
#              room=sid)


# @sio.event
# def close_room(sid, message):
#     sio.emit('my_response',
#              {'data': 'Room ' + message['room'] + ' is closing.'},
#              room=message['room'])
#     sio.close_room(message['room'])


# @sio.event
# def my_room_event(sid, message):
#     sio.emit('my_response', {'data': message['data']}, room=message['room'])


# @sio.event
# def disconnect_request(sid):
#     sio.disconnect(sid)


# @sio.event
# def connect(sid, environ):
#     sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)


# @sio.event
# def disconnect(sid):
#     print('Client disconnected')