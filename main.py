from moviepy.editor import *
import os
# color
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
#end
logo ='''

%s __   __  _______  _   ___ %s _______  _______ %s __   __  _______  _______ 
%s|  |_|  ||       || | |   |%s|       ||       |%s|  |_|  ||       ||       |
%s|       ||    _  || |_|   |%s|_     _||   _   |%s|       ||    _  ||___    |
%s|       ||   |_| ||       | %s |   |  |  | |  |%s|       ||   |_| | ___|   |
%s|       ||    ___||___    | %s |   |  |  |_|  |%s|       ||    ___||___    |
%s| ||_|| ||   |        |   | %s |   |  |       |%s| ||_|| ||   |     ___|   |
%s|_|   |_||___|        |___| %s |___|  |_______|%s|_|   |_||___|    |_______|%s
'''%( k,b,u,k,b,u,k,b,u,k,b,u,k,b,u,k,b,u,k,b,u,p )
def mp4tomp3(_,__):
	convert = VideoFileClip(_)
	convert.audio.write_audiofile('%s.mp3'%__)
	print('  %s[%s+%s]%s tersimpan : %s.mp3 %s'%(k,u,k,b,__,p))
def Main():
	os.system('clear')
	print(logo)
	print('  %s[%s!%s]%s support url/file video, not support Youtube%s'%(k,m,k,m,p))
	while True:
		file = input('  %s[%s+%s]%s file :%s '%(k,u,k,b,p))
		if file in os.listdir('.'):
			out = input('  %s[%s+%s]%s simpan :%s '%(k,u,k,b,p))
			if out in ['',' ']:
				print('  %s[x] nama tidak valid%s'%(m,p))
			else:
				mp4tomp3(file,out)
				break
		else:
			print('  %s[%s+%s]%s File Tidak Ada%s'%(k,u,k,b,p))
if __name__ == '__main__':
	Main()
