import os
import pygame
from playsound import playsound
import speech_recognition as sr
import serial
import random

#function for checking the user input to the predicited user inputs
def check_for_match(input: str, match_list: list) -> bool:
    for match in match_list:
        if match in input:
            return True
    return False


#all potential dialog/responses for the user user
user_greetings = ["hello", "hi", "hey", "hay"]
user_y = ["yes", "yeah", "yea", "yup"]
user_n = ["no", "nope", "nah"]
user_hungry = ["food", "eat", "hunger", "hungry", "starving", "eating", "ate"]
user_what = ["what", "whats", "what's"]

#connecting to the arduino
ser = serial.Serial('/dev/cu.usbmodem14201')

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

#n responses  mp3s
n_responses = [file for file in os.listdir(folder_path) if file.startswith('n_response')]

#secondary_greetings responses  mp3s
secondary_greetings = [file for file in os.listdir(folder_path) if file.startswith('secondary_greeting')]

#idk responses  mp3s
idk = [file for file in os.listdir(folder_path) if file.startswith('idk')]

#hungry responses  mp3s
hungry = [file for file in os.listdir(folder_path) if file.startswith('hungry')]

#what responses  mp3s
what = [file for file in os.listdir(folder_path) if file.startswith('what')]


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
			MyText = MyText.split()
			print(MyText)
			print(user_hungry)
			
			# greeting the user
			if check_for_match(MyText, user_greetings):
				print("match greeting")
				#combining secondary greetings and convo starters as both potential responses.
				random_response = secondary_greetings + starters
				random_mp3_starter = random.choice(random_response)
				file_path_for_starter = os.path.join(folder_path, random_mp3_starter)
				pygame.mixer.music.load(file_path_for_starter)
				print(file_path_for_starter)
				#sends the signal to the arduino to start the motor
				ser.write(b'1')
				print(ser.name)
				print("arduino start")

				playsound(file_path_for_starter)

				#sends the signal to the arduino to stop the motor
				ser.write(b'0')
				print("arduino stop")

			# repsoning to the user when they say yes or something similar
			if check_for_match(MyText, user_y):
				print("match y")
				random_mp3_y_response = random.choice(y_responses)
				file_path_for_y_response = os.path.join(folder_path, random_mp3_y_response)
				pygame.mixer.music.load(file_path_for_y_response)
				print(file_path_for_y_response)

				ser.write(b'1')
				print(ser.name)
				print("arduino start")

				playsound(file_path_for_y_response)

				ser.write(b'0')
				print("arduino stop")

			# repsponding to the user when they say no or something similar
			if check_for_match(MyText, user_n):
				print("match n")
				random_mp3_n_response = random.choice(n_responses)
				file_path_for_n_response = os.path.join(folder_path, random_mp3_n_response)
				pygame.mixer.music.load(file_path_for_n_response)
				print(file_path_for_n_response)

				ser.write(b'1')
				print(ser.name)
				print("arduino start")

				playsound(file_path_for_n_response)

				ser.write(b'0')
				print("arduino stop")

				# responding to the user when they say something pertaining to food or hunger.
				if check_for_match(MyText, user_hungry):
					print("match hungry")
					random_mp3_hungry = random.choice(hungry)
					file_path_for_hungry = os.path.join(folder_path, random_mp3_hungry)
					pygame.mixer.music.load(file_path_for_hungry)
					print(file_path_for_hungry)

					ser.write(b'1')
					print(ser.name)
					print("arduino start")

					playsound(file_path_for_hungry)

					ser.write(b'0')
					print("arduino stop")

				# responding to the user if they say what.
				if check_for_match(MyText, user_what):
					print("match what")
					random_mp3_what = random.choice(what)
					file_path_for_what = os.path.join(folder_path, random_mp3_what)
					pygame.mixer.music.load(file_path_for_what)
					print(file_path_for_what)

					ser.write(b'1')
					print(ser.name)
					print("arduino start")

					playsound(file_path_for_what)

					ser.write(b'0')
					print("arduino stop")

				# responding to the user if they say something luffy cant understand.
				if (MyText not in user_greetings) or (MyText not in user_n) or (MyText not in user_hungry) or (MyText not in user_what) or (MyText not in user_y):
					print("match idk")
					random_mp3_idk = random.choice(idk)
					file_path_for_idk = os.path.join(folder_path, random_mp3_idk)
					pygame.mixer.music.load(file_path_for_idk)
					print(file_path_for_idk)

					ser.write(b'1')
					print(ser.name)
					print("arduino start")

					playsound(file_path_for_idk)

					ser.write(b'0')
					print("arduino stop")
						

	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		#saying something to the user when the program cant understand them or hear them
		print("match error")
		random_mp3_error = random.choice(errors)
		file_path_for_error = os.path.join(folder_path, random_mp3_error)
		pygame.mixer.music.load(file_path_for_error)
		print(file_path_for_error)

		ser.write(b'1')
		print(ser.name)
		print("arduino start")

		playsound(file_path_for_error)

		ser.write(b'0')
		print("arduino stop")
