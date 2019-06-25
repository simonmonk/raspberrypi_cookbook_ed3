import subprocess

sound_file = '/home/pi/raspberrypi_cookbook_ed3/python/school_bell.mp3'
sound_out = 'local'

subprocess.run(['omxplayer', '-o', sound_out, sound_file])
