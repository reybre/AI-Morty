__author__ = 'bjreynol'
import basic_functions
import variables
import interpreter

variables.basicinforeader()
basic_functions.intro()



while variables.quit == False:


    if variables.counter == 0:
        variables.current_phrase = input(" What can I help you with today? \n\n>>> ")
        interpreter.interpreter()
        variables.counter += 1

    variables.current_phrase = input(" \n\nWhat else can I help with? \n\n>>> ")
    interpreter.interpreter()
    variables.counter += 1

