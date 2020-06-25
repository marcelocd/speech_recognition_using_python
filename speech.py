import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)

	print('Say anything: ')

	audio = r.listen(source)

	try: 
		text = r.recognize_google(audio)
		
		print('You said: {}'.format(text))
	except:
		print('Sorry. Could not recognize your voice')