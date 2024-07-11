import os
import pygame
from playsound import playsound
import speech_recognition as sr
import pyttsx3 
import random

#organize and store the mp3 files
pygame.mixer.init()

folder_path = 'luffy_mp3s'

#greeting mp3s
greetings = [file for file in os.listdir(folder_path) if file.startswith('greeting')]

#error mp3s
errors = [file for file in os.listdir(folder_path) if file.startswith('error')]

#y mp3s
y = [file for file in os.listdir(folder_path) if file.startswith('y')]

#y responses mp3s
y_responses = [file for file in os.listdir(folder_path) if file.startswith('y_response')]

#starters  mp3s
starters = [file for file in os.listdir(folder_path) if file.startswith('starter')]
print(starters)

#n responses  mp3s
n_responses = [file for file in os.listdir(folder_path) if file.startswith('n_response')]

#all potential dialog/responses for the user user
user_greetings = ["hello", "hi", "whats up", "hey", "what's up"]
user_y = ["yes", "yeah", "yea", "yup"]
user_n = ["no", "nope", "nah"]

#intial phone ring
# playsound('ring.mp3')
playsound("luffy_mp3s/greeting_hey.mp3")
r = sr.Recognizer() 


#speech recognition starts listening here
while(1): 
	
	try:

		#turing what it hears into text
		with sr.Microphone() as source2:
			r.adjust_for_ambient_noise(source2, duration=0.2)
			audio2 = r.listen(source2)
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("user input: ", MyText)
			
			# greeting the user
			if MyText in user_greetings:
				random_mp3_starter = random.choice(starters)
				file_path_for_starter = os.path.join(folder_path, random_mp3_starter)
				pygame.mixer.music.load(file_path_for_starter)
				print(file_path_for_starter)
				playsound(file_path_for_starter)

			# repsoning to the user when they say yes or something similar
			if MyText in user_y:
				random_mp3_y_response = random.choice(y_responses)
				file_path_for_y_response = os.path.join(folder_path, random_mp3_y_response)
				pygame.mixer.music.load(file_path_for_y_response)
				print(file_path_for_y_response)
				playsound(file_path_for_y_response)

			# repsponding to the user when they say no or something similar
			if MyText in user_n:
				random_mp3_n_response = random.choice(n_responses)
				file_path_for_n_response = os.path.join(folder_path, random_mp3_n_response)
				pygame.mixer.music.load(file_path_for_n_response)
				print(file_path_for_n_response)
				playsound(file_path_for_n_response)


						

	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:

		random_mp3_error = random.choice(errors)
		file_path_for_error = os.path.join(folder_path, random_mp3_error)
		pygame.mixer.music.load(file_path_for_error)
		print(file_path_for_error)
		playsound(file_path_for_error)