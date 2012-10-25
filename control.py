import bottle
import json
import os
import subprocess


@bottle.get('<file:re:^.*\.(css|less|js|jpg|png|gif|ttf)>')
def static_file(file):
    return bottle.static_file(file, root=os.getcwd()+'/static/')

@bottle.get('/')
@bottle.view('index')
def index(name='World'):
    filedict = {}
    files = sorted(os.listdir(media_dir))
    for f in range(len(files)):
        filedict[f] = files[f]
    
    return {'filedict': filedict}

@bottle.get('/control')
def control():
    action = bottle.request.query.action
    track = bottle.request.query.track
    if action == 'playtrack':
        print "track" + track
        filepath = os.path.join(media_dir, track)
        blink1 = blinken.BlinkRun(0.2)
        blink1.start()
        subprocess.call(["mplayer", filepath])
        blink1.stop()
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

    media_dir = '/home/pi/files'
    import blinken
    bottle.run(host='0.0.0.0', port=8081, reloader=True)
