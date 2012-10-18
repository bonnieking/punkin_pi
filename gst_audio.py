import os
import gst
import gobject


class AudioPlayer:
    def __init__(self):
        self.playbin = gst.element_factory_make('playbin2')
        self.bus = self.playbin.get_bus()
        self.bus.connect("message::eos", self.on_finish)
        self.bus.add_signal_watch()
        self.is_playing = False  
        self.playbin.set_property('uri', 'file:///home/pi/files/h.wav')
        self.mainloop = gobject.MainLoop()
 
    def play(self):
        if self.get_state() != 'GST_STATE_PLAYING':
            self.playbin.set_state(gst.STATE_PLAYING)
            self.mainloop.run()
        else:
            print 'playing'

    def pause(self):
        self.playbin.set_state(gst.STATE_PAUSED)

    def on_finish(self, bus, message):
	self.playbin.set_state(gst.STATE_NULL)
	self.mainloop.quit()

    def get_state(self):
        s = self.playbin.get_state()[1]
        return s.value_name
