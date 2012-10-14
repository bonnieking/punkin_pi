import bobo, os
import gst_audio 

audioplayer = gst_audio.AudioPlayer()

def config(config):
    global top
    top = config['directory']
    if not os.path.exists(top):
        os.mkdir(top)

player_html = os.path.join(os.path.dirname(__file__), 'player.html')

@bobo.query('/')
def index():
    return """<html><head><title>Bobo Wiki</title></head><body>
    SCARY MUSIC 
    <hr />
    %(docs)s
    </body></html>
    """ % dict(
        docs='<br />'.join('<a href="%s">%s</a>' % (name, name)
                           for name in sorted(os.listdir(top)))
        )

@bobo.post('/:name')
def toggle(bobo_request, name, butan):
    if butan not in ['start', 'stop']:
        return '500'
    foo = "BAR"
    path = os.path.join(top, name)

    if butan == 'start':
        foo = 'we are playing, so we will stop'
        if os.path.exists(path):
            audioplayer.start(path)
            butan = 'stop'
        else:
            return "No Such File %s" % (name)

    elif butan == 'stop':
        foo = 'we are stopped, so we will play'
        audioplayer.stop()
        butan = 'start'
    return open(player_html).read() % dict(name=name, 
        butan=butan, b=bobo_request, foo=foo)



@bobo.query('/:name')
def player(name, action='start'):
    foo = 'this is a get'
    butan = 'start'
    return open(player_html).read() % dict(name=name, 
        butan=butan, foo=foo, b='get')
