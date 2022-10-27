import re
import random

print ("Hi I'm LIZA, I'm a bot authored my krish lalwani.")

#variables for long responses
krish = ("Yeah he is a freak!")
eat = ("i do not eat anything because i am a bot made by Krish Lalwani")
code = ("you can get our source code on github/krishlalwani0")
calc =("I'm not a calculator dumbo!")
date = ("I'm just a bot, but you can solve your loneliness on TINDER :)")



def unknown():
    response = ["Could you please re-phrase that? ",
                "I don't know the answer of that.",
                "What was that?.",
                "What does that mean?",
                "Sorry, i couldn't understand that",
                "IDK :) ", 
                "You can also Google that"   ] [random.randrange(7)]
    return response


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def yo(name):
	
	N1 = int(input("Enter N1:\n"))
	N2 = int(input("Enter N2:\n"))

	print ("enter what to do with numbers")
	print ("1 for sum.\n2 for subtract.\n3 for multiply.\n4 for divide.")	
	B = input()
	print ("\n")
	if B == ('1'):
		print (N1+N2)
	elif B == ('2'):
		print (N1-N2)
	elif B == ('3'):
		print (N1*N2)
	elif B == ('4'):
		print (N1/N2)
	else:
		print ("Please try again.")
	

a = input("I can calculate number, should i do that?\nType yes or Press no to talk something else.\n")
if a == ("yes"):
	yo(" krish")
elif a == ("no"):
	print ("Hi")
	pass 

Simp =["you are very beautiful", " you are such a gorgeous", " you are such a nice user.", "i love you ", "I LIKE YOU!"][random.randrange(5)]
	
	
	
	
def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
        
    # Responses ---------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response(krish, ['i', 'love', 'krish', 'lalwani'], required_words=['krish'])
    response(code, ['can', 'get', 'source', 'code'],required_words=['source','code']) 
    response(Simp, ['lovely', 'cute','loveyou','marry','pretty'], single_response=True)
    # Longer responses
    response('if i were you, i would go to google', ['give', 'advice'], required_words=['advice'])
    response(eat, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system

while True:
    print('Bot: ' + get_response(input('You: ')))
    
 #made with love by krishlalwani
#github/krishlalwani0


