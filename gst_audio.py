import os
import gst


class AudioPlayer:
    def __init__(self):   
        self.player = gst.element_factory_make("playbin", "player")
    
    def stop(self):
        self.player.set_state(gst.STATE_NULL)

    def start(self, filepath):
        self.player.set_property('uri','file://'+os.path.abspath(filepath))
        self.player.set_state(gst.STATE_PLAYING)
  
    #def toggle_pause(self):
        # current state is 1th item in the tuple
    #    current_state = self.player.get_state[1]
        


