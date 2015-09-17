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
cats=[1,1,1]
cats[2] = '''
                 ________________
                |                |_____    __
                |  I Love You!   |     |__|  |_________
                |________________|     |::|  |        /
   /\**/\       |                \.____|::|__|      <
  ( o_o  )_     |                      \::/  \._______
   (u--u   \_)  |
    (||___   )==
  ,dP"/b/=( /P"/b
  |8 || 8\=== || 8
  `b,  ,P  `b,  ,P

'''
cats[1] = '''
    ("`-''-/").___..--''"`-._
     `6_ 6  )   `-.  (     ).`-.__.`)
     (_Y_.)'  ._   )  `._ `. ``-..-'
   _..`--'_..-_/  /--'_.' ,'
  (il),-''  (li),'  ((!.-'
  '''
cats[0]= '''
.../\„,„/\..
..( =';'= ).
.../*♥♥*\..
.(.|.|..|.|.).
'''


