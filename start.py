__author__ = 'bjreynol'
import basic_functions
import variables
import interpreter
import os
import time
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
        for i in range(0,5):
            print(str(5-i)+" seconds....\n")
            time.sleep(1)
        os.system("start "+"cat.jpg")
    if variables.counter == 20:
        print("\n\nCongratulations! Youve asked me 20 questions! A little persistent but alright...\n\nIn honor of this moment, " + variables.creator + " has asked me to give you this:")
        for i in range(0,5):
            print(str(5-i)+" seconds....\n")
            time.sleep(1)
        os.system("start "+"cat2.jpg")
    if variables.counter == 30:
        print("\n\nWhoah! Youve asked me 30 questions! You must be bored\n\nIn honor of this moment, " + variables.creator + " has asked me to give you this:")
        for i in range(0,5):
            print(str(5-i)+" seconds....\n")
            time.sleep(1)
        os.system("start "+"cat3.jpg")
        print("\n\n Also Im out of cats, please forgive me")
    if variables.counter > 30 and (variables.counter%10==0):
        print("\n\nWWOOOOOOOOOOOOOOOOOO " + str(variables.counter) + "!!!\n\n I guess my love and enthusiasm will have to do?")
        print("\n\nYou're very fun and delightful to be around")
