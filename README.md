punkin_pi
=========

Scary halloween Pumpkin

run the demo server:

<code>
pi@raspberrypi ~/punkin_pi $ export PYTHONPATH=$PWD #this is needed so the modules are found
</code>

<code>
pi@raspberrypi ~/punkin_pi $ sudo python ./json_test3.py 
</code>

Required to install (assuming Debian or Raspbian):

<code>
apt-get install python-dev python-gst0.10 gstreamer0.10-plugins-base gstreamer0.10-plugins-good gstreamer0.10-plugins-bad gstreamer0.10-plugins-ugly
</code>

<code>
sudo easy_install RPi.GPIO
</code>