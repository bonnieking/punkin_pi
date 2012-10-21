import bottle
import gst_audio
import json


@bottle.get('<file:re:^.*\.(css|less|js|jpg|png|gif|ttf)>')
def static_file(file):
    return bottle.static_file(file, root='/home/pi/web')


@bottle.get('/')
@bottle.view('index.tpl')
def index():

    return '''<!DOCTYPE html><html><head><meta charset="utf-8">
<meta http-equiv="Content-Script-Type" content="text/javascript">
<title>SCARY</title>
<pre id="console"></pre>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>

<script type="text/javascript">
    $(document).ready(function() { 
    $('#soundtoggle').click(function() {
        $('#status').empty()
        $.ajax({ url: '/control?action=playtrack&track=a',
            cache: false, type: 'GET',
            success: function(data) {
            $('#status').append(data);}
        });
    })
    $('#lighttoggle1').click(function() {
        $('#status').empty()
        $.ajax({ url: '/control?action=blinken1',
            cache: false, type: 'GET',
            success: function(data) {
            $('#status').append(data);}
        });
    })
});
</script>
<style>
        body { background-color: white; }
        pre { font-family: monospace;
              color: black;
        }
        h2 { color: orange;
             font-family: 'arial';}
</style>
</head>
<body>
<h3>Pumpkin Pi control</h3>
<button id='soundtoggle'>Play sound</button> <br><br>
<button id='lighttoggle1'>Flash lights</button> <br><br>
<div id='status'></div>

</body></html>'''



@bottle.get('/control')
def control():
    action = bottle.request.query.action
    track = bottle.request.query.track
    if action == 'playtrack':
        print "track" + track
        audioplayer.setUri("file:///home/pi/files/h.wav")     
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
    import gst_audio
    import blinken
    bottle.run(host='0.0.0.0', port=8081, reloader=True)
