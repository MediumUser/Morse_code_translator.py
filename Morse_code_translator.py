from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import winsound
import time
import os
import sys


#Important variables
dic = {'#': '█', ' ':''}

diacritic_dictionary = {'č':'c', 'ć':'c', 'š':'s', 'đ':'d', 'ž':'z', 'ł':'l', 'ę':'e',
                        'ż':'z', 'é':'e', 'ä':'a', 'ë':'e', 'ö':'o', 'ü':'u'}

input_result = ''

dictionary = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
              'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
              'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
              's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..', #latin
              '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
              #Numbers
              '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '.-.-.--', '/': '--..-.',  #Punctuation
              '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
              '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
              '$': '...-..-', '@': '.--.-.', '¿': '..-.-', '¡': '--...-', "'": "--...-",
              ' ': '/' #Gap
              }

dictionary_reversed = {}
for k, v in dictionary.items():
    dictionary_reversed[v] = k

dictionary_reversed.update(dic)

default_primary_color = 'lightgrey'
default_secondary_color = 'black'
default_green_color = 'green'

language_english = ['Settings', 'Help', 'Normal text',
                      'Translate', 'Morse code',
                      'Mode', 'Light mode', 'Dark mode', 'Language',
                      'English(US)', 'Croatian', 'About',
                    'Author: Andrija Rakić\nReleased: June 7, 2022.\nVersion: 1.0\nMade in Croatia',
                    'Morse code characters:\n.  short press\n-  long press\n/  gap\n#  unknown character(null)',
                    'Clear', 'Error', 'Invalid characters.']

language_croatian = ['Postavke', 'Pomoć', 'Normalni tekst',
                       'Prevedi', 'Morseov kod',
                       'Mod', 'Svijetli mod', 'Tamni mod', 'Jezik',
                       'Engleski(SAD)', 'Hrvatski', 'O programu',
                     'Autor: Andrija Rakić\nObjavljeno: 7. lipnja 2022.\nVerzija: 1.0\nIsprogramirano u Hrvatskoj',
                     'Znakovi morseovog koda:\n.  kratki pritisak\n-  dugi pritisak\n/  razmak\n#  nepoznati znak(nema podataka)',
                     'Očisti', 'Greška', 'Nevažeći znakovi.']

language_default = language_english #Standard language


t = Tk()
t.title('Morse code translator')
t.config(width=500, height=180, bg=default_primary_color)

#Defining functions

def change_mode(Mode=0):
    if Mode == 0:
        default_primary_color = 'black'
        default_secondary_color = 'white'
        default_green_color = 'lightgreen'
        t.config(bg = default_primary_color)
        TEXT1.config(bg = default_primary_color, fg = default_secondary_color)
        TEXT2.config(bg = default_primary_color, fg = default_secondary_color)
        TEXT3.config(bg = default_primary_color, fg = default_secondary_color)
        TEXT4.config(bg = default_primary_color, fg = default_secondary_color)
        NT.config(bg = default_primary_color, fg = default_secondary_color)
        MK.config(bg = default_primary_color, fg = default_secondary_color)
        TNM.config(bg = default_primary_color, fg = default_secondary_color)
        TMK.config(bg = default_primary_color, fg = default_secondary_color)
        PLAYSOUND.config(bg = default_primary_color, fg = default_green_color)
        LIGHTSIGNAL.config(bg = default_primary_color)
        return
    elif Mode == 1:
        default_primary_color = 'lightgrey'
        default_secondary_color = 'black'
        default_green_color = 'green'
        t.config(bg = default_primary_color)
        TEXT1.config(bg = default_primary_color, fg = default_secondary_color)
        TEXT2.config(bg = default_primary_color, fg = default_secondary_color)
        TEXT3.config(bg = default_primary_color, fg = default_secondary_color)
        TEXT4.config(bg = default_primary_color, fg = default_secondary_color)
        NT.config(bg = default_primary_color, fg = default_secondary_color)
        MK.config(bg = default_primary_color, fg = default_secondary_color)
        TNM.config(bg = default_primary_color, fg = default_secondary_color)
        TMK.config(bg = default_primary_color, fg = default_secondary_color)
        PLAYSOUND.config(bg = default_primary_color, fg = default_green_color)
        LIGHTSIGNAL.config(bg = default_primary_color)
        return
    else:
        return

def change_language(Language=0):
    if Language == 0:
        language_default = language_english
        TEXT1.config(text = language_default[2])
        TEXT2.config(text = language_default[4])
        TEXT3.config(text = language_default[3])
        TEXT4.config(text = language_default[13])
        CLEAR.config(text = language_default[14])
        return
    elif Language == 1:
        language_default = language_croatian
        TEXT1.config(text = language_default[2])
        TEXT2.config(text = language_default[4])
        TEXT3.config(text = language_default[3])
        TEXT4.config(text = language_default[13])
        CLEAR.config(text = language_default[14])
        return
    else:
        return

def about_program():
    showinfo(language_default[11], language_default[12])
    return

def normal_to_morse(input_text):
    #Diacritic sign distinction
    input_text = str(input_text)
    input_text = input_text.lower()
    input_result = ''
    for i in input_text:
        if i in diacritic_dictionary.keys():
            input_result += diacritic_dictionary[i]
        else:
            input_result += i
    input_text = input_result
    input_result = ''
    #Code converter
    for i in input_text:
        if i in dictionary.keys():
            input_result += dictionary[i] + ' '
        else:
            input_result += '#' + ' '
    return input_result

def morse_to_normal(input_text):
    #Decoding
    input_result = ''
    input_text = input_text.split()
    for i in input_text:
        if i in dictionary_reversed.keys():
            input_result += dictionary_reversed[i]
        else:
            showerror(language_default[15], language_default[16])
            break
    return input_result

def translate_to_morse_code():
    MK.delete(0, END)
    text_insert = NT.get()
    output = normal_to_morse(text_insert)
    MK.insert(0, output)

def translate_to_normal_text():
    NT.delete(0, END)
    text_insert = MK.get()
    output = morse_to_normal(text_insert)
    NT.insert(0, output)

def clear_all():
    NT.delete(0, END)
    MK.delete(0, END)
    return

def signal_state(State):
    if State == 0:
        LIGHTSIGNAL.config(fg = 'gray')
        LIGHTSIGNAL.update()
        time.sleep(0.0009)
        return
    elif State == 1:
        LIGHTSIGNAL.config(fg = 'gold')
        LIGHTSIGNAL.update()
        time.sleep(0.0009)
        return
    else:
        return

def simulate_beep():
    text_insert = MK.get()
    signal_state(0)
    for i in text_insert:
        if i == '.': #Short press = dit
            signal_state(1)
            winsound.Beep(750, 200)#Dit
            signal_state(0)
            continue
        elif i == '-': #Long press = dah
            signal_state(1)
            winsound.Beep(750, 600)#Dah = 3 times longer than dit
            signal_state(0)
            continue
        elif i == '/':
            signal_state(0)
            time.sleep(0.6)#Pause between words = 2 * dah(maybe)
            
            continue
        elif i == ' ':
            signal_state(0)
            time.sleep(0.6)#Pause between letters = dah
            
            continue
        else:
            signal_state(0)
            showerror(language_default[15], language_default[16])
            break
    signal_state(0)
    return



#Toplevel buttons

menubar = Menu(t)
submenu_settings = Menu(menubar)
submenu_help = Menu(menubar)
settings_mode = Menu(submenu_settings)
settings_language = Menu(submenu_settings)

#Settings
menubar.add_cascade(label = language_default[0], menu = submenu_settings)
submenu_settings.add_cascade(label = language_default[5], menu = settings_mode)
settings_mode.add_command(label = language_default[6], command = lambda : change_mode(1))
settings_mode.add_command(label = language_default[7], command = lambda : change_mode())

submenu_settings.add_cascade(label = language_default[8], menu = settings_language)
settings_language.add_command(label = language_default[9], command = lambda : change_language())
settings_language.add_command(label = language_default[10], command = lambda : change_language(1))


#Help

menubar.add_cascade(label = language_default[1], menu = submenu_help)
submenu_help.add_command(label = language_default[11], command = lambda : about_program())

#Entry

TEXT1 = Label(t, text = language_default[2],bg = default_primary_color, fg = default_secondary_color, font=('Calibri', 10, 'normal'))
TEXT1.place(x=30, y=30)
TEXT2 = Label(t, text = language_default[4],bg = default_primary_color, fg = default_secondary_color, font=('Calibri', 10, 'normal'))
TEXT2.place(x=300, y=30)

NT = Entry(t, width = 25, bg = default_primary_color, fg=default_secondary_color)
NT.place(x=30, y=50)


MK = Entry(t, width = 25, bg = default_primary_color, fg=default_secondary_color)
MK.place(x = 300, y = 50)

TEXT3 = Label(t, text = language_default[3], bg = default_primary_color, fg=default_secondary_color)
TEXT3.place(x = 215, y = 30)

TEXT4 = Label(t, text = language_default[13], bg = default_primary_color, fg=default_secondary_color, justify='left' , font=('Calibri', 8, 'normal'))
TEXT4.place(x = 10, y = 105)

LIGHTSIGNAL = Label(t, text = '●', bg = default_primary_color, fg = 'Gray', font=('arial', 40))
LIGHTSIGNAL.place(x = 435, y = 73)

#Buttons
TNM = Button(t, text = '->', bg = default_primary_color, fg = default_secondary_color, command = translate_to_morse_code) 
TNM.place(x = 245, y = 50)

TMK = Button(t, text = '<-', bg = default_primary_color, fg = default_secondary_color, command = translate_to_normal_text)
TMK.place(x = 215, y = 50)

CLEAR = Button(t, text = language_default[14], bg = 'red', fg = 'white', command = clear_all)
CLEAR.place(x = 220, y = 95)

PLAYSOUND = Button(t, text = '▶', bg = default_primary_color, fg = 'green', command = simulate_beep)
PLAYSOUND.place(x = 390, y = 95)


t.config(menu = menubar)

t.mainloop()
