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
    if variables.counter == 10:
        print("\n\nCongratulations! Youve asked me 10 questions!\n\nIn honor of this moment, " + variables.creator + " has asked me to give you this:")
        print("\n\n" + variables.cats[0])
    if variables.counter == 20:
        print("\n\nCongratulations! Youve asked me 20 questions! A little persistent but alright...\n\nIn honor of this moment, " + variables.creator + " has asked me to give you this:")
        print("\n\n" + variables.cats[1])
    if variables.counter == 30:
        print("\n\nWhoah! Youve asked me 30 questions! You must be bored\n\nIn honor of this moment, " + variables.creator + " has asked me to give you this:")
        print("\n\n" + variables.cats[2])
        print("\n\n Also Im out of cats, please forgive me")
    if variables.counter > 30 and (variables.counter%10==0):
        print("\n\nWWOOOOOOOOOOOOOOOOOO " + str(variables.counter) + "!!!\n\n I guess my love and enthusiasm will have to do?")
        print("\n\nYou're very fun and delightful to be around")
