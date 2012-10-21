import bottle
import gst_audio
import json
import os


@bottle.get('<file:re:^.*\.(css|less|js|jpg|png|gif|ttf)>')
def static_file(file):
    return bottle.static_file(file, root='/home/pi/web')


@bottle.get('/')
@bottle.view('index')
def index():
    return "index stuff"

@bottle.route('/hello')
@bottle.route('/hello/<name>')
@bottle.view('index')
def hello(name='World'):
    files = sorted(os.listdir("/home/pi/files"))
    return {'files': files}

@bottle.get('/control')
def control():
    action = bottle.request.query.action
    track = bottle.request.query.track
    if action == 'playtrack':
        print "track" + track
        filepath = os.path.join(media_dir, track)
        audioplayer.setUri("file:///"+filepath)     
        audioplayer.play()     
    elif action == 'blinken1':
        blink1 = blinken.BlinkRun(0.2)
        blink1.start()
    print action
    yield '{0}: {1}\n'.format('action', action)
    

@bottle.post('/doit')
def doit():
    bottle.response.set_header('Content-Type', 'text/plain')
    print bottle.request.headers.keys()
    print bottle.request.forms.keys()
    for key in sorted(bottle.request.forms.keys()):
        print key, bottle.request.forms[key]
        yield '{0}: {1}\n'.format(key, bottle.request.forms[key])

if __name__ == '__main__':
    bottle.debug(True)

    audioplayer = gst_audio.AudioPlayer()
    media_dir = '/home/pi/files'
    import gst_audio
    import blinken
    bottle.run(host='0.0.0.0', port=8081, reloader=True)
