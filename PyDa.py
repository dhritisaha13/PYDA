# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3

client = wolframalpha.Client("RWGKQ6-PL8HKXJUXG")

sg.theme('DarkPurple')
layout =[[sg.Text('Hello I am PyDa, the Python Digital Assistant. How can I help you?')],[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('PyDa', layout)
engine = pyttsx3.init()
engine.setProperty('rate', 150)  


while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        res = client.query(values[0])
        wolfram_res = next(res.results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: " + wolfram_res)
    
    except:
        wiki_res = wikipedia.summary(values[0], sentences = 3)
        engine.say(wiki_res)
        sg.PopupNonBlocking("Wikipedia Result: " + wiki_res)
        
    engine.runAndWait()
        
            

window.close()        
