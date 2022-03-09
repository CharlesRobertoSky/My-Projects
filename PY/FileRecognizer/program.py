import os
import shutil
from time import sleep
import PySimpleGUI
formato_de_imagens = ['jpeg', 'jpg', 'png', 'gif', 'webp', 'tiff']
formato_de_audio = ['mp3', 'wav']
formato_de_video = ['mp4', 'avi', 'webm']
formato_de_docs = ['ai', 'ait', 'txt', 'rtf']
formato_de_py = ['py']

try:
	os.mkdir('images')
	os.mkdir('audios')
	os.mkdir('videos')
	os.mkdir('docs')
	os.mkdir('others')
except:
	num = 0

atual_cwd = os.getcwd()

while True:

	files = os.listdir(atual_cwd)
	for file in files:
		if os.path.isfile(file) and file != "app.py":
			ext = (file.split(".")[-1]).lower()
			if ext in formato_de_imagens:
				shutil.move(file, "images/"+file)
			elif ext in formato_de_audio:
				shutil.move(file, "audios/"+file) 
				
			elif ext in formato_de_video:
				shutil.move(file, "videos/"+file)
			elif ext in formato_de_docs:
				shutil.move(file, "docs/"+file)
			elif ext in formato_de_py:
				pass
			else:
				shutil.move(file, "others/"+file)
	sleep(20)
