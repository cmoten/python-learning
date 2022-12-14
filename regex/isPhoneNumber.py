#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Cardy Moten III
# Created Date: 2022-10-07
# version ='1.0'
# ---------------------------------------------------------------------------
""" Simple script to find a phone number pattern without regular expressions.
Code is from the book Automate the Boring Stuff with Python by Al Sweigart."""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# functions
# ---------------------------------------------------------------------------
def isPhoneNumber(text) -> bool:
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

def main() -> None:
    print('415-555-4242 is a phone number:')
    print(isPhoneNumber('415-555-4242'))
    print('Moshi Moshi is a phone number:')
    print(isPhoneNumber('Moshi Moshi'))
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: {}'.format(chunk))
    print('Done')
# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
