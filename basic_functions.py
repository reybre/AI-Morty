__author__ = 'bjreynol'
import variables
import random
import datetime





def intro():
    print(
        "Hello, " + variables.user + " \n\nI am a companion written for you by " + variables.creator + ", my name is " + variables.ai_name + "\n\n")
    print("I currently have your location set to: " + variables.location + '\n\n')


def joker():
    rand_number = random.randint(0, 99)
    with open('jokes', 'r') as file:
        jokes = file.readlines()
        print('\n\n ' + jokes[rand_number])
        jokes = None


def infochanger(item, new_info):
    if item == 'ai_name':
        variables.ai_name = new_info
        print('\n\n Got it! My new name is ' + variables.ai_name)
    elif item == 'creator_name':

        if('poop' in new_info):
            print("\n\n Not nice! My creators name is now 'The Greatest Boyfriend Alive'")
            variables.creator = 'The Greatest Boyfriend Alive'
        else:
            variables.creator = new_info
            print('\n\n Got it! my maker is called ' + variables.creator)
    elif item == 'user_name':
        variables.user = new_info
        print('\n\n Got it! I will call you ' + variables.user + ' from now on')
    elif item == 'location':
        variables.location = new_info
        print('\n\n Got it! your new location is ' + variables.location)
    else:
        print("panic! Something went wrong when trying to save to variables")


def quit():
    print('\n\n Okay! Let me save any changed data first')
    data = [variables.ai_name, variables.creator, variables.user, variables.location]
    data = data + variables.command_list
    for x in range(len(data)):
        data[x] += '\n'
    with open('info', 'w') as file:
        file.writelines(data)
    print('\n\n Alright! Data saved! See you around, ' + variables.user)
    variables.quit = True


def math(type, x, y):
    if type == 'multiply':
        ans = x * y
        print('\n\n ' + str(x) + ' times ' + str(y) + ' is equal to ' + str(ans))
    if type == 'divide':
        ans = x / y
        print('\n\n ' + str(x) + ' divided by ' + str(y) + ' is equal to ' + str(ans))
    if type == 'addition':
        ans = x + y
        print('\n\n ' + str(x) + ' plus ' + str(y) + ' is equal to ' + str(ans))
    if type == 'subtraction':
        ans = x - y
        print('\n\n ' + str(x) + ' minus ' + str(y) + ' is equal to ' + str(ans))
    ans = None

def info():
    print('\n\nI currently have ' + str(len(variables.command_list)) + ' functions' + '\n\nThe functions I can currently do are: \n\n')
    for item in variables.command_list:
        print(str(item) + '\n')
def date():

    today = datetime.date.today()
    print("\n\nToday's date is {:%b, %d %Y}".format(today))

def haiku_spitter():
    haikus = []

    with open('Haikus','r') as file:
        haikus = file.readlines()

        rand_number = random.randint(0,(len(haikus)/3))
        print("\n\n")
        for x in range(0,3):
            print(haikus[rand_number*3-3+x])
    haikus = None





