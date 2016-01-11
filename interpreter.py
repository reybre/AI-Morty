__author__ = 'bjreynol'

import variables
import basic_functions



def interpreter():
    if 'joke' in variables.current_phrase:
        basic_functions.joker()
    elif variables.current_phrase == "change my name":
        print('\n\n Your current name is ' + variables.user)
        basic_functions.infochanger('user_name',input("\n\n What shall I call you in the future? \n\n >>> "))
    elif variables.current_phrase == 'quit':
        basic_functions.quit()
    elif 'change my name to ' in variables.current_phrase:
        basic_functions.infochanger('user_name',variables.current_phrase.lstrip('change my name to '))
    elif 'change your name to ' in variables.current_phrase:
        basic_functions.infochanger('ai_name',variables.current_phrase.lstrip('change your name to '))
    elif 'change the creators name to ' in variables.current_phrase:
        basic_functions.infochanger('creator_name',variables.current_phrase.lstrip('change the creators name to '))
    elif 'change my location to ' in variables.current_phrase:
        basic_functions.infochanger('location',variables.current_phrase.lstrip('change my location to '))

    elif 'divided by ' in variables.current_phrase:
        try:
            l = []
            for t in variables.current_phrase.split():
                try:
                    l.append(float(t))
                except ValueError:
                    pass
            if len(l)!=2:
                print("\n\nYou're trying to divide...but I dont understand...\nAre you typing or spelling the number?")

            else:
                basic_functions.math('divide',l[0],l[1])
        except ValueError or IndexError:
            print("\n\nYou're trying to divide...but I dont understand...\nAre you typing or spelling the number?")
    elif ('multiplied by ' in variables.current_phrase) or ('times' in variables.current_phrase):
        try:
            l = []
            for t in variables.current_phrase.split():
                try:
                    l.append(float(t))
                except ValueError:
                    pass
            if len(l)!= 2:
                print("\n\nYou're trying to multiply...but I dont understand...\nAre you typing or spelling the number?")

            else:
                basic_functions.math('multiply',l[0],l[1])
        except ValueError or IndexError:
            print("\n\nYou're trying to multiply...but I dont understand...\nAre you typing or spelling the number?")
    elif ('plus ' in variables.current_phrase) or ('added to ' in variables.current_phrase):

        l = []
        for t in variables.current_phrase.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        if len(l)!=2:
            print("\n\nYou're trying to add...but I dont understand...\nAre you typing or spelling the number?")
        else:

            basic_functions.math('addition',l[0],l[1])


    elif ('subtracted by ' in variables.current_phrase) or ('minus ' in variables.current_phrase):

        l = []
        for t in variables.current_phrase.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        if len(l)!=2:
             print("\n\nYou're trying to subtract...but I dont understand...\nAre you typing or spelling the number?")
        else:
            basic_functions.math('subtraction',l[0],l[1])


    elif ('info' in variables.current_phrase) or ('what do you know' in variables.current_phrase):
        basic_functions.info()
    elif 'what does the fox say' in variables.current_phrase:
        print('\n\n2012 called and they want their stupid video back')
    elif (' date' in variables.current_phrase) or (' day ' in variables.current_phrase):
        basic_functions.date()
    elif 'haiku' in variables.current_phrase:
        basic_functions.haiku_spitter()
    elif 'weather'==variables.current_phrase:
        print("\n\nThat is a word......")
    elif ('weather' in variables.current_phrase) and ('weather'!=variables.current_phrase):
        loc = variables.current_phrase.split("in",1)[1]
        basic_functions.weather(loc,'current')
    elif ('woof' in variables.current_phrase):
        print("\n\nWoof Woof!! I am dog!")






    else:
        print("\n\nI don't think I know what you're saying.....")









