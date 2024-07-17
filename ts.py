import os
import pygame
from playsound import playsound
import speech_recognition as sr
import serial
import random
import time

start_time = time.perf_counter()


#function for checking the user input to the predicited user inputs
def check_for_match(input: str, match_list: list) -> bool:
    for match in match_list:
        if match in input:
            return True
    return False


#all potential dialog/responses for the user user
user_greetings = ["hello", "hi", "hey", "hay"]
user_y = ["yes", "yeah", "yea", "yup", "yep"]
user_n = ["no", "nope", "nah"]
user_hungry = ["food", "eat", "hunger", "hungry", "starving", "eating", "ate"]
user_what = ["what", "whats", "what's"]
user_question = ["are", "is"]
user_question1 = ["who", "when", "where", "why"]
user_bye = ["bye", "goodbye"]

#connecting to the arduino
# ser = serial.Serial('/dev/cu.usbmodem14201')

#organize and store the mp3 files
pygame.mixer.init()

folder_path = 'luffy_mp3s'

#greeting mp3s
greetings = [file for file in os.listdir(folder_path) if file.startswith('greeting')]
#error mp3s
errors = [file for file in os.listdir(folder_path) if file.startswith('error')]
#y mp3s
y = [file for file in os.listdir(folder_path) if file.startswith('y')]
#n mp3s
n = [file for file in os.listdir(folder_path) if file.startswith('n')]
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
#thankyou responses  mp3s
ty_response = [file for file in os.listdir(folder_path) if file.startswith('ty_response')]
#luffy singing  mp3s
song = [file for file in os.listdir(folder_path) if file.startswith('song')]
#when luffy is mad  mp3s
mad = [file for file in os.listdir(folder_path) if file.startswith('mad')]
#you cant responses  mp3s
you_cant_response = [file for file in os.listdir(folder_path) if file.startswith('you_cant_response')]
#when the user says idk responses  mp3s
useridk = [file for file in os.listdir(folder_path) if file.startswith('useridk_response')]
#convo enders  mp3s
enders = [file for file in os.listdir(folder_path) if file.startswith('enders')]
#when lufyy is saying bye  mp3s
bye = [file for file in os.listdir(folder_path) if file.startswith('bye')]

#intial phone ring
# playsound('ring.mp3')

#luffy answering the phone
playsound("luffy_mp3s/greeting_hey.mp3")
r = sr.Recognizer()

# luffy starts a convo after 5 seconds of silence
def convo_starter():
	print("match starter")
	random_mp3_starter = random.choice(starters)
	file_path_for_starter = os.path.join(folder_path, random_mp3_starter)
	pygame.mixer.music.load(file_path_for_starter)
	print(file_path_for_starter)

	# ser.write(b'1')
	# print(ser.name)
	# print("arduino start")

	playsound(file_path_for_starter)

	# ser.write(b'0')
	# print("arduino stop")


# luffy starts a convo after 5 seconds of silence
last_time_luffy_spoke = time.perf_counter()
print(last_time_luffy_spoke)
starter_timer = last_time_luffy_spoke + 5
print(starter_timer)
if starter_timer <= last_time_luffy_spoke:
	print("match starter")
	random_mp3_starter = random.choice(starters)
	file_path_for_starter = os.path.join(folder_path, random_mp3_starter)
	pygame.mixer.music.load(file_path_for_starter)
	print(file_path_for_starter)

	# ser.write(b'1')
	# print(ser.name)
	# print("arduino start")

	playsound(file_path_for_starter)

	# ser.write(b'0')
	# print("arduino stop")

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
			
			# greeting the user
			if check_for_match(MyText, user_greetings):
				print("match greeting")
				#combining secondary greetings and convo starters as both potential responses.
				random_mp3_starter = random.choice(secondary_greetings + starters)
				file_path_for_starter = os.path.join(folder_path, random_mp3_starter)
				pygame.mixer.music.load(file_path_for_starter)
				print(file_path_for_starter)
				#sends the signal to the arduino to start the motor
				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")

				playsound(file_path_for_starter)

				#sends the signal to the arduino to stop the motor
				# ser.write(b'0')
				# print("arduino stop")

				# luffy starts a convo after 5 seconds of silence
				last_time_luffy_spoke = time.perf_counter()
				if last_time_luffy_spoke + 5 <= last_time_luffy_spoke:
					convo_starter()

			# repsoning to the user when they say yes or something similar
			if check_for_match(MyText, user_y):
				print("match y")
				random_mp3_y_response = random.choice(y_responses)
				file_path_for_y_response = os.path.join(folder_path, random_mp3_y_response)
				pygame.mixer.music.load(file_path_for_y_response)
				print(file_path_for_y_response)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")

				playsound(file_path_for_y_response)

				# ser.write(b'0')
				# print("arduino stop")

				# luffy starts a convo after 5 seconds of silence
				last_time_luffy_spoke = time.perf_counter()
				if last_time_luffy_spoke + 5 <= last_time_luffy_spoke:
					convo_starter()

			# repsponding to the user when they say no or something similar
			if check_for_match(MyText, user_n):
				print("match n")
				random_mp3_n_response = random.choice(n_responses)
				file_path_for_n_response = os.path.join(folder_path, random_mp3_n_response)
				pygame.mixer.music.load(file_path_for_n_response)
				print(file_path_for_n_response)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")

				playsound(file_path_for_n_response)

				# ser.write(b'0')
				# print("arduino stop")

				# luffy starts a convo after 5 seconds of silence
				last_time_luffy_spoke = time.perf_counter()
				if last_time_luffy_spoke + 5 <= last_time_luffy_spoke:
					convo_starter()

			# responding to the user when they say something pertaining to food or hunger.
			if check_for_match(MyText, user_hungry):
				print("match hungry")
				random_mp3_hungry = random.choice(hungry)
				file_path_for_hungry = os.path.join(folder_path, random_mp3_hungry)
				pygame.mixer.music.load(file_path_for_hungry)
				print(file_path_for_hungry)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")

				playsound(file_path_for_hungry)

				# ser.write(b'0')
				# print("arduino stop")

				# luffy starts a convo after 5 seconds of silence
				last_time_luffy_spoke = time.perf_counter()
				if last_time_luffy_spoke + 5 <= last_time_luffy_spoke:
					convo_starter()

			# responding to the user if they say what.
			if check_for_match(MyText, user_what):
				print("match what")
				random_mp3_what = random.choice(what + y + n + idk)
				file_path_for_what = os.path.join(folder_path, random_mp3_what)
				pygame.mixer.music.load(file_path_for_what)
				print(file_path_for_what)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")

				playsound(file_path_for_what)

				# ser.write(b'0')
				# print("arduino stop")

				# luffy starts a convo after 5 seconds of silence
				last_time_luffy_spoke = time.perf_counter()
				if last_time_luffy_spoke + 5 <= last_time_luffy_spoke:
					convo_starter()



			# responding to the user if they ask a yes or n question.
			if check_for_match(MyText, user_question):
				print("match question")
				random_mp3_question = random.choice(y + n + idk)
				file_path_for_question = os.path.join(folder_path, random_mp3_question)
				pygame.mixer.music.load(file_path_for_question)
				print(file_path_for_question)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")
				playsound(file_path_for_question)
				# ser.write(b'0')
				# print("arduino stop")

				#starts a new convo or ends the convo
				print("match starter or enders")
				random_mp3_next = random.choice(starters + enders)
				file_path_for_next = os.path.join(folder_path, random_mp3_next)
				pygame.mixer.music.load(file_path_for_next)
				print(file_path_for_next)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")
				playsound(file_path_for_next)
				# ser.write(b'0')
				# print("arduino stop")

				#starts a convo after 5 secons of silence
				last_time_luffy_spoke = time.perf_counter()
				if last_time_luffy_spoke + 5 <= last_time_luffy_spoke:
					convo_starter()

			# responding to the user if they ask a yes or n question.
			if check_for_match(MyText, user_question1):
				print("match question1")
				random_mp3_question1 = random.choice(idk)
				file_path_for_question1 = os.path.join(folder_path, random_mp3_question1)
				pygame.mixer.music.load(file_path_for_question1)
				print(file_path_for_question1)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")
				playsound(file_path_for_question1)
				# ser.write(b'0')
				# print("arduino stop")

				#starts a new convo or ends the convo
				print("match starter or enders")
				random_mp3_next = random.choice(starters + enders)
				file_path_for_next = os.path.join(folder_path, random_mp3_next)
				pygame.mixer.music.load(file_path_for_next)
				print(file_path_for_next)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")
				playsound(file_path_for_next)
				# ser.write(b'0')
				# print("arduino stop")

				#starts a convo after 5 secons of silence
				last_time_luffy_spoke = time.perf_counter()
				if last_time_luffy_spoke + 5 <= last_time_luffy_spoke:
					convo_starter()

						
			# responding to the user if they say luffy cant.
			if ("you can't" in MyText) or ("you can not" in MyText):
				print("match you cant")
				random_mp3_mad = random.choice(mad)
				file_path_for_mad = os.path.join(folder_path, random_mp3_mad)
				pygame.mixer.music.load(file_path_for_mad)
				print(file_path_for_mad)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")
				playsound(file_path_for_mad)
				# ser.write(b'0')
				# print("arduino stop")

				#starts a new convo or ends the convo
				print("match starter or enders")
				random_mp3_next = random.choice(starters + enders)
				file_path_for_next = os.path.join(folder_path, random_mp3_next)
				pygame.mixer.music.load(file_path_for_next)
				print(file_path_for_next)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")
				playsound(file_path_for_next)
				# ser.write(b'0')
				# print("arduino stop")

				#luffy starts a convo after 5 secons of silence
				last_time_luffy_spoke = time.perf_counter()
				if last_time_luffy_spoke + 5 <= last_time_luffy_spoke:
					convo_starter()

			# responding to asking luffy is he does or doesn't cant.
			if ("do you" in MyText) or ("dont you" in MyText):
				print("match do/dont you")
				random_mp3_do = random.choice(idk + y + n)
				file_path_for_do = os.path.join(folder_path, random_mp3_do)
				pygame.mixer.music.load(file_path_for_do)
				print(file_path_for_do)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")
				playsound(file_path_for_do)
				# ser.write(b'0')
				# print("arduino stop")

				#starts a new convo or ends the convo
				print("match starter or enders")
				random_mp3_next = random.choice(starters + enders)
				file_path_for_next = os.path.join(folder_path, random_mp3_next)
				pygame.mixer.music.load(file_path_for_next)
				print(file_path_for_next)

				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")
				playsound(file_path_for_next)
				# ser.write(b'0')
				# print("arduino stop")

				#luffy starts a convo after 5 secons of silence
				last_time_luffy_spoke = time.perf_counter()
				if last_time_luffy_spoke + 5 <= last_time_luffy_spoke:
					convo_starter()

			# saying by to the user
			if check_for_match(MyText, user_bye):
				print("match bye")
				#combining secondary greetings and convo starters as both potential responses.
				random_mp3_bye = random.choice(bye)
				file_path_for_bye = os.path.join(folder_path, random_mp3_bye)
				pygame.mixer.music.load(file_path_for_bye)
				print(file_path_for_bye)
				#sends the signal to the arduino to start the motor
				# ser.write(b'1')
				# print(ser.name)
				# print("arduino start")
				playsound(file_path_for_bye)
				quit()
				#sends the signal to the arduino to stop the motor
				# ser.write(b'0')
				# print("arduino stop")



	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		#saying something to the user when the program cant understand them or hear them
		print("match error")
		random_mp3_error = random.choice(errors)
		file_path_for_error = os.path.join(folder_path, random_mp3_error)
		pygame.mixer.music.load(file_path_for_error)
		print(file_path_for_error)

		# ser.write(b'1')
		# print(ser.name)
		# print("arduino start")

		playsound(file_path_for_error)

		# ser.write(b'0')
		# print("arduino stop")

		# luffy starts a convo after 5 seconds of silence
		last_time_luffy_spoke = time.perf_counter()
		print(last_time_luffy_spoke)
		starter_timer = last_time_luffy_spoke + 5
		print(starter_timer)
		if starter_timer <= last_time_luffy_spoke:
			print("match starter")
			random_mp3_starter = random.choice(starters)
			file_path_for_starter = os.path.join(folder_path, random_mp3_starter)
			pygame.mixer.music.load(file_path_for_starter)
			print(file_path_for_starter)

			# ser.write(b'1')
			# print(ser.name)
			# print("arduino start")

			playsound(file_path_for_starter)

			# ser.write(b'0')
			# print("arduino stop")