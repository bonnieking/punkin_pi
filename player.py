import bobo, os
import gst_audio 

audioplayer = gst_audio.AudioPlayer()

def config(config):
    global media_dir
    media_dir = config['media_dir']
    if not os.path.exists(media_dir):
        pass

player_html = os.path.join(os.path.dirname(__file__), 'player.html')

@bobo.query('/')
def index():
    return """<html><head><title>Bobo Wiki</title></head><body>
    SCARY MUSIC 
    <hr />
    %(docs)s
    </body></html>
    """ % dict(
        docs='<br />'.join('<a href="%s?button=start">%s</a>' % (name, name)
                           for name in sorted(os.listdir(media_dir)))
        )

@bobo.query('/:name')
def toggle(bobo_request, name, button):
    if button not in ['start', 'stop']:
        return '500'
    foo = "BAR"
    path = os.path.join(media_dir, name)

    if button == 'start':
        foo = 'we are playing, so we will stop'
        if os.path.exists(path):
            audioplayer.start(path)
            button = 'stop'
        else:
            return "No Such File %s" % (name)

    elif button == 'stop':
        foo = 'we are stopped, so we will play'
        audioplayer.stop()
        button = 'start'
    return open(player_html).read() % dict(name=name, 
        button=button, b=bobo_request, foo=foo)



#@bobo.query('/:name')
#def player(name, action='start'):
#    foo = 'this is a get'
#    button = 'start'
#    return open(player_html).read() % dict(name=name, 
#        button=button, foo=foo, b='get')
