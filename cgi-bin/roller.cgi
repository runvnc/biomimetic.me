#!/usr/bin/python
from gemini import *

with open('roller.sq','r') as f:
  text = f.read()

respond(SUCCESS, 'application/subleq')
print(text)
