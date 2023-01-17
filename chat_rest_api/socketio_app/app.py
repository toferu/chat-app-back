import socketio

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins = "*")
app = socketio.ASGIApp(sio)

background_task_started = False

def background_task(sid):
    sio.sleep(5)
    result = sio.call('mult', {'numbers': [3,4]}, to=sid)
    print(result)

@sio.on('connect')
async def test_connect(sid,environ):
    global background_task_started
    if not background_task_started:
        sio.start_background_task(background_task)
        background_task_started = True
    await sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)

@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')

@sio.event
async def send_message(sid, data):
    # await sio.emit('my_response', {'message' : data}, to=sid)
    response = {sid: data}
    return response