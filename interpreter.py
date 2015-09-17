__author__ = 'bjreynol'

import variables
import basic_functions


def interpreter():
    if 'joke' in variables.current_phrase:
        basic_functions.joker()
    if variables.current_phrase == "change my name":
        print('\n\n Your current name is ' + variables.user)
        basic_functions.infochanger('user_name',input("\n\n What shall I call you in the future? \n\n >>> "))
    if variables.current_phrase == 'quit':
        basic_functions.quit()
    if 'change my name to ' in variables.current_phrase:
        basic_functions.infochanger('user_name',variables.current_phrase.lstrip('change my name to '))
    if 'change your name to ' in variables.current_phrase:
        basic_functions.infochanger('ai_name',variables.current_phrase.lstrip('change your name to '))
    if 'change the creators name to ' in variables.current_phrase:
        basic_functions.infochanger('creator_name',variables.current_phrase.lstrip('change the creators name to '))
    if 'change my location to ' in variables.current_phrase:
        basic_functions.infochanger('location',variables.current_phrase.lstrip('change my location to '))

    if 'divided by ' in variables.current_phrase:
        l = []
        for t in variables.current_phrase.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        basic_functions.math('divide',l[0],l[1])
    if ('multiplied by ' in variables.current_phrase) or ('times' in variables.current_phrase):
        l = []
        for t in variables.current_phrase.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        basic_functions.math('multiply',l[0],l[1])
    if ('plus ' in variables.current_phrase) or ('added to ' in variables.current_phrase):
        l = []
        for t in variables.current_phrase.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        basic_functions.math('addition',l[0],l[1])
    if ('subtracted by ' in variables.current_phrase) or ('minus ' in variables.current_phrase):
        l = []
        for t in variables.current_phrase.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        basic_functions.math('subtraction',l[0],l[1])
    if ('info' in variables.current_phrase) or ('what do you know' in variables.current_phrase):
        basic_functions.info()
    if 'what does the fox say' in variables.current_phrase:
        print('\n\n2012 called and they want their stupid video back')
    if ('date' in variables.current_phrase) or ('day' in variables.current_phrase):
        basic_functions.date()
    if 'haiku' in variables.current_phrase:
        basic_functions.haiku_spitter()








