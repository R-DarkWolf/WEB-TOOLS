# Create por R-DarkWolf
from termcolor import colored
from pyfiglet import Figlet
from gtts import gTTS
import webbrowser
import youtube_dl
import wikipedia
import pafy
import time
import sys
import os

def mod(s):
	for p in s + '\n':
		sys.stdout.write(p)
		sys.stdout.flush()
		time.sleep(1./70)
	
def menu():
	#Menu
	print("\n")
	print("\n")
	b = Figlet(font='banner3-D')
	print(colored(b.renderText("+WEB+"), 'green'))
	print(colored(b.renderText("TOOLS"), 'yellow'))
	print("\033[31m")
	mod("""	******************
		MENÚ
	******************
	
	1] GOOGLE
	2] YOUTUBE
	3] DESCARGAR-VIDEOS
	4] CONVERTIR TEXTO A VOZ
	5] SALIR
	""")
def naomi():
	# Desarrollo del menu
	menu()
	opc = int(input("\033[32m Elija una opcion del menu: "))
	while (opc >0 and opc <6):
		if (opc==1):
			g = input("Ingrese el texto a buscar ")
			webbrowser.open('https://google.com/?#q=' + g)
		elif (opc==2):
			y = input("Ingrese lo que quiere buscar: ")
			webbrowser.open('https://www.youtube.com/results?search_query=' + y)
		elif (opc==3):
			mod("Descargar Videos")
			url = input("\033[31m[\033[33m*\033[31m]\033[34m Ingrese la URL: ")
			video = pafy.new(url)
			
			videostrams = video.streams
			for i in videostrams:
				print(i)
				best = video.getbest()
				if(best):
					mod("\033[32m Iniciando descarga")
					mod("\033[32m Descargando video...")
					print(best.resolution, best.extension)
					best.download()
					mod("\033[36m Vídeo descargado")
					input("Presione ENTER para continuar...")
					os.system("clear")
					naomi()
		elif (opc==4):
			mod("Convertir texto a voz desde wikipedia")
			wikipedia.set_lang('es')
			name = input("Ingrese la palabra para buscar en wikipedia: ")
			sentences = int(input("Ingrese el número de sentences: "))
			texto_wiki = wikipedia.summary(name, sentences)
			tts = gTTS(texto_wiki, lang = 'es')
			audio = input("Ingrese nombre para su archivo: ")
			tts.save(audio+".mp3")
			input("Presione ENTER para continuar...")
			os.system("clear")
			naomi()
			
		elif (opc==5):
			os.system('clear')
			mod('')
			mod("Gracias")
			sys.exit()
	else:
			os.system("clear")
			mod("\n")
			mod("\n")
			mod("Opcion Incorrecta ")
			time.sleep(3)
			os.system('clear')
			naomi()
naomi()

#Final 
