

from playsound import playsound
import speech_recognition as sr
import pyttsx3 
import random


#intial phone ring
playsound('ring.mp3')
r = sr.Recognizer() 

#all the dialog/responses for the charaters and user
user_greetings = ["hello", "hi", "greetings", "yo"]
user_y = ["yes", "yeah", "yea", "yup"]
user_n = ["no", "nope", "nah"]
characters = ["luffy", "robin", "choppa"]
luffy_greetings = ["luffy: hi", "luffy: hello", "luffy: whats up"]
luffy_error = ["luffy: i didnt hear that", "luffy: what did you say", "luffy: can you repeate that"]
luffy_converstaion_ender = ["luffy: i have to go"]
luffy_converstaion_starter = ["luffy: im gonna be king of the pirates", "luffy: the one piece is real", "luffy: im hungry", "luffy: talk to robin", "luffy: talk to choppa"]
luffy_y_response = ["luffy: alright!", "luffy: awesome!", "luffy: lets go!"]
luffy_n_response = ["luffy: why not", "luffy: thats dumb"]
choppa_greetings = ["choppa: hi", "choppa: hello", "choppa: whats up"]
choppa_y_response = ["choppa: alright!", "choppa: awesome!", "choppa: lets go!"]
choppa_error = ["choppa: i didnt hear that", "choppa: what did you say", "choppa: can you repeate that"]
choppa_converstaion_ender = ["choppa: i have to go, bye"]
choppa_converstaion_starter = ["choppa: i will be able to cure any dease", "choppa: i found some ingredients for medicine", "choppa: talk to luffy, i have to go", "choppa: talk to robin, i have to go"]
choppa_n_response = ["choppa: why not", "choppa: thats dumb"]
robin_greetings = ["robin: hi", "robin: hello", "robin: whats up"]
robin_error = ["robin: i didnt hear that", "robin: what did you say", "robin: can you repeate that"]
robin_converstaion_ender = ["robin: i have to go, bye"]
robin_converstaion_starter = ["robin: i can read the poneglyphs", "robin: im so grateful to have found friends", "robin: talk to luffy, i have to go", "robin: talk to robin, i have to go"]
robin_y_response = ["robin: alright!", "robin: awesome!", "robin: lets go!"]
robin_n_response = ["robin: why not", "robin: thats dumb"]

#starting the converstaion by randomly selection a character to answer the phone and greet the user.
charater_speaking = random.choice(characters)
print(charater_speaking)
if charater_speaking == "luffy":
	charater_response = random.choice(luffy_greetings)
	print(charater_response)
elif charater_speaking == "choppa":
	charater_response = random.choice(choppa_greetings)
	print(charater_response)
else:
	charater_response = random.choice(robin_greetings)
	print(charater_response)


#starts listening here
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
				if charater_speaking == "luffy":
					charater_response = random.choice(luffy_greetings)
				elif charater_speaking == "choppa":
					charater_response = random.choice(choppa_greetings)
				else:
					charater_response = random.choice(robin_greetings)

				print(charater_response)

			# repsoning to the user when they say yes or something similar
			if MyText in user_y:
				if charater_speaking == "luffy":
					charater_response = random.choice(luffy_y_response)
				elif charater_speaking == "choppa":
					charater_response = random.choice(choppa_y_response)
				else:
					charater_response = random.choice(robin_y_response)

				print(charater_response)

			# repsoning to the user when they say no or something similar
			if MyText in user_n:
				if charater_speaking == "luffy":
					charater_response = random.choice(luffy_n_response)
				elif charater_speaking == "choppa":
					charater_response = random.choice(choppa_n_response)
				else:
					charater_response = random.choice(robin_n_response)

				print(charater_response)

			# if the user wants to talk to a different charater
			if "to chopper" in MyText:
				charater_response = random.choice(choppa_greetings)
				charater_speaking = "choppa"
				print(charater_response)

			if "to robin" in MyText:
				charater_response = random.choice(robin_greetings)
				charater_speaking = "robin"
				print(charater_response)

			if "to luffy" in MyText:
				charater_response = random.choice(luffy_greetings)
				charater_speaking = "luffy"
				print(charater_response)
						

	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:				
		if charater_speaking == "luffy":
			charater_response = random.choice(luffy_error)
		elif charater_speaking == "choppa":
			charater_response = random.choice(choppa_error)
		else:
			charater_response = random.choice(robin_error)
		print(charater_response)
