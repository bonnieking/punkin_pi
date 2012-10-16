import bottle
import gst_audio
import json


@bottle.get('<file:re:^.*\.(css|less|js|jpg|png|gif|ttf)>')
def static_file(file):
    return bottle.static_file(file, root='./web')


@bottle.get('/')
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
        $.ajax({ url: '/control?action=playtrack',
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
    $('#lighttoggle2').click(function() {
        $('#status').empty()
        $.ajax({ url: '/control?action=blinken2',
            cache: false, type: 'GET',
            success: function(data) {
            $('#status').append(data);}
        });
    })
});
</script>

</head><body>
<button id='soundtoggle'>sound toggle</button> <br><br>
<button id='lighttoggle1'>light toggle 1</button> <br><br>
<button id='lighttoggle2'>light toggle 2</button> <br><br>
<div id='status'></div>

</body></html>'''

@bottle.get('/control')
def control():
    #ret_dict = {'action': action,
    #            'blink1': b1_state,
    #            'blink2': b2_state}
    
    action = bottle.request.query.action
    if action == 'playtrack':
        pass         
    elif action == 'blinken1':
        blink1 = blinken.BlinkRun(17, 0.2)
        blink1.start()
    elif action == 'blinken2':   
        blink2 = blinken.BlinkRun(18, 0.2)
        blink2.blinker.reset()
        blink2.start()
        pass
    print action
    yield '{0}: {1}\n'.format('action', action)
    

@bottle.post('/doit')
def doit():
    bottle.response.set_header('Content-Type', 'text/plain')
    print bottle.request.headers.keys()
    print bottle.request.forms.keys()
    for key in sorted(bottle.request.forms.keys()):
        print key, bottle.request.forms[key]
    #for key in bottle.request.headers.keys():
        yield '{0}: {1}\n'.format(key, bottle.request.forms[key])
    #yield '\n'
#    for row in bottle.request.body:
#        yield row
#    yield '=*=*=*=*=*=*=*=*=*=*=\n'
#    for key in sorted(bottle.request.forms.keys()):
#        yield '{}: {}\n'.format(key, bottle.request.forms[key])
#    for key in bottle.request.files.keys():
#        yield 'file: {!r}'.format(bottle.request.files[key].filename)

if __name__ == '__main__':
    bottle.debug(True)

    import gst_audio
    import blinken
    audioplayer = gst_audio.AudioPlayer()
    bottle.run(host='0.0.0.0', port=8081, reloader=True)
