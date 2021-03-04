import os
# os.system('omxplayer /home/pi/Music/deadman-no-sugar.mp3 &')
#os.system('mpg321 /home/pi/Music/deadman-no-sugar.mp3&')
#os.system('pkill mpg321&')

musicDir = os.listdir('/home/pi/Music/')
#for song in musicDir:
print(musicDir[2])

#with os.scandir('/home/pi/Music/') as musicDir:
#    for song in musicDir:
#        print(song.name)
# os.system('omxplayer  --no-keys --vol -100 Newt.mp3 &')

#simple example in python
#p = subprocess.Popen(['mpg321', '-R', 'anyword'], stdin=PIPE)
#p.stdin.write('LOAD test.mp3\n')