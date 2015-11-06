__author__ = 'bjreynol'
import variables
import random
import datetime
import pywapi





def intro():
    '''An intro program, it basically just reads out data'''
    print(
        "Hello, " + variables.user + " \n\nI am a companion written for you by " + variables.creator + ", my name is " + variables.ai_name + "\n\n")
    print("I currently have your location set to: " + variables.location + '\n\n')


def joker():
    '''Randomly tells you one of one hundred jokes!!! If you want to add a joke just place
    it in a new line in jokes.txt
    '''
    rand_number = random.randint(0, 99)
    with open('jokes', 'r') as file:
        jokes = file.readlines()
        print('\n\n ' + jokes[rand_number])
        jokes = None


def infochanger(item, new_info):
    '''

    :param item: the object you wish to change (ai_name, user_name,location)
    :param new_info: the new string containing the name of the new item
    :return: returns 0
    '''
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
    '''
    quits the program
    :return:
    '''
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
    '''

    :param type: str specifying the type of math to be done
    :param x: first number (must be float)
    :param y: second number (must be float)
    :return:
    '''
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
    '''
    tells you what Morty knows. Can be modified by writing new lines in info.txt
    :return:
    '''
    print('\n\nI currently have ' + str(len(variables.command_list)) + ' functions' + '\n\nThe functions I can currently do are: \n\n')
    for item in variables.command_list:
        print(str(item) + '\n')
def date():
    '''
    tells you the date
    :return:
    '''

    today = datetime.date.today()
    print("\n\nToday's date is {:%b, %d %Y}".format(today))

def haiku_spitter():
    '''
    spits out one of the 16ish haikus in haiku.txt

    to add a new one just write it in new lines
    :return:
    '''
    haikus = []

    with open('Haikus','r') as file:
        haikus = file.readlines()

        rand_number = random.randint(0,(len(haikus)/3))
        print("\n\n")
        for x in range(0,3):
            print(haikus[rand_number*3-3+x])
    haikus = None
def weather(loc,type):
    '''
    tells you the weather
    :param loc: a str containing a location
    :param type: the type of weather asked for (current only works right now)
    :return:
    '''

    lookup = pywapi.get_location_ids(loc)
    loc_id='blank'
    for i in lookup:
        loc_id = i
    if(loc_id=='blank'):
        print("\n\nI couldn't figure out where " + loc + " is, try again?")
        return 0
    weather_com_result = pywapi.get_weather_from_weather_com(loc_id,'imperial')
    try:
        if(type=='current'):

            text = weather_com_result['current_conditions']['text']

            if text == 'N/A':
                text = "I dont know current cloud conditions here :("
            temp = str(weather_com_result['current_conditions']['temperature'])
            moon = weather_com_result['current_conditions']['moon_phase']['text']
            print("\n\nAcquiring current conditions in " + weather_com_result['location']['name'] + "\n" + text +
                 "\nTemperature is " + temp + '\nMoon phase is ' + moon )
    except KeyError or IndexError or ValueError:

        print("\n\nSorry, something broken...\n\nTry again!")
        pass





#





