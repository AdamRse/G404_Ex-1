import datetime
import math
from operator import index
from pydoc import text
import re
import sys
import time
import random
import os
import itertools

sys.set_int_max_str_digits(0)
inp = ""
inp2 = ""

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def get_inp(msg):
    global inp
    inp = input(msg)

def get_inp2(msg):
    global inp2
    inp2 = input(msg)

def printError(msg):
    print(bcolors.FAIL + msg + bcolors.ENDC)


def printSuccess(msg):
    print(bcolors.OKGREEN + msg + bcolors.ENDC)

def printWrong(msg):
    print(bcolors.WARNING + msg + bcolors.ENDC)

def del_accents(texte):
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    output=""
    for lettre in texte:
        try:
            id=accent.index(lettre)
            output+=sans_accent[id]
        except ValueError:
            output+=lettre
    return output
