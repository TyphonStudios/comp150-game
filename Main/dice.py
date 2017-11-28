"""
Author: Connor Sean Rodgers
Class: Dice

"""

"""
========================================================================================================================
Dice Class

Define coinToss
    Random number of an inclusive range between 1 and 2 to simulate a coin toss.

Define rollFour
    Random number of an inclucive range between 1 and 4 to simulate rolling a 4 sided die

Define rollSix
    Random number of an inclucive range between 1 and 6 to simulate rolling a 6 sided die

Define rolEight
    Random number of an inclucive range between 1 and 8 to simulate rolling a 8 sided die

Define rollTen
    Random number of an inclucive range between 1 and 10 to simulate rolling a 10 sided die

Define rollTwelve
    Random number of an inclucive range between 1 and 12 to simulate rolling a 12 sided die

Define rollTwenty
    Random number of an inclucive range between 1 and 20 to simulate rolling a 20 sided die

Define rollHundred
    Random number of an inclucive range between 1 and 10 to simulate rolling a 100 sided die

========================================================================================================================
"""
from random import randint
# ======================================================================================================================
def coinToss():
    toss = randint(1,2)
    return (toss)
# ======================================================================================================================
def rollThree():
    roll = randint(1,3)
    return (roll)
# ======================================================================================================================
def rollFour():
    roll = randint(1,4)
    return (roll)
# ======================================================================================================================
def rollSix():
    roll = randint(1,6)
    return (roll)
# ======================================================================================================================
def rollEight():
    roll = randint(1,8)
    return (roll)
# ======================================================================================================================
def rollTen():
    roll = randint(1,10)
    return (roll)
# ======================================================================================================================
def rollTwelve():
    roll = randint(1,12)
    return (roll)
# ======================================================================================================================
def rollTwenty():
    roll = randint(1,20)
    return (roll)
# ======================================================================================================================
def rollHundred():
    roll = randint(1,100)
    return (roll)
# ======================================================================================================================