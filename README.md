Project: punkin_pi
====================
Scary Halloween pumpkin with lights and sound controlled by a Raspberry Pi.  Refer to element14 blog posts for more info: http://www.element14.com/community/groups/raspberry-pi/blog/tags/pumpkin_pi

Written by Bonnie King and Drew Fustini.  Code and design is public domain.

Install dependencies:
---------------------
<code>
sudo apt-get install git-core mplayer python-setuptools 
</code>

<code>
sudo easy_install bottle
</code>

<code>
sudo easy_install RPi.GPIO  #note: already installed in the latest Sept-18 Raspbian image
</code>

Install sound clip files:
--------------------------

<code>
pi@raspberrypi ~ $ mkdir files
</code>

<code>
pi@raspberrypi ~ $ cd files
</code>

<code>
pi@raspberrypi ~/files $ wget http://www.countessbloodshalloweenhorror.com/sounds/howl.wav
</code>

<code>
pi@raspberrypi ~/files $ wget http://www.countessbloodshalloweenhorror.com/sounds/scream.wav
</code>

<code>
pi@raspberrypi ~/files $ wget http://www.countessbloodshalloweenhorror.com/sounds/ghostgigl.wav
</code>

Any files that mplayer can play can be put into /home/pi/files such as .wav, .mp3 & .ogg.


Install & run punkin_pi:
------------------------
<code>
pi@raspberrypi ~ $ git clone https://github.com/pdp7/punkin_pi.git
</code>

To run the demo server:

<code>
pi@raspberrypi ~/punkin_pi $ sudo python ./control.py
</code>

Audio troubleshooting:
----------------------
If you want to check if punkin_pi will be able to play a particular file in /home/pi/files, then try to play it with mplayer:

<code>
mplayer /home/pi/files/<filename>
</code>

Sometimes the sound system may become unstable and produce errors.  Restarting ALSA should resolve this:

<code>
/etc/init.d/alsa-utils restart
</code>

If your speakers lack a volume control, then the ALSA mixer can be used:

<code>
alsamixer
</code>