import os
import pygame
from playsound import playsound
import speech_recognition as sr
import serial
import random
from threading import Timer




#function for checking the user input to the predicited user inputs
def check_for_match(input: str, match_list: list) -> bool:
    for match in match_list:
        if match in input:
            return True
    return False

#function for checking the user input to the predicited user inputs
def check_for_no_match(input: str, match_list: list) -> bool:
    for match in match_list:
        if match in input:
            return False
    return True

#all potential dialog/responses for the user user
user_greetings = ["hello", "hi", "hey", "hay"]
user_y = ["yes", "yeah", "yea", "yup", "yep"]
user_n = ["no", "nope", "nah"]
user_hungry = ["food", "eat", "hunger", "hungry", "starving", "eating", "ate", "meat"]
user_what = ["what", "whats", "what's"]
user_question = ["are", "is", "do", "don't"]
user_question1 = ["who", "when", "where", "why", "how"]
user_bye = ["bye", "goodbye"]
user_ty = ["thanks", "thank"]
user_sleep = ["sleep", "sleeping"]

all_lists = (user_greetings + user_y + user_n + user_hungry + user_what + user_question + user_question1 + user_bye)

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
y = [file for file in os.listdir(folder_path) if file.startswith('yes')]
#n mp3s
n = [file for file in os.listdir(folder_path) if file.startswith('no')]
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
enders = [file for file in os.listdir(folder_path) if file.startswith('ender')]
#when lufyy is saying bye  mp3s
bye = [file for file in os.listdir(folder_path) if file.startswith('bye')]
#when lufyy is saying fillers
fillers = [file for file in os.listdir(folder_path) if file.startswith('filler')]

r = sr.Recognizer()

# luffy starts a convo
def convo_starter():
	print("match starter")
	random_mp3_starter = random.choice(starters + song)
	file_path_for_starter = os.path.join(folder_path, random_mp3_starter)
	pygame.mixer.music.load(file_path_for_starter)
	print(file_path_for_starter)
	ser.write(b'1')
	print(ser.name)
	print("arduino start")
	playsound(file_path_for_starter)
	ser.write(b'0')
	print("arduino stop")

#luffy ends the convo
def convo_over():
	print("match bye")
	# combining secondary greetings and convo starters as both potential responses.
	random_mp3_bye = random.choice(bye)
	file_path_for_bye = os.path.join(folder_path, random_mp3_bye)
	pygame.mixer.music.load(file_path_for_bye)
	print(file_path_for_bye)
	# sends the signal to the arduino to start the motor
	ser.write(b'1')
	print(ser.name)
	print("arduino start")
	playsound(file_path_for_bye)
	# sends the signal to the arduino to stop the motor
	ser.write(b'0')
	print("arduino stop")
	playsound("click.mp3")
	quit()

#luffy starts or ends the convo
def convo_both():
	print("match starter or enders")
	random_mp3_next = random.choice(starters + enders)
	file_path_for_next = os.path.join(folder_path, random_mp3_next)
	pygame.mixer.music.load(file_path_for_next)
	print(file_path_for_next)
	ser.write(b'1')
	print(ser.name)
	print("arduino start")
	playsound(file_path_for_next)
	ser.write(b'0')
	print("arduino stop")
	#theres a 1 in 4 chance that if these sound clips play luffy end the convo and hand up
	x = random.randint(1, 4)
	if file_path_for_next.startswith("ender"):
		if x == 1:
			convo_over()


# intial phone ring
# ser.write(b'1')
# print(ser.name)
# print("arduino start")
# playsound('ring.mp3')
# ser.write(b'0')
# print("arduino stop")

# intial phone ring
ser.write(b'1')
print(ser.name)
print("arduino start")
playsound('ring.mp3')
ser.write(b'0')
print("arduino stop")

playsound("click.mp3")

# luffy answering the phone
ser.write(b'1')
print(ser.name)
print("arduino start")
playsound("luffy_mp3s/greeting_hey.mp3")
ser.write(b'0')
print("arduino stop")


#speech recognition starts listening here
while(1):

	try:
		#turing what it hears into text
		with sr.Microphone() as source2:
			r.adjust_for_ambient_noise(source2, duration=0.1)
			#timers for convo functions
			t = Timer(7, convo_starter)
			t1 = Timer(5, convo_over)
			t2 = Timer(7, convo_both)
			t.start()
			audio2 = r.listen(source2)
			MyText_nosplit = r.recognize_google(audio2)
			MyText_nosplit = MyText_nosplit.lower()
			#if the user speaks and breaks the silence cancel the timers for the convo functions
			t2.cancel()
			t1.cancel()
			t.cancel()
			#displays what the user is saying
			print("user input: ", MyText_nosplit)
			MyText = MyText_nosplit.split()
			print(MyText)

			#greeting the user
			if check_for_match(MyText, user_greetings):
				print("match greeting")
				#combining secondary greetings and convo starters as both potential responses.
				random_mp3_starter = random.choice(secondary_greetings)
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

			#repsoning to the user when they say yes or something similar
			elif check_for_match(MyText, user_y):
				print("match y")
				random_mp3_y_response = random.choice(y_responses + song)
				file_path_for_y_response = os.path.join(folder_path, random_mp3_y_response)
				pygame.mixer.music.load(file_path_for_y_response)
				print(file_path_for_y_response)
				ser.write(b'1')
				print(ser.name)
				print("arduino start")
				playsound(file_path_for_y_response)
				ser.write(b'0')
				print("arduino stop")

			#repsponding to the user when they say no or something similar
			elif check_for_match(MyText, user_n):
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

			#responding to the user when they say something pertaining to food or hunger.
			elif check_for_match(MyText, user_hungry):
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

			#responding to the user if they say what.
			elif check_for_match(MyText, user_what):
				print("match what")
				random_mp3_what = random.choice(what + idk)
				file_path_for_what = os.path.join(folder_path, random_mp3_what)
				pygame.mixer.music.load(file_path_for_what)
				print(file_path_for_what)
				ser.write(b'1')
				print(ser.name)
				print("arduino start")
				playsound(file_path_for_what)
				ser.write(b'0')
				print("arduino stop")

			#responding to the user if they ask a yes or n question.
			elif check_for_match(MyText, user_question):
				print("match question")
				random_mp3_question = random.choice(y + n + idk)
				file_path_for_question = os.path.join(folder_path, random_mp3_question)
				pygame.mixer.music.load(file_path_for_question)
				print(file_path_for_question)
				ser.write(b'1')
				print(ser.name)
				print("arduino start")
				playsound(file_path_for_question)
				ser.write(b'0')
				print("arduino stop")

			#responding to the user if they ask a yes or n question.
			elif check_for_match(MyText, user_question1):
				print("match question1")
				random_mp3_question1 = random.choice(idk)
				file_path_for_question1 = os.path.join(folder_path, random_mp3_question1)
				pygame.mixer.music.load(file_path_for_question1)
				print(file_path_for_question1)
				ser.write(b'1')
				print(ser.name)
				print("arduino start")
				playsound(file_path_for_question1)
				ser.write(b'0')
				print("arduino stop")

			#responding to the user if they say ty.
			elif check_for_match(MyText, user_ty):
				print("match ty")
				random_mp3_ty = random.choice(ty_response)
				file_path_for_ty = os.path.join(folder_path, random_mp3_ty)
				pygame.mixer.music.load(file_path_for_ty)
				print(file_path_for_ty)
				ser.write(b'1')
				print(ser.name)
				print("arduino start")
				playsound(file_path_for_ty)
				ser.write(b'0')
				print("arduino stop")


			#responding to the user if they say idk.
			elif MyText_nosplit.startswith("i don't know"):
				print("match user idk")
				random_mp3_useridk = random.choice(useridk)
				file_path_for_useridk = os.path.join(folder_path, random_mp3_useridk)
				pygame.mixer.music.load(file_path_for_useridk)
				print(file_path_for_useridk)
				ser.write(b'1')
				print(ser.name)
				print("arduino start")
				playsound(file_path_for_useridk)
				ser.write(b'0')
				print("arduino stop")

			# responding to the user if they say luffy cant.
			elif ("you can't" in MyText_nosplit) or ("you can not" in MyText_nosplit):
				print("match you cant")
				random_mp3_mad = random.choice(mad)
				file_path_for_mad = os.path.join(folder_path, random_mp3_mad)
				pygame.mixer.music.load(file_path_for_mad)
				print(file_path_for_mad)
				ser.write(b'1')
				print(ser.name)
				print("arduino start")
				playsound(file_path_for_mad)
				ser.write(b'0')
				print("arduino stop")

			# saying bye to the user
			elif check_for_match(MyText, user_bye):
				convo_over()

			#starting convo ender
			elif check_for_no_match(MyText, all_lists):
				print("match ender or filler")
				#combining secondary greetings and convo starters as both potential responses.
				random_mp3_ender = random.choice(fillers + enders + fillers)
				file_path_for_ender = os.path.join(folder_path, random_mp3_ender)
				pygame.mixer.music.load(file_path_for_ender)
				print(file_path_for_ender)
				#sends the signal to the arduino to start the motor
				ser.write(b'1')
				print(ser.name)
				print("arduino start")
				playsound(file_path_for_ender)
				#sends the signal to the arduino to stop the motor
				ser.write(b'0')
				print("arduino stop")
				#starting the timer for a convo if there is silence
				t1.start()
				# if these sounds clips are played there is a 1 out of 3 chance that luffy will end the convo and hang up
				x = random.randint(1, 3)
				if file_path_for_ender.startswith("ender"):
					if x == 1:
						convo_over()

	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		#saying something to the user when the program cant understand them or hear them
		print("match error")
		t.cancel()
		t1.cancel()
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

