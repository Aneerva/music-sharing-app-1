import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def setup ():
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER = socket.socket (socket.AF_INET, socket.SOCK_STREAM)   
    SERVER.connect((IP_ADDRESS, PORT))
    setup()

def musicWindow():
    from tkinter import *
    