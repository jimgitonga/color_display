# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:22:56 2019

Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”
"""

color=input("enter your favorite color: ").strip()

if color=='RED' or 'Red' or 'red':
    print('i like {}'.format(color))
else:
    print('I don’t like {}, I prefer red'.format(color))