#########################################
############# WiFinder V1.0 #############
#########################################

import os
import sys

from start_menu import StartMenu
start_menu = StartMenu()

isRunning = True

while isRunning == True:
    start_menu.menu()

    if start_menu.quit():
        isRunning = False