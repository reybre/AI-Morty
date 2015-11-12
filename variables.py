__author__ = 'bjreynol'

# Variables used for interpreter

current_phrase = ""
quit = False

# Variables read off info file

creator = ""
user = ""
ai_name = ""
location = ""
command_list = []
counter = 0


def basicinforeader():

    global ai_name, creator, user, location, command_list

    with open('info','r') as file:
        data = file.readlines()
    for x in range(0,len(data)):
        data[x] = data[x].strip('\n')
    ai_name = data[0]
    creator = data[1]
    user = data[2]
    location = data[3]
    for x in range(4,len(data)):

        command_list.append(data[x])



